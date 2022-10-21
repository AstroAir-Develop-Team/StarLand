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

import config

class background(wx.Panel):

    def __init__(self,parent,id=wx.ID_ANY,size=wx.Size( 650,360 )):

        wx.Panel.__init__(self,parent,id=id,size=size)
        
        self.Bind(wx.EVT_ERASE_BACKGROUND,self.on_eraze_background)

    # 绘制背景图片
    def on_eraze_background(self,event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
            dc.Clear()
        bmp = wx.Bitmap(config.assets["textures"]["background"],wx.BITMAP_TYPE_JPEG).ConvertToImage().Scale(650,360)
        dc.DrawBitmap(wx.Bitmap(bmp,wx.BITMAP_SCREEN_DEPTH), 0, 0)
