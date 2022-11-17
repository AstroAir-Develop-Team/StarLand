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

import wx

from core.ui.cameraui import m_camera
from core.device.camera.zwoasi import zwoasi

class starcamera(m_camera):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size( 1920,1080 ), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        super().__init__(parent, id, pos, size, style, name)
    
    def __del__(self):
        return super().__del__()

    def on_camera_start(self, event):
        return super().on_camera_start(event)

    def on_camera_stop(self, event):
        return super().on_camera_stop(event)

    def on_startcool_click(self, event):
        return super().on_startcool_click(event)

    def on_stopcool_click(self, event):
        return super().on_stopcool_click(event)

    def on_coolon_click(self, event):
        return super().on_coolon_click(event)

    def on_cooloff_click(self, event):
        return super().on_cooloff_click(event)

    def on_queue_start(self, event):
        return super().on_queue_start(event)
    
    def on_queue_stop(self, event):
        return super().on_queue_stop(event)

    def on_temp_click(self, event):
        return super().on_temp_click(event)

    def on_temp_click(self, event):
        return super().on_temp_click(event)