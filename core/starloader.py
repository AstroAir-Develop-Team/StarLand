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

from core.ui.loaderui import my_loader_panel
from core.ui.splashscreen import m_splash_screen
from core.lib.starlog import starlog
from core.starmain import starmain

import config

import gettext
_ = gettext.gettext

log = starlog(__name__)

class starloader(my_loader_panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size( 640,360 ), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        
        super().__init__(parent, id, pos, size, style, name)

        self.Bind(wx.EVT_ERASE_BACKGROUND,self.on_eraze_background)
        self.parent = parent

        self.m_mod_title_icon.SetBitmap(wx.Bitmap(config.assets["textures"]["loader"]["icon"],wx.BITMAP_TYPE_PNG))
        self.m_mod_title_help.SetBitmap(wx.Bitmap(config.assets["textures"]["help"],wx.BITMAP_TYPE_PNG))
        self.buildin_icon.SetBitmap(wx.Bitmap(config.assets["textures"]["logo"],wx.BITMAP_TYPE_PNG))
        self.m_mod_gotomain.SetBitmap(wx.Bitmap(config.assets["textures"]["loader"]["gotomain"],wx.BITMAP_TYPE_PNG))
        self.m_mod_refresh.SetBitmap(wx.Bitmap(config.assets["textures"]["loader"]["refresh"],wx.BITMAP_TYPE_PNG))
        self.m_mod_config.SetBitmap(wx.Bitmap(config.assets["textures"]["loader"]["config"],wx.BITMAP_TYPE_PNG))
        self.m_mod_folder.SetBitmap(wx.Bitmap(config.assets["textures"]["loader"]["folder"],wx.BITMAP_TYPE_PNG))

    def __del__(self):
        return super().__del__()

    def refreshlist(self,event):
        mod = wx.Button( self.pnl.m_loader_unuse, wx.ID_ANY, _(u'刷新'), wx.DefaultPosition, wx.Size( 70,-1 ), wx.BU_AUTODRAW|0 )
        self.pnl.m_unuse_container.Add(mod)
        self.pnl.m_loader_unuse.Layout()
        self.pnl.Layout()
    
    def on_loader_help( self, event ):
        event.Skip()

    def on_link_clicked( self, event ):
        event.Skip()

    # 进入主界面
    def on_gotomain( self, event ):
        event.Skip()
        log.log(_("Enter main frame and hide mod loader"))
        self.Hide()
        self.parent.Hide()
        m_splash_screen(starmain(None))

    def on_refresh( self, event ):
        event.Skip()

    def m_config( self, event ):
        event.Skip()

    def m_folder( self, event ):
        event.Skip()

    # 绘制背景图片
    def on_eraze_background(self,event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
            dc.Clear()
        dc.DrawBitmap(wx.Bitmap(config.assets["textures"]["background"],wx.BITMAP_TYPE_BMP), 0, 0)    

class starloaderframe(wx.Frame):

    def __init__(self, *args, **kw):
        wx.Frame.__init__(self,parent=None,title = _(u"模组加载"),pos = wx.DefaultPosition, size = wx.Size( 660,390 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL)

        self.pnl = starloader(self)

        self.SetIcon(wx.Icon(config.assets["textures"]["icon"]))

        self.SetSizeHints( wx.DefaultSize, wx.Size( 660,390 ) )

        self.Center()     
