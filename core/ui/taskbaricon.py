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

import wx,wx.adv

import config

class m_taskbar_icon(wx.adv.TaskBarIcon):
    TBMENU_CLOSE   = wx.NewIdRef()
    TBMENU_REMOVE  = wx.NewIdRef()

    def __init__(self,frame):
        wx.adv.TaskBarIcon.__init__(self, wx.adv.TBI_DOCK)
        self.frame = frame
        # 设置图标
        self.SetIcon(wx.Bitmap(config.assets["textures"]["icon"],wx.BITMAP_TYPE_ANY), "StarHunter")

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarActivate)
        self.Bind(wx.EVT_MENU, self.OnTaskBarClose, id=self.TBMENU_CLOSE)
        self.Bind(wx.EVT_MENU, self.OnTaskBarRemove, id=self.TBMENU_REMOVE)

    def __del__(self):
        pass

    # 创建菜单栏
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.TBMENU_CLOSE,   "关闭")
        menu.AppendSeparator()
        menu.Append(self.TBMENU_REMOVE, "移除任务栏图标")
        return menu

    def OnTaskBarActivate(self, event):
        if self.frame.IsIconized():
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
        self.frame.Raise()

    def OnTaskBarClose(self, event):
        wx.CallAfter(self.frame.Close)
        exit(0)

    def OnTaskBarRemove(self, event):
        self.RemoveIcon()