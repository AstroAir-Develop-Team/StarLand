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
from core.ui.mainui import m_main_panel
from core.ui.starinfoui import m_starinfo_panel
from core.ui.weatherui import m_weather_panel
from core.ui.serverui import m_server_panel
from core.stardevice import stardevice

from core.ui.taskbaricon import m_taskbar_icon
from core.ui.aboutui import m_ahout_ui

import core.ui.images as imglib

import config

# 所有的内置库
from core.lib.qweather import Qweather
from core.lib.starlog import starlog
from core.lib.server import starserver

log = starlog(__name__)

class starmain(wx.Frame):
    
    def __init__(self,parent):

        log.log("Prepare main ui and load infomation")
        wx.Frame.__init__(self,parent,title = u"星空猎手",pos = wx.DefaultPosition, size = wx.Size( 660,410 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        self.pnl = m_main_panel(self)

        self.tb = m_taskbar_icon(self)
        self.SetIcon(wx.Icon(config.assets["textures"]["icon"]))

        #设置背景
        self.SetSizeHints( wx.DefaultSize, wx.Size( 660,410 ) )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.pnl.m_main_starinfo = m_starinfo_panel(self.pnl.m_main_starinfo)
        
        self.pnl.m_main_weather = m_weather_panel(self.pnl.m_main_weather)

        self.pnl.m_main_server = m_server_panel(self.pnl.m_main_server)
        
        self.pnl.m_main_device = stardevice(self.pnl.m_main_device)

        

        self.qweather = Qweather()
        self.server = starserver()

        self.pnl.m_main_server.m_native_start.Bind(wx.EVT_BUTTON,self.on_server_start,id=self.pnl.m_main_server.m_native_start.GetId())

        self.Bind(wx.EVT_CLOSE,self.OnClose)

        # 创建菜单
        self.m_menubar = wx.MenuBar( 0 )
        self.m_menu_file = wx.Menu()
        self.m_menuItem_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"退出"+ u"\t" + u"ALT + F4", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem_exit.SetBitmap(wx.Bitmap(config.assets["textures"]["menu"]["exit"],wx.BITMAP_TYPE_PNG))
        self.m_menu_file.Append( self.m_menuItem_exit )

        self.m_menubar.Append( self.m_menu_file, u"文件" )

        self.m_menu_help = wx.Menu()
        self.m_menuItem_ahout = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem_ahout.SetBitmap(wx.Bitmap(config.assets["textures"]["menu"]["about"],wx.BITMAP_TYPE_PNG))
        self.m_menu_help.Append( self.m_menuItem_ahout )

        self.m_menubar.Append( self.m_menu_help, u"帮助" )

        self.SetMenuBar( self.m_menubar )

        self.Centre( wx.BOTH )

        self.Bind( wx.EVT_MENU, self.on_exit_selected, id = self.m_menuItem_exit.GetId() )
        self.Bind( wx.EVT_MENU, self.on_show_help, id = self.m_menuItem_ahout.GetId() )

    def OnClose(self,event):
        self.Destroy()
        exit(0)

    def on_exit_selected( self, event ):
        exit(0)

    def on_show_help( self, event ):
        about = m_ahout_ui()
        about.OnAboutBox()

    def on_server_start(self,event):
        server_thread = threading.Thread(target=self.server.runserver)
        server_thread.setDaemon(True)
        server_thread.setName("Falsk thread")
        server_thread.start()    
