# Copyright 2008 Mike Wakerly <opensource@hoho.com>
#
# This file is part of the Kegboard package of the Kegbot project.
# For more information on Kegboard or Kegbot, see http://kegbot.org/
#
# Kegboard is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Kegboard is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Kegboard.  If not, see <http://www.gnu.org/licenses/>.

import io
import struct

from .exceptions import KegboardError, UnknownMessageError
from . import util
from . import crc16


KBSP_PREFIX = b"KBSP v1:"
KBSP_PAYLOAD_MAXLEN = 112
KBSP_TRAILER = b"\r\n"
KBSP_MAXLEN = KBSP_PAYLOAD_MAXLEN + len(KBSP_PREFIX) + len(KBSP_TRAILER)


class Field(util.Field):
  def __init__(self, tagnum):
    self.tagnum = tagnum

  def ToBytes(self, value):
    raise NotImplementedError

  def ToString(self, value):
    return str(value)

  def _Validate(self, value):
    pass

  def ParseValue(self, value):
    self._Validate(value)
    return value


class StructField(Field):
  _STRUCT_FORMAT = '<'
  def __init__(self, tagnum):
    Field.__init__(self, tagnum)
    self._packed_size = struct.calcsize(self._STRUCT_FORMAT)

  def ParseValue(self, value):
    if len(value) != self._packed_size:
      raise ValueError("Bad length, must be exactly {} bytes".format(self._packed_size))
    return struct.unpack(self._STRUCT_FORMAT, value)[0]

  def ToBytes(self, value):
    return struct.pack(self._STRUCT_FORMAT, value)


class Uint8Field(StructField):
  _STRUCT_FORMAT = 'B'


class Uint16Field(StructField):
  _STRUCT_FORMAT = '<H'


class Int32Field(StructField):
  _STRUCT_FORMAT = '<i'


class Uint32Field(StructField):
  _STRUCT_FORMAT = '<I'


class Uint64Field(StructField):
  _STRUCT_FORMAT = '<Q'


class OnewireIdField(Uint64Field):
  def ToString(self, value):
    return "0x%x" % (value,)


class StringField(Field):
  def ParseValue(self, bytes):
    return bytes.strip(b'\x00').decode('ascii')

  def ToBytes(self, value):
    return value.encode() + b'\x00'


class BytesField(Field):
  def ToString(self, value):
    return '0x%s' % ''.join('%02x' % ord(c) for c in value)

  def ParseValue(self, bytes):
    return bytes

  def ToBytes(self, value):
    return value


class OutputField(Uint16Field):
  def ParseValue(self, bytes):
    if bytes.strip('\x00'):
      return 1
    else:
      return 0

  def ToString(self, value):
    if value:
      return 'on'
    else:
      return 'off'


class TempField(Int32Field):
  def ParseValue(self, value):
    value = Int32Field.ParseValue(self, value)
    value /= 1000000.0
    return value


class BaseMessage(metaclass=util.DeclarativeMetaclass):
  def __init__(self, initial=None, **kwargs):
    self._fields = self.fields.copy()
    self._values = dict((k, None) for k in list(self._fields.keys()))

    if initial is not None:
      self._UpdateFromDict(initial)
    else:
      self._UpdateFromDict(kwargs)

  def __setattr__(self, name, value):
    if name != '_fields' and name in self._fields:
      parsed = self._fields[name].ParseValue(value)
      self._values[name] = parsed
    else:
      super(BaseMessage, self).__setattr__(name, value)

  def __getattr__(self, name):
    if name in self.__class__.fields:
      return self._values[name]
    raise AttributeError('No such field {}'.format(name))

  def __str__(self):
    clsname = self.__class__.__name__
    vallist = []
    for fieldname, fieldvalue in self._values.items():
      field = self._fields[fieldname]
      vallist.append('%s=%s' % (fieldname, field.ToString(fieldvalue)))
    valstr = (' '.join(vallist))
    return '<%s: %s>' % (clsname, valstr)

  def __iter__(self):
    for name, field in list(self._GetFields().items()):
      yield field

  def __eq__(self, other):
    if not other or type(other) != type(self):
      return False
    return self._values == other._values

  def _GetFields(self):
    return self._fields

  def _UpdateFromDict(self, d):
    for k, v in d.items():
      setattr(self, k, v)

  def AsDict(self):
    ret = {}
    for k, v in self._fields.items():
      ret[k] = self._values.get(k)
    return ret

  def SetValue(self, fieldname, value):
    if fieldname not in self._values:
      raise KeyError
    self._values[fieldname] = value


