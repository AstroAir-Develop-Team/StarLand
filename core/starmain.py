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
from core.ui.serverui import m_server_panel
from core.starweather import starweather
from core.stardevice import stardevice

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

class starmain(wx.Frame):
    
    def __init__(self,parent):

        log.log(_("Prepare main ui and load infomation"))
        wx.Frame.__init__(self,parent,title = _(u"星空猎手"),pos = wx.DefaultPosition, size = wx.Size( 660,410 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        self.pnl = m_main_panel(self)

        self.tb = m_taskbar_icon(self)
        self.SetIcon(wx.Icon(config.assets["textures"]["icon"]))

        #设置背景
        self.SetSizeHints( wx.DefaultSize, wx.Size( 660,410 ) )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        self.pnl.m_main_starinfo = m_starinfo_panel(self.pnl.m_main_starinfo)
        
        self.pnl.m_main_weather = starweather(self.pnl.m_main_weather)

        self.pnl.m_main_server = m_server_panel(self.pnl.m_main_server)
        
        self.pnl.m_main_device = stardevice(self.pnl.m_main_device)

        

        self.qweather = Qweather()
        self.server = starserver()

        self.pnl.m_main_server.m_native_start.Bind(wx.EVT_BUTTON,self.on_server_start,id=self.pnl.m_main_server.m_native_start.GetId())

        self.Bind(wx.EVT_CLOSE,self.OnClose)

        # 创建菜单
        self.m_menubar = wx.MenuBar( 0 )
        self.m_menu_file = wx.Menu()
        self.m_menuItem_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"退出")+ u"\t" + u"ALT + F4", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem_exit.SetBitmap(wx.Bitmap(config.assets["textures"]["menu"]["exit"],wx.BITMAP_TYPE_PNG))
        self.m_menu_file.Append( self.m_menuItem_exit )
        self.m_menubar.Append( self.m_menu_file, _(u"文件") )

        self.m_menu_gui = wx.Menu()
        self.m_menu_device = wx.Menu()
        self.m_menuItem_camera = wx.MenuItem( self.m_menu_device, wx.ID_ANY, _(u"相机"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_device.Append( self.m_menuItem_camera )

        self.m_menuItem__mount = wx.MenuItem( self.m_menu_device, wx.ID_ANY, _(u"赤道仪"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_device.Append( self.m_menuItem__mount )

        self.m_menuItem_guider = wx.MenuItem( self.m_menu_device, wx.ID_ANY, _(u"导星"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_device.Append( self.m_menuItem_guider )

        self.m_menuItem_focuser = wx.MenuItem( self.m_menu_device, wx.ID_ANY, _(u"电调"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_device.Append( self.m_menuItem_focuser )

        self.m_menuItem_align = wx.MenuItem( self.m_menu_device, wx.ID_ANY, _(u"校准"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_device.Append( self.m_menuItem_align )

        self.m_menu_gui.AppendSubMenu( self.m_menu_device, _(u"设备") )

        self.m_menu_weather = wx.Menu()
        self.m_menuItem_qweather = wx.MenuItem( self.m_menu_weather, wx.ID_ANY, _(u"和风天气"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_weather.Append( self.m_menuItem_qweather )

        self.m_menuItem_windy = wx.MenuItem( self.m_menu_weather, wx.ID_ANY, _(u"在线云图"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_weather.Append( self.m_menuItem_windy )

        self.m_menu_gui.AppendSubMenu( self.m_menu_weather, _(u"天气") )

        self.m_menu_search = wx.Menu()
        self.m_menuItem_offline = wx.MenuItem( self.m_menu_search, wx.ID_ANY, _(u"离线搜索"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_search.Append( self.m_menuItem_offline )

        self.m_menuItem_online = wx.MenuItem( self.m_menu_search, wx.ID_ANY, _(u"在线搜索"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_search.Append( self.m_menuItem_online )

        self.m_menu_gui.AppendSubMenu( self.m_menu_search, _(u"天体搜索") )

        self.m_menu_starinfo = wx.Menu()
        self.m_menuItem_sun = wx.MenuItem( self.m_menu_starinfo, wx.ID_ANY, _(u"太阳"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_starinfo.Append( self.m_menuItem_sun )

        self.m_menuItem_moon = wx.MenuItem( self.m_menu_starinfo, wx.ID_ANY, _(u"月球"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_starinfo.Append( self.m_menuItem_moon )

        self.m_menu_solar = wx.Menu()
        self.m_menuItem_mercury = wx.MenuItem( self.m_menu_solar, wx.ID_ANY, _(u"水星"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_solar.Append( self.m_menuItem_mercury )

        self.m_menuItem_venus = wx.MenuItem( self.m_menu_solar, wx.ID_ANY, _(u"金星"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_solar.Append( self.m_menuItem_venus )

        self.m_menuItem_earth = wx.MenuItem( self.m_menu_solar, wx.ID_ANY, _(u"地球"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_solar.Append( self.m_menuItem_earth )

        self.m_menuItem_mars = wx.MenuItem( self.m_menu_solar, wx.ID_ANY, _(u"火星"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_solar.Append( self.m_menuItem_mars )

        self.m_menuItem_jupiter = wx.MenuItem( self.m_menu_solar, wx.ID_ANY, _(u"木星"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_solar.Append( self.m_menuItem_jupiter )

        self.m_menuItem_satura = wx.MenuItem( self.m_menu_solar, wx.ID_ANY, _(u"土星"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_solar.Append( self.m_menuItem_satura )

        self.m_menuItem_urance = wx.MenuItem( self.m_menu_solar, wx.ID_ANY, _(u"天王星"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_solar.Append( self.m_menuItem_urance )

        self.m_menuItem_neptune = wx.MenuItem( self.m_menu_solar, wx.ID_ANY, _(u"海王星"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_solar.Append( self.m_menuItem_neptune )

        self.m_menu_starinfo.AppendSubMenu( self.m_menu_solar, _(u"太阳系") )

        self.m_menuItem_polar = wx.MenuItem( self.m_menu_starinfo, wx.ID_ANY, _(u"极轴"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_starinfo.Append( self.m_menuItem_polar )

        self.m_menu_gui.AppendSubMenu( self.m_menu_starinfo, _(u"天体信息") )

        self.m_menu_server = wx.Menu()
        self.m_menuItem_native = wx.MenuItem( self.m_menu_server, wx.ID_ANY, _(u"内置"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_server.Append( self.m_menuItem_native )

        self.m_menuItem_ascom = wx.MenuItem( self.m_menu_server, wx.ID_ANY, _(u"Ascom"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_server.Append( self.m_menuItem_ascom )

        self.m_menuItem_indi = wx.MenuItem( self.m_menu_server, wx.ID_ANY, _(u"INDI"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_server.Append( self.m_menuItem_indi )

        self.m_menuItem_novnc = wx.MenuItem( self.m_menu_server, wx.ID_ANY, _(u"noVNC"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_server.Append( self.m_menuItem_novnc )

        self.m_menu_gui.AppendSubMenu( self.m_menu_server, _(u"服务器") )

        self.m_menubar.Append( self.m_menu_gui, _(u"界面") )

        self.m_menu_help = wx.Menu()
        self.m_menuItem_ahout = wx.MenuItem( self.m_menu_help, wx.ID_ANY, _(u"关于"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuItem_ahout.SetBitmap(wx.Bitmap(config.assets["textures"]["menu"]["about"],wx.BITMAP_TYPE_PNG))
        self.m_menu_help.Append( self.m_menuItem_ahout )

        self.m_menubar.Append( self.m_menu_help, _(u"帮助") )

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
