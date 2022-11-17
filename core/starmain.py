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

# 所有的内置UI
from core.ui.mainui import m_main_frame
from core.ui.serverui import m_server_panel
from core.device.ui.stardeivce import stardevice

from core.starweather import starweather
from core.device.ui.stardeivce import stardevice

import config

# 所有的内置库
from core.lib.starlog import starlog

import gettext
_ = gettext.gettext

log = starlog(__name__)

import wx
import wx.xrc
import wx.aui

import gettext
_ = gettext.gettext

###########################################################################
## Class starmain
###########################################################################

class starmain ( m_main_frame ):

    def __init__( self, parent ):
        super().__init__ ( parent)  

        self.parent = parent
        self.SetIcon(wx.Icon(config.assets.get("textures").get("icon"),wx.BITMAP_TYPE_ICO))
        
        self.m_main_device = stardevice(self.m_main_device)
        self.m_main_server = m_server_panel(self.m_main_server)
        self.m_main_weather = starweather(self.m_main_weather)

    def __del__(self):
        return super().__del__()
    
    def on_frame_close(self, event):
        """Event on frame close"""
        log.log(_("Destroy main frame , it is the time to say goodbye"))
        self.Destroy()
        exit(0)

    def on_frame_hide(self, event):
        """Event on frame hide"""
        return super().on_frame_hide(event)

    def on_frame_show(self, event):
        """Event on frame show"""
        return super().on_frame_show(event)

    def on_page_close(self, event):
        """Event on aui noteboook page close"""
        print(str(event))
        return super().on_page_close(event)