# Copyright 2020 The Flax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Write Summaries from JAX for use with Tensorboard.
"""

import io
import struct
import sys
import time
import warnings
import wave
import matplotlib as mpl
# Necessary to prevent attempted Tk import:
with warnings.catch_warnings():
  warnings.simplefilter('ignore')
  if 'google.colab' in sys.modules or 'ipykernel' in sys.modules:
    pass
  else:
    mpl.use('Agg')
# pylint: disable=g-import-not-at-top
import matplotlib.pyplot as plt
import numpy as onp
import tensorflow.compat.v1 as tf
from tensorflow.compat.v1 import HistogramProto
from tensorflow.compat.v1 import Summary
from tensorflow.compat.v1 import SummaryMetadata
from tensorflow.compat.v1.io import gfile

from tensorflow.core.util import event_pb2  # pylint: disable=g-direct-tensorflow-import
from tensorflow.python.summary.writer.event_file_writer import EventFileWriter  # pylint: disable=g-direct-tensorflow-import


class SummaryWriter(object):
  """Saves data in event and summary protos for tensorboard."""

  def __init__(self, log_dir):
    """Create a new SummaryWriter.

    Args:
      log_dir: path to record tfevents files in.
    """
    # If needed, create log_dir directory as well as missing parent directories.
    if not gfile.isdir(log_dir):
      gfile.makedirs(log_dir)

    self._event_writer = EventFileWriter(log_dir, 10, 120, None)
    self._closed = False

  def _add_summary(self, summary, step):
    event = event_pb2.Event(summary=summary)
    event.wall_time = time.time()
    if step is not None:
      event.step = int(step)
    self._event_writer.add_event(event)

  def close(self):
    """Close SummaryWriter. Final!"""
    if not self._closed:
      self._event_writer.close()
      self._closed = True
      del self._event_writer

  def flush(self):
    self._event_writer.flush()

  def scalar(self, tag, value, step):
    """Saves scalar value.

    Args:
      tag: str: label for this data
      value: int/float: number to log
      step: int: training step
    """
    value = float(onp.array(value))
    summary = Summary(value=[Summary.Value(tag=tag, simple_value=value)])
    self._add_summary(summary, step)

  def image(self, tag, image, step):
    """Saves RGB image summary from onp.ndarray [H,W], [H,W,1], or [H,W,3].

    Args:
      tag: str: label for this data
      image: ndarray: [H,W], [H,W,1], [H,W,3] save image in greyscale or colors.
        Pixel values should be in the range [0, 1].
      step: int: training step
    """
    image = onp.array(image)
    if len(onp.shape(image)) == 2:
      image = image[:, :, onp.newaxis]
    if onp.shape(image)[-1] == 1:
      image = onp.repeat(image, 3, axis=-1)
    image_strio = io.BytesIO()
    plt.imsave(image_strio, image, vmin=0., vmax=1., format='png')
    image_summary = Summary.Image(
        encoded_image_string=image_strio.getvalue(),
        colorspace=3,
        height=image.shape[0],
        width=image.shape[1])
    summary = Summary(value=[Summary.Value(tag=tag, image=image_summary)])
    self._add_summary(summary, step)

  def audio(self, tag, audiodata, step, sample_rate=44100):
    """Saves audio.

    NB: single channel only right now.

    Args:
      tag: str: label for this data
      audiodata: ndarray [Nsamples,]: audo data to be saves as wave.
        The data will be clipped to [-1, 1].

      step: int: training step
      sample_rate: sample rate of passed in audio buffer
    """
    audiodata = onp.array(audiodata)
    audiodata = onp.clip(onp.squeeze(audiodata), -1, 1)
    if audiodata.ndim != 1:
      raise ValueError('Audio data must be 1D.')
    # convert from [-1, 1] -> [-2^15-1, 2^15-1]
    sample_list = (32767.0 * audiodata).astype(int).tolist()
    wio = io.BytesIO()
    wav_buf = wave.open(wio, 'wb')
    wav_buf.setnchannels(1)
    wav_buf.setsampwidth(2)
    wav_buf.setframerate(sample_rate)
    enc = b''.join([struct.pack('<h', v) for v in sample_list])
    wav_buf.writeframes(enc)
    wav_buf.close()
    encoded_audio_bytes = wio.getvalue()
    wio.close()
    audio = Summary.Audio(
        sample_rate=sample_rate,
        num_channels=1,
        length_frames=len(sample_list),
        encoded_audio_string=encoded_audio_bytes,
        content_type='audio/wav')
    summary = Summary(value=[Summary.Value(tag=tag, audio=audio)])
    self._add_summary(summary, step)

  def histogram(self, tag, values, bins, step):
    """Saves histogram of values.

    Args:
      tag: str: label for this data
      values: ndarray: will be flattened by this routine
      bins: number of bins in histogram, or a sequence defining a monotonically
        increasing array of bin edges, including the rightmost edge.
      step: int: training step
    """
    values = onp.array(values)
    bins = onp.array(bins)
    values = onp.reshape(values, -1)
    counts, limits = onp.histogram(values, bins=bins)
    # boundary logic
    # TODO(flax-dev) Investigate whether this logic can be simplified.
    cum_counts = onp.cumsum(onp.greater(counts, 0, dtype=onp.int32))
    start, end = onp.searchsorted(
        cum_counts, [0, cum_counts[-1] - 1], side='right')
    start, end = int(start), int(end) + 1
    counts = (
        counts[start -
               1:end] if start > 0 else onp.concatenate([[0], counts[:end]]))
    limits = limits[start:end + 1]
    sum_sq = values.dot(values)
    histo = HistogramProto(
        min=values.min(),
        max=values.max(),
        num=len(values),
        sum=values.sum(),
        sum_squares=sum_sq,
        bucket_limit=limits.tolist(),
        bucket=counts.tolist())
    summary = Summary(value=[Summary.Value(tag=tag, histo=histo)])
    self._add_summary(summary, step)

  def text(self, tag, textdata, step):
    """Saves a text summary.

    Args:
      tag: str: label for this data
      textdata: string, or 1D/2D list/numpy array of strings
      step: int: training step
    Note: markdown formatting is rendered by tensorboard.
    """
    smd = SummaryMetadata(
        plugin_data=SummaryMetadata.PluginData(plugin_name='text'))
    if isinstance(textdata, (str, bytes)):
      tensor = tf.make_tensor_proto(
          values=[textdata.encode(encoding='utf_8')], shape=(1,))
    else:
      textdata = onp.array(textdata)  # convert lists, jax arrays, etc.
      datashape = onp.shape(textdata)
      if len(datashape) == 1:
        tensor = tf.make_tensor_proto(
            values=[td.encode(encoding='utf_8') for td in textdata],
            shape=(datashape[0],))
      elif len(datashape) == 2:
        tensor = tf.make_tensor_proto(
            values=[
                td.encode(encoding='utf_8') for td in onp.reshape(textdata, -1)
            ],
            shape=(datashape[0], datashape[1]))
    summary = Summary(
        value=[Summary.Value(tag=tag, metadata=smd, tensor=tensor)])
    self._add_summary(summary, step)
