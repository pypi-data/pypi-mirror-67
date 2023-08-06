# Copyright 2008 Mike Wakerly <opensource@hoho.com>
#
# This file is part of the Pykeg package of the Kegbot project.
# For more information on Pykeg or Kegbot, see http://kegbot.org/
#
# Pykeg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Pykeg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pykeg.  If not, see <http://www.gnu.org/licenses/>.

"""General purpose utilities, bits, and bobs"""

import errno
import os
import sys
import traceback
from collections import OrderedDict


class Field:
  """Base field type for use with DeclarativeMetaclass."""


class DeclarativeMetaclass(type):
  """Collect Fields declared on the base classes, and exposes as `.fields`.
  
  Borrowed from django.forms.ModelForm.
  """
  def __new__(mcs, name, bases, attrs):
    fields = []
    for key, value in list(attrs.items()):
      if isinstance(value, Field):
        fields.append((key, value))
        attrs.pop(key)
    attrs['fields'] = OrderedDict(fields)
    new_class = super(DeclarativeMetaclass, mcs).__new__(mcs, name, bases, attrs)
    return new_class

  @classmethod
  def __prepare__(metacls, name, bases, **kwds):
    return OrderedDict()


def daemonize():
  # Fork once
  if os.fork() != 0:
    os._exit(0)
  os.setsid()  # Create new session
  # Fork twice
  if os.fork() != 0:
    os._exit(0)
  #os.chdir("/")
  os.umask(0)

  os.close(sys.__stdin__.fileno())
  os.close(sys.__stdout__.fileno())
  os.close(sys.__stderr__.fileno())

  os.open('/dev/null', os.O_RDONLY)
  os.open('/dev/null', os.O_RDWR)
  os.open('/dev/null', os.O_RDWR)

def PidIsAlive(pid):
  try:
    os.kill(pid, 0)
  except OSError as e:
    if e.errno == errno.ESRCH:
      return False
  return True

def LogTraceback(log_method, tb_tuple=None):
  if tb_tuple is None:
    tb_tuple = sys.exc_info()

  tb_type, tb_value, tb_obj = tb_tuple

  if tb_obj is None:
    log_method('No exception')
    return
  stack = traceback.extract_tb(tb_obj)
  for frame in traceback.format_list(stack):
    for line in frame.split('\n'):
      log_method('    ' + line.strip())
  log_method('Error was: %s: %s' % (tb_type, tb_value))
