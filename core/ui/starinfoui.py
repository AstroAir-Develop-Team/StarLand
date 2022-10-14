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

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class m_starinfo
###########################################################################

class m_starinfo_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 650,360 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		m_starinfo_box = wx.BoxSizer( wx.VERTICAL )

		self.m_starinfo_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_sun = wx.Panel( self.m_starinfo_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_sun_info_box = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_sun_info_box.SetFlexibleDirection( wx.BOTH )
		m_sun_info_box.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_sun_info = wx.FlexGridSizer( 0, 4, 0, 0 )
		m_sun_info.SetFlexibleDirection( wx.BOTH )
		m_sun_info.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_starinfo_sun_info_ra = wx.StaticText( self.m_sun, wx.ID_ANY, u"赤经", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_starinfo_sun_info_ra.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_ra, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_ra_show = wx.StaticText( self.m_sun, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.m_starinfo_sun_info_ra_show.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_ra_show, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_dec = wx.StaticText( self.m_sun, wx.ID_ANY, u"赤纬", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_dec.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_dec, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_dec_show = wx.StaticText( self.m_sun, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.m_starinfo_sun_info_dec_show.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_dec_show, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_sunrise = wx.StaticText( self.m_sun, wx.ID_ANY, u"升起", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_sunrise.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_sunrise, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_sunrise_show = wx.StaticText( self.m_sun, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_sunrise_show.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_sunrise_show, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_sunset = wx.StaticText( self.m_sun, wx.ID_ANY, u"落下", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_sunset.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_sunset, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_sunset_show = wx.StaticText( self.m_sun, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_sunset_show.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_sunset_show, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_mid = wx.StaticText( self.m_sun, wx.ID_ANY, u"中天", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_mid.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_mid, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_mid_show = wx.StaticText( self.m_sun, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_mid_show.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_mid_show, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_az = wx.StaticText( self.m_sun, wx.ID_ANY, u"地平经度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_az.Wrap( -1 )

		self.m_starinfo_sun_info_az.SetToolTip( u"地平经度" )

		m_sun_info.Add( self.m_starinfo_sun_info_az, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_az_show = wx.StaticText( self.m_sun, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_az_show.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_az_show, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_alt = wx.StaticText( self.m_sun, wx.ID_ANY, u"地平纬度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_alt.Wrap( -1 )

		self.m_starinfo_sun_info_alt.SetToolTip( u"地平纬度" )

		m_sun_info.Add( self.m_starinfo_sun_info_alt, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_alt_show = wx.StaticText( self.m_sun, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_alt_show.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_alt_show, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_season = wx.StaticText( self.m_sun, wx.ID_ANY, u"冬至", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_season.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_season, 0, wx.ALL, 5 )

		self.m_starinfo_sun_info_season_show = wx.StaticText( self.m_sun, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_sun_info_season_show.Wrap( -1 )

		m_sun_info.Add( self.m_starinfo_sun_info_season_show, 0, wx.ALL, 5 )


		m_sun_info_box.Add( m_sun_info, 1, wx.EXPAND, 5 )


		self.m_sun.SetSizer( m_sun_info_box )
		self.m_sun.Layout()
		m_sun_info_box.Fit( self.m_sun )
		self.m_starinfo_notebook.AddPage( self.m_sun, u"太阳", True )
		self.m_moon = wx.Panel( self.m_starinfo_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_moon_info_box = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_moon_info_box.SetFlexibleDirection( wx.BOTH )
		m_moon_info_box.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_moon_info = wx.FlexGridSizer( 0, 4, 0, 0 )
		m_moon_info.SetFlexibleDirection( wx.BOTH )
		m_moon_info.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_starinfo_moon_info_ra = wx.StaticText( self.m_moon, wx.ID_ANY, u"赤经", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_ra.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_ra, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_ra_show = wx.StaticText( self.m_moon, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.m_starinfo_moon_info_ra_show.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_ra_show, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_dec = wx.StaticText( self.m_moon, wx.ID_ANY, u"赤纬", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_dec.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_dec, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_dec_show = wx.StaticText( self.m_moon, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_dec_show.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_dec_show, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_moonrise = wx.StaticText( self.m_moon, wx.ID_ANY, u"升起", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_moonrise.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_moonrise, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_moonrise_show = wx.StaticText( self.m_moon, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_moonrise_show.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_moonrise_show, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_moonset = wx.StaticText( self.m_moon, wx.ID_ANY, u"落下", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_moonset.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_moonset, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_moonset_show = wx.StaticText( self.m_moon, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_moonset_show.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_moonset_show, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_mid = wx.StaticText( self.m_moon, wx.ID_ANY, u"中天", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_mid.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_mid, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_mid_show = wx.StaticText( self.m_moon, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_mid_show.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_mid_show, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_az = wx.StaticText( self.m_moon, wx.ID_ANY, u"地平经度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_az.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_az, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_az_show = wx.StaticText( self.m_moon, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_az_show.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_az_show, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_alt = wx.StaticText( self.m_moon, wx.ID_ANY, u"地平纬度", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_alt.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_alt, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_alt_show = wx.StaticText( self.m_moon, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_alt_show.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_alt_show, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_full = wx.StaticText( self.m_moon, wx.ID_ANY, u"下个满月", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_full.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_full, 0, wx.ALL, 5 )

		self.m_starinfo_moon_info_full_show = wx.StaticText( self.m_moon, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_moon_info_full_show.Wrap( -1 )

		m_moon_info.Add( self.m_starinfo_moon_info_full_show, 0, wx.ALL, 5 )


		m_moon_info_box.Add( m_moon_info, 1, wx.EXPAND, 5 )


		self.m_moon.SetSizer( m_moon_info_box )
		self.m_moon.Layout()
		m_moon_info_box.Fit( self.m_moon )
		self.m_starinfo_notebook.AddPage( self.m_moon, u"月球", False )
		self.m_planet = wx.Panel( self.m_starinfo_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_starinfo_solar_info = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_starinfo_solar_info.SetFlexibleDirection( wx.BOTH )
		m_starinfo_solar_info.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_starinfo_solar_choose = wx.FlexGridSizer( 0, 4, 0, 0 )
		m_starinfo_solar_choose.SetFlexibleDirection( wx.BOTH )
		m_starinfo_solar_choose.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_starinfo_solar_mercury_button = wx.BitmapButton( self.m_planet, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 35,35 ), wx.BU_AUTODRAW|0 )
		m_starinfo_solar_choose.Add( self.m_starinfo_solar_mercury_button, 0, wx.ALL, 1 )

		self.m_starinfo_solar_venus_button = wx.BitmapButton( self.m_planet, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 35,35 ), wx.BU_AUTODRAW|0 )
		m_starinfo_solar_choose.Add( self.m_starinfo_solar_venus_button, 0, wx.ALL, 1 )

		self.m_starinfo_solar_earth_button = wx.BitmapButton( self.m_planet, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 35,35 ), wx.BU_AUTODRAW|0 )
		m_starinfo_solar_choose.Add( self.m_starinfo_solar_earth_button, 0, wx.ALL, 1 )

		self.m_starinfo_solar_mars_button = wx.BitmapButton( self.m_planet, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 35,35 ), wx.BU_AUTODRAW|0 )
		m_starinfo_solar_choose.Add( self.m_starinfo_solar_mars_button, 0, wx.ALL, 1 )

		self.m_starinfo_solar_jupiter_button = wx.BitmapButton( self.m_planet, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 35,35 ), wx.BU_AUTODRAW|0 )
		m_starinfo_solar_choose.Add( self.m_starinfo_solar_jupiter_button, 0, wx.ALL, 1 )

		self.m_starinfo_solar_saturn_button = wx.BitmapButton( self.m_planet, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 35,35 ), wx.BU_AUTODRAW|0 )
		m_starinfo_solar_choose.Add( self.m_starinfo_solar_saturn_button, 0, wx.ALL, 1 )

		self.m_starinfo_solar_uranus_button = wx.BitmapButton( self.m_planet, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 35,35 ), wx.BU_AUTODRAW|0 )
		m_starinfo_solar_choose.Add( self.m_starinfo_solar_uranus_button, 0, wx.ALL, 1 )

		self.m_starinfo_solar_neptune_button = wx.BitmapButton( self.m_planet, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 35,35 ), wx.BU_AUTODRAW|0 )
		m_starinfo_solar_choose.Add( self.m_starinfo_solar_neptune_button, 0, wx.ALL, 1 )


		m_starinfo_solar_info.Add( m_starinfo_solar_choose, 1, wx.EXPAND, 1 )

		m_starinfo_solar_choose_info = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_starinfo_solar_choose_info.SetFlexibleDirection( wx.BOTH )
		m_starinfo_solar_choose_info.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_starinfo_solar_info_ra = wx.StaticText( self.m_planet, wx.ID_ANY, u"赤经        ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_solar_info_ra.Wrap( -1 )

		m_starinfo_solar_choose_info.Add( self.m_starinfo_solar_info_ra, 0, wx.ALL, 5 )

		self.m_starinfo_solar_info_ra_show = wx.StaticText( self.m_planet, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.m_starinfo_solar_info_ra_show.Wrap( -1 )

		m_starinfo_solar_choose_info.Add( self.m_starinfo_solar_info_ra_show, 0, wx.ALL, 5 )

		self.m_starinfo_solar_info_dec = wx.StaticText( self.m_planet, wx.ID_ANY, u"赤纬", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_solar_info_dec.Wrap( -1 )

		m_starinfo_solar_choose_info.Add( self.m_starinfo_solar_info_dec, 0, wx.ALL, 5 )

		self.m_starinfo_solar_info_dec_show = wx.StaticText( self.m_planet, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_solar_info_dec_show.Wrap( -1 )

		m_starinfo_solar_choose_info.Add( self.m_starinfo_solar_info_dec_show, 0, wx.ALL, 5 )

		self.m_starinfo_solar_info_rise = wx.StaticText( self.m_planet, wx.ID_ANY, u"升起", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_solar_info_rise.Wrap( -1 )

		m_starinfo_solar_choose_info.Add( self.m_starinfo_solar_info_rise, 0, wx.ALL, 5 )

		self.m_starinfo_solar_info_rise_show = wx.StaticText( self.m_planet, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_solar_info_rise_show.Wrap( -1 )

		m_starinfo_solar_choose_info.Add( self.m_starinfo_solar_info_rise_show, 0, wx.ALL, 5 )

		self.m_starinfo_solar_info_set = wx.StaticText( self.m_planet, wx.ID_ANY, u"落下", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_solar_info_set.Wrap( -1 )

		m_starinfo_solar_choose_info.Add( self.m_starinfo_solar_info_set, 0, wx.ALL, 5 )

		self.m_starinfo_solar_info_set_show = wx.StaticText( self.m_planet, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_solar_info_set_show.Wrap( -1 )

		m_starinfo_solar_choose_info.Add( self.m_starinfo_solar_info_set_show, 0, wx.ALL, 5 )

		self.m_starinfo_solar_info_mid = wx.StaticText( self.m_planet, wx.ID_ANY, u"中天", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_solar_info_mid.Wrap( -1 )

		m_starinfo_solar_choose_info.Add( self.m_starinfo_solar_info_mid, 0, wx.ALL, 5 )

		self.m_starinfo_solar_info_mid_show = wx.StaticText( self.m_planet, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_solar_info_mid_show.Wrap( -1 )

		m_starinfo_solar_choose_info.Add( self.m_starinfo_solar_info_mid_show, 0, wx.ALL, 5 )


		m_starinfo_solar_info.Add( m_starinfo_solar_choose_info, 1, wx.EXPAND, 5 )


		self.m_planet.SetSizer( m_starinfo_solar_info )
		self.m_planet.Layout()
		m_starinfo_solar_info.Fit( self.m_planet )
		self.m_starinfo_notebook.AddPage( self.m_planet, u"行星", False )
		self.m_polar = wx.Panel( self.m_starinfo_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		m_starinfo_polar_info = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_starinfo_polar_info.SetFlexibleDirection( wx.BOTH )
		m_starinfo_polar_info.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_starinfo_polar_info_angle = wx.StaticText( self.m_polar, wx.ID_ANY, u"时角", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_angle.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_angle, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_angle_show = wx.StaticText( self.m_polar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
		self.m_starinfo_polar_info_angle_show.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_angle_show, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_next = wx.StaticText( self.m_polar, wx.ID_ANY, u"下次过境", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_next.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_next, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_next_show = wx.StaticText( self.m_polar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_next_show.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_next_show, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_3 = wx.StaticText( self.m_polar, wx.ID_ANY, u"在3点时", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_3.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_3, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_3_show = wx.StaticText( self.m_polar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_3_show.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_3_show, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_12 = wx.StaticText( self.m_polar, wx.ID_ANY, u"在12点时", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_12.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_12, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_12_show = wx.StaticText( self.m_polar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_12_show.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_12_show, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_9 = wx.StaticText( self.m_polar, wx.ID_ANY, u"在9点时", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_9.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_9, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_9_show = wx.StaticText( self.m_polar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_9_show.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_9_show, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_lo = wx.StaticText( self.m_polar, wx.ID_ANY, u"海拔", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_lo.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_lo, 0, wx.ALL, 5 )

		self.m_starinfo_polar_info_lo_show = wx.StaticText( self.m_polar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_starinfo_polar_info_lo_show.Wrap( -1 )

		m_starinfo_polar_info.Add( self.m_starinfo_polar_info_lo_show, 0, wx.ALL, 5 )


		self.m_polar.SetSizer( m_starinfo_polar_info )
		self.m_polar.Layout()
		m_starinfo_polar_info.Fit( self.m_polar )
		self.m_starinfo_notebook.AddPage( self.m_polar, u"极轴", False )

		m_starinfo_box.Add( self.m_starinfo_notebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( m_starinfo_box )
		self.Layout()

	def __del__( self ):
		pass


