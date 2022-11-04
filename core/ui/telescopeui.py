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
## Class m_telescope
###########################################################################

class m_telescope ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 780,600 ), style = wx.TAB_TRAVERSAL, name = u"Telescope" ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.m_ts_info_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_ts_info_panel.SetBackgroundColour( wx.Colour( 40, 44, 52 ) )
		self.m_ts_info_panel.SetMinSize( wx.Size( 300,300 ) )

		self.m_mgr.AddPane( self.m_ts_info_panel, wx.aui.AuiPaneInfo() .Name( u"a_telesope_info" ).Left() .Caption( _(u"Telescope Info") ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.Size( 150,-1 ) ).Floatable( False ).Row( 0 ).BestSize( wx.Size( 150,-1 ) ).MinSize( wx.Size( 160,300 ) ).Layer( 10 ) )

		m_ts_info_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_info_container = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_ts_info_container.SetFlexibleDirection( wx.BOTH )
		m_ts_info_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_ts_crood_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_crood_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_ts_crood_container.SetFlexibleDirection( wx.BOTH )
		m_ts_crood_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_ts_i_ra_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"RA"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_ra_t.Wrap( -1 )

		self.m_ts_i_ra_t.SetToolTip( _(u"Show Current RA") )
		self.m_ts_i_ra_t.SetHelpText( _(u"Telescope RA info") )

		m_ts_crood_container.Add( self.m_ts_i_ra_t, 0, wx.ALL, 5 )

		self.m_ts_i_ra = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_ra.Wrap( -1 )

		self.m_ts_i_ra.SetHelpText( _(u"Telescope RA info") )

		m_ts_crood_container.Add( self.m_ts_i_ra, 0, wx.ALL, 5 )

		self.m_ts_i_dec_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"DEC"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_dec_t.Wrap( -1 )

		self.m_ts_i_dec_t.SetToolTip( _(u"Show Current DEC") )
		self.m_ts_i_dec_t.SetHelpText( _(u"Telescope DEC info") )

		m_ts_crood_container.Add( self.m_ts_i_dec_t, 0, wx.ALL, 5 )

		self.m_ts_i_dec = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_dec.Wrap( -1 )

		self.m_ts_i_dec.SetHelpText( _(u"Telescope DEC info") )

		m_ts_crood_container.Add( self.m_ts_i_dec, 0, wx.ALL, 5 )

		self.m_ts_i_az_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"AZ"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_az_t.Wrap( -1 )

		self.m_ts_i_az_t.SetToolTip( _(u"Show Current AZ") )

		m_ts_crood_container.Add( self.m_ts_i_az_t, 0, wx.ALL, 5 )

		self.m_ts_i_az = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_az.Wrap( -1 )

		m_ts_crood_container.Add( self.m_ts_i_az, 0, wx.ALL, 5 )

		self.m_ts_i_alt_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"ALT"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_alt_t.Wrap( -1 )

		self.m_ts_i_alt_t.SetToolTip( _(u"Show Current ALT") )

		m_ts_crood_container.Add( self.m_ts_i_alt_t, 0, wx.ALL, 5 )

		self.m_ts_i_alt = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_alt.Wrap( -1 )

		m_ts_crood_container.Add( self.m_ts_i_alt, 0, wx.ALL, 5 )


		m_ts_crood_box.Add( m_ts_crood_container, 1, wx.EXPAND, 5 )


		m_ts_info_container.Add( m_ts_crood_box, 1, wx.EXPAND, 5 )

		m_ts_status_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_status_container = wx.FlexGridSizer( 0, 4, 0, 0 )
		m_ts_status_container.SetFlexibleDirection( wx.BOTH )
		m_ts_status_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_ts_moving_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"Moving"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_moving_t.Wrap( -1 )

		m_ts_status_container.Add( self.m_ts_moving_t, 0, wx.ALL, 5 )

		self.m_ts_moving_s = wx.StaticBitmap( self.m_ts_info_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 16,16 ), 0 )
		self.m_ts_moving_s.SetMinSize( wx.Size( 16,16 ) )
		self.m_ts_moving_s.SetMaxSize( wx.Size( 32,32 ) )

		m_ts_status_container.Add( self.m_ts_moving_s, 0, wx.ALL, 5 )

		self.m_ts_traking_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"Traking"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_traking_t.Wrap( -1 )

		m_ts_status_container.Add( self.m_ts_traking_t, 0, wx.ALL, 5 )

		self.m_ts_traking_s = wx.StaticBitmap( self.m_ts_info_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 16,16 ), 0 )
		self.m_ts_traking_s.SetMinSize( wx.Size( 16,16 ) )
		self.m_ts_traking_s.SetMaxSize( wx.Size( 32,32 ) )

		m_ts_status_container.Add( self.m_ts_traking_s, 0, wx.ALL, 5 )

		self.m_ts_parked_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"Parked"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_parked_t.Wrap( -1 )

		m_ts_status_container.Add( self.m_ts_parked_t, 0, wx.ALL, 5 )

		self.m_ts_parked_s = wx.StaticBitmap( self.m_ts_info_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 16,16 ), 0 )
		self.m_ts_parked_s.SetMinSize( wx.Size( 16,16 ) )
		self.m_ts_parked_s.SetMaxSize( wx.Size( 32,32 ) )

		m_ts_status_container.Add( self.m_ts_parked_s, 0, wx.ALL, 5 )

		self.m_ts_home_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"Home"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_home_t.Wrap( -1 )

		m_ts_status_container.Add( self.m_ts_home_t, 0, wx.ALL, 5 )

		self.m_ts_home_s = wx.StaticBitmap( self.m_ts_info_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 16,16 ), 0 )
		self.m_ts_home_s.SetMinSize( wx.Size( 16,16 ) )
		self.m_ts_home_s.SetMaxSize( wx.Size( 32,32 ) )

		m_ts_status_container.Add( self.m_ts_home_s, 0, wx.ALL, 5 )


		m_ts_status_box.Add( m_ts_status_container, 1, wx.EXPAND, 5 )


		m_ts_info_container.Add( m_ts_status_box, 1, wx.EXPAND, 5 )


		m_ts_info_box.Add( m_ts_info_container, 1, wx.EXPAND, 5 )


		self.m_ts_info_panel.SetSizer( m_ts_info_box )
		self.m_ts_info_panel.Layout()
		m_ts_info_box.Fit( self.m_ts_info_panel )
		self.m_ts_control_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_ts_control_panel.SetBackgroundColour( wx.Colour( 40, 44, 52 ) )

		self.m_mgr.AddPane( self.m_ts_control_panel, wx.aui.AuiPaneInfo() .Name( u"a_telescope_control" ).Left() .Caption( _(u"Telescope Control") ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Floatable( False ).MinSize( wx.Size( 200,-1 ) ) )

		m_ts_control_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_control_container = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_ts_control_container.SetFlexibleDirection( wx.BOTH )
		m_ts_control_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_ts_dir_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_dir_container = wx.GridSizer( 0, 3, 0, 0 )

		self.m_ts_c_b_wn = wx.BitmapButton( self.m_ts_control_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )
		self.m_ts_c_b_wn.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_ts_c_b_wn.SetMinSize( wx.Size( 64,64 ) )
		self.m_ts_c_b_wn.SetMaxSize( wx.Size( 128,128 ) )

		m_ts_dir_container.Add( self.m_ts_c_b_wn, 0, wx.ALL, 0 )

		self.m_ts_c_b_n = wx.BitmapButton( self.m_ts_control_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )
		self.m_ts_c_b_n.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_ts_c_b_n.SetMinSize( wx.Size( 64,64 ) )
		self.m_ts_c_b_n.SetMaxSize( wx.Size( 128,128 ) )

		m_ts_dir_container.Add( self.m_ts_c_b_n, 0, wx.ALL, 0 )

		self.m_ts_c_b_en = wx.BitmapButton( self.m_ts_control_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )
		self.m_ts_c_b_en.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_ts_c_b_en.SetMinSize( wx.Size( 64,64 ) )
		self.m_ts_c_b_en.SetMaxSize( wx.Size( 128,128 ) )

		m_ts_dir_container.Add( self.m_ts_c_b_en, 0, wx.ALL, 0 )

		self.m_ts_c_b_w = wx.BitmapButton( self.m_ts_control_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )
		self.m_ts_c_b_w.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_ts_c_b_w.SetMinSize( wx.Size( 64,64 ) )
		self.m_ts_c_b_w.SetMaxSize( wx.Size( 128,128 ) )

		m_ts_dir_container.Add( self.m_ts_c_b_w, 0, wx.ALL, 0 )

		self.m_ts_c_b_stop = wx.BitmapButton( self.m_ts_control_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )
		self.m_ts_c_b_stop.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_ts_c_b_stop.SetMinSize( wx.Size( 64,64 ) )
		self.m_ts_c_b_stop.SetMaxSize( wx.Size( 128,128 ) )

		m_ts_dir_container.Add( self.m_ts_c_b_stop, 0, wx.ALL, 0 )

		self.m_ts_c_b_e = wx.BitmapButton( self.m_ts_control_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )
		self.m_ts_c_b_e.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_ts_c_b_e.SetMinSize( wx.Size( 64,64 ) )
		self.m_ts_c_b_e.SetMaxSize( wx.Size( 128,128 ) )

		m_ts_dir_container.Add( self.m_ts_c_b_e, 0, wx.ALL, 0 )

		self.m_ts_c_b_ws = wx.BitmapButton( self.m_ts_control_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )
		self.m_ts_c_b_ws.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_ts_c_b_ws.SetMinSize( wx.Size( 64,64 ) )
		self.m_ts_c_b_ws.SetMaxSize( wx.Size( 128,128 ) )

		m_ts_dir_container.Add( self.m_ts_c_b_ws, 0, wx.ALL, 0 )

		self.m_ts_c_b_s = wx.BitmapButton( self.m_ts_control_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )
		self.m_ts_c_b_s.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_ts_c_b_s.SetMinSize( wx.Size( 64,64 ) )
		self.m_ts_c_b_s.SetMaxSize( wx.Size( 128,128 ) )

		m_ts_dir_container.Add( self.m_ts_c_b_s, 0, wx.ALL, 0 )

		self.m_ts_c_b_es = wx.BitmapButton( self.m_ts_control_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 64,64 ), wx.BU_AUTODRAW|0 )
		self.m_ts_c_b_es.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_ts_c_b_es.SetMinSize( wx.Size( 64,64 ) )
		self.m_ts_c_b_es.SetMaxSize( wx.Size( 128,128 ) )

		m_ts_dir_container.Add( self.m_ts_c_b_es, 0, wx.ALL, 0 )


		m_ts_dir_box.Add( m_ts_dir_container, 1, wx.EXPAND, 5 )


		m_ts_control_container.Add( m_ts_dir_box, 1, wx.EXPAND, 5 )

		m_ts_ccrood_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_ccrood_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_ts_ccrood_container.SetFlexibleDirection( wx.BOTH )
		m_ts_ccrood_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText229 = wx.StaticText( self.m_ts_control_panel, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText229.Wrap( -1 )

		m_ts_ccrood_container.Add( self.m_staticText229, 0, wx.ALL, 5 )

		self.m_textCtrl30 = wx.TextCtrl( self.m_ts_control_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_ts_ccrood_container.Add( self.m_textCtrl30, 0, wx.ALL, 5 )

		self.m_staticText230 = wx.StaticText( self.m_ts_control_panel, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText230.Wrap( -1 )

		m_ts_ccrood_container.Add( self.m_staticText230, 0, wx.ALL, 5 )

		self.m_textCtrl31 = wx.TextCtrl( self.m_ts_control_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_ts_ccrood_container.Add( self.m_textCtrl31, 0, wx.ALL, 5 )

		self.m_staticText231 = wx.StaticText( self.m_ts_control_panel, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )

		m_ts_ccrood_container.Add( self.m_staticText231, 0, wx.ALL, 5 )

		self.m_textCtrl32 = wx.TextCtrl( self.m_ts_control_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_ts_ccrood_container.Add( self.m_textCtrl32, 0, wx.ALL, 5 )

		self.m_staticText232 = wx.StaticText( self.m_ts_control_panel, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText232.Wrap( -1 )

		m_ts_ccrood_container.Add( self.m_staticText232, 0, wx.ALL, 5 )

		self.m_textCtrl33 = wx.TextCtrl( self.m_ts_control_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_ts_ccrood_container.Add( self.m_textCtrl33, 0, wx.ALL, 5 )


		m_ts_ccrood_box.Add( m_ts_ccrood_container, 1, wx.EXPAND, 5 )


		m_ts_control_container.Add( m_ts_ccrood_box, 1, wx.EXPAND, 5 )

		bSizer59 = wx.BoxSizer( wx.VERTICAL )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_ts_c_b_goto = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Goto"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_ts_c_b_goto, 0, wx.ALL, 5 )

		self.m_button54 = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Park"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button54, 0, wx.ALL, 5 )

		self.m_button55 = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Home"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button55, 0, wx.ALL, 5 )

		self.m_button56 = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Align"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button56, 0, wx.ALL, 5 )

		self.m_button57 = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Sync"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button57, 0, wx.ALL, 5 )

		self.m_button58 = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Settings"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer10.Add( self.m_button58, 0, wx.ALL, 5 )


		bSizer59.Add( gSizer10, 1, wx.EXPAND, 5 )


		m_ts_control_container.Add( bSizer59, 1, wx.EXPAND, 5 )


		m_ts_control_box.Add( m_ts_control_container, 1, wx.EXPAND, 5 )


		self.m_ts_control_panel.SetSizer( m_ts_control_box )
		self.m_ts_control_panel.Layout()
		m_ts_control_box.Fit( self.m_ts_control_panel )
		self.m_ts_search_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_ts_search_panel.SetBackgroundColour( wx.Colour( 40, 44, 52 ) )

		self.m_mgr.AddPane( self.m_ts_search_panel, wx.aui.AuiPaneInfo() .Name( u"a_telescope_search" ).Left() .Caption( _(u"Star Search") ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Floatable( False ).Row( 1 ).BestSize( wx.Size( 200,-1 ) ).MinSize( wx.Size( 200,-1 ) ).MaxSize( wx.Size( 400,-1 ) ) )

		bSizer60 = wx.BoxSizer( wx.VERTICAL )

		fgSizer91 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer91.SetFlexibleDirection( wx.BOTH )
		fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		fgSizer92 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer92.SetFlexibleDirection( wx.BOTH )
		fgSizer92.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText233 = wx.StaticText( self.m_ts_search_panel, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText233.Wrap( -1 )

		fgSizer92.Add( self.m_staticText233, 0, wx.ALL, 5 )

		self.m_textCtrl34 = wx.TextCtrl( self.m_ts_search_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_textCtrl34, 0, wx.ALL, 5 )

		self.m_staticText234 = wx.StaticText( self.m_ts_search_panel, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText234.Wrap( -1 )

		fgSizer92.Add( self.m_staticText234, 0, wx.ALL, 5 )

		self.m_textCtrl35 = wx.TextCtrl( self.m_ts_search_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_textCtrl35, 0, wx.ALL, 5 )

		self.m_staticText235 = wx.StaticText( self.m_ts_search_panel, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText235.Wrap( -1 )

		fgSizer92.Add( self.m_staticText235, 0, wx.ALL, 5 )

		self.m_textCtrl36 = wx.TextCtrl( self.m_ts_search_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_textCtrl36, 0, wx.ALL, 5 )

		self.m_staticText236 = wx.StaticText( self.m_ts_search_panel, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText236.Wrap( -1 )

		fgSizer92.Add( self.m_staticText236, 0, wx.ALL, 5 )

		self.m_textCtrl37 = wx.TextCtrl( self.m_ts_search_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_textCtrl37, 0, wx.ALL, 5 )


		bSizer61.Add( fgSizer92, 1, wx.EXPAND, 5 )


		fgSizer91.Add( bSizer61, 1, wx.EXPAND, 5 )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		fgSizer93 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer93.SetFlexibleDirection( wx.BOTH )
		fgSizer93.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button59 = wx.Button( self.m_ts_search_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_button59, 0, wx.ALL, 5 )

		self.m_button60 = wx.Button( self.m_ts_search_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_button60, 0, wx.ALL, 5 )

		self.m_button61 = wx.Button( self.m_ts_search_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_button61, 0, wx.ALL, 5 )

		self.m_button62 = wx.Button( self.m_ts_search_panel, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_button62, 0, wx.ALL, 5 )


		bSizer62.Add( fgSizer93, 1, wx.EXPAND, 5 )


		fgSizer91.Add( bSizer62, 1, wx.EXPAND, 5 )

		self.m_collapsiblePane3 = wx.CollapsiblePane( self.m_ts_search_panel, wx.ID_ANY, _(u"collapsible"), wx.DefaultPosition, wx.DefaultSize, wx.CP_DEFAULT_STYLE )
		self.m_collapsiblePane3.Collapse( True )

		bSizer63 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel47 = wx.Panel( self.m_collapsiblePane3.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer64 = wx.BoxSizer( wx.VERTICAL )


		self.m_panel47.SetSizer( bSizer64 )
		self.m_panel47.Layout()
		bSizer64.Fit( self.m_panel47 )
		bSizer63.Add( self.m_panel47, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel48 = wx.Panel( self.m_collapsiblePane3.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer65 = wx.BoxSizer( wx.VERTICAL )


		self.m_panel48.SetSizer( bSizer65 )
		self.m_panel48.Layout()
		bSizer65.Fit( self.m_panel48 )
		bSizer63.Add( self.m_panel48, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel49 = wx.Panel( self.m_collapsiblePane3.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer66 = wx.BoxSizer( wx.VERTICAL )


		self.m_panel49.SetSizer( bSizer66 )
		self.m_panel49.Layout()
		bSizer66.Fit( self.m_panel49 )
		bSizer63.Add( self.m_panel49, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel50 = wx.Panel( self.m_collapsiblePane3.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer67 = wx.BoxSizer( wx.VERTICAL )


		self.m_panel50.SetSizer( bSizer67 )
		self.m_panel50.Layout()
		bSizer67.Fit( self.m_panel50 )
		bSizer63.Add( self.m_panel50, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel51 = wx.Panel( self.m_collapsiblePane3.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer68 = wx.BoxSizer( wx.VERTICAL )


		self.m_panel51.SetSizer( bSizer68 )
		self.m_panel51.Layout()
		bSizer68.Fit( self.m_panel51 )
		bSizer63.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_collapsiblePane3.GetPane().SetSizer( bSizer63 )
		self.m_collapsiblePane3.GetPane().Layout()
		bSizer63.Fit( self.m_collapsiblePane3.GetPane() )
		fgSizer91.Add( self.m_collapsiblePane3, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer60.Add( fgSizer91, 1, wx.EXPAND, 5 )


		self.m_ts_search_panel.SetSizer( bSizer60 )
		self.m_ts_search_panel.Layout()
		bSizer60.Fit( self.m_ts_search_panel )
		self.m_panel46 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.m_panel46, wx.aui.AuiPaneInfo() .Left() .CloseButton( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Floatable( False ) )


		self.m_mgr.Update()

		# Connect Events
		self.Bind( wx.EVT_ERASE_BACKGROUND, self.on_background_erase )
		self.Bind( wx.EVT_INIT_DIALOG, self.on_init_dialog )
		self.m_ts_c_b_wn.Bind( wx.EVT_BUTTON, self.on_b_wn_click )
		self.m_ts_c_b_n.Bind( wx.EVT_BUTTON, self.on_b_n_click )
		self.m_ts_c_b_en.Bind( wx.EVT_BUTTON, self.on_b_en_click )
		self.m_ts_c_b_w.Bind( wx.EVT_BUTTON, self.on_b_w_click )
		self.m_ts_c_b_stop.Bind( wx.EVT_BUTTON, self.on_b_stop_click )
		self.m_ts_c_b_e.Bind( wx.EVT_BUTTON, self.on_b_e_click )
		self.m_ts_c_b_ws.Bind( wx.EVT_BUTTON, self.on_b_ws_click )
		self.m_ts_c_b_s.Bind( wx.EVT_BUTTON, self.on_b_s_click )
		self.m_ts_c_b_es.Bind( wx.EVT_BUTTON, self.on_b_es_click )

	def __del__( self ):
		self.m_mgr.UnInit()



	# Virtual event handlers, override them in your derived class
	def on_background_erase( self, event ):
		event.Skip()

	def on_init_dialog( self, event ):
		event.Skip()

	def on_b_wn_click( self, event ):
		event.Skip()

	def on_b_n_click( self, event ):
		event.Skip()

	def on_b_en_click( self, event ):
		event.Skip()

	def on_b_w_click( self, event ):
		event.Skip()

	def on_b_stop_click( self, event ):
		event.Skip()

	def on_b_e_click( self, event ):
		event.Skip()

	def on_b_ws_click( self, event ):
		event.Skip()

	def on_b_s_click( self, event ):
		event.Skip()

	def on_b_es_click( self, event ):
		event.Skip()


