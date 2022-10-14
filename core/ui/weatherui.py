# -*- coding: utf-8 -*-

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

###########################################################################
## Class m_weather_panel
###########################################################################

class m_weather_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 650360,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		m_weather_container = wx.FlexGridSizer( 0, 3, 0, 0 )
		m_weather_container.SetFlexibleDirection( wx.BOTH )
		m_weather_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_weather_box = wx.GridBagSizer( 0, 0 )
		m_weather_box.SetFlexibleDirection( wx.BOTH )
		m_weather_box.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_weather_info = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_weather_info.SetFlexibleDirection( wx.BOTH )
		m_weather_info.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_info_t = wx.GridSizer( 0, 4, 0, 0 )

		self.m_info_status = wx.StaticText( self, wx.ID_ANY, u"状态", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_info_status.Wrap( -1 )

		m_info_t.Add( self.m_info_status, 0, wx.ALL, 5 )

		self.m_info_status_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_info_status_t.Wrap( -1 )

		m_info_t.Add( self.m_info_status_t, 0, wx.ALL, 5 )

		self.m_info_city = wx.StaticText( self, wx.ID_ANY, u"城市", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_info_city.Wrap( -1 )

		m_info_t.Add( self.m_info_city, 0, wx.ALL, 5 )

		self.m_info_city_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_info_city_t.Wrap( -1 )

		m_info_t.Add( self.m_info_city_t, 0, wx.ALL, 5 )

		self.m_info_weather = wx.StaticText( self, wx.ID_ANY, u"天气", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_weather.Wrap( -1 )

		m_info_t.Add( self.m_info_weather, 0, wx.ALL, 5 )

		self.m_info_weather_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_weather_t.Wrap( -1 )

		m_info_t.Add( self.m_info_weather_t, 0, wx.ALL, 5 )

		self.m_info_winddir = wx.StaticText( self, wx.ID_ANY, u"风向", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_winddir.Wrap( -1 )

		m_info_t.Add( self.m_info_winddir, 0, wx.ALL, 5 )

		self.m_info_windir_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_windir_t.Wrap( -1 )

		m_info_t.Add( self.m_info_windir_t, 0, wx.ALL, 5 )

		self.m_info_humidity = wx.StaticText( self, wx.ID_ANY, u"湿度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_humidity.Wrap( -1 )

		m_info_t.Add( self.m_info_humidity, 0, wx.ALL, 5 )

		self.m_info_humidity_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_humidity_t.Wrap( -1 )

		m_info_t.Add( self.m_info_humidity_t, 0, wx.ALL, 5 )

		self.m_info_precip = wx.StaticText( self, wx.ID_ANY, u"降水", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_precip.Wrap( -1 )

		m_info_t.Add( self.m_info_precip, 0, wx.ALL, 5 )

		self.m_info_precip_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_precip_t.Wrap( -1 )

		m_info_t.Add( self.m_info_precip_t, 0, wx.ALL, 5 )

		self.m_info_pressure = wx.StaticText( self, wx.ID_ANY, u"气压", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_pressure.Wrap( -1 )

		m_info_t.Add( self.m_info_pressure, 0, wx.ALL, 5 )

		self.m_info_pressure_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_pressure_t.Wrap( -1 )

		m_info_t.Add( self.m_info_pressure_t, 0, wx.ALL, 5 )

		self.m_info_vis = wx.StaticText( self, wx.ID_ANY, u"能见度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_vis.Wrap( -1 )

		m_info_t.Add( self.m_info_vis, 0, wx.ALL, 5 )

		self.m_info_vis_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_vis_t.Wrap( -1 )

		m_info_t.Add( self.m_info_vis_t, 0, wx.ALL, 5 )

		self.m_info_cloud = wx.StaticText( self, wx.ID_ANY, u"云量", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_cloud.Wrap( -1 )

		m_info_t.Add( self.m_info_cloud, 0, wx.ALL, 5 )

		self.m_info_cloud_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_cloud_t.Wrap( -1 )

		m_info_t.Add( self.m_info_cloud_t, 0, wx.ALL, 5 )

		self.m_info_warning = wx.StaticText( self, wx.ID_ANY, u"预警", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_warning.Wrap( -1 )

		m_info_t.Add( self.m_info_warning, 0, wx.ALL, 5 )

		self.m_info_warning_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_warning_t.Wrap( -1 )

		m_info_t.Add( self.m_info_warning_t, 0, wx.ALL, 5 )

		self.m_info_sunrise = wx.StaticText( self, wx.ID_ANY, u"日出", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_sunrise.Wrap( -1 )

		m_info_t.Add( self.m_info_sunrise, 0, wx.ALL, 5 )

		self.m_info_sunrise_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_sunrise_t.Wrap( -1 )

		m_info_t.Add( self.m_info_sunrise_t, 0, wx.ALL, 5 )

		self.m_info_sunset = wx.StaticText( self, wx.ID_ANY, u"日落", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_sunset.Wrap( -1 )

		m_info_t.Add( self.m_info_sunset, 0, wx.ALL, 5 )

		self.m_info_sunset_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_sunset_t.Wrap( -1 )

		m_info_t.Add( self.m_info_sunset_t, 0, wx.ALL, 5 )

		self.m_info_moonrise = wx.StaticText( self, wx.ID_ANY, u"月升", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_moonrise.Wrap( -1 )

		m_info_t.Add( self.m_info_moonrise, 0, wx.ALL, 5 )

		self.m_info_moonrise_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_moonrise_t.Wrap( -1 )

		m_info_t.Add( self.m_info_moonrise_t, 0, wx.ALL, 5 )

		self.m_info_moonset = wx.StaticText( self, wx.ID_ANY, u"月落", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_moonset.Wrap( -1 )

		m_info_t.Add( self.m_info_moonset, 0, wx.ALL, 5 )

		self.m_info_moonset_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_moonset_t.Wrap( -1 )

		m_info_t.Add( self.m_info_moonset_t, 0, wx.ALL, 5 )

		self.m_info_moonphase = wx.StaticText( self, wx.ID_ANY, u"月相", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_moonphase.Wrap( -1 )

		m_info_t.Add( self.m_info_moonphase, 0, wx.ALL, 5 )

		self.m_info_moonphase_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_moonphase_t.Wrap( -1 )

		m_info_t.Add( self.m_info_moonphase_t, 0, wx.ALL, 5 )

		self.m_info_angle = wx.StaticText( self, wx.ID_ANY, u"高度角", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_angle.Wrap( -1 )

		m_info_t.Add( self.m_info_angle, 0, wx.ALL, 5 )

		self.m_info_angle_t = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_info_angle_t.Wrap( -1 )

		m_info_t.Add( self.m_info_angle_t, 0, wx.ALL, 5 )


		m_weather_info.Add( m_info_t, 1, wx.EXPAND, 5 )

		m_info_b = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_info_b.SetFlexibleDirection( wx.BOTH )
		m_info_b.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_weather_b_refresh = wx.Button( self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		m_info_b.Add( self.m_weather_b_refresh, 0, wx.ALL, 5 )

		self.m_weather_b_relocate = wx.Button( self, wx.ID_ANY, u"重定位", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		m_info_b.Add( self.m_weather_b_relocate, 0, wx.ALL, 5 )

		self.m_weather_b_config = wx.Button( self, wx.ID_ANY, u"配置", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		m_info_b.Add( self.m_weather_b_config, 0, wx.ALL, 5 )

		self.m_weather_b_sync = wx.Button( self, wx.ID_ANY, u"同步", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		m_info_b.Add( self.m_weather_b_sync, 0, wx.ALL, 5 )


		m_weather_info.Add( m_info_b, 1, wx.EXPAND, 5 )


		m_weather_box.Add( m_weather_info, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		m_weather_city_location = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_weather_city_location.SetFlexibleDirection( wx.BOTH )
		m_weather_city_location.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_city_search_t = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_weather_city_location.Add( self.m_city_search_t, 0, wx.ALL, 5 )

		self.m_city_search = wx.Button( self, wx.ID_ANY, u"搜索", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_weather_city_location.Add( self.m_city_search, 0, wx.ALL, 5 )

		self.m_city_result = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )

		m_weather_city_location.Add( self.m_city_result, 1, wx.EXPAND |wx.ALL, 5 )


		m_weather_box.Add( m_weather_city_location, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		m_weather_container.Add( m_weather_box, 1, wx.EXPAND, 5 )


		m_weather_container.Add( ( 10, 0), 1, wx.EXPAND, 5 )

		m_weather_image = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_weather_image.SetFlexibleDirection( wx.BOTH )
		m_weather_image.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap10 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		m_weather_image.Add( self.m_bitmap10, 0, wx.ALL, 5 )

		self.m_bitmap11 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		m_weather_image.Add( self.m_bitmap11, 0, wx.ALL, 5 )


		m_weather_container.Add( m_weather_image, 1, wx.EXPAND, 5 )


		self.SetSizer( m_weather_container )
		self.Layout()

		# Connect Events
		self.m_weather_b_refresh.Bind( wx.EVT_BUTTON, self.on_weather_refresh )
		self.m_weather_b_relocate.Bind( wx.EVT_BUTTON, self.on_weather_relocate )
		self.m_weather_b_config.Bind( wx.EVT_BUTTON, self.on_weather_config )
		self.m_weather_b_sync.Bind( wx.EVT_BUTTON, self.on_weather_sync )
		self.m_city_search.Bind( wx.EVT_BUTTON, self.on_weather_search )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_weather_refresh( self, event ):
		event.Skip()

	def on_weather_relocate( self, event ):
		event.Skip()

	def on_weather_config( self, event ):
		event.Skip()

	def on_weather_sync( self, event ):
		event.Skip()

	def on_weather_search( self, event ):
		event.Skip()


