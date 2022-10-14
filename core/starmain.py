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

# 所有的内置UI
from core.ui.mainui import m_main_panel
from core.ui.starinfoui import m_starinfo_panel
from core.ui.weatherui import m_weather_panel
from core.ui.taskbaricon import m_taskbar_icon
from core.ui.serverui import m_server_panel
from core.ui.deviceui import m_device_panel

import config

# 所有的内置库
from core.lib.qweather import Qweather
from core.lib.starlog import starlog

log = starlog(__name__)

class starmain(wx.Frame):
    
    def __init__(self,parent):

        log.log("Prepare main ui and load infomation")
        wx.Frame.__init__(self,parent,title = u"星空猎手",pos = wx.DefaultPosition, size = wx.Size( 660,390 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        
        self.pnl = m_main_panel(self)
        self.tb = m_taskbar_icon(self)
        self.SetIcon(wx.Icon(config.assets["textures"]["icon"]))

        #设置背景
        self.SetSizeHints( wx.DefaultSize, wx.Size( 660,390 ) )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.pnl.m_main_starinfo = m_starinfo_panel(self.pnl.m_main_starinfo)
        self.pnl.m_main_weather = m_weather_panel(self.pnl.m_main_weather)
        self.pnl.m_main_server = m_server_panel(self.pnl.m_main_server)
        self.pnl.m_main_device = m_device_panel(self.pnl.m_main_device)

        self.qweather = Qweather()

        self.Bind(wx.EVT_CLOSE,self.OnClose)

        # 创建菜单
        self.m_menubar = wx.MenuBar( 0 )
        self.m_menu_file = wx.Menu()
        self.m_menuItem_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"退出"+ u"\t" + u"ALT + F4", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menuItem_exit )

        self.m_menubar.Append( self.m_menu_file, u"文件" )

        self.m_menu_help = wx.Menu()
        self.m_menuItem_ahout = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_help.Append( self.m_menuItem_ahout )

        self.m_menubar.Append( self.m_menu_help, u"帮助" )

        self.SetMenuBar( self.m_menubar )

        self.Centre( wx.BOTH )

        self.Bind( wx.EVT_MENU, self.on_exit_selected, id = self.m_menuItem_exit.GetId() )
        self.Bind( wx.EVT_MENU, self.on_show_help, id = self.m_menuItem_ahout.GetId() )

    def __del__(self):
        pass

    def OnClose(self,event):
        self.Destroy()
        exit(0)

    def on_exit_selected( self, event ):
        event.Skip()
        exit(0)

    def on_show_help( self, event ):
        event.Skip()


