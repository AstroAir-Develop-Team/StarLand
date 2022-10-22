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
import wx.adv
import wx.richtext

from core.ui.transparent import TransparentStaticText

import gettext
_ = gettext.gettext

###########################################################################
## Class m_mod_main
###########################################################################

class my_loader_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 640,360 ), style = wx.TAB_TRAVERSAL|wx.TRANSPARENT_WINDOW, name = wx.EmptyString ):
		
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		m_mod = wx.BoxSizer( wx.VERTICAL )

		m_mod_ui = wx.FlexGridSizer( 0, 3, 0, 0 )
		m_mod_ui.SetFlexibleDirection( wx.BOTH )
		m_mod_ui.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_mod_container = wx.FlexGridSizer( 0, 1, 0, 0 )
		m_mod_container.SetFlexibleDirection( wx.BOTH )
		m_mod_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_mod_spacer_container = wx.BoxSizer( wx.VERTICAL )
		m_mod_spacer_container.Add( ( 0, 30), 1, wx.EXPAND, 5 )
		m_mod_container.Add( m_mod_spacer_container, 1, wx.EXPAND, 5 )

		m_mod_title = wx.BoxSizer( wx.VERTICAL )

		m_mod_title_container = wx.FlexGridSizer( 0, 5, 0, 0 )
		m_mod_title_container.SetFlexibleDirection( wx.BOTH )
		m_mod_title_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_mod_title_container.SetMinSize( wx.Size( -1,32 ) )

		m_mod_title_container.Add( ( 225, 0), 1, wx.EXPAND, 5 )

		self.m_mod_title_icon = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 32,32 ), 0 )
		m_mod_title_container.Add( self.m_mod_title_icon, 0, wx.ALL, 0 )

		self.m_mod_title_title = TransparentStaticText( self, wx.ID_ANY, _(u"模组加载"), wx.DefaultPosition, wx.Size( 86,-1 ))

		self.m_mod_title_title.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.m_mod_title_title.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_mod_title_title.Wrap( -1 )
		m_mod_title_container.Add( self.m_mod_title_title, 0, wx.ALL, 5 )

		self.m_mod_title_help = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 32,32 ), wx.BU_AUTODRAW|0 )
		self.m_mod_title_help.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_mod_title_help.SetToolTip( _(u"模组加载帮助") )
		self.m_mod_title_help.SetHelpText( _(u"模组加载帮助") )
		m_mod_title_container.Add( self.m_mod_title_help, 0, wx.ALL, 0 )

		m_mod_title_container.Add( ( 245, 0), 1, wx.EXPAND, 5 )

		m_mod_title.Add( m_mod_title_container, 1, wx.EXPAND, 0 )

		m_mod_container.Add( m_mod_title, 1, wx.EXPAND, 0 )

		m_mod_content = wx.BoxSizer( wx.VERTICAL )

		m_mod_content_container = wx.FlexGridSizer( 0, 3, 0, 0 )
		m_mod_content_container.SetFlexibleDirection( wx.BOTH )
		m_mod_content_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		m_mod_content_container.Add( ( 110, 0), 1, wx.EXPAND, 5 )

		self.m_mod_listbook = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 420,200 ), wx.LB_DEFAULT )
		m_mod_listbookImageSize = wx.Size( 32,32 )
		m_mod_listbookIndex = 0
		m_mod_listbookImages = wx.ImageList( m_mod_listbookImageSize.GetWidth(), m_mod_listbookImageSize.GetHeight() )
		self.m_mod_listbook.AssignImageList( m_mod_listbookImages )
		self.mod_buildin = wx.Panel( self.m_mod_listbook, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		mod_buildin_box = wx.BoxSizer( wx.VERTICAL )

		buildin_content = wx.FlexGridSizer( 0, 1, 0, 0 )
		buildin_content.SetFlexibleDirection( wx.BOTH )
		buildin_content.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		buildin_info = wx.FlexGridSizer( 0, 6, 0, 0 )
		buildin_info.SetFlexibleDirection( wx.BOTH )
		buildin_info.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_t_author_t = wx.StaticText( self.mod_buildin, wx.ID_ANY, _(u"作者"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_t_author_t.Wrap( -1 )

		buildin_info.Add( self.m_t_author_t, 0, wx.ALL, 5 )

		self.buildin_author = wx.StaticText( self.mod_buildin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.buildin_author.Wrap( -1 )

		buildin_info.Add( self.buildin_author, 0, wx.ALL, 5 )

		self.m_t_version_t = wx.StaticText( self.mod_buildin, wx.ID_ANY, _(u"版本"), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_t_version_t.Wrap( -1 )

		buildin_info.Add( self.m_t_version_t, 0, wx.ALL, 5 )

		self.buildin_version = wx.StaticText( self.mod_buildin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.buildin_version.Wrap( -1 )

		buildin_info.Add( self.buildin_version, 0, wx.ALL, 5 )

		self.m_t_license_t = wx.StaticText( self.mod_buildin, wx.ID_ANY, _(u"证书"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_license_t.Wrap( -1 )

		buildin_info.Add( self.m_t_license_t, 0, wx.ALL, 5 )

		self.buildin_license = wx.StaticText( self.mod_buildin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.buildin_license.Wrap( -1 )

		buildin_info.Add( self.buildin_license, 0, wx.ALL, 5 )

		buildin_content.Add( buildin_info, 1, wx.EXPAND, 5 )

		buildin_link = wx.FlexGridSizer( 0, 6, 0, 0 )
		buildin_link.SetFlexibleDirection( wx.BOTH )
		buildin_link.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_t_link_t = wx.StaticText( self.mod_buildin, wx.ID_ANY, _(u"链接"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_t_link_t.Wrap( -1 )
		buildin_link.Add( self.m_t_link_t, 0, wx.ALL, 5 )

		self.buildin_link = wx.adv.HyperlinkCtrl( self.mod_buildin, wx.ID_ANY, _(u"View source code"), u"https://github.com/AstroAir-Develop-Team/StarLand", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		buildin_link.Add( self.buildin_link, 0, wx.ALL, 5 )
		buildin_link.Add( ( 40, 0), 1, wx.EXPAND, 5 )

		self.buildin_is_load = wx.StaticText( self.mod_buildin, wx.ID_ANY, _(u"加载"), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buildin_is_load.Wrap( -1 )

		buildin_link.Add( self.buildin_is_load, 0, wx.ALL, 5 )

		buildin_link.Add( ( 20, 0), 1, wx.EXPAND, 5 )

		self.buildin_check = wx.CheckBox( self.mod_buildin, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.buildin_check.SetValue(True)
		buildin_link.Add( self.buildin_check, 0, wx.ALL, 5 )

		buildin_content.Add( buildin_link, 1, wx.EXPAND, 5 )

		buildin_ds = wx.FlexGridSizer( 0, 2, 0, 0 )
		buildin_ds.SetFlexibleDirection( wx.BOTH )
		buildin_ds.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.buildin_describtion = wx.richtext.RichTextCtrl( self.mod_buildin, wx.ID_ANY, _(u"内置模块"), wx.DefaultPosition, wx.Size( 150,128 ), 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.buildin_describtion.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.buildin_describtion.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.buildin_describtion.Enable( False )

		buildin_ds.Add( self.buildin_describtion, 1, wx.EXPAND |wx.ALL, 5 )

		self.buildin_icon = wx.StaticBitmap( self.mod_buildin, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 128,128 ), 0 )
		buildin_ds.Add( self.buildin_icon, 0, wx.ALL, 5 )


		buildin_content.Add( buildin_ds, 1, wx.EXPAND, 5 )


		mod_buildin_box.Add( buildin_content, 1, wx.EXPAND, 5 )


		self.mod_buildin.SetSizer( mod_buildin_box )
		self.mod_buildin.Layout()
		mod_buildin_box.Fit( self.mod_buildin )
		self.m_mod_listbook.AddPage( self.mod_buildin, wx.EmptyString, True )

		m_mod_content_container.Add( self.m_mod_listbook, 1, wx.EXPAND |wx.ALL, 5 )


		m_mod_content.Add( m_mod_content_container, 1, wx.EXPAND, 5 )


		m_mod_container.Add( m_mod_content, 1, wx.EXPAND, 5 )

		m_mod_button = wx.BoxSizer( wx.VERTICAL )

		m_mod_button_container = wx.FlexGridSizer( 0, 6, 0, 0 )
		m_mod_button_container.SetFlexibleDirection( wx.BOTH )
		m_mod_button_container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		m_mod_button_container.Add( ( 150, 0), 1, wx.EXPAND, 5 )

		self.m_mod_gotomain = wx.Button( self, wx.ID_ANY, _(u"主界面"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_mod_button_container.Add( self.m_mod_gotomain, 0, wx.ALL, 5 )

		self.m_mod_refresh = wx.Button( self, wx.ID_ANY, _(u"刷新"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_mod_button_container.Add( self.m_mod_refresh, 0, wx.ALL, 5 )

		self.m_mod_config = wx.Button( self, wx.ID_ANY, _(u"配置"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_mod_button_container.Add( self.m_mod_config, 0, wx.ALL, 5 )

		self.m_mod_folder = wx.Button( self, wx.ID_ANY, _(u"文件夹"), wx.DefaultPosition, wx.DefaultSize, 0 )
		m_mod_button_container.Add( self.m_mod_folder, 0, wx.ALL, 5 )

		m_mod_button_container.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		m_mod_button.Add( m_mod_button_container, 1, wx.EXPAND, 5 )


		m_mod_container.Add( m_mod_button, 1, wx.EXPAND, 5 )


		m_mod_ui.Add( m_mod_container, 1, wx.EXPAND, 0 )


		m_mod_ui.Add( ( 100, 0), 1, wx.EXPAND, 5 )


		m_mod.Add( m_mod_ui, 1, wx.EXPAND, 0 )


		self.SetSizer( m_mod )
		self.Layout()

		# Connect Events
		self.m_mod_title_help.Bind( wx.EVT_BUTTON, self.on_loader_help )
		self.buildin_link.Bind( wx.adv.EVT_HYPERLINK, self.on_link_clicked )
		self.m_mod_gotomain.Bind( wx.EVT_BUTTON, self.on_gotomain )
		self.m_mod_refresh.Bind( wx.EVT_BUTTON, self.on_refresh )
		self.m_mod_config.Bind( wx.EVT_BUTTON, self.m_config )
		self.m_mod_folder.Bind( wx.EVT_BUTTON, self.m_folder )

	def __del__( self ):
		pass

	# Virtual event handlers, override them in your derived class
	def on_loader_help( self, event ):
		event.Skip()

	def on_link_clicked( self, event ):
		event.Skip()

	def on_gotomain( self, event ):
		event.Skip()

	def on_refresh( self, event ):
		event.Skip()

	def m_config( self, event ):
		event.Skip()

	def m_folder( self, event ):
		event.Skip()
		