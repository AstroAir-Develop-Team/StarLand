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

import wx
import wx.xrc

import gettext
_ = gettext.gettext

import config

###########################################################################
## Class m_location
###########################################################################

class m_location ( wx.Dialog ):

    def __init__( self, parent ):

        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"设置地理信息"), pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.SetIcon(wx.Icon(config.assets["textures"]["icon"],wx.BITMAP_TYPE_ICON))

        m_location_box = wx.BoxSizer( wx.VERTICAL )

        self.m_location_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        m_l_b = wx.BoxSizer( wx.VERTICAL )

        m_location_container = wx.FlexGridSizer( 0, 1, 0, 0 )
        m_location_container.SetFlexibleDirection( wx.BOTH )
        m_location_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        m_location_textctrl = wx.FlexGridSizer( 0, 2, 0, 0 )
        m_location_textctrl.SetFlexibleDirection( wx.BOTH )
        m_location_textctrl.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_d_lat = wx.StaticText( self.m_location_panel, wx.ID_ANY, _(u"经度"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_d_lat.Wrap( -1 )

        m_location_textctrl.Add( self.m_d_lat, 0, wx.ALL, 5 )

        self.m_location_lat = wx.TextCtrl( self.m_location_panel, wx.ID_ANY, _(u"30.00"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_location_lat.SetToolTip( _(u"所处位置的经度，用\".\"分割") )

        m_location_textctrl.Add( self.m_location_lat, 0, wx.ALL, 5 )

        self.m_d_lon = wx.StaticText( self.m_location_panel, wx.ID_ANY, _(u"纬度"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_d_lon.Wrap( -1 )

        m_location_textctrl.Add( self.m_d_lon, 0, wx.ALL, 5 )

        self.m_location_lon = wx.TextCtrl( self.m_location_panel, wx.ID_ANY, _(u"120.00"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_location_lon.SetToolTip( _(u"所处位置的纬度，用\".\"分割") )

        m_location_textctrl.Add( self.m_location_lon, 0, wx.ALL, 5 )

        self.m_d_eva = wx.StaticText( self.m_location_panel, wx.ID_ANY, _(u"海拔"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_d_eva.Wrap( -1 )

        m_location_textctrl.Add( self.m_d_eva, 0, wx.ALL, 5 )

        self.m_location_eva = wx.TextCtrl( self.m_location_panel, wx.ID_ANY, _(u"10"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_location_eva.SetToolTip( _(u"所处位置的海拔") )

        m_location_textctrl.Add( self.m_location_eva, 0, wx.ALL, 5 )

        m_location_container.Add( m_location_textctrl, 1, wx.EXPAND, 5 )

        m_location_button = wx.GridSizer( 0, 2, 0, 0 )

        self.m_d_confrm = wx.Button( self.m_location_panel, wx.ID_ANY, _(u"确认"), wx.DefaultPosition, wx.DefaultSize, 0 )
        m_location_button.Add( self.m_d_confrm, 0, wx.ALL, 5 )

        self.m_d_cancel = wx.Button( self.m_location_panel, wx.ID_ANY, _(u"取消"), wx.DefaultPosition, wx.DefaultSize, 0 )
        m_location_button.Add( self.m_d_cancel, 0, wx.ALL, 5 )

        m_location_container.Add( m_location_button, 1, wx.EXPAND, 5 )

        m_l_b.Add( m_location_container, 1, wx.EXPAND, 5 )

        self.m_location_panel.SetSizer( m_l_b )
        self.m_location_panel.Layout()
        m_l_b.Fit( self.m_location_panel )
        m_location_box.Add( self.m_location_panel, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( m_location_box )
        self.Layout()
        m_location_box.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_d_confrm.Bind( wx.EVT_BUTTON, self.on_confirm_click )
        self.m_d_cancel.Bind( wx.EVT_BUTTON, self.on_cancel_click )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_confirm_click( self, event ):
        event.Skip()

    def on_cancel_click( self, event ):
        event.Skip()