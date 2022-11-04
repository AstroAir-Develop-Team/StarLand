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

import gettext

import wx

_ = gettext.gettext

import core.ui.images as imglib
from core.lib.starcamera import starcamera
from core.lib.startelescope import startelescope

class stardevice(wx.Panel):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 780,600 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )
        m_device_container = wx.BoxSizer( wx.VERTICAL )

        self.m_device_listbook = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )

        self.m_camera = starcamera( self.m_device_listbook )

        self.m_telescope = startelescope( self.m_device_listbook )
              
        self.m_guider = wx.Panel( self.m_device_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
              
        self.m_focuser = wx.Panel( self.m_device_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
              
        self.m_align = wx.Panel( self.m_device_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
              
        lb_icon = wx.ImageList(48,48)

        lb_icon.Add(getattr(imglib,"camera").GetBitmap())
        lb_icon.Add(getattr(imglib,"mount").GetBitmap())
        lb_icon.Add(getattr(imglib,"guider").GetBitmap())
        lb_icon.Add(getattr(imglib,"focuser").GetBitmap())
        lb_icon.Add(getattr(imglib,"align").GetBitmap())

        self.m_device_listbook.AssignImageList(lb_icon)

        self.m_device_listbook.AddPage( self.m_camera, _(u"相机"), True ,imageId=0)
        self.m_device_listbook.AddPage( self.m_telescope, _(u"赤道仪"), False ,imageId=1)
        self.m_device_listbook.AddPage( self.m_guider, _(u"导星"), False ,imageId=2)
        self.m_device_listbook.AddPage( self.m_focuser, _(u"电调"), False ,imageId=3)
        self.m_device_listbook.AddPage( self.m_align, _(u"校准"), False ,imageId=4)

        m_device_container.Add( self.m_device_listbook, 1, wx.EXPAND |wx.ALL, 5 )

        self.SetSizer( m_device_container )
        self.Layout()
