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
## Class m_server_panel
###########################################################################

class m_server_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 650,360 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		m_server_container = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook5 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_server_native = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		m_server_native_container = wx.FlexGridSizer( 0, 3, 0, 0 )
		m_server_native_container.SetFlexibleDirection( wx.BOTH )
		m_server_native_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		m_server_native_container.Add( ( 0, 20), 1, wx.EXPAND, 5 )


		m_server_native_container.Add( ( 0, 20), 1, wx.EXPAND, 5 )


		m_server_native_container.Add( ( 0, 20), 1, wx.EXPAND, 5 )

		m_native_box = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_native_box.SetFlexibleDirection( wx.BOTH )
		m_native_box.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_native_t_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_native_t_container.SetFlexibleDirection( wx.BOTH )
		m_native_t_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_native_ip = wx.StaticText( self.m_server_native, wx.ID_ANY, u"IP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_native_ip.Wrap( -1 )

		self.m_native_ip.SetToolTip( u"默认为 127.0.0.1" )

		m_native_t_container.Add( self.m_native_ip, 0, wx.ALL, 5 )

		self.m_native_ip_t = wx.TextCtrl( self.m_server_native, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_native_t_container.Add( self.m_native_ip_t, 0, wx.ALL, 5 )

		self.m_native_port = wx.StaticText( self.m_server_native, wx.ID_ANY, u"端口", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_native_port.Wrap( -1 )

		self.m_native_port.SetToolTip( u"默认为 8000" )

		m_native_t_container.Add( self.m_native_port, 0, wx.ALL, 5 )

		self.m_native_port_t = wx.TextCtrl( self.m_server_native, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_native_t_container.Add( self.m_native_port_t, 0, wx.ALL, 5 )

		self.m_native_ssl = wx.StaticText( self.m_server_native, wx.ID_ANY, u"SSL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_native_ssl.Wrap( -1 )

		self.m_native_ssl.SetToolTip( u"默认不开启，可能有bug" )

		m_native_t_container.Add( self.m_native_ssl, 0, wx.ALL, 5 )

		self.m_native_ssl_c = wx.CheckBox( self.m_server_native, wx.ID_ANY, u"开启", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_native_t_container.Add( self.m_native_ssl_c, 0, wx.ALL, 5 )

		self.m_native_alone = wx.StaticText( self.m_server_native, wx.ID_ANY, u"独立", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_native_alone.Wrap( -1 )

		self.m_native_alone.SetToolTip( u"图形界面关闭后依旧可以运行" )

		m_native_t_container.Add( self.m_native_alone, 0, wx.ALL, 5 )

		self.m_native_alone_c = wx.CheckBox( self.m_server_native, wx.ID_ANY, u"开启", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_native_t_container.Add( self.m_native_alone_c, 0, wx.ALL, 5 )


		m_native_box.Add( m_native_t_container, 1, wx.EXPAND, 5 )

		m_native_b_container = wx.FlexGridSizer( 0, 2, 0, 0 )
		m_native_b_container.SetFlexibleDirection( wx.BOTH )
		m_native_b_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_native_start = wx.Button( self.m_server_native, wx.ID_ANY, u"启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_native_b_container.Add( self.m_native_start, 0, wx.ALL, 5 )

		self.m_native_stop = wx.Button( self.m_server_native, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_native_b_container.Add( self.m_native_stop, 0, wx.ALL, 5 )

		self.m_native_restart = wx.Button( self.m_server_native, wx.ID_ANY, u"重启", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_native_b_container.Add( self.m_native_restart, 0, wx.ALL, 5 )

		self.m_native__open = wx.Button( self.m_server_native, wx.ID_ANY, u"打开", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_native_b_container.Add( self.m_native__open, 0, wx.ALL, 5 )


		m_native_box.Add( m_native_b_container, 1, wx.EXPAND, 5 )


		m_server_native_container.Add( m_native_box, 1, wx.EXPAND, 5 )

		m_native_s_container = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_native_s_container.SetFlexibleDirection( wx.BOTH )
		m_native_s_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_native_s_title = wx.FlexGridSizer( 0, 6, 0, 0 )
		m_native_s_title.SetFlexibleDirection( wx.BOTH )
		m_native_s_title.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_native_s_status = wx.StaticText( self.m_server_native, wx.ID_ANY, u"状态", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_native_s_status.Wrap( -1 )

		m_native_s_title.Add( self.m_native_s_status, 0, wx.ALL, 5 )

		self.m_native_s_icon = wx.StaticBitmap( self.m_server_native, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		m_native_s_title.Add( self.m_native_s_icon, 0, wx.ALL, 5 )

		self.m_native_s_scode = wx.StaticText( self.m_server_native, wx.ID_ANY, u"状态码", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_native_s_scode.Wrap( -1 )

		m_native_s_title.Add( self.m_native_s_scode, 0, wx.ALL, 5 )

		self.m_native_s_scode_t = wx.StaticText( self.m_server_native, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_native_s_scode_t.Wrap( -1 )

		m_native_s_title.Add( self.m_native_s_scode_t, 0, wx.ALL, 5 )


		m_native_s_title.Add( ( 110, 0), 1, wx.EXPAND, 5 )

		self.m_native_l_clear = wx.Button( self.m_server_native, wx.ID_ANY, u"清除日志", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_native_s_title.Add( self.m_native_l_clear, 0, wx.ALL, 5 )


		m_native_s_container.Add( m_native_s_title, 1, wx.EXPAND, 5 )

		m_native_l_container = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl4 = wx.TextCtrl( self.m_server_native, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,180 ), 0 )
		m_native_l_container.Add( self.m_textCtrl4, 0, wx.ALL, 5 )


		m_native_s_container.Add( m_native_l_container, 1, wx.EXPAND, 5 )


		m_server_native_container.Add( m_native_s_container, 1, wx.EXPAND, 5 )


		self.m_server_native.SetSizer( m_server_native_container )
		self.m_server_native.Layout()
		m_server_native_container.Fit( self.m_server_native )
		self.m_notebook5.AddPage( self.m_server_native, u"内置", True )
		self.m_indi = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook5.AddPage( self.m_indi, u"INDI", False )
		self.m_indiweb = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook5.AddPage( self.m_indiweb, u"INDIWeb", False )
		self.m_novnc = wx.Panel( self.m_notebook5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook5.AddPage( self.m_novnc, u"noVNC", False )

		m_server_container.Add( self.m_notebook5, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( m_server_container )
		self.Layout()

		# Connect Events
		self.m_native_start.Bind( wx.EVT_BUTTON, self.on_buildin_start )
		self.m_native_stop.Bind( wx.EVT_BUTTON, self.on_buildin_stop )
		self.m_native_restart.Bind( wx.EVT_BUTTON, self.on_buildin_restart )
		self.m_native__open.Bind( wx.EVT_BUTTON, self.on_buildin_open )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def on_buildin_start( self, event ):
		event.Skip()

	def on_buildin_stop( self, event ):
		event.Skip()

	def on_buildin_restart( self, event ):
		event.Skip()

	def on_buildin_open( self, event ):
		event.Skip()


