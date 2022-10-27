# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

import gettext
_ = gettext.gettext

###########################################################################
## Class m_leader_wizard
###########################################################################

class m_leader_wizard ( wx.adv.Wizard ):

	def __init__( self, parent ):
		wx.adv.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"引导设置"), bitmap = wx.Bitmap( u"东/python/StarLand/assets/textures/icon/m_leader_page_icon.png", wx.BITMAP_TYPE_ANY ), pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.m_pages = []

		self.m_welcome_page = wx.adv.WizardPageSimple( self , None, None, wx.Bitmap( u"东/python/StarLand/assets/textures/icon/m_leader_icon.png", wx.BITMAP_TYPE_ANY ) )
		self.add_page( self.m_welcome_page )

		self.m_welcome_page.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTIONTEXT ) )
		self.m_welcome_page.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		m_welcome_box = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText116 = wx.StaticText( self.m_welcome_page, wx.ID_ANY, _(u"欢迎来到星空之境"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText116.Wrap( -1 )

		self.m_staticText116.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		m_welcome_box.Add( self.m_staticText116, 0, wx.ALL, 5 )

		self.m_bitmap14 = wx.StaticBitmap( self.m_welcome_page, wx.ID_ANY, wx.Bitmap( u"东/python/StarLand/assets/textures/icon/m_logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_welcome_box.Add( self.m_bitmap14, 0, wx.ALL, 5 )

		self.m_staticText117 = wx.StaticText( self.m_welcome_page, wx.ID_ANY, _(u"下面是引导设置awa"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText117.Wrap( -1 )

		m_welcome_box.Add( self.m_staticText117, 0, wx.ALL, 5 )


		self.m_welcome_page.SetSizer( m_welcome_box )
		self.m_welcome_page.Layout()
		m_welcome_box.Fit( self.m_welcome_page )
		self.m_device_page = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_device_page )

		m_device_box = wx.BoxSizer( wx.VERTICAL )

		m_device_container = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_device_container.SetFlexibleDirection( wx.BOTH )
		m_device_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_device_title = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_device_title.SetFlexibleDirection( wx.BOTH )
		m_device_title.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_title_icon = wx.StaticBitmap( self.m_device_page, wx.ID_ANY, wx.Bitmap( u"东/python/StarLand/assets/textures/icon/m_leader_device_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_device_title.Add( self.m_title_icon, 0, wx.ALL, 5 )

		self.m_title_title = wx.StaticText( self.m_device_page, wx.ID_ANY, _(u"设备设置"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_title_title.Wrap( -1 )

		self.m_title_title.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		m_device_title.Add( self.m_title_title, 0, wx.ALL, 5 )


		m_device_container.Add( m_device_title, 1, wx.EXPAND, 5 )

		m_device_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_device_container.SetFlexibleDirection( wx.BOTH )
		m_device_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_t_d_camera = wx.StaticText( self.m_device_page, wx.ID_ANY, _(u"相机"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_d_camera.Wrap( -1 )

		m_device_container.Add( self.m_t_d_camera, 0, wx.ALL, 5 )

		m_device_cameraChoices = []
		self.m_device_camera = wx.Choice( self.m_device_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_device_cameraChoices, 0 )
		self.m_device_camera.SetSelection( 0 )
		m_device_container.Add( self.m_device_camera, 0, wx.ALL, 5 )

		self.m_t_d_mount = wx.StaticText( self.m_device_page, wx.ID_ANY, _(u"赤道仪"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_d_mount.Wrap( -1 )

		m_device_container.Add( self.m_t_d_mount, 0, wx.ALL, 5 )

		m_device_mountChoices = []
		self.m_device_mount = wx.Choice( self.m_device_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_device_mountChoices, 0 )
		self.m_device_mount.SetSelection( 0 )
		m_device_container.Add( self.m_device_mount, 0, wx.ALL, 5 )

		self.m_t_d_focuser = wx.StaticText( self.m_device_page, wx.ID_ANY, _(u"电调"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_d_focuser.Wrap( -1 )

		m_device_container.Add( self.m_t_d_focuser, 0, wx.ALL, 5 )

		m_device_focuserChoices = []
		self.m_device_focuser = wx.Choice( self.m_device_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_device_focuserChoices, 0 )
		self.m_device_focuser.SetSelection( 0 )
		m_device_container.Add( self.m_device_focuser, 0, wx.ALL, 5 )

		self.m_t_d_guider = wx.StaticText( self.m_device_page, wx.ID_ANY, _(u"导星"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_d_guider.Wrap( -1 )

		m_device_container.Add( self.m_t_d_guider, 0, wx.ALL, 5 )

		m_device_guiderChoices = []
		self.m_device_guider = wx.Choice( self.m_device_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_device_guiderChoices, 0 )
		self.m_device_guider.SetSelection( 0 )
		m_device_container.Add( self.m_device_guider, 0, wx.ALL, 5 )

		self.m_t_d_align = wx.StaticText( self.m_device_page, wx.ID_ANY, _(u"对齐"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_d_align.Wrap( -1 )

		m_device_container.Add( self.m_t_d_align, 0, wx.ALL, 5 )

		m_device_alighChoices = []
		self.m_device_aligh = wx.Choice( self.m_device_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_device_alighChoices, 0 )
		self.m_device_aligh.SetSelection( 0 )
		m_device_container.Add( self.m_device_aligh, 0, wx.ALL, 5 )


		m_device_container.Add( m_device_container, 1, wx.EXPAND, 5 )


		m_device_box.Add( m_device_container, 1, wx.EXPAND, 5 )


		self.m_device_page.SetSizer( m_device_box )
		self.m_device_page.Layout()
		m_device_box.Fit( self.m_device_page )
		self.m_weather_page = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_weather_page )

		m_weather_box = wx.BoxSizer( wx.VERTICAL )

		m_weather_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_weather_container.SetFlexibleDirection( wx.BOTH )
		m_weather_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_t_w_city = wx.StaticText( self.m_weather_page, wx.ID_ANY, _(u"城市"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_w_city.Wrap( -1 )

		m_weather_container.Add( self.m_t_w_city, 0, wx.ALL, 5 )

		self.m_weather_city = wx.TextCtrl( self.m_weather_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_weather_container.Add( self.m_weather_city, 0, wx.ALL, 5 )

		self.m_t_w_license = wx.StaticText( self.m_weather_page, wx.ID_ANY, _(u"证书"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_w_license.Wrap( -1 )

		m_weather_container.Add( self.m_t_w_license, 0, wx.ALL, 5 )

		m_weather_licenseChoices = [ _(u"开源"), _(u"商业") ]
		self.m_weather_license = wx.Choice( self.m_weather_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_weather_licenseChoices, 0 )
		self.m_weather_license.SetSelection( 0 )
		m_weather_container.Add( self.m_weather_license, 0, wx.ALL, 5 )

		self.m_t_w_key = wx.StaticText( self.m_weather_page, wx.ID_ANY, _(u"密钥"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_w_key.Wrap( -1 )

		m_weather_container.Add( self.m_t_w_key, 0, wx.ALL, 5 )

		self.m_weather_key = wx.TextCtrl( self.m_weather_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_weather_container.Add( self.m_weather_key, 0, wx.ALL, 5 )

		self.m_t_w_lat = wx.StaticText( self.m_weather_page, wx.ID_ANY, _(u"经度"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_w_lat.Wrap( -1 )

		m_weather_container.Add( self.m_t_w_lat, 0, wx.ALL, 5 )

		self.m_weather_lat = wx.TextCtrl( self.m_weather_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_weather_container.Add( self.m_weather_lat, 0, wx.ALL, 5 )

		self.m_t_w_lon = wx.StaticText( self.m_weather_page, wx.ID_ANY, _(u"纬度"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_w_lon.Wrap( -1 )

		m_weather_container.Add( self.m_t_w_lon, 0, wx.ALL, 5 )

		self.m_weather_lon = wx.TextCtrl( self.m_weather_page, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_weather_container.Add( self.m_weather_lon, 0, wx.ALL, 5 )


		m_weather_box.Add( m_weather_container, 1, wx.EXPAND, 5 )


		self.m_weather_page.SetSizer( m_weather_box )
		self.m_weather_page.Layout()
		m_weather_box.Fit( self.m_weather_page )
		self.m_starsearch_page = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_starsearch_page )

		m_starsearch_box = wx.BoxSizer( wx.VERTICAL )

		m_starsearch_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_starsearch_container.SetFlexibleDirection( wx.BOTH )
		m_starsearch_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_t_ss_stardata = wx.StaticText( self.m_starsearch_page, wx.ID_ANY, _(u"星表"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_ss_stardata.Wrap( -1 )

		m_starsearch_container.Add( self.m_t_ss_stardata, 0, wx.ALL, 5 )

		m_starsearch_stardataChoices = [ _(u"默认") ]
		self.m_starsearch_stardata = wx.Choice( self.m_starsearch_page, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_starsearch_stardataChoices, 0 )
		self.m_starsearch_stardata.SetSelection( 0 )
		m_starsearch_container.Add( self.m_starsearch_stardata, 0, wx.ALL, 5 )


		m_starsearch_box.Add( m_starsearch_container, 1, wx.EXPAND, 5 )


		self.m_starsearch_page.SetSizer( m_starsearch_box )
		self.m_starsearch_page.Layout()
		m_starsearch_box.Fit( self.m_starsearch_page )
		self.m_finish_page = wx.adv.WizardPageSimple( self  )
		self.add_page( self.m_finish_page )

		m_finish_box = wx.BoxSizer( wx.VERTICAL )

		m_finish_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_finish_container.SetFlexibleDirection( wx.BOTH )
		m_finish_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_ = wx.StaticBitmap( self.m_finish_page, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_finish_container.Add( self.m_, 0, wx.ALL, 5 )

		self.m_staticText130 = wx.StaticText( self.m_finish_page, wx.ID_ANY, _(u"结束咯"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText130.Wrap( -1 )

		m_finish_container.Add( self.m_staticText130, 0, wx.ALL, 5 )


		m_finish_box.Add( m_finish_container, 1, wx.EXPAND, 5 )


		self.m_finish_page.SetSizer( m_finish_box )
		self.m_finish_page.Layout()
		m_finish_box.Fit( self.m_finish_page )
		self.Centre( wx.BOTH )

	def add_page(self, page):
		if self.m_pages:
			previous_page = self.m_pages[-1]
			page.SetPrev(previous_page)
			previous_page.SetNext(page)
		self.m_pages.append(page)

	def __del__( self ):
		pass


