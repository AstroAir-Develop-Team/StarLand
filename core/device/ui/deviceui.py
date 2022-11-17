# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-8e3463c)
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
## Class m_device_panel
###########################################################################

class m_device_panel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		self.screen_size = [wx.GetDisplaySize()[0],wx.GetDisplaySize()[1]]
		
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_device_info = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_img = wx.StaticBitmap( self.m_device_info, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,wx.Size(int(self.screen_size[0]/4),int(self.screen_size[1]/4)), 0 )
		gbSizer5.Add( self.m_img, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_img_info = wx.Panel( self.m_device_info, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer5.Add( self.m_img_info, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )


		bSizer52.Add( gbSizer5, 1, wx.EXPAND, 5 )


		self.m_device_info.SetSizer( bSizer52 )
		self.m_device_info.Layout()
		bSizer52.Fit( self.m_device_info )
		gbSizer4.Add( self.m_device_info, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_device_nb = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )

		gbSizer4.Add( self.m_device_nb, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( gbSizer4 )
		self.Layout()
		gbSizer4.Fit( self )

		# Connect Events
		self.m_device_nb.Bind( wx.EVT_SIZE, self.refresh )
		self.m_device_nb.Bind( wx.EVT_UPDATE_UI, self.a )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def refresh( self, event ):
		event.Skip()

	def a( self, event ):
		event.Skip()


###########################################################################
## Class m_device_info
###########################################################################

class m_device_info ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.m_img = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_mgr.AddPane( self.m_img, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).CentrePane() )

		self.m_img_info = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.m_img_info, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Row( 0 ).CentrePane() )


		self.m_mgr.Update()

	def __del__( self ):
		self.m_mgr.UnInit()

###########################################################################
## Class m_img_info
###########################################################################

class m_img_info ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)

		self.m_info_img = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.m_info_img, wx.aui.AuiPaneInfo() .Name( u"a_info_img" ).Left() .CloseButton( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Floatable( False ).Row( 0 ).CentrePane() )

		self.m_info_guide = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.m_info_guide, wx.aui.AuiPaneInfo() .Name( u"a_info_guide" ).Left() .CloseButton( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Floatable( False ).Row( 0 ).CentrePane() )


		self.m_mgr.Update()

	def __del__( self ):
		self.m_mgr.UnInit()