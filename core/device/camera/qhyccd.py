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

import os
import ctypes

from core.lib.starlog import starlog

log = starlog(__name__)

class qhyccd():

    def __init__(self) -> None:
        """Initialize"""
        self.qhylib = None

    def __del__(self) -> None:
        """Close"""
        self.disconnect()

    def init(self) -> None:
        """Initialize"""
        if self.qhylib is not None:
            return
        _p = os.path.join
        libpath = _p(_p(os.getcwd(),"lib"),"qhyccd")
        # 判断系统位数 - 32/64
        if 'PROGRAMFILES(X86)' in os.environ:
            libpath = _p(_p(libpath,"x64"),"qhyccd.dll")
        else:
            libpath = _p(_p(libpath,"x86"),"qhyccd.dll")
        # 检查库是否存在
        if os.path.isfile(libpath):
            log.log(f"Find {libpath}")
        else:
            log.loge(f"Failed to find {libpath}")
        # 加载动态库
        self.qhylib = ctypes.cdll.LoadLibrary(libpath)
        self.init_dll()

    def init_dll(self) -> None:
        """Initialize qhyccd library"""
    
    def connect(self,name) -> dict:
        """Connect"""

    def disconnect(self) -> dict:
        """Disconnect"""