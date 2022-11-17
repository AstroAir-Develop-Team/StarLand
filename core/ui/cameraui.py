# coding=utf-8

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
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class m_camera
###########################################################################

class m_camera ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		m_c_b = wx.BoxSizer( wx.VERTICAL )

		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer42 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer42.SetFlexibleDirection( wx.BOTH )
		fgSizer42.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap11 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 300,300 ), 0 )
		fgSizer42.Add( self.m_bitmap11, 0, wx.ALL, 5 )

		self.m_staticline_l_1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer42.Add( self.m_staticline_l_1, 0, wx.EXPAND |wx.ALL, 5 )


		gbSizer3.Add( fgSizer42, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )

		fgSizer43 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer43.SetFlexibleDirection( wx.BOTH )
		fgSizer43.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		fgSizer44 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer44.SetFlexibleDirection( wx.BOTH )
		fgSizer44.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText90 = wx.StaticText( self, wx.ID_ANY, _(u"相机"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText90.Wrap( -1 )

		fgSizer44.Add( self.m_staticText90, 0, wx.ALL, 5 )

		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		fgSizer44.Add( self.m_choice1, 0, wx.ALL, 5 )

		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, _(u"Bin"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )

		fgSizer44.Add( self.m_staticText91, 0, wx.ALL, 5 )

		m_choice2Choices = []
		self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 0 )
		fgSizer44.Add( self.m_choice2, 0, wx.ALL, 5 )

		self.m_staticText92 = wx.StaticText( self, wx.ID_ANY, _(u"曝光"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )

		fgSizer44.Add( self.m_staticText92, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, _(u"1"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.m_textCtrl9, 0, wx.ALL, 5 )

		self.m_staticText93 = wx.StaticText( self, wx.ID_ANY, _(u"次数"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )

		fgSizer44.Add( self.m_staticText93, 0, wx.ALL, 5 )

		self.m_textCtrl10 = wx.TextCtrl( self, wx.ID_ANY, _(u"1"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.m_textCtrl10, 0, wx.ALL, 5 )

		self.m_staticText94 = wx.StaticText( self, wx.ID_ANY, _(u"增益"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText94.Wrap( -1 )

		fgSizer44.Add( self.m_staticText94, 0, wx.ALL, 5 )

		self.m_textCtrl11 = wx.TextCtrl( self, wx.ID_ANY, _(u"50"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.m_textCtrl11, 0, wx.ALL, 5 )

		self.m_staticText95 = wx.StaticText( self, wx.ID_ANY, _(u"偏置"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText95.Wrap( -1 )

		fgSizer44.Add( self.m_staticText95, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, _(u"10"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText96 = wx.StaticText( self, wx.ID_ANY, _(u"电调"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText96.Wrap( -1 )

		fgSizer44.Add( self.m_staticText96, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer44.Add( self.m_textCtrl13, 0, wx.ALL, 5 )

		self.m_staticText97 = wx.StaticText( self, wx.ID_ANY, _(u"滤镜轮"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText97.Wrap( -1 )

		fgSizer44.Add( self.m_staticText97, 0, wx.ALL, 5 )

		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		fgSizer44.Add( self.m_choice3, 0, wx.ALL, 5 )


		bSizer20.Add( fgSizer44, 1, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer20.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )


		fgSizer43.Add( bSizer20, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		fgSizer46 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer46.SetFlexibleDirection( wx.BOTH )
		fgSizer46.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText98 = wx.StaticText( self, wx.ID_ANY, _(u"升温幅度"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText98.Wrap( -1 )

		fgSizer46.Add( self.m_staticText98, 0, wx.ALL, 5 )

		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer46.Add( self.m_slider1, 0, wx.ALL, 5 )

		self.m_staticText99 = wx.StaticText( self, wx.ID_ANY, _(u"降温幅度"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( -1 )

		fgSizer46.Add( self.m_staticText99, 0, wx.ALL, 5 )

		self.m_slider2 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer46.Add( self.m_slider2, 0, wx.ALL, 5 )

		self.m_staticText100 = wx.StaticText( self, wx.ID_ANY, _(u"温度上限"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText100.Wrap( -1 )

		fgSizer46.Add( self.m_staticText100, 0, wx.ALL, 5 )

		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.m_textCtrl15, 0, wx.ALL, 5 )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, _(u"温度下限"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		fgSizer46.Add( self.m_staticText101, 0, wx.ALL, 5 )

		self.m_textCtrl16 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer46.Add( self.m_textCtrl16, 0, wx.ALL, 5 )


		bSizer22.Add( fgSizer46, 1, wx.EXPAND, 5 )


		fgSizer43.Add( bSizer22, 1, wx.EXPAND, 5 )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		fgSizer47 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer47.SetFlexibleDirection( wx.BOTH )
		fgSizer47.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button39 = wx.Button( self, wx.ID_ANY, _(u"制冷"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.m_button39, 0, wx.ALL, 5 )

		self.m_button40 = wx.Button( self, wx.ID_ANY, _(u"停止"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.m_button40, 0, wx.ALL, 5 )

		self.m_button41 = wx.Button( self, wx.ID_ANY, _(u"升温"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.m_button41, 0, wx.ALL, 5 )

		self.m_button42 = wx.Button( self, wx.ID_ANY, _(u"降温"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer47.Add( self.m_button42, 0, wx.ALL, 5 )


		bSizer23.Add( fgSizer47, 1, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button43 = wx.Button( self, wx.ID_ANY, _(u"开始"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button43, 0, wx.ALL, 5 )

		self.m_button44 = wx.Button( self, wx.ID_ANY, _(u"停止"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button44, 0, wx.ALL, 5 )


		bSizer23.Add( gSizer5, 1, wx.EXPAND, 5 )

		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer23.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )


		fgSizer43.Add( bSizer23, 1, wx.EXPAND, 5 )


		gbSizer3.Add( fgSizer43, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )


		m_c_b.Add( gbSizer3, 1, wx.EXPAND, 5 )

		fgSizer57 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer57.SetFlexibleDirection( wx.BOTH )
		fgSizer57.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer52 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer52.SetFlexibleDirection( wx.BOTH )
		fgSizer52.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		fgSizer48 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer48.SetFlexibleDirection( wx.BOTH )
		fgSizer48.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer60 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer60.SetFlexibleDirection( wx.BOTH )
		fgSizer60.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel30 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,150 ), wx.TAB_TRAVERSAL )
		self.m_panel30.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )

		fgSizer60.Add( self.m_panel30, 1, wx.EXPAND |wx.ALL, 5 )


		fgSizer48.Add( fgSizer60, 1, wx.EXPAND, 5 )

		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		fgSizer48.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )


		bSizer24.Add( fgSizer48, 1, wx.EXPAND, 5 )


		fgSizer52.Add( bSizer24, 1, wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer52.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )


		fgSizer57.Add( fgSizer52, 1, wx.EXPAND, 5 )

		fgSizer53 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer53.SetFlexibleDirection( wx.BOTH )
		fgSizer53.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		fgSizer55 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer55.SetFlexibleDirection( wx.BOTH )
		fgSizer55.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_bitmap12 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer55.Add( self.m_bitmap12, 0, wx.ALL, 5 )

		self.m_staticText118 = wx.StaticText( self, wx.ID_ANY, _(u"计划拍摄"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText118.Wrap( -1 )

		fgSizer55.Add( self.m_staticText118, 0, wx.ALL, 5 )

		self.m_bitmap13 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer55.Add( self.m_bitmap13, 0, wx.ALL, 5 )


		fgSizer53.Add( fgSizer55, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		fgSizer56 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer56.SetFlexibleDirection( wx.BOTH )
		fgSizer56.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText110 = wx.StaticText( self, wx.ID_ANY, _(u"次数"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText110.Wrap( -1 )

		fgSizer56.Add( self.m_staticText110, 0, wx.ALL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer56.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, _(u"时间"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		fgSizer56.Add( self.m_staticText111, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer56.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText112 = wx.StaticText( self, wx.ID_ANY, _(u"类型"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText112.Wrap( -1 )

		fgSizer56.Add( self.m_staticText112, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer56.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_staticText113 = wx.StaticText( self, wx.ID_ANY, _(u"格式"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText113.Wrap( -1 )

		fgSizer56.Add( self.m_staticText113, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer56.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText116 = wx.StaticText( self, wx.ID_ANY, _(u"温度补偿"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText116.Wrap( -1 )

		fgSizer56.Add( self.m_staticText116, 0, wx.ALL, 5 )

		self.m_checkBox6 = wx.CheckBox( self, wx.ID_ANY, _(u"Check Me!"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer56.Add( self.m_checkBox6, 0, wx.ALL, 5 )

		self.m_staticText117 = wx.StaticText( self, wx.ID_ANY, _(u"中天翻转"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText117.Wrap( -1 )

		fgSizer56.Add( self.m_staticText117, 0, wx.ALL, 5 )

		self.m_checkBox7 = wx.CheckBox( self, wx.ID_ANY, _(u"Check Me!"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer56.Add( self.m_checkBox7, 0, wx.ALL, 5 )


		bSizer25.Add( fgSizer56, 1, wx.EXPAND, 5 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button48 = wx.Button( self, wx.ID_ANY, _(u"开始"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button48, 0, wx.ALL, 5 )

		self.m_button49 = wx.Button( self, wx.ID_ANY, _(u"停止"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button49, 0, wx.ALL, 5 )


		bSizer25.Add( gSizer6, 1, wx.EXPAND, 5 )


		fgSizer53.Add( bSizer25, 1, wx.EXPAND, 5 )


		fgSizer57.Add( fgSizer53, 1, wx.EXPAND, 5 )


		m_c_b.Add( fgSizer57, 1, wx.EXPAND, 5 )


		self.SetSizer( m_c_b )
		self.Layout()

		# Connect Events
		self.m_button39.Bind( wx.EVT_BUTTON, self.on_startcool_click )
		self.m_button40.Bind( wx.EVT_BUTTON, self.on_stopcool_click )
		self.m_button41.Bind( wx.EVT_BUTTON, self.on_coolon_click )
		self.m_button42.Bind( wx.EVT_BUTTON, self.on_cooloff_click )
		self.m_button43.Bind( wx.EVT_BUTTON, self.on_camera_start )
		self.m_button44.Bind( wx.EVT_BUTTON, self.on_camera_stop )
		self.m_checkBox6.Bind( wx.EVT_CHECKBOX, self.on_temp_click )
		self.m_checkBox7.Bind( wx.EVT_CHECKBOX, self.on_transmit_click )
		self.m_button48.Bind( wx.EVT_BUTTON, self.on_queue_start )
		self.m_button49.Bind( wx.EVT_BUTTON, self.on_queue_stop )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_startcool_click( self, event ):
		event.Skip()

	def on_stopcool_click( self, event ):
		event.Skip()

	def on_coolon_click( self, event ):
		event.Skip()

	def on_cooloff_click( self, event ):
		event.Skip()

	def on_camera_start( self, event ):
		event.Skip()

	def on_camera_stop( self, event ):
		event.Skip()

	def on_temp_click( self, event ):
		event.Skip()

	def on_transmit_click( self, event ):
		event.Skip()

	def on_queue_start( self, event ):
		event.Skip()

	def on_queue_stop( self, event ):
		event.Skip()


