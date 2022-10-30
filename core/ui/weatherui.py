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

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx

import gettext
_ = gettext.gettext

###########################################################################
## Class MyPanel11
###########################################################################

class m_weather_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 780,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetMinSize( wx.Size( 390,300 ) )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		fgSizer66 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer66.SetFlexibleDirection( wx.BOTH )
		fgSizer66.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer37 = wx.BoxSizer( wx.VERTICAL )

		fgSizer87 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer87.SetFlexibleDirection( wx.BOTH )
		fgSizer87.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer68 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer68.SetFlexibleDirection( wx.HORIZONTAL )
		fgSizer68.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_title = wx.StaticText( self, wx.ID_ANY, _(u"天气预报"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_title.Wrap( -1 )

		self.m_title.SetFont( wx.Font( 22, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "楷体" ) )

		fgSizer68.Add( self.m_title, 0, wx.ALL, 5 )

		self.m_search = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		fgSizer68.Add( self.m_search, 0, wx.ALL, 5 )

		self.m_location = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		fgSizer68.Add( self.m_location, 0, wx.ALL, 5 )

		self.m_help = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		fgSizer68.Add( self.m_help, 0, wx.ALL, 5 )


		fgSizer87.Add( fgSizer68, 1, wx.EXPAND, 5 )

		self.m_bitmap35 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		fgSizer87.Add( self.m_bitmap35, 0, wx.ALL, 5 )


		bSizer37.Add( fgSizer87, 1, wx.EXPAND, 5 )


		fgSizer66.Add( bSizer37, 1, wx.EXPAND, 5 )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		fgSizer70 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer70.SetFlexibleDirection( wx.BOTH )
		fgSizer70.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer39 = wx.BoxSizer( wx.VERTICAL )

		fgSizer74 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer74.SetFlexibleDirection( wx.BOTH )
		fgSizer74.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer41 = wx.BoxSizer( wx.VERTICAL )

		fgSizer72 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer72.SetFlexibleDirection( wx.BOTH )
		fgSizer72.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer71 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap18 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.m_bitmap18, 0, wx.ALL, 5 )

		self.m_staticText133 = wx.StaticText( self, wx.ID_ANY, _(u"实时天气"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133.Wrap( -1 )

		self.m_staticText133.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.m_staticText133.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer71.Add( self.m_staticText133, 0, wx.ALL, 5 )


		fgSizer72.Add( fgSizer71, 1, wx.EXPAND, 5 )

		self.m_panel51 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel51.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )

		fgSizer73 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer73.SetFlexibleDirection( wx.BOTH )
		fgSizer73.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText134 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText134.Wrap( -1 )

		fgSizer73.Add( self.m_staticText134, 0, wx.ALL, 5 )

		self.m_staticText135 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText135.Wrap( -1 )

		fgSizer73.Add( self.m_staticText135, 0, wx.ALL, 5 )

		self.m_staticText136 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText136.Wrap( -1 )

		fgSizer73.Add( self.m_staticText136, 0, wx.ALL, 5 )

		self.m_staticText137 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText137.Wrap( -1 )

		fgSizer73.Add( self.m_staticText137, 0, wx.ALL, 5 )

		self.m_staticText138 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText138.Wrap( -1 )

		fgSizer73.Add( self.m_staticText138, 0, wx.ALL, 5 )

		self.m_staticText139 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText139.Wrap( -1 )

		fgSizer73.Add( self.m_staticText139, 0, wx.ALL, 5 )

		self.m_staticText140 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText140.Wrap( -1 )

		fgSizer73.Add( self.m_staticText140, 0, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		fgSizer73.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.m_staticText142 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText142.Wrap( -1 )

		fgSizer73.Add( self.m_staticText142, 0, wx.ALL, 5 )

		self.m_staticText143 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText143.Wrap( -1 )

		fgSizer73.Add( self.m_staticText143, 0, wx.ALL, 5 )

		self.m_staticText144 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText144.Wrap( -1 )

		fgSizer73.Add( self.m_staticText144, 0, wx.ALL, 5 )

		self.m_staticText145 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText145.Wrap( -1 )

		fgSizer73.Add( self.m_staticText145, 0, wx.ALL, 5 )

		self.m_staticText146 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText146.Wrap( -1 )

		fgSizer73.Add( self.m_staticText146, 0, wx.ALL, 5 )

		self.m_staticText147 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText147.Wrap( -1 )

		fgSizer73.Add( self.m_staticText147, 0, wx.ALL, 5 )

		self.m_staticText148 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText148.Wrap( -1 )

		fgSizer73.Add( self.m_staticText148, 0, wx.ALL, 5 )

		self.m_staticText149 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText149.Wrap( -1 )

		fgSizer73.Add( self.m_staticText149, 0, wx.ALL, 5 )

		self.m_staticText150 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText150.Wrap( -1 )

		fgSizer73.Add( self.m_staticText150, 0, wx.ALL, 5 )

		self.m_staticText151 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )

		fgSizer73.Add( self.m_staticText151, 0, wx.ALL, 5 )

		self.m_staticText152 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText152.Wrap( -1 )

		fgSizer73.Add( self.m_staticText152, 0, wx.ALL, 5 )

		self.m_staticText153 = wx.StaticText( self.m_panel51, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText153.Wrap( -1 )

		fgSizer73.Add( self.m_staticText153, 0, wx.ALL, 5 )


		self.m_panel51.SetSizer( fgSizer73 )
		self.m_panel51.Layout()
		fgSizer73.Fit( self.m_panel51 )
		fgSizer72.Add( self.m_panel51, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer41.Add( fgSizer72, 1, wx.EXPAND, 5 )


		fgSizer74.Add( bSizer41, 1, wx.EXPAND, 5 )

		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		fgSizer75 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer75.SetFlexibleDirection( wx.BOTH )
		fgSizer75.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer46 = wx.BoxSizer( wx.VERTICAL )

		fgSizer76 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer76.SetFlexibleDirection( wx.BOTH )
		fgSizer76.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap19 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer76.Add( self.m_bitmap19, 0, wx.ALL, 5 )

		self.m_staticText155 = wx.StaticText( self, wx.ID_ANY, _(u"七天天气"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText155.Wrap( -1 )

		self.m_staticText155.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )

		fgSizer76.Add( self.m_staticText155, 0, wx.ALL, 5 )


		bSizer46.Add( fgSizer76, 1, wx.EXPAND, 5 )


		fgSizer75.Add( bSizer46, 1, wx.EXPAND, 5 )

		bSizer42 = wx.BoxSizer( wx.VERTICAL )

		fgSizer77 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer77.SetFlexibleDirection( wx.BOTH )
		fgSizer77.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel44 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel44.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer47 = wx.BoxSizer( wx.VERTICAL )

		fgSizer78 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer78.SetFlexibleDirection( wx.BOTH )
		fgSizer78.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap20 = wx.StaticBitmap( self.m_panel44, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer78.Add( self.m_bitmap20, 0, wx.ALL, 5 )

		self.m_staticText156 = wx.StaticText( self.m_panel44, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText156.Wrap( -1 )

		fgSizer78.Add( self.m_staticText156, 0, wx.ALL, 5 )

		self.m_staticText157 = wx.StaticText( self.m_panel44, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText157.Wrap( -1 )

		fgSizer78.Add( self.m_staticText157, 0, wx.ALL, 5 )

		self.m_staticText158 = wx.StaticText( self.m_panel44, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText158.Wrap( -1 )

		fgSizer78.Add( self.m_staticText158, 0, wx.ALL, 5 )

		self.m_staticText159 = wx.StaticText( self.m_panel44, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText159.Wrap( -1 )

		fgSizer78.Add( self.m_staticText159, 0, wx.ALL, 5 )

		self.m_staticText160 = wx.StaticText( self.m_panel44, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText160.Wrap( -1 )

		fgSizer78.Add( self.m_staticText160, 0, wx.ALL, 5 )

		self.m_staticText161 = wx.StaticText( self.m_panel44, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		fgSizer78.Add( self.m_staticText161, 0, wx.ALL, 5 )

		self.m_staticText162 = wx.StaticText( self.m_panel44, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )

		fgSizer78.Add( self.m_staticText162, 0, wx.ALL, 5 )

		self.m_staticText163 = wx.StaticText( self.m_panel44, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText163.Wrap( -1 )

		fgSizer78.Add( self.m_staticText163, 0, wx.ALL, 5 )


		bSizer47.Add( fgSizer78, 1, wx.EXPAND, 5 )


		self.m_panel44.SetSizer( bSizer47 )
		self.m_panel44.Layout()
		bSizer47.Fit( self.m_panel44 )
		fgSizer77.Add( self.m_panel44, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel45 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel45.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer471 = wx.BoxSizer( wx.VERTICAL )

		fgSizer781 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer781.SetFlexibleDirection( wx.BOTH )
		fgSizer781.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap201 = wx.StaticBitmap( self.m_panel45, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer781.Add( self.m_bitmap201, 0, wx.ALL, 5 )

		self.m_staticText1561 = wx.StaticText( self.m_panel45, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1561.Wrap( -1 )

		fgSizer781.Add( self.m_staticText1561, 0, wx.ALL, 5 )

		self.m_staticText1571 = wx.StaticText( self.m_panel45, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1571.Wrap( -1 )

		fgSizer781.Add( self.m_staticText1571, 0, wx.ALL, 5 )

		self.m_staticText1581 = wx.StaticText( self.m_panel45, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1581.Wrap( -1 )

		fgSizer781.Add( self.m_staticText1581, 0, wx.ALL, 5 )

		self.m_staticText1591 = wx.StaticText( self.m_panel45, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1591.Wrap( -1 )

		fgSizer781.Add( self.m_staticText1591, 0, wx.ALL, 5 )

		self.m_staticText1601 = wx.StaticText( self.m_panel45, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1601.Wrap( -1 )

		fgSizer781.Add( self.m_staticText1601, 0, wx.ALL, 5 )

		self.m_staticText1611 = wx.StaticText( self.m_panel45, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1611.Wrap( -1 )

		fgSizer781.Add( self.m_staticText1611, 0, wx.ALL, 5 )

		self.m_staticText1621 = wx.StaticText( self.m_panel45, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1621.Wrap( -1 )

		fgSizer781.Add( self.m_staticText1621, 0, wx.ALL, 5 )

		self.m_staticText1631 = wx.StaticText( self.m_panel45, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1631.Wrap( -1 )

		fgSizer781.Add( self.m_staticText1631, 0, wx.ALL, 5 )


		bSizer471.Add( fgSizer781, 1, wx.EXPAND, 5 )


		self.m_panel45.SetSizer( bSizer471 )
		self.m_panel45.Layout()
		bSizer471.Fit( self.m_panel45 )
		fgSizer77.Add( self.m_panel45, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel46 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel46.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer472 = wx.BoxSizer( wx.VERTICAL )

		fgSizer782 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer782.SetFlexibleDirection( wx.BOTH )
		fgSizer782.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap202 = wx.StaticBitmap( self.m_panel46, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer782.Add( self.m_bitmap202, 0, wx.ALL, 5 )

		self.m_staticText1562 = wx.StaticText( self.m_panel46, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1562.Wrap( -1 )

		fgSizer782.Add( self.m_staticText1562, 0, wx.ALL, 5 )

		self.m_staticText1572 = wx.StaticText( self.m_panel46, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1572.Wrap( -1 )

		fgSizer782.Add( self.m_staticText1572, 0, wx.ALL, 5 )

		self.m_staticText1582 = wx.StaticText( self.m_panel46, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1582.Wrap( -1 )

		fgSizer782.Add( self.m_staticText1582, 0, wx.ALL, 5 )

		self.m_staticText1592 = wx.StaticText( self.m_panel46, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1592.Wrap( -1 )

		fgSizer782.Add( self.m_staticText1592, 0, wx.ALL, 5 )

		self.m_staticText1602 = wx.StaticText( self.m_panel46, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1602.Wrap( -1 )

		fgSizer782.Add( self.m_staticText1602, 0, wx.ALL, 5 )

		self.m_staticText1612 = wx.StaticText( self.m_panel46, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1612.Wrap( -1 )

		fgSizer782.Add( self.m_staticText1612, 0, wx.ALL, 5 )

		self.m_staticText1622 = wx.StaticText( self.m_panel46, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1622.Wrap( -1 )

		fgSizer782.Add( self.m_staticText1622, 0, wx.ALL, 5 )

		self.m_staticText1632 = wx.StaticText( self.m_panel46, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1632.Wrap( -1 )

		fgSizer782.Add( self.m_staticText1632, 0, wx.ALL, 5 )


		bSizer472.Add( fgSizer782, 1, wx.EXPAND, 5 )


		self.m_panel46.SetSizer( bSizer472 )
		self.m_panel46.Layout()
		bSizer472.Fit( self.m_panel46 )
		fgSizer77.Add( self.m_panel46, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel47 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel47.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer473 = wx.BoxSizer( wx.VERTICAL )

		fgSizer783 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer783.SetFlexibleDirection( wx.BOTH )
		fgSizer783.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap203 = wx.StaticBitmap( self.m_panel47, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer783.Add( self.m_bitmap203, 0, wx.ALL, 5 )

		self.m_staticText1563 = wx.StaticText( self.m_panel47, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1563.Wrap( -1 )

		fgSizer783.Add( self.m_staticText1563, 0, wx.ALL, 5 )

		self.m_staticText1573 = wx.StaticText( self.m_panel47, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1573.Wrap( -1 )

		fgSizer783.Add( self.m_staticText1573, 0, wx.ALL, 5 )

		self.m_staticText1583 = wx.StaticText( self.m_panel47, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1583.Wrap( -1 )

		fgSizer783.Add( self.m_staticText1583, 0, wx.ALL, 5 )

		self.m_staticText1593 = wx.StaticText( self.m_panel47, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1593.Wrap( -1 )

		fgSizer783.Add( self.m_staticText1593, 0, wx.ALL, 5 )

		self.m_staticText1603 = wx.StaticText( self.m_panel47, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1603.Wrap( -1 )

		fgSizer783.Add( self.m_staticText1603, 0, wx.ALL, 5 )

		self.m_staticText1613 = wx.StaticText( self.m_panel47, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1613.Wrap( -1 )

		fgSizer783.Add( self.m_staticText1613, 0, wx.ALL, 5 )

		self.m_staticText1623 = wx.StaticText( self.m_panel47, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1623.Wrap( -1 )

		fgSizer783.Add( self.m_staticText1623, 0, wx.ALL, 5 )

		self.m_staticText1633 = wx.StaticText( self.m_panel47, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1633.Wrap( -1 )

		fgSizer783.Add( self.m_staticText1633, 0, wx.ALL, 5 )


		bSizer473.Add( fgSizer783, 1, wx.EXPAND, 5 )


		self.m_panel47.SetSizer( bSizer473 )
		self.m_panel47.Layout()
		bSizer473.Fit( self.m_panel47 )
		fgSizer77.Add( self.m_panel47, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel48 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel48.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer474 = wx.BoxSizer( wx.VERTICAL )

		fgSizer784 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer784.SetFlexibleDirection( wx.BOTH )
		fgSizer784.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap204 = wx.StaticBitmap( self.m_panel48, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer784.Add( self.m_bitmap204, 0, wx.ALL, 5 )

		self.m_staticText1564 = wx.StaticText( self.m_panel48, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1564.Wrap( -1 )

		fgSizer784.Add( self.m_staticText1564, 0, wx.ALL, 5 )

		self.m_staticText1574 = wx.StaticText( self.m_panel48, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1574.Wrap( -1 )

		fgSizer784.Add( self.m_staticText1574, 0, wx.ALL, 5 )

		self.m_staticText1584 = wx.StaticText( self.m_panel48, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1584.Wrap( -1 )

		fgSizer784.Add( self.m_staticText1584, 0, wx.ALL, 5 )

		self.m_staticText1594 = wx.StaticText( self.m_panel48, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1594.Wrap( -1 )

		fgSizer784.Add( self.m_staticText1594, 0, wx.ALL, 5 )

		self.m_staticText1604 = wx.StaticText( self.m_panel48, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1604.Wrap( -1 )

		fgSizer784.Add( self.m_staticText1604, 0, wx.ALL, 5 )

		self.m_staticText1614 = wx.StaticText( self.m_panel48, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1614.Wrap( -1 )

		fgSizer784.Add( self.m_staticText1614, 0, wx.ALL, 5 )

		self.m_staticText1624 = wx.StaticText( self.m_panel48, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1624.Wrap( -1 )

		fgSizer784.Add( self.m_staticText1624, 0, wx.ALL, 5 )

		self.m_staticText1634 = wx.StaticText( self.m_panel48, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1634.Wrap( -1 )

		fgSizer784.Add( self.m_staticText1634, 0, wx.ALL, 5 )


		bSizer474.Add( fgSizer784, 1, wx.EXPAND, 5 )


		self.m_panel48.SetSizer( bSizer474 )
		self.m_panel48.Layout()
		bSizer474.Fit( self.m_panel48 )
		fgSizer77.Add( self.m_panel48, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel49 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel49.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer475 = wx.BoxSizer( wx.VERTICAL )

		fgSizer785 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer785.SetFlexibleDirection( wx.BOTH )
		fgSizer785.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap205 = wx.StaticBitmap( self.m_panel49, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer785.Add( self.m_bitmap205, 0, wx.ALL, 5 )

		self.m_staticText1565 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1565.Wrap( -1 )

		fgSizer785.Add( self.m_staticText1565, 0, wx.ALL, 5 )

		self.m_staticText1575 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1575.Wrap( -1 )

		fgSizer785.Add( self.m_staticText1575, 0, wx.ALL, 5 )

		self.m_staticText1585 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1585.Wrap( -1 )

		fgSizer785.Add( self.m_staticText1585, 0, wx.ALL, 5 )

		self.m_staticText1595 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1595.Wrap( -1 )

		fgSizer785.Add( self.m_staticText1595, 0, wx.ALL, 5 )

		self.m_staticText1605 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1605.Wrap( -1 )

		fgSizer785.Add( self.m_staticText1605, 0, wx.ALL, 5 )

		self.m_staticText1615 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1615.Wrap( -1 )

		fgSizer785.Add( self.m_staticText1615, 0, wx.ALL, 5 )

		self.m_staticText1625 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1625.Wrap( -1 )

		fgSizer785.Add( self.m_staticText1625, 0, wx.ALL, 5 )

		self.m_staticText1635 = wx.StaticText( self.m_panel49, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1635.Wrap( -1 )

		fgSizer785.Add( self.m_staticText1635, 0, wx.ALL, 5 )


		bSizer475.Add( fgSizer785, 1, wx.EXPAND, 5 )


		self.m_panel49.SetSizer( bSizer475 )
		self.m_panel49.Layout()
		bSizer475.Fit( self.m_panel49 )
		fgSizer77.Add( self.m_panel49, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel50 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel50.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )

		bSizer476 = wx.BoxSizer( wx.VERTICAL )

		fgSizer786 = wx.FlexGridSizer( 1, 0, 0, 0 )
		fgSizer786.SetFlexibleDirection( wx.BOTH )
		fgSizer786.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap206 = wx.StaticBitmap( self.m_panel50, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer786.Add( self.m_bitmap206, 0, wx.ALL, 5 )

		self.m_staticText1566 = wx.StaticText( self.m_panel50, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1566.Wrap( -1 )

		fgSizer786.Add( self.m_staticText1566, 0, wx.ALL, 5 )

		self.m_staticText1576 = wx.StaticText( self.m_panel50, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1576.Wrap( -1 )

		fgSizer786.Add( self.m_staticText1576, 0, wx.ALL, 5 )

		self.m_staticText1586 = wx.StaticText( self.m_panel50, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1586.Wrap( -1 )

		fgSizer786.Add( self.m_staticText1586, 0, wx.ALL, 5 )

		self.m_staticText1596 = wx.StaticText( self.m_panel50, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1596.Wrap( -1 )

		fgSizer786.Add( self.m_staticText1596, 0, wx.ALL, 5 )

		self.m_staticText1606 = wx.StaticText( self.m_panel50, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1606.Wrap( -1 )

		fgSizer786.Add( self.m_staticText1606, 0, wx.ALL, 5 )

		self.m_staticText1616 = wx.StaticText( self.m_panel50, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1616.Wrap( -1 )

		fgSizer786.Add( self.m_staticText1616, 0, wx.ALL, 5 )

		self.m_staticText1626 = wx.StaticText( self.m_panel50, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1626.Wrap( -1 )

		fgSizer786.Add( self.m_staticText1626, 0, wx.ALL, 5 )

		self.m_staticText1636 = wx.StaticText( self.m_panel50, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1636.Wrap( -1 )

		fgSizer786.Add( self.m_staticText1636, 0, wx.ALL, 5 )


		bSizer476.Add( fgSizer786, 1, wx.EXPAND, 5 )


		self.m_panel50.SetSizer( bSizer476 )
		self.m_panel50.Layout()
		bSizer476.Fit( self.m_panel50 )
		fgSizer77.Add( self.m_panel50, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer42.Add( fgSizer77, 1, wx.EXPAND, 5 )


		fgSizer75.Add( bSizer42, 1, wx.EXPAND, 5 )


		bSizer40.Add( fgSizer75, 1, wx.EXPAND, 5 )


		fgSizer74.Add( bSizer40, 1, wx.EXPAND, 5 )


		bSizer39.Add( fgSizer74, 1, wx.EXPAND, 5 )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		fgSizer86 = wx.FlexGridSizer( 0, 7, 0, 0 )
		fgSizer86.SetFlexibleDirection( wx.BOTH )
		fgSizer86.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap28 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_bitmap28, 0, wx.ALL, 5 )

		self.m_bitmap29 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_bitmap29, 0, wx.ALL, 5 )

		self.m_bitmap30 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_bitmap30, 0, wx.ALL, 5 )

		self.m_bitmap31 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_bitmap31, 0, wx.ALL, 5 )

		self.m_bitmap32 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_bitmap32, 0, wx.ALL, 5 )

		self.m_bitmap33 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_bitmap33, 0, wx.ALL, 5 )

		self.m_bitmap34 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer86.Add( self.m_bitmap34, 0, wx.ALL, 5 )

		self.m_staticText220 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText220.Wrap( -1 )

		fgSizer86.Add( self.m_staticText220, 0, wx.ALL, 5 )

		self.m_staticText221 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		fgSizer86.Add( self.m_staticText221, 0, wx.ALL, 5 )

		self.m_staticText222 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText222.Wrap( -1 )

		fgSizer86.Add( self.m_staticText222, 0, wx.ALL, 5 )

		self.m_staticText223 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText223.Wrap( -1 )

		fgSizer86.Add( self.m_staticText223, 0, wx.ALL, 5 )

		self.m_staticText224 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText224.Wrap( -1 )

		fgSizer86.Add( self.m_staticText224, 0, wx.ALL, 5 )

		self.m_staticText225 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText225.Wrap( -1 )

		fgSizer86.Add( self.m_staticText225, 0, wx.ALL, 5 )

		self.m_staticText226 = wx.StaticText( self, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText226.Wrap( -1 )

		fgSizer86.Add( self.m_staticText226, 0, wx.ALL, 5 )


		bSizer61.Add( fgSizer86, 1, wx.EXPAND, 5 )


		bSizer39.Add( bSizer61, 1, wx.EXPAND, 5 )


		fgSizer70.Add( bSizer39, 1, wx.EXPAND, 5 )


		bSizer38.Add( fgSizer70, 1, wx.EXPAND, 5 )


		fgSizer66.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer36.Add( fgSizer66, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer36 )
		self.Layout()

		# Connect Events
		self.m_search.Bind( wx.EVT_BUTTON, self.on_search_click )
		self.m_location.Bind( wx.EVT_BUTTON, self.on_location_click )
		self.m_help.Bind( wx.EVT_BUTTON, self.on_help_click )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_search_click( self, event ):
		event.Skip()

	def on_location_click( self, event ):
		event.Skip()

	def on_help_click( self, event ):
		event.Skip()


