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

from core.lib.pyascom.camera import Camera
from core.lib.pyascom.telescope import Telescope
from core.lib.pyascom.focuser import Focuser
from core.lib.pyascom.filterwheel import FilterWheel
from core.lib.pyascom.dome import Dome

import core.lib.socket

class star_camera(Camera):
    """
    Camera driver for StarHunter base on ASCOM
    """
    def __init__(self, address: str, device_number: int, protocol: str = "http"):
        super().__init__(address, device_number, protocol)

class star_telescope(Telescope):
    """
    Telescope driver for StarHunter base on ASCOM
    """
    def __init__(self, address: str, device_number: int, protocol: str = "http"):
        super().__init__(address, device_number, protocol)

class star_focuser(Focuser):
    """
    Focuser driver for StarHunter base on ASCOM
    """
    def __init__(self, address: str, device_number: int, protocol: str = "http"):
        super().__init__(address, device_number, protocol)

class star_filterwheel(FilterWheel):
    """
    Filterwheel driver for StarHunter base on ASCOM
    """
    def __init__(self, address: str, device_number: int, protocol: str = "http"):
        super().__init__(address, device_number, protocol)

class star_dome(Dome):
    """
    Dome driver for StarHunter base on ASCOM
    """
    def __init__(self, address: str, device_number: int, protocol: str = "http"):
        super().__init__(address, device_number, protocol)