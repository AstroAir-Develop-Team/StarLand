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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 780,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.m_server_nb = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.m_server_nb, wx.aui.AuiPaneInfo() .Name( u"a_server_nb" ).Left() .Caption( _(u"Server") ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Floatable( False ).MinSize( wx.Size( 300,-1 ) ).CentrePane() )

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

		m_buildin_main_container3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_buildin_main_container3.SetFlexibleDirection( wx.BOTH )
		m_buildin_main_container3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_buildin_start = wx.Button( self.m_server_buildin_panel, wx.ID_ANY, _(u"Start"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_buildin_main_container3.Add( self.m_buildin_start, 0, wx.ALL, 5 )

		self.m_buildin_stop = wx.Button( self.m_server_buildin_panel, wx.ID_ANY, _(u"Stop"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_buildin_main_container3.Add( self.m_buildin_stop, 0, wx.ALL, 5 )

		self.m_buildin_restart = wx.Button( self.m_server_buildin_panel, wx.ID_ANY, _(u"Restart"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_buildin_main_container3.Add( self.m_buildin_restart, 0, wx.ALL, 5 )

		self.m_buildin_open = wx.Button( self.m_server_buildin_panel, wx.ID_ANY, _(u"Open"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_buildin_main_container3.Add( self.m_buildin_open, 0, wx.ALL, 5 )


		m_buildin_main_box.Add( m_buildin_main_container3, 1, wx.EXPAND, 5 )


		m_buildin_container.Add( m_buildin_main_box, 1, wx.EXPAND, 5 )


		m_buildin_box.Add( m_buildin_container, 1, wx.EXPAND, 5 )


		self.m_server_buildin_panel.SetSizer( m_buildin_box )
		self.m_server_buildin_panel.Layout()
		m_buildin_box.Fit( self.m_server_buildin_panel )
		self.m_server_nb.AddPage( self.m_server_buildin_panel, _(u"Buildin"), True, wx.NullBitmap )
		self.m_panel57 = wx.Panel( self.m_server_nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_server_nb.AddPage( self.m_panel57, _(u"ASCOM"), False, wx.NullBitmap )
		self.m_panel58 = wx.Panel( self.m_server_nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
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

		self.m_terminal_panel = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.m_terminal_panel, wx.aui.AuiPaneInfo() .Name( u"a_terminal_nb" ).Left() .Caption( _(u"Terminal") ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Floatable( False ).CentrePane() )

		self.m_shell_panel = wx.Panel( self.m_terminal_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer78 = wx.BoxSizer( wx.VERTICAL )

		fgSizer109 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer109.SetFlexibleDirection( wx.BOTH )
		fgSizer109.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer80 = wx.BoxSizer( wx.VERTICAL )

		self.m_button89 = wx.Button( self.m_shell_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.m_button89, 0, wx.ALL, 5 )

		self.m_button90 = wx.Button( self.m_shell_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.m_button90, 0, wx.ALL, 5 )

		self.m_button91 = wx.Button( self.m_shell_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_button92 = wx.Button( self.m_shell_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.m_button92, 0, wx.ALL, 5 )

		self.m_button93 = wx.Button( self.m_shell_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.m_button93, 0, wx.ALL, 5 )

		self.m_button94 = wx.Button( self.m_shell_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.m_button94, 0, wx.ALL, 5 )

		self.m_button95 = wx.Button( self.m_shell_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer80.Add( self.m_button95, 0, wx.ALL, 5 )


		fgSizer109.Add( bSizer80, 1, wx.EXPAND, 5 )

		fgSizer111 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer111.SetFlexibleDirection( wx.BOTH )
		fgSizer111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel65 = wx.Panel( self.m_shell_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel65.SetMinSize( wx.Size( 400,200 ) )

		fgSizer111.Add( self.m_panel65, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer82 = wx.BoxSizer( wx.VERTICAL )

		fgSizer112 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer112.SetFlexibleDirection( wx.BOTH )
		fgSizer112.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText278 = wx.StaticText( self.m_shell_panel, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText278.Wrap( -1 )

		fgSizer112.Add( self.m_staticText278, 0, wx.ALL, 5 )

		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self.m_shell_panel, wx.ID_ANY, _(u"Combo!"), wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		fgSizer112.Add( self.m_comboBox1, 0, wx.ALL, 5 )


		bSizer82.Add( fgSizer112, 1, wx.EXPAND, 5 )


		fgSizer111.Add( bSizer82, 1, wx.EXPAND, 5 )


		fgSizer109.Add( fgSizer111, 1, wx.EXPAND, 5 )


		bSizer78.Add( fgSizer109, 1, wx.EXPAND, 5 )


		self.m_shell_panel.SetSizer( bSizer78 )
		self.m_shell_panel.Layout()
		bSizer78.Fit( self.m_shell_panel )
		self.m_terminal_panel.AddPage( self.m_shell_panel, _(u"Shell"), True, wx.NullBitmap )
		self.m_python_panel = wx.Panel( self.m_terminal_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_terminal_panel.AddPage( self.m_python_panel, _(u"Python"), False, wx.NullBitmap )
		self.m_debug_panel = wx.Panel( self.m_terminal_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_terminal_panel.AddPage( self.m_debug_panel, _(u"Debug"), False, wx.NullBitmap )


		self.m_mgr.Update()

	def __del__( self ):
		self.m_mgr.UnInit()



