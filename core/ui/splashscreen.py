# -*- coding: utf-8 -*-

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
from wx.adv import SplashScreen

import config

from core.ui.loaderui import my_loader_panel

class m_splash_screen(SplashScreen):
    def __init__(self):
        bmp = wx.Image(wx.opj(config.assets["textures"]["splash"])).ConvertToBitmap()
        SplashScreen.__init__(self, bmp,
                                 wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT,
                                 5000, None, -1)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.fc = wx.CallLater(1000, self.ShowMain)

    def OnClose(self, evt):
        evt.Skip()
        self.Hide()
        if self.fc.IsRunning():
            self.fc.Stop()
            self.ShowMain()

    def ShowMain(self):
        frame = wx.Frame(None)
        frame.Show()
        if self.fc.IsRunning():
            self.Raise()
        wx.CallAfter(frame.ShowTip)