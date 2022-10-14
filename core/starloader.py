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

from core.ui.loaderui import my_loader_panel
from core.lib.starlog import starlog
from core.starmain import starmain

import config

log = starlog(__name__)

class starloader(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self,parent,title = u"模组加载",pos = wx.DefaultPosition, size = wx.Size( 650,360 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        self.is_opened = False

        self.pnl = my_loader_panel(self)

        self.SetIcon(wx.Icon(config.assets["textures"]["icon"]))

        #设置背景
        self.SetSizeHints( wx.DefaultSize, wx.Size( 650,370 ) )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.Bind(wx.EVT_BUTTON,self.refreshlist,id=self.pnl.m_b_refresh.GetId())
        self.Bind(wx.EVT_BUTTON,self.on_enter_click,id=self.pnl.m_b_gotomain.GetId())

        self.pnl.m_unuse_container = wx.FlexGridSizer( 0, 4, 0, 0 )
        self.pnl.m_unuse_container.SetFlexibleDirection( wx.BOTH )
        self.pnl.m_unuse_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        self.pnl.m_loader_unuse.SetSizer( self.pnl.m_unuse_container )

        self.pnl.m_use_container = wx.FlexGridSizer( 0, 4, 0, 0 )
        self.pnl.m_use_container.SetFlexibleDirection( wx.BOTH )
        self.pnl.m_use_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        self.pnl.m_loader_use.SetSizer( self.pnl.m_use_container )
        
    def __del__(self):
        pass

    def OnCLose(self,event):
        self.Hide()
        log.log("Close mod loader frame")
        self.is_opened = False

    def refreshlist(self,event):
        mod = wx.Button( self.pnl.m_loader_unuse, wx.ID_ANY, u'刷新', wx.DefaultPosition, wx.Size( 70,-1 ), wx.BU_AUTODRAW|0 )
        
        self.pnl.m_unuse_container.Add(mod)
        
        self.pnl.m_loader_unuse.Layout()
        self.pnl.Layout()
        pass

    def on_enter_click(self,event):
        log.log("Enter main frame and hide mod loader")
        self.Hide()
        main_frame = starmain(None)
        main_frame.Show()     

