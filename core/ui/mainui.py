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

import core.ui.images as imglib

import gettext
_ = gettext.gettext

###########################################################################
## Class m_main_panel
###########################################################################

class m_main_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 650,360 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		m_main_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_main_container = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_main_device = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_weather = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_starparser = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_starinfo = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_server = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_mod = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_config = wx.Panel( self.m_main_container, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )

		lb_icon = wx.ImageList(16,16)

		lb_icon.Add(getattr(imglib,"device").GetBitmap())
		lb_icon.Add(getattr(imglib,"weather").GetBitmap())
		lb_icon.Add(getattr(imglib,"search").GetBitmap())
		lb_icon.Add(getattr(imglib,"starinfo").GetBitmap())
		lb_icon.Add(getattr(imglib,"server").GetBitmap())
		lb_icon.Add(getattr(imglib,"mod").GetBitmap())
		lb_icon.Add(getattr(imglib,"config").GetBitmap())

		self.m_main_container.AssignImageList(lb_icon)

		self.m_main_container.AddPage( self.m_main_device, _(u"设备"), True,imageId=0)
		self.m_main_container.AddPage( self.m_main_weather, _(u"天气"), False ,imageId=1)
		self.m_main_container.AddPage( self.m_main_starparser, _(u"天体搜索"), False ,imageId=2)
		self.m_main_container.AddPage( self.m_main_starinfo, _(u"天体信息"), False ,imageId=3)
		self.m_main_container.AddPage( self.m_main_server, _(u"服务器"), False ,imageId=4)
		self.m_main_container.AddPage( self.m_main_mod, _(u"模组"), False ,imageId=5)
		self.m_main_container.AddPage( self.m_main_config, _(u"配置"), False ,imageId=6)

		m_main_sizer.Add( self.m_main_container, 1, wx.EXPAND |wx.ALL, 5 )

		self.SetSizer( m_main_sizer )
		self.Layout()

	def __del__( self ):
		pass
