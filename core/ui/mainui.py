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
## Class m_main_frame
###########################################################################

class m_main_frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Star Hunter"), pos = wx.DefaultPosition, size = wx.Size( 854,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menuItem_exit = wx.MenuItem( self.m_menu_file, wx.ID_ANY, _(u"退出")+ u"\t" + u"ALT + F4", _(u"结束你的星空之旅"), wx.ITEM_NORMAL )
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
		self.m_menu_help.Append( self.m_menuItem_ahout )

		self.m_menubar.Append( self.m_menu_help, _(u"帮助") )

		self.SetMenuBar( self.m_menubar )

		self.m_main_container = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.m_main_container, wx.aui.AuiPaneInfo() .Name( u"a_main_nb" ).Left() .CaptionVisible( False ).CloseButton( False ).PinButton( True ).PaneBorder( False ).Movable( False ).Dock().Fixed().BestSize( wx.Size( 854,480 ) ).MinSize( wx.Size( 854,480 ) ).CentrePane() )

		self.m_main_device = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_device.SetToolTip( _(u"Device Page") )

		self.m_main_container.AddPage( self.m_main_device, _(u"Device"), True, wx.NullBitmap )
		self.m_main_weather = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_weather.SetToolTip( _(u"Weather Page") )

		self.m_main_container.AddPage( self.m_main_weather, _(u"Weather"), False, wx.NullBitmap )
		self.m_main_starparser = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_starparser.SetToolTip( _(u"StarParser Page") )

		self.m_main_container.AddPage( self.m_main_starparser, _(u"StarParser"), False, wx.NullBitmap )
		self.m_main_starinfo = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_starinfo.SetToolTip( _(u"StarInfo Page") )

		self.m_main_container.AddPage( self.m_main_starinfo, _(u"StarInfo"), False, wx.NullBitmap )
		self.m_main_mod = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_mod.SetToolTip( _(u"Mod Page") )

		self.m_main_container.AddPage( self.m_main_mod, _(u"Mod"), False, wx.NullBitmap )
		self.m_main_config = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_config.SetToolTip( _(u"Config Page") )

		self.m_main_container.AddPage( self.m_main_config, _(u"Config"), False, wx.NullBitmap )

		self.m_statusbar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.m_mgr.Update()
		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_ACTIVATE, self.on_frame_activate )
		self.Bind( wx.EVT_CLOSE, self.on_frame_close )
		self.Bind( wx.EVT_HIBERNATE, self.on_frame_hide )
		self.Bind( wx.EVT_IDLE, self.on_frame_idle )
		self.Bind( wx.EVT_SHOW, self.on_frame_show )
		self.Bind( wx.EVT_MENU, self.on_exit_selected, id = self.m_menuItem_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.on_show_help, id = self.m_menuItem_ahout.GetId() )
		self.m_main_container.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.on_page_close )

	def __del__( self ):
		self.m_mgr.UnInit()



	# Virtual event handlers, override them in your derived class
	def on_frame_activate( self, event ):
		event.Skip()

	def on_frame_close( self, event ):
		event.Skip()

	def on_frame_hide( self, event ):
		event.Skip()

	def on_frame_idle( self, event ):
		event.Skip()

	def on_frame_show( self, event ):
		event.Skip()

	def on_exit_selected( self, event ):
		event.Skip()

	def on_show_help( self, event ):
		event.Skip()

	def on_page_close( self, event ):
		event.Skip()


