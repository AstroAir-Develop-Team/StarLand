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
import wx.xrc
import wx.aui

import gettext
_ = gettext.gettext

###########################################################################
## Class m_search_panel
###########################################################################

class m_search_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 710,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.m_search_quick_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.m_search_quick_panel, wx.aui.AuiPaneInfo() .Name( u"_search_box_" ).Left() .Caption( _(u"搜索框") ).PinButton( True ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).BestSize( wx.Size( 200,100 ) ).MinSize( wx.Size( 200,100 ) ).MaxSize( wx.Size( 200,100 ) ) )

		m_search_quick_box = wx.BoxSizer( wx.VERTICAL )

		m_search_quick_panel_box = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_search_quick_panel_box.SetFlexibleDirection( wx.BOTH )
		m_search_quick_panel_box.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_search_quick_panel_containre = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_search_quick_panel_containre.SetFlexibleDirection( wx.BOTH )
		m_search_quick_panel_containre.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText113 = wx.StaticText( self.m_search_quick_panel, wx.ID_ANY, _(u"名称"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText113.Wrap( -1 )

		m_search_quick_panel_containre.Add( self.m_staticText113, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self.m_search_quick_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_search_quick_panel_containre.Add( self.m_textCtrl24, 0, wx.ALL, 5 )

		self.m_staticText114 = wx.StaticText( self.m_search_quick_panel, wx.ID_ANY, _(u"赤经"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText114.Wrap( -1 )

		m_search_quick_panel_containre.Add( self.m_staticText114, 0, wx.ALL, 5 )

		self.m_textCtrl25 = wx.TextCtrl( self.m_search_quick_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_search_quick_panel_containre.Add( self.m_textCtrl25, 0, wx.ALL, 5 )

		self.m_staticText115 = wx.StaticText( self.m_search_quick_panel, wx.ID_ANY, _(u"赤纬"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText115.Wrap( -1 )

		m_search_quick_panel_containre.Add( self.m_staticText115, 0, wx.ALL, 5 )

		self.m_textCtrl26 = wx.TextCtrl( self.m_search_quick_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_search_quick_panel_containre.Add( self.m_textCtrl26, 0, wx.ALL, 5 )


		m_search_quick_panel_box.Add( m_search_quick_panel_containre, 1, wx.EXPAND, 5 )

		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button41 = wx.Button( self.m_search_quick_panel, wx.ID_ANY, _(u"搜索"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_button41, 0, wx.ALL, 5 )

		self.m_button42 = wx.Button( self.m_search_quick_panel, wx.ID_ANY, _(u"快速搜索"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_button42, 0, wx.ALL, 5 )

		self.m_button43 = wx.Button( self.m_search_quick_panel, wx.ID_ANY, _(u"同步"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_button43, 0, wx.ALL, 5 )

		self.m_button44 = wx.Button( self.m_search_quick_panel, wx.ID_ANY, _(u"配置"), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_button44, 0, wx.ALL, 5 )


		m_search_quick_panel_box.Add( gSizer8, 1, wx.EXPAND, 5 )


		m_search_quick_box.Add( m_search_quick_panel_box, 1, wx.EXPAND, 5 )


		self.m_search_quick_panel.SetSizer( m_search_quick_box )
		self.m_search_quick_panel.Layout()
		m_search_quick_box.Fit( self.m_search_quick_panel )
		self.m_collapsiblePane1 = wx.CollapsiblePane( self, wx.ID_ANY, _(u"collapsible"), wx.DefaultPosition, wx.DefaultSize, wx.CP_DEFAULT_STYLE )
		self.m_collapsiblePane1.Collapse( False )

		self.m_mgr.AddPane( self.m_collapsiblePane1, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )

		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		fgSizer60 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer60.SetFlexibleDirection( wx.BOTH )
		fgSizer60.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button45 = wx.Button( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer60.Add( self.m_button45, 0, wx.ALL, 5 )

		self.m_button46 = wx.Button( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer60.Add( self.m_button46, 0, wx.ALL, 5 )

		self.m_button47 = wx.Button( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer60.Add( self.m_button47, 0, wx.ALL, 5 )

		self.m_button48 = wx.Button( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer60.Add( self.m_button48, 0, wx.ALL, 5 )

		self.m_button49 = wx.Button( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer60.Add( self.m_button49, 0, wx.ALL, 5 )

		self.m_button50 = wx.Button( self.m_collapsiblePane1.GetPane(), wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer60.Add( self.m_button50, 0, wx.ALL, 5 )


		bSizer31.Add( fgSizer60, 1, wx.EXPAND, 5 )


		self.m_collapsiblePane1.GetPane().SetSizer( bSizer31 )
		self.m_collapsiblePane1.GetPane().Layout()
		bSizer31.Fit( self.m_collapsiblePane1.GetPane() )
		self.m_panel39 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.m_panel39, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )


		self.m_mgr.Update()

	def __del__( self ):
		self.m_mgr.UnInit()



