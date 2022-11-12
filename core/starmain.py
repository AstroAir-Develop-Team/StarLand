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
import threading

# 所有的内置UI
from core.ui.mainui import m_main_frame
from core.ui.starinfoui import m_starinfo_panel
from core.ui.serverui import m_server_panel
from core.ui.deviceui import m_device_panel
from core.starweather import starweather
from core.stardevice import stardevice
from core.starsearch import starsearch

from core.ui.taskbaricon import m_taskbar_icon
from core.ui.aboutui import m_ahout_ui

import core.ui.images as imglib

import config

# 所有的内置库
from core.lib.qweather import Qweather
from core.lib.starlog import starlog
from core.lib.server import starserver

import gettext
_ = gettext.gettext

log = starlog(__name__)

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-8e3463c)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

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
        
        self.m_main_device = m_device_panel(self.m_main_device)
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