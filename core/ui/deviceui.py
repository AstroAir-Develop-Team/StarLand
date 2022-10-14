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

import wx

###########################################################################
## Class m_device_panel
###########################################################################

class m_device_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 620,310 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		m_device_b_container = wx.GridSizer( 0, 4, 0, 0 )

		self.m_device_camera = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 150,150 ), wx.BU_AUTODRAW|0 )
		m_device_b_container.Add( self.m_device_camera, 0, wx.ALL, 5 )

		self.m_device_mount = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 150,150 ), wx.BU_AUTODRAW|0 )
		m_device_b_container.Add( self.m_device_mount, 0, wx.ALL, 5 )

		self.m_device_focuser = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 150,150 ), wx.BU_AUTODRAW|0 )
		m_device_b_container.Add( self.m_device_focuser, 0, wx.ALL, 5 )

		self.m_device_guider = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 150,150 ), wx.BU_AUTODRAW|0 )
		m_device_b_container.Add( self.m_device_guider, 0, wx.ALL, 5 )

		self.m_device_wheel = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 150,150 ), wx.BU_AUTODRAW|0 )
		m_device_b_container.Add( self.m_device_wheel, 0, wx.ALL, 5 )


		self.SetSizer( m_device_b_container )
		self.Layout()

		# Connect Events
		self.m_device_camera.Bind( wx.EVT_BUTTON, self.on_camera_click )
		self.m_device_mount.Bind( wx.EVT_BUTTON, self.on_mount_click )
		self.m_device_focuser.Bind( wx.EVT_BUTTON, self.on_focuser_click )
		self.m_device_guider.Bind( wx.EVT_BUTTON, self.on_guider_click )
		self.m_device_wheel.Bind( wx.EVT_BUTTON, self.on_wheel_click )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_camera_click( self, event ):
		event.Skip()

	def on_mount_click( self, event ):
		event.Skip()

	def on_focuser_click( self, event ):
		event.Skip()

	def on_guider_click( self, event ):
		event.Skip()

	def on_wheel_click( self, event ):
		event.Skip()