class Message(BaseMessage):
  def __init__(self, initial=None, bytes=None, payload_bytes=None, **kwargs):
    BaseMessage.__init__(self, initial, **kwargs)
    self._tag_to_field_name = {}
    for name, field in self._fields.items():
      self._tag_to_field_name[field.tagnum] = name
    if bytes is not None:
      self.UnpackFromBytes(bytes)
    if payload_bytes is not None:
      self.UnpackFromPayload(payload_bytes)

  def UnpackFromBytes(self, bytes_or_string):
    if hasattr(bytes_or_string, 'decode'):
      input_bytes = bytes_or_string
    else:
      input_bytes = bytes_or_string.encode()

    if len(input_bytes) < 16:
      raise ValueError("Not enough bytes")

    header = input_bytes[:12]
    payload = input_bytes[12:-4]
    trailer = input_bytes[-4:]
    crcd_bytes = input_bytes[:-2]

    prefix, message_id, message_len = struct.unpack('<8sHH', header)

    if len(payload) != message_len:
      raise ValueError("Payload size does not match tag")

    # TODO(mikey): assert checked_crc == 0
    checked_crc = crc16.crc16_ccitt(crcd_bytes)
    self.UnpackFromPayload(payload)

  def UnpackFromPayload(self, payload):
    pos = 0
    payload_len = len(payload)
    while (pos + 2) <= payload_len:
      fieldlen = self._ParseField(payload[pos:])
      pos += 2 + fieldlen

  def _ParseField(self, field_bytes):
    tag, length = struct.unpack('<BB', field_bytes[:2])
    data = field_bytes[2:2+length]
    # If field number is known, set its value. (Ignore it otherwise.)
    field_name = self._tag_to_field_name.get(tag)
    if field_name:
      setattr(self, field_name, data)
    return length

  def ToBytes(self):
    payload = bytes([])
    for field_name, field in self._fields.items():
      field_bytes = field.ToBytes(self._values[field_name])
      payload += struct.pack('<BB', field.tagnum, len(field_bytes))
      payload += field_bytes

    out = bytes(KBSP_PREFIX)
    out += struct.pack('<HH', self.MESSAGE_ID, len(payload))
    out += payload
    crc = crc16.crc16_ccitt(out)
    out += struct.pack('<H', crc)
    out += KBSP_TRAILER
    return out


class HelloMessage(Message):
  MESSAGE_ID = 0x01
  firmware_version = Uint16Field(0x01)
  protocol_version = Uint16Field(0x02)
  serial_number = StringField(0x03)
  uptime_millis = Uint32Field(0x04)
  uptime_days = Uint32Field(0x05)


class ConfigurationMessage(Message):
  MESSAGE_ID = 0x02
  board_name = StringField(0x01)
  baud_rate = Uint16Field(0x02)
  update_interval = Uint16Field(0x03)


class MeterStatusMessage(Message):
  MESSAGE_ID = 0x10
  meter_name = StringField(0x01)
  meter_reading = Uint32Field(0x02)


class TemperatureReadingMessage(Message):
  MESSAGE_ID = 0x11
  sensor_name = StringField(0x01)
  sensor_reading = TempField(0x02)


class OutputStatusMessage(Message):
  MESSAGE_ID = 0x12
  output_name = StringField(0x01)
  output_reading = OutputField(0x02)


class OnewirePresenceMessage(Message):
  """Deprecated."""
  MESSAGE_ID = 0x13
  device_id = OnewireIdField(0x01)
  status = Uint8Field(0x02)


class AuthTokenMessage(Message):
  MESSAGE_ID = 0x14
  device = StringField(0x01)
  token = BytesField(0x02)
  status = Uint8Field(0x03)


class PingCommand(Message):
  MESSAGE_ID = 0x81


class SetOutputCommand(Message):
  MESSAGE_ID = 0x84
  output_id = Uint8Field(0x01)
  output_mode = OutputField(0x02)


class SetSerialNumberCommand(Message):
  MESSAGE_ID = 0x85
  serial_number = StringField(0x01)


MESSAGE_ID_TO_CLASS = {}
for cls in Message.__subclasses__():
  idnum = cls.MESSAGE_ID
  if idnum in MESSAGE_ID_TO_CLASS:
    raise RuntimeError("More than one message for id: {}".format(idnum))
  MESSAGE_ID_TO_CLASS[idnum] = cls


def get_message_for_bytes(bytes):
  if len(bytes) < 6:
    raise ValueError("Not enough bytes")
  prefix, message_id = struct.unpack('<8sH', bytes[:10])
  cls = MESSAGE_ID_TO_CLASS.get(message_id)
  if not cls:
    raise UnknownMessageError
  return cls(bytes=bytes)


def get_message_by_id(message_id, payload_bytes=None):
  cls = MESSAGE_ID_TO_CLASS.get(message_id)
  if not cls:
    raise UnknownMessageError
  return cls(payload_bytes=payload_bytes)

