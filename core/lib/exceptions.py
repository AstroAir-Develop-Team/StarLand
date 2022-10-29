# coding=utf-8

"""

Copyright(c) 2022 Max Qian  <astroair.cn>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License version 3 as published by the Free Software Foundation.
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.
You should have received a copy of the GNU Library General Public License
along with this library; see the file COPYING.LIB.  If not, write to
the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
Boston, MA 02110-1301, USA.

"""

###########################################################################

class gps_timeout(Exception):
	"""Exception class for gps errors from the :mod: `astropanel` modules"""
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

###########################################################################

class ZWO_Error(Exception):
    """Exception class for errors returned from the :mod:`zwoasi` module."""
    def __init__(self, message):
        Exception.__init__(self, message)


class ZWO_IOError(ZWO_Error):
    """Exception class for all errors returned from the ASI SDK library."""
    def __init__(self, message, error_code=None):
        ZWO_Error.__init__(self, message)
        self.error_code = error_code

class ZWO_CaptureError(ZWO_Error):
    """Exception class for when :func:`Camera.capture()` fails."""
    def __init__(self, message, exposure_status=None):
        ZWO_Error.__init__(self, message)
        self.exposure_status = exposure_status

###########################################################################