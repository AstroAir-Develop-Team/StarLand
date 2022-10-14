import wx

###########################################################################
## Class m_mod_main
###########################################################################

class my_loader_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		m_mod_container = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_mod_container.SetFlexibleDirection( wx.BOTH )
		m_mod_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_loader_infobar = wx.InfoBar( self )
		self.m_loader_infobar.SetShowHideEffects( wx.SHOW_EFFECT_SLIDE_TO_BOTTOM, wx.SHOW_EFFECT_NONE )
		self.m_loader_infobar.SetEffectDuration( 500 )
		m_mod_container.Add( self.m_loader_infobar, 0, wx.ALL, 5 )

		m_mod_loader = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_mod_loader.SetFlexibleDirection( wx.BOTH )
		m_mod_loader.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_loader_title = wx.FlexGridSizer( 0, 5, 0, 0 )
		m_loader_title.SetFlexibleDirection( wx.BOTH )
		m_loader_title.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		m_loader_title.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_loader_icon = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_loader_title.Add( self.m_loader_icon, 0, wx.ALL, 5 )

		self.m_loader_text = wx.StaticText( self, wx.ID_ANY, u"模组加载", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_loader_text.Wrap( -1 )

		m_loader_title.Add( self.m_loader_text, 0, wx.ALL, 5 )

		self.m_loader_help = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		m_loader_title.Add( self.m_loader_help, 0, wx.ALL, 5 )


		m_loader_title.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		m_mod_loader.Add( m_loader_title, 1, wx.EXPAND, 5 )

		m_loader_container = wx.FlexGridSizer( 0, 3, 0, 0 )
		m_loader_container.SetFlexibleDirection( wx.BOTH )
		m_loader_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_loader_unuse = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_loader_unuse.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		m_unuse_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_unuse_container.SetFlexibleDirection( wx.BOTH )
		m_unuse_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		self.m_loader_unuse.SetSizer( m_unuse_container )
		self.m_loader_unuse.Layout()
		m_unuse_container.Fit( self.m_loader_unuse )
		m_loader_container.Add( self.m_loader_unuse, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_loader_way = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_loader_container.Add( self.m_loader_way, 0, wx.ALL, 5 )

		self.m_loader_use = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_use_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_use_container.SetFlexibleDirection( wx.BOTH )
		m_use_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		self.m_loader_use.SetSizer( m_use_container )
		self.m_loader_use.Layout()
		m_use_container.Fit( self.m_loader_use )
		m_loader_container.Add( self.m_loader_use, 1, wx.EXPAND |wx.ALL, 5 )


		m_mod_loader.Add( m_loader_container, 1, wx.EXPAND, 5 )

		m_loader_b_container = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_loader_b_container.SetFlexibleDirection( wx.BOTH )
		m_loader_b_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_b_container = wx.FlexGridSizer( 0, 4, 0, 0 )
		m_b_container.SetFlexibleDirection( wx.BOTH )
		m_b_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_b_load = wx.Button( self, wx.ID_ANY, u"加载", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_container.Add( self.m_b_load, 0, wx.ALL, 5 )

		self.m_b_refresh = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_container.Add( self.m_b_refresh, 0, wx.ALL, 5 )

		self.m_b_reload = wx.Button( self, wx.ID_ANY, u"重载", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_container.Add( self.m_b_reload, 0, wx.ALL, 5 )

		self.m_b_config = wx.Button( self, wx.ID_ANY, u"配置", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_container.Add( self.m_b_config, 0, wx.ALL, 5 )


		m_loader_b_container.Add( m_b_container, 1, wx.EXPAND, 5 )

		m_b_to_main = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_b_to_main.SetFlexibleDirection( wx.BOTH )
		m_b_to_main.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_b_gotomain = wx.Button( self, wx.ID_ANY, u"进入", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_to_main.Add( self.m_b_gotomain, 0, wx.ALL, 5 )

		self.m_b_opendic = wx.Button( self, wx.ID_ANY, u"打开文件夹", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_to_main.Add( self.m_b_opendic, 0, wx.ALL, 5 )


		m_loader_b_container.Add( m_b_to_main, 1, wx.EXPAND, 5 )


		m_mod_loader.Add( m_loader_b_container, 1, wx.EXPAND, 5 )


		m_mod_container.Add( m_mod_loader, 1, wx.EXPAND, 5 )


		self.SetSizer( m_mod_container )
		self.Layout()

	def __del__( self ):
		pass
 