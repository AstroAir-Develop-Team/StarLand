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
## Class m_server_panel
###########################################################################

class m_server_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 2000,1200 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 780,600 ) )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.m_server_nb = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.m_server_nb, wx.aui.AuiPaneInfo() .Name( u"a_server_nb" ).Left() .Caption( _(u"Server") ).CaptionVisible( False ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Fixed().DockFixed( True ).Floatable( False ).BestSize( wx.Size( 260,-1 ) ).MinSize( wx.Size( 260,300 ) ) )

		self.m_server_buildin_panel = wx.Panel( self.m_server_nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_buildin_box = wx.BoxSizer( wx.VERTICAL )

		m_buildin_container = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_buildin_container.SetFlexibleDirection( wx.BOTH )
		m_buildin_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_buildin_title_box = wx.BoxSizer( wx.VERTICAL )

		m_buildin_title_container = wx.FlexGridSizer( 0, 3, 0, 0 )
		m_buildin_title_container.SetFlexibleDirection( wx.BOTH )
		m_buildin_title_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buildin_title = wx.StaticText( self.m_server_buildin_panel, wx.ID_ANY, _(u"Buildin Server"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buildin_title.Wrap( -1 )

		m_buildin_title_container.Add( self.m_buildin_title, 0, wx.ALL, 5 )

		self.m_buildin_status = wx.StaticText( self.m_server_buildin_panel, wx.ID_ANY, _(u"Status"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buildin_status.Wrap( -1 )

		m_buildin_title_container.Add( self.m_buildin_status, 0, wx.ALL, 5 )

		self.m_buildin_status_icon = wx.StaticBitmap( self.m_server_buildin_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_buildin_title_container.Add( self.m_buildin_status_icon, 0, wx.ALL, 5 )


		m_buildin_title_box.Add( m_buildin_title_container, 1, wx.EXPAND, 5 )


		m_buildin_container.Add( m_buildin_title_box, 1, wx.EXPAND, 5 )

		m_buildin_main_box = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		m_buildin_main_container1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_buildin_main_container1.SetFlexibleDirection( wx.BOTH )
		m_buildin_main_container1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buildin_host_t = wx.StaticText( self.m_server_buildin_panel, wx.ID_ANY, _(u"Host"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buildin_host_t.Wrap( -1 )

		m_buildin_main_container1.Add( self.m_buildin_host_t, 0, wx.ALL, 5 )

		self.m_buildin_host = wx.TextCtrl( self.m_server_buildin_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buildin_host.SetMaxLength( 50 )
		m_buildin_main_container1.Add( self.m_buildin_host, 0, wx.ALL, 5 )

		self.m_buildin_port_t = wx.StaticText( self.m_server_buildin_panel, wx.ID_ANY, _(u"Port"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buildin_port_t.Wrap( -1 )

		m_buildin_main_container1.Add( self.m_buildin_port_t, 0, wx.ALL, 5 )

		self.m_buildin_port = wx.TextCtrl( self.m_server_buildin_panel, wx.ID_ANY, _(u"8000"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buildin_port.SetMaxLength( 4 )
		m_buildin_main_container1.Add( self.m_buildin_port, 0, wx.ALL, 5 )


		m_buildin_main_box.Add( m_buildin_main_container1, 1, wx.EXPAND, 5 )

		m_buildin_main_container2 = wx.FlexGridSizer( 0, 4, 0, 0 )
		m_buildin_main_container2.SetFlexibleDirection( wx.BOTH )
		m_buildin_main_container2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buildin_ssl_t = wx.StaticText( self.m_server_buildin_panel, wx.ID_ANY, _(u"SSL"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buildin_ssl_t.Wrap( -1 )

		m_buildin_main_container2.Add( self.m_buildin_ssl_t, 0, wx.ALL, 5 )

		self.m_buildin_ssl_c = wx.CheckBox( self.m_server_buildin_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_buildin_main_container2.Add( self.m_buildin_ssl_c, 0, wx.ALL, 5 )

		self.m_buildin_alone_t = wx.StaticText( self.m_server_buildin_panel, wx.ID_ANY, _(u"Standard"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_buildin_alone_t.Wrap( -1 )

		m_buildin_main_container2.Add( self.m_buildin_alone_t, 0, wx.ALL, 5 )

		self.m_buildin_alone = wx.CheckBox( self.m_server_buildin_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_buildin_main_container2.Add( self.m_buildin_alone, 0, wx.ALL, 5 )


		m_buildin_main_box.Add( m_buildin_main_container2, 1, wx.EXPAND, 5 )

		m_buildin_main_container3 = wx.FlexGridSizer( 0, 3, 0, 0 )
		m_buildin_main_container3.SetFlexibleDirection( wx.BOTH )
		m_buildin_main_container3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buildin_start = wx.Button( self.m_server_buildin_panel, wx.ID_ANY, _(u"Start"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_buildin_main_container3.Add( self.m_buildin_start, 0, wx.ALL, 5 )

		self.m_buildin_stop = wx.Button( self.m_server_buildin_panel, wx.ID_ANY, _(u"Stop"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_buildin_main_container3.Add( self.m_buildin_stop, 0, wx.ALL, 5 )

		self.m_buildin_restart = wx.Button( self.m_server_buildin_panel, wx.ID_ANY, _(u"Restart"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_buildin_main_container3.Add( self.m_buildin_restart, 0, wx.ALL, 5 )


		m_buildin_main_box.Add( m_buildin_main_container3, 1, wx.EXPAND, 0 )


		m_buildin_container.Add( m_buildin_main_box, 1, wx.EXPAND, 5 )


		m_buildin_box.Add( m_buildin_container, 1, wx.EXPAND, 5 )


		self.m_server_buildin_panel.SetSizer( m_buildin_box )
		self.m_server_buildin_panel.Layout()
		m_buildin_box.Fit( self.m_server_buildin_panel )
		self.m_server_nb.AddPage( self.m_server_buildin_panel, _(u"Buildin"), True, wx.NullBitmap )
		self.m_panel57 = wx.Panel( self.m_server_nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer58 = wx.BoxSizer( wx.VERTICAL )


		self.m_panel57.SetSizer( bSizer58 )
		self.m_panel57.Layout()
		bSizer58.Fit( self.m_panel57 )
		self.m_server_nb.AddPage( self.m_panel57, _(u"ASCOM"), False, wx.NullBitmap )
		self.m_panel58 = wx.Panel( self.m_server_nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer59 = wx.BoxSizer( wx.VERTICAL )


		self.m_panel58.SetSizer( bSizer59 )
		self.m_panel58.Layout()
		bSizer59.Fit( self.m_panel58 )
		self.m_server_nb.AddPage( self.m_panel58, _(u"INDI"), False, wx.NullBitmap )
		self.m_panel59 = wx.Panel( self.m_server_nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer77 = wx.BoxSizer( wx.VERTICAL )

		fgSizer107 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer107.SetFlexibleDirection( wx.BOTH )
		fgSizer107.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer108 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer108.SetFlexibleDirection( wx.BOTH )
		fgSizer108.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer108.Add( gbSizer5, 1, wx.EXPAND, 5 )


		fgSizer107.Add( fgSizer108, 1, wx.EXPAND, 5 )


		bSizer77.Add( fgSizer107, 1, wx.EXPAND, 5 )


		self.m_panel59.SetSizer( bSizer77 )
		self.m_panel59.Layout()
		bSizer77.Fit( self.m_panel59 )
		self.m_server_nb.AddPage( self.m_panel59, _(u"WebClient"), False, wx.NullBitmap )

		self.m_server_web_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.m_server_web_panel, wx.aui.AuiPaneInfo() .Name( u"a_server_web" ).Left() .CaptionVisible( False ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Fixed().DockFixed( True ).Floatable( False ).MinSize( wx.Size( 300,300 ) ).CentrePane() )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		self.m_button65 = wx.Button( self.m_server_web_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.m_button65, 0, wx.ALL, 5 )


		self.m_server_web_panel.SetSizer( bSizer60 )
		self.m_server_web_panel.Layout()
		bSizer60.Fit( self.m_server_web_panel )

		self.m_mgr.Update()

		# Connect Events
		self.m_buildin_host.Bind( wx.EVT_TEXT, self.on_host_update )
		self.m_buildin_host.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_buildin_port.Bind( wx.EVT_TEXT, self.on_port_update )
		self.m_buildin_port.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_buildin_ssl_c.Bind( wx.EVT_CHECKBOX, self.on_server_ssl )
		self.m_buildin_alone.Bind( wx.EVT_CHECKBOX, self.on_server_alone )
		self.m_buildin_start.Bind( wx.EVT_BUTTON, self.on_server_start )
		self.m_buildin_stop.Bind( wx.EVT_BUTTON, self.on_server_stop )
		self.m_buildin_restart.Bind( wx.EVT_BUTTON, self.on_server_restart )

	def __del__( self ):
		self.m_mgr.UnInit()



	# Virtual event handlers, override them in your derived class
	def on_host_update( self, event ):
		event.Skip()

	def on_max_length( self, event ):
		event.Skip()

	def on_port_update( self, event ):
		event.Skip()


	def on_server_ssl( self, event ):
		event.Skip()

	def on_server_alone( self, event ):
		event.Skip()

	def on_server_start( self, event ):
		event.Skip()

	def on_server_stop( self, event ):
		event.Skip()

	def on_server_restart( self, event ):
		event.Skip()


