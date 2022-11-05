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
import wx.richtext

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
		self.m_ts_info_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_ts_info_panel.SetMinSize( wx.Size( 160,150 ) )

		self.m_mgr.AddPane( self.m_ts_info_panel, wx.aui.AuiPaneInfo() .Name( u"a_telesope_info" ).Left() .Caption( _(u"Telescope Info") ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.Size( -1,-1 ) ).Floatable( False ).Row( 0 ).MinSize( wx.Size( 160,200 ) ).Layer( 10 ) )

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

		self.m_ts_i_ra_t.SetToolTip( _(u"Show Current RA (JNow)") )
		self.m_ts_i_ra_t.SetHelpText( _(u"Telescope RA info") )

		m_ts_crood_container.Add( self.m_ts_i_ra_t, 0, wx.ALL, 5 )

		self.m_ts_i_ra = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_ra.Wrap( -1 )

		self.m_ts_i_ra.SetHelpText( _(u"Telescope RA info") )

		m_ts_crood_container.Add( self.m_ts_i_ra, 0, wx.ALL, 5 )

		self.m_ts_i_dec_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"DEC"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_dec_t.Wrap( -1 )

		self.m_ts_i_dec_t.SetToolTip( _(u"Show Current DEC (JNow)") )
		self.m_ts_i_dec_t.SetHelpText( _(u"Telescope DEC info") )

		m_ts_crood_container.Add( self.m_ts_i_dec_t, 0, wx.ALL, 5 )

		self.m_ts_i_dec = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_dec.Wrap( -1 )

		self.m_ts_i_dec.SetHelpText( _(u"Telescope DEC info") )

		m_ts_crood_container.Add( self.m_ts_i_dec, 0, wx.ALL, 5 )

		self.m_ts_i_az_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"AZ"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_az_t.Wrap( -1 )

		self.m_ts_i_az_t.SetToolTip( _(u"Show Current AZ (JNow)") )

		m_ts_crood_container.Add( self.m_ts_i_az_t, 0, wx.ALL, 5 )

		self.m_ts_i_az = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_az.Wrap( -1 )

		m_ts_crood_container.Add( self.m_ts_i_az, 0, wx.ALL, 5 )

		self.m_ts_i_alt_t = wx.StaticText( self.m_ts_info_panel, wx.ID_ANY, _(u"ALT"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_i_alt_t.Wrap( -1 )

		self.m_ts_i_alt_t.SetToolTip( _(u"Show Current ALT (JNow)") )

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

		self.m_sl_2 = wx.StaticLine( self.m_ts_info_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		m_ts_info_container.Add( self.m_sl_2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_current_image = wx.StaticBitmap( self.m_ts_info_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_current_image.SetMinSize( wx.Size( 150,150 ) )

		m_ts_info_container.Add( self.m_current_image, 0, wx.ALL, 5 )

		self.m_sl_3 = wx.StaticLine( self.m_ts_info_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		m_ts_info_container.Add( self.m_sl_3, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_current_info = wx.richtext.RichTextCtrl( self.m_ts_info_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.m_current_info.Enable( False )
		self.m_current_info.SetMinSize( wx.Size( 150,150 ) )

		m_ts_info_container.Add( self.m_current_info, 1, wx.EXPAND |wx.ALL, 5 )


		m_ts_info_box.Add( m_ts_info_container, 1, wx.EXPAND, 5 )


		self.m_ts_info_panel.SetSizer( m_ts_info_box )
		self.m_ts_info_panel.Layout()
		m_ts_info_box.Fit( self.m_ts_info_panel )
		self.m_ts_control_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_ts_control_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_mgr.AddPane( self.m_ts_control_panel, wx.aui.AuiPaneInfo() .Name( u"a_telescope_control" ).Left() .Caption( _(u"Telescope Control") ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Floatable( False ).Row( 0 ).MinSize( wx.Size( 200,440 ) ) )

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

		self.m_sl4 = wx.StaticLine( self.m_ts_control_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		m_ts_control_container.Add( self.m_sl4, 0, wx.EXPAND |wx.ALL, 5 )

		m_ts_ccrood_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_ccrood_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_ts_ccrood_container.SetFlexibleDirection( wx.BOTH )
		m_ts_ccrood_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_ts_c_ra_t = wx.StaticText( self.m_ts_control_panel, wx.ID_ANY, _(u"RA"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_c_ra_t.Wrap( -1 )

		self.m_ts_c_ra_t.SetToolTip( _(u"JNow") )

		m_ts_ccrood_container.Add( self.m_ts_c_ra_t, 0, wx.ALL, 5 )

		self.m_ts_c_ra = wx.TextCtrl( self.m_ts_control_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_ts_ccrood_container.Add( self.m_ts_c_ra, 0, wx.ALL, 5 )

		self.m_ts_c_dec_t = wx.StaticText( self.m_ts_control_panel, wx.ID_ANY, _(u"DEC"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_c_dec_t.Wrap( -1 )

		self.m_ts_c_dec_t.SetToolTip( _(u"JNow") )

		m_ts_ccrood_container.Add( self.m_ts_c_dec_t, 0, wx.ALL, 5 )

		self.m_ts_c_dec = wx.TextCtrl( self.m_ts_control_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_ts_ccrood_container.Add( self.m_ts_c_dec, 0, wx.ALL, 5 )

		self.m_ts_c_az_t = wx.StaticText( self.m_ts_control_panel, wx.ID_ANY, _(u"AZ"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_c_az_t.Wrap( -1 )

		self.m_ts_c_az_t.SetToolTip( _(u"JNow") )

		m_ts_ccrood_container.Add( self.m_ts_c_az_t, 0, wx.ALL, 5 )

		self.m_ts_c_az = wx.TextCtrl( self.m_ts_control_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_ts_ccrood_container.Add( self.m_ts_c_az, 0, wx.ALL, 5 )

		self.m_ts_c_alt_t = wx.StaticText( self.m_ts_control_panel, wx.ID_ANY, _(u"ALT"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_c_alt_t.Wrap( -1 )

		self.m_ts_c_alt_t.SetToolTip( _(u"JNow") )

		m_ts_ccrood_container.Add( self.m_ts_c_alt_t, 0, wx.ALL, 5 )

		self.m_ts_c_alt = wx.TextCtrl( self.m_ts_control_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_ts_ccrood_container.Add( self.m_ts_c_alt, 0, wx.ALL, 5 )


		m_ts_ccrood_box.Add( m_ts_ccrood_container, 1, wx.EXPAND, 5 )


		m_ts_control_container.Add( m_ts_ccrood_box, 1, wx.EXPAND, 5 )

		self.m_sl5 = wx.StaticLine( self.m_ts_control_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		m_ts_control_container.Add( self.m_sl5, 0, wx.EXPAND |wx.ALL, 5 )

		m_ts_c_b_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_c_b_container = wx.GridSizer( 0, 2, 0, 0 )

		self.m_ts_c_b_goto = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Goto"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_c_b_goto.SetMinSize( wx.Size( 90,-1 ) )
		self.m_ts_c_b_goto.SetMaxSize( wx.Size( 180,-1 ) )

		m_ts_c_b_container.Add( self.m_ts_c_b_goto, 0, wx.ALL, 5 )

		self.m_ts_c_b_track = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Track"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_c_b_track.SetMinSize( wx.Size( 90,-1 ) )
		self.m_ts_c_b_track.SetMaxSize( wx.Size( 180,-1 ) )

		m_ts_c_b_container.Add( self.m_ts_c_b_track, 0, wx.ALL, 5 )

		self.m_ts_c_b_park = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Park"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_c_b_park.SetMinSize( wx.Size( 90,-1 ) )
		self.m_ts_c_b_park.SetMaxSize( wx.Size( 180,-1 ) )

		m_ts_c_b_container.Add( self.m_ts_c_b_park, 0, wx.ALL, 5 )

		self.m_ts_c_b_home = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Home"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_c_b_home.SetMinSize( wx.Size( 90,-1 ) )
		self.m_ts_c_b_home.SetMaxSize( wx.Size( 180,-1 ) )

		m_ts_c_b_container.Add( self.m_ts_c_b_home, 0, wx.ALL, 5 )

		self.m_ts_c_b_align = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Align"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_c_b_align.SetMinSize( wx.Size( 90,-1 ) )
		self.m_ts_c_b_align.SetMaxSize( wx.Size( 180,-1 ) )

		m_ts_c_b_container.Add( self.m_ts_c_b_align, 0, wx.ALL, 5 )

		self.m_ts_c_b_sync = wx.Button( self.m_ts_control_panel, wx.ID_ANY, _(u"Sync"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_c_b_sync.SetMinSize( wx.Size( 90,-1 ) )
		self.m_ts_c_b_sync.SetMaxSize( wx.Size( 180,-1 ) )

		m_ts_c_b_container.Add( self.m_ts_c_b_sync, 0, wx.ALL, 5 )


		m_ts_c_b_box.Add( m_ts_c_b_container, 1, wx.EXPAND, 5 )


		m_ts_control_container.Add( m_ts_c_b_box, 1, wx.EXPAND, 5 )


		m_ts_control_box.Add( m_ts_control_container, 1, wx.EXPAND, 5 )


		self.m_ts_control_panel.SetSizer( m_ts_control_box )
		self.m_ts_control_panel.Layout()
		m_ts_control_box.Fit( self.m_ts_control_panel )
		self.m_ts_search_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_ts_search_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_mgr.AddPane( self.m_ts_search_panel, wx.aui.AuiPaneInfo() .Name( u"a_telescope_search" ).Right() .Caption( _(u"Star Search") ).CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.Size( 100,-1 ) ).Floatable( False ).Row( 0 ).BestSize( wx.Size( 200,-1 ) ).MinSize( wx.Size( 400,-1 ) ).MaxSize( wx.Size( 400,-1 ) ) )

		m_ts_search_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_search_container = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_ts_search_container.SetFlexibleDirection( wx.BOTH )
		m_ts_search_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_ts_search_nb = wx.Notebook( self.m_ts_search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_search_nb_p_type = wx.Panel( self.m_ts_search_nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_ts_search_nb_p_type_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_search_nb_p_type_container = wx.FlexGridSizer( 0, 4, 0, 0 )
		m_ts_search_nb_p_type_container.SetFlexibleDirection( wx.BOTH )
		m_ts_search_nb_p_type_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_ts_s_t_type_t = wx.StaticText( self.m_ts_search_nb_p_type, wx.ID_ANY, _(u"Type"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_s_t_type_t.Wrap( -1 )

		m_ts_search_nb_p_type_container.Add( self.m_ts_s_t_type_t, 0, wx.ALL, 5 )

		m_ts_s_t_typeChoices = [ _(u"Messier"), _(u"NGCIC"), _(u"SAC") ]
		self.m_ts_s_t_type = wx.Choice( self.m_ts_search_nb_p_type, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_ts_s_t_typeChoices, 0 )
		self.m_ts_s_t_type.SetSelection( 0 )
		m_ts_search_nb_p_type_container.Add( self.m_ts_s_t_type, 0, wx.ALL, 5 )

		self.m_ts_s_t_num_t = wx.StaticText( self.m_ts_search_nb_p_type, wx.ID_ANY, _(u"Number"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_s_t_num_t.Wrap( -1 )

		m_ts_search_nb_p_type_container.Add( self.m_ts_s_t_num_t, 0, wx.ALL, 5 )

		self.m_ts_s_t_num = wx.TextCtrl( self.m_ts_search_nb_p_type, wx.ID_ANY, _(u"1"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ts_s_t_num.SetMaxLength( 4 )
		self.m_ts_s_t_num.SetMinSize( wx.Size( 75,-1 ) )

		m_ts_search_nb_p_type_container.Add( self.m_ts_s_t_num, 0, wx.ALL, 5 )

		self.m_staticText2341 = wx.StaticText( self.m_ts_search_nb_p_type, wx.ID_ANY, _(u"Name"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2341.Wrap( -1 )

		m_ts_search_nb_p_type_container.Add( self.m_staticText2341, 0, wx.ALL, 5 )

		self.m_textCtrl351 = wx.TextCtrl( self.m_ts_search_nb_p_type, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl351.SetMaxLength( 100 )
		self.m_textCtrl351.SetMinSize( wx.Size( 75,-1 ) )

		m_ts_search_nb_p_type_container.Add( self.m_textCtrl351, 0, wx.ALL, 5 )

		self.m_staticText2351 = wx.StaticText( self.m_ts_search_nb_p_type, wx.ID_ANY, _(u"CNAME"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2351.Wrap( -1 )

		m_ts_search_nb_p_type_container.Add( self.m_staticText2351, 0, wx.ALL, 5 )

		self.m_textCtrl361 = wx.TextCtrl( self.m_ts_search_nb_p_type, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl361.SetMaxLength( 20 )
		self.m_textCtrl361.SetMinSize( wx.Size( 75,-1 ) )

		m_ts_search_nb_p_type_container.Add( self.m_textCtrl361, 0, wx.ALL, 5 )


		m_ts_search_nb_p_type_box.Add( m_ts_search_nb_p_type_container, 1, wx.EXPAND, 5 )


		self.m_ts_search_nb_p_type.SetSizer( m_ts_search_nb_p_type_box )
		self.m_ts_search_nb_p_type.Layout()
		m_ts_search_nb_p_type_box.Fit( self.m_ts_search_nb_p_type )
		self.m_ts_search_nb.AddPage( self.m_ts_search_nb_p_type, _(u"Type"), False )
		self.m_ts_search_nb_p_coord = wx.Panel( self.m_ts_search_nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_ts_search_nb_p_coord_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_search_nb_p_coord_container = wx.FlexGridSizer( 0, 7, 0, 0 )
		m_ts_search_nb_p_coord_container.SetFlexibleDirection( wx.BOTH )
		m_ts_search_nb_p_coord_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_s_c_ra_t = wx.StaticText( self.m_ts_search_nb_p_coord, wx.ID_ANY, _(u"RA"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_ra_t.Wrap( -1 )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_ra_t, 0, wx.ALL, 5 )

		self.m_s_c_ra_h = wx.TextCtrl( self.m_ts_search_nb_p_coord, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_ra_h.SetMinSize( wx.Size( 30,-1 ) )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_ra_h, 0, wx.ALL, 5 )

		self.m_s_c_ra_h_t = wx.StaticText( self.m_ts_search_nb_p_coord, wx.ID_ANY, _(u"h"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_ra_h_t.Wrap( -1 )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_ra_h_t, 0, wx.ALL, 5 )

		self.m_s_c_ra_m = wx.TextCtrl( self.m_ts_search_nb_p_coord, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_ra_m.SetMinSize( wx.Size( 30,-1 ) )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_ra_m, 0, wx.ALL, 5 )

		self.m_s_c_ra_m_t = wx.StaticText( self.m_ts_search_nb_p_coord, wx.ID_ANY, _(u"m"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_ra_m_t.Wrap( -1 )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_ra_m_t, 0, wx.ALL, 5 )

		self.m_s_c_ra_s = wx.TextCtrl( self.m_ts_search_nb_p_coord, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_ra_s.SetMinSize( wx.Size( 30,-1 ) )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_ra_s, 0, wx.ALL, 5 )

		self.m_s_c_ra_s_t = wx.StaticText( self.m_ts_search_nb_p_coord, wx.ID_ANY, _(u"s"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_ra_s_t.Wrap( -1 )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_ra_s_t, 0, wx.ALL, 5 )

		self.m_s_c_dec_t = wx.StaticText( self.m_ts_search_nb_p_coord, wx.ID_ANY, _(u"DEC"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_dec_t.Wrap( -1 )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_dec_t, 0, wx.ALL, 5 )

		self.m_s_c_dec_h = wx.TextCtrl( self.m_ts_search_nb_p_coord, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_dec_h.SetMinSize( wx.Size( 30,-1 ) )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_dec_h, 0, wx.ALL, 5 )

		self.m_s_c_dec_h_t = wx.StaticText( self.m_ts_search_nb_p_coord, wx.ID_ANY, _(u"h"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_dec_h_t.Wrap( -1 )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_dec_h_t, 0, wx.ALL, 5 )

		self.m_s_c_dec_m = wx.TextCtrl( self.m_ts_search_nb_p_coord, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_dec_m.SetMinSize( wx.Size( 30,-1 ) )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_dec_m, 0, wx.ALL, 5 )

		self.m_s_c_dec_m_t = wx.StaticText( self.m_ts_search_nb_p_coord, wx.ID_ANY, _(u"m"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_dec_m_t.Wrap( -1 )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_dec_m_t, 0, wx.ALL, 5 )

		self.m_s_c_dec_s = wx.TextCtrl( self.m_ts_search_nb_p_coord, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_dec_s.SetMinSize( wx.Size( 30,-1 ) )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_dec_s, 0, wx.ALL, 5 )

		self.m_s_c_dec_s_t = wx.StaticText( self.m_ts_search_nb_p_coord, wx.ID_ANY, _(u"s"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_s_c_dec_s_t.Wrap( -1 )

		m_ts_search_nb_p_coord_container.Add( self.m_s_c_dec_s_t, 0, wx.ALL, 5 )


		m_ts_search_nb_p_coord_box.Add( m_ts_search_nb_p_coord_container, 1, wx.EXPAND, 5 )


		self.m_ts_search_nb_p_coord.SetSizer( m_ts_search_nb_p_coord_box )
		self.m_ts_search_nb_p_coord.Layout()
		m_ts_search_nb_p_coord_box.Fit( self.m_ts_search_nb_p_coord )
		self.m_ts_search_nb.AddPage( self.m_ts_search_nb_p_coord, _(u"Coord"), True )

		m_ts_search_container.Add( self.m_ts_search_nb, 1, wx.EXPAND |wx.ALL, 5 )

		m_ts_s_b_box = wx.BoxSizer( wx.VERTICAL )

		m_ts_s_b_container = wx.FlexGridSizer( 0, 3, 0, 0 )
		m_ts_s_b_container.SetFlexibleDirection( wx.BOTH )
		m_ts_s_b_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_ts_s_b_search = wx.Button( self.m_ts_search_panel, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		m_ts_s_b_container.Add( self.m_ts_s_b_search, 0, wx.ALL, 5 )

		self.m_ts_s_b_reset = wx.Button( self.m_ts_search_panel, wx.ID_ANY, _(u"Reset"), wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		m_ts_s_b_container.Add( self.m_ts_s_b_reset, 0, wx.ALL, 5 )

		self.m_ts_s_b_sync = wx.Button( self.m_ts_search_panel, wx.ID_ANY, _(u"Sync"), wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		m_ts_s_b_container.Add( self.m_ts_s_b_sync, 0, wx.ALL, 5 )


		m_ts_s_b_box.Add( m_ts_s_b_container, 1, wx.EXPAND, 5 )


		m_ts_search_container.Add( m_ts_s_b_box, 1, wx.EXPAND, 5 )

		self.m_sl_1 = wx.StaticLine( self.m_ts_search_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		m_ts_search_container.Add( self.m_sl_1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_result_cp = wx.CollapsiblePane( self.m_ts_search_panel, wx.ID_ANY, _(u"Search Results"), wx.DefaultPosition, wx.DefaultSize, wx.CP_DEFAULT_STYLE )
		self.m_result_cp.Collapse( False )

		m_result_box = wx.BoxSizer( wx.VERTICAL )

		self.m_target_panel = wx.Panel( self.m_result_cp.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_target_box = wx.BoxSizer( wx.VERTICAL )

		m_target_container = wx.FlexGridSizer( 1, 0, 0, 0 )
		m_target_container.SetFlexibleDirection( wx.BOTH )
		m_target_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_target_icon = wx.StaticBitmap( self.m_target_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_icon.SetMinSize( wx.Size( 32,32 ) )

		m_target_container.Add( self.m_target_icon, 0, wx.ALL, 5 )

		self.m_target_name = wx.StaticText( self.m_target_panel, wx.ID_ANY, _(u"Name"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_name.Wrap( -1 )

		self.m_target_name.SetMinSize( wx.Size( 40,-1 ) )

		m_target_container.Add( self.m_target_name, 0, wx.ALL, 5 )

		self.m_target_ra = wx.StaticText( self.m_target_panel, wx.ID_ANY, _(u"RA"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_ra.Wrap( -1 )

		self.m_target_ra.SetMinSize( wx.Size( 50,-1 ) )

		m_target_container.Add( self.m_target_ra, 0, wx.ALL, 5 )

		self.m_target_dec = wx.StaticText( self.m_target_panel, wx.ID_ANY, _(u"DEC"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_dec.Wrap( -1 )

		self.m_target_dec.SetMinSize( wx.Size( 50,-1 ) )

		m_target_container.Add( self.m_target_dec, 0, wx.ALL, 5 )

		self.m_target_mid = wx.StaticText( self.m_target_panel, wx.ID_ANY, _(u"Midnight"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_mid.Wrap( -1 )

		self.m_target_mid.SetMinSize( wx.Size( 50,-1 ) )

		m_target_container.Add( self.m_target_mid, 0, wx.ALL, 5 )


		m_target_box.Add( m_target_container, 1, wx.EXPAND, 5 )


		self.m_target_panel.SetSizer( m_target_box )
		self.m_target_panel.Layout()
		m_target_box.Fit( self.m_target_panel )
		m_result_box.Add( self.m_target_panel, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_target_panel1 = wx.Panel( self.m_result_cp.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_target_box1 = wx.BoxSizer( wx.VERTICAL )

		m_target_container1 = wx.FlexGridSizer( 1, 0, 0, 0 )
		m_target_container1.SetFlexibleDirection( wx.BOTH )
		m_target_container1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_target_icon1 = wx.StaticBitmap( self.m_target_panel1, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_icon1.SetMinSize( wx.Size( 32,32 ) )

		m_target_container1.Add( self.m_target_icon1, 0, wx.ALL, 5 )

		self.m_target_name2 = wx.StaticText( self.m_target_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_name2.Wrap( -1 )

		self.m_target_name2.SetMinSize( wx.Size( 40,-1 ) )

		m_target_container1.Add( self.m_target_name2, 0, wx.ALL, 5 )

		self.m_target_ra2 = wx.StaticText( self.m_target_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_ra2.Wrap( -1 )

		m_target_container1.Add( self.m_target_ra2, 0, wx.ALL, 5 )

		self.m_target_dec2 = wx.StaticText( self.m_target_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_dec2.Wrap( -1 )

		m_target_container1.Add( self.m_target_dec2, 0, wx.ALL, 5 )

		self.m_target_mid2 = wx.StaticText( self.m_target_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_mid2.Wrap( -1 )

		m_target_container1.Add( self.m_target_mid2, 0, wx.ALL, 5 )


		m_target_box1.Add( m_target_container1, 1, wx.EXPAND, 5 )


		self.m_target_panel1.SetSizer( m_target_box1 )
		self.m_target_panel1.Layout()
		m_target_box1.Fit( self.m_target_panel1 )
		m_result_box.Add( self.m_target_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_target_panel2 = wx.Panel( self.m_result_cp.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_target_box2 = wx.BoxSizer( wx.VERTICAL )

		m_target_container2 = wx.FlexGridSizer( 1, 0, 0, 0 )
		m_target_container2.SetFlexibleDirection( wx.BOTH )
		m_target_container2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_target_icon2 = wx.StaticBitmap( self.m_target_panel2, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_icon2.SetMinSize( wx.Size( 32,32 ) )

		m_target_container2.Add( self.m_target_icon2, 0, wx.ALL, 5 )

		self.m_target_name1 = wx.StaticText( self.m_target_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_name1.Wrap( -1 )

		self.m_target_name1.SetMinSize( wx.Size( 40,-1 ) )

		m_target_container2.Add( self.m_target_name1, 0, wx.ALL, 5 )

		self.m_target_ra1 = wx.StaticText( self.m_target_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_ra1.Wrap( -1 )

		m_target_container2.Add( self.m_target_ra1, 0, wx.ALL, 5 )

		self.m_target_dec1 = wx.StaticText( self.m_target_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_dec1.Wrap( -1 )

		m_target_container2.Add( self.m_target_dec1, 0, wx.ALL, 5 )

		self.m_target_mid1 = wx.StaticText( self.m_target_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_mid1.Wrap( -1 )

		m_target_container2.Add( self.m_target_mid1, 0, wx.ALL, 5 )


		m_target_box2.Add( m_target_container2, 1, wx.EXPAND, 5 )


		self.m_target_panel2.SetSizer( m_target_box2 )
		self.m_target_panel2.Layout()
		m_target_box2.Fit( self.m_target_panel2 )
		m_result_box.Add( self.m_target_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_target_panel3 = wx.Panel( self.m_result_cp.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_target_box3 = wx.BoxSizer( wx.VERTICAL )

		m_target_container3 = wx.FlexGridSizer( 1, 0, 0, 0 )
		m_target_container3.SetFlexibleDirection( wx.BOTH )
		m_target_container3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_target_icon3 = wx.StaticBitmap( self.m_target_panel3, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_icon3.SetMinSize( wx.Size( 32,32 ) )

		m_target_container3.Add( self.m_target_icon3, 0, wx.ALL, 5 )

		self.m_target_name3 = wx.StaticText( self.m_target_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_name3.Wrap( -1 )

		self.m_target_name3.SetMinSize( wx.Size( 40,-1 ) )

		m_target_container3.Add( self.m_target_name3, 0, wx.ALL, 5 )

		self.m_target_ra3 = wx.StaticText( self.m_target_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_ra3.Wrap( -1 )

		m_target_container3.Add( self.m_target_ra3, 0, wx.ALL, 5 )

		self.m_target_dec3 = wx.StaticText( self.m_target_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_dec3.Wrap( -1 )

		m_target_container3.Add( self.m_target_dec3, 0, wx.ALL, 5 )

		self.m_target_mid3 = wx.StaticText( self.m_target_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_mid3.Wrap( -1 )

		m_target_container3.Add( self.m_target_mid3, 0, wx.ALL, 5 )


		m_target_box3.Add( m_target_container3, 1, wx.EXPAND, 5 )


		self.m_target_panel3.SetSizer( m_target_box3 )
		self.m_target_panel3.Layout()
		m_target_box3.Fit( self.m_target_panel3 )
		m_result_box.Add( self.m_target_panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_target_panel4 = wx.Panel( self.m_result_cp.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_target_box4 = wx.BoxSizer( wx.VERTICAL )

		m_target_container4 = wx.FlexGridSizer( 1, 0, 0, 0 )
		m_target_container4.SetFlexibleDirection( wx.BOTH )
		m_target_container4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_target_icon4 = wx.StaticBitmap( self.m_target_panel4, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_icon4.SetMinSize( wx.Size( 32,32 ) )

		m_target_container4.Add( self.m_target_icon4, 0, wx.ALL, 5 )

		self.m_target_name4 = wx.StaticText( self.m_target_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_name4.Wrap( -1 )

		self.m_target_name4.SetMinSize( wx.Size( 40,-1 ) )

		m_target_container4.Add( self.m_target_name4, 0, wx.ALL, 5 )

		self.m_target_ra4 = wx.StaticText( self.m_target_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_ra4.Wrap( -1 )

		m_target_container4.Add( self.m_target_ra4, 0, wx.ALL, 5 )

		self.m_target_dec4 = wx.StaticText( self.m_target_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_dec4.Wrap( -1 )

		m_target_container4.Add( self.m_target_dec4, 0, wx.ALL, 5 )

		self.m_target_mid4 = wx.StaticText( self.m_target_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_mid4.Wrap( -1 )

		m_target_container4.Add( self.m_target_mid4, 0, wx.ALL, 5 )


		m_target_box4.Add( m_target_container4, 1, wx.EXPAND, 5 )


		self.m_target_panel4.SetSizer( m_target_box4 )
		self.m_target_panel4.Layout()
		m_target_box4.Fit( self.m_target_panel4 )
		m_result_box.Add( self.m_target_panel4, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_target_panel5 = wx.Panel( self.m_result_cp.GetPane(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_target_box5 = wx.BoxSizer( wx.VERTICAL )

		m_target_container5 = wx.FlexGridSizer( 1, 0, 0, 0 )
		m_target_container5.SetFlexibleDirection( wx.BOTH )
		m_target_container5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_target_icon5 = wx.StaticBitmap( self.m_target_panel5, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_icon5.SetMinSize( wx.Size( 32,32 ) )

		m_target_container5.Add( self.m_target_icon5, 0, wx.ALL, 5 )

		self.m_target_name5 = wx.StaticText( self.m_target_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_name5.Wrap( -1 )

		self.m_target_name5.SetMinSize( wx.Size( 40,-1 ) )

		m_target_container5.Add( self.m_target_name5, 0, wx.ALL, 5 )

		self.m_target_ra5 = wx.StaticText( self.m_target_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_ra5.Wrap( -1 )

		m_target_container5.Add( self.m_target_ra5, 0, wx.ALL, 5 )

		self.m_target_dec5 = wx.StaticText( self.m_target_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_dec5.Wrap( -1 )

		m_target_container5.Add( self.m_target_dec5, 0, wx.ALL, 5 )

		self.m_target_mid5 = wx.StaticText( self.m_target_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_target_mid5.Wrap( -1 )

		m_target_container5.Add( self.m_target_mid5, 0, wx.ALL, 5 )


		m_target_box5.Add( m_target_container5, 1, wx.EXPAND, 5 )


		self.m_target_panel5.SetSizer( m_target_box5 )
		self.m_target_panel5.Layout()
		m_target_box5.Fit( self.m_target_panel5 )
		m_result_box.Add( self.m_target_panel5, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_result_cp.GetPane().SetSizer( m_result_box )
		self.m_result_cp.GetPane().Layout()
		m_result_box.Fit( self.m_result_cp.GetPane() )
		m_ts_search_container.Add( self.m_result_cp, 1, wx.EXPAND |wx.ALL, 5 )


		m_ts_search_box.Add( m_ts_search_container, 1, wx.EXPAND, 5 )


		self.m_ts_search_panel.SetSizer( m_ts_search_box )
		self.m_ts_search_panel.Layout()
		m_ts_search_box.Fit( self.m_ts_search_panel )

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
		self.m_ts_c_b_goto.Bind( wx.EVT_BUTTON, self.on_b_goto_click )
		self.m_ts_c_b_track.Bind( wx.EVT_BUTTON, self.on_b_track_click )
		self.m_ts_c_b_park.Bind( wx.EVT_BUTTON, self.on_b_park_click )
		self.m_ts_c_b_home.Bind( wx.EVT_BUTTON, self.on_b_home_click )
		self.m_ts_c_b_align.Bind( wx.EVT_BUTTON, self.on_b_align_click )
		self.m_ts_c_b_sync.Bind( wx.EVT_BUTTON, self.on_b_sync_click )
		self.m_ts_s_t_type.Bind( wx.EVT_CHOICE, self.on_search_update )
		self.m_ts_s_t_num.Bind( wx.EVT_TEXT, self.on_number_update )
		self.m_ts_s_t_num.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_textCtrl351.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_textCtrl361.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_s_c_ra_h.Bind( wx.EVT_TEXT, self.on_ra_h_update )
		self.m_s_c_ra_h.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_s_c_ra_m.Bind( wx.EVT_TEXT, self.on_ra_m_update )
		self.m_s_c_ra_m.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_s_c_ra_s.Bind( wx.EVT_TEXT, self.on_ra_s_update )
		self.m_s_c_ra_s.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_s_c_dec_h.Bind( wx.EVT_TEXT, self.on_dec_h_update )
		self.m_s_c_dec_h.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_s_c_dec_m.Bind( wx.EVT_TEXT, self.on_dec_m_update )
		self.m_s_c_dec_m.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_s_c_dec_s.Bind( wx.EVT_TEXT, self.on_dec_s_update )
		self.m_s_c_dec_s.Bind( wx.EVT_TEXT_MAXLEN, self.on_max_length )
		self.m_ts_s_b_search.Bind( wx.EVT_BUTTON, self.on_search_click )
		self.m_ts_s_b_reset.Bind( wx.EVT_BUTTON, self.on_reset_click )
		self.m_ts_s_b_sync.Bind( wx.EVT_BUTTON, self.on_sync_click )
		self.m_result_cp.Bind( wx.EVT_COLLAPSIBLEPANE_CHANGED, self.on_result_change )
		self.m_target_panel1.Bind( wx.EVT_LEFT_DCLICK, self.on_target_click )
		self.m_target_panel2.Bind( wx.EVT_LEFT_DCLICK, self.on_target_click )
		self.m_target_panel3.Bind( wx.EVT_LEFT_DCLICK, self.on_target_click )
		self.m_target_panel4.Bind( wx.EVT_LEFT_DCLICK, self.on_target_click )
		self.m_target_panel5.Bind( wx.EVT_LEFT_DCLICK, self.on_target_click )

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

	def on_b_goto_click( self, event ):
		event.Skip()

	def on_b_track_click( self, event ):
		event.Skip()

	def on_b_park_click( self, event ):
		event.Skip()

	def on_b_home_click( self, event ):
		event.Skip()

	def on_b_align_click( self, event ):
		event.Skip()

	def on_b_sync_click( self, event ):
		event.Skip()

	def on_search_update( self, event ):
		event.Skip()

	def on_number_update( self, event ):
		event.Skip()

	def on_max_length( self, event ):
		event.Skip()



	def on_ra_h_update( self, event ):
		event.Skip()


	def on_ra_m_update( self, event ):
		event.Skip()


	def on_ra_s_update( self, event ):
		event.Skip()


	def on_dec_h_update( self, event ):
		event.Skip()


	def on_dec_m_update( self, event ):
		event.Skip()


	def on_dec_s_update( self, event ):
		event.Skip()


	def on_search_click( self, event ):
		event.Skip()

	def on_reset_click( self, event ):
		event.Skip()

	def on_sync_click( self, event ):
		event.Skip()

	def on_result_change( self, event ):
		event.Skip()

	def on_target_click( self, event ):
		event.Skip()
