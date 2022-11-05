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

import config

from core.ui.telescopeui import m_telescope

class startelescope(m_telescope):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size( 780,600 ), style=wx.TAB_TRAVERSAL, name=u"Telescope"):
        super().__init__(parent, id, pos, size, style, name)
        img = wx.Image(config.assets["textures"]["device"]["telescope"]["m_d_ts_n"],wx.BITMAP_TYPE_PNG).Scale(64,64,wx.IMAGE_QUALITY_HIGH)
        self.m_ts_c_b_n.SetBitmap(wx.Bitmap(img,wx.BITMAP_SCREEN_DEPTH))
        img = wx.Image(config.assets["textures"]["device"]["telescope"]["m_d_ts_s"],wx.BITMAP_TYPE_PNG).Scale(64,64,wx.IMAGE_QUALITY_HIGH)
        self.m_ts_c_b_s.SetBitmap(wx.Bitmap(img,wx.BITMAP_SCREEN_DEPTH))
        img = wx.Image(config.assets["textures"]["device"]["telescope"]["m_d_ts_e"],wx.BITMAP_TYPE_PNG).Scale(64,64,wx.IMAGE_QUALITY_HIGH)
        self.m_ts_c_b_e.SetBitmap(wx.Bitmap(img,wx.BITMAP_SCREEN_DEPTH))
        img = wx.Image(config.assets["textures"]["device"]["telescope"]["m_d_ts_w"],wx.BITMAP_TYPE_PNG).Scale(64,64,wx.IMAGE_QUALITY_HIGH)
        self.m_ts_c_b_w.SetBitmap(wx.Bitmap(img,wx.BITMAP_SCREEN_DEPTH))

        img = wx.Image(config.assets["textures"]["device"]["telescope"]["m_d_ts_en"],wx.BITMAP_TYPE_PNG).Scale(64,64,wx.IMAGE_QUALITY_HIGH)
        self.m_ts_c_b_en.SetBitmap(wx.Bitmap(img,wx.BITMAP_SCREEN_DEPTH))
        img = wx.Image(config.assets["textures"]["device"]["telescope"]["m_d_ts_wn"],wx.BITMAP_TYPE_PNG).Scale(64,64,wx.IMAGE_QUALITY_HIGH)
        self.m_ts_c_b_wn.SetBitmap(wx.Bitmap(img,wx.BITMAP_SCREEN_DEPTH))
        img = wx.Image(config.assets["textures"]["device"]["telescope"]["m_d_ts_es"],wx.BITMAP_TYPE_PNG).Scale(64,64,wx.IMAGE_QUALITY_HIGH)
        self.m_ts_c_b_es.SetBitmap(wx.Bitmap(img,wx.BITMAP_SCREEN_DEPTH))
        img = wx.Image(config.assets["textures"]["device"]["telescope"]["m_d_ts_ws"],wx.BITMAP_TYPE_PNG).Scale(64,64,wx.IMAGE_QUALITY_HIGH)
        self.m_ts_c_b_ws.SetBitmap(wx.Bitmap(img,wx.BITMAP_SCREEN_DEPTH))

        img = wx.Image(config.assets["textures"]["device"]["telescope"]["m_d_ts_stop"],wx.BITMAP_TYPE_PNG).Scale(64,64,wx.IMAGE_QUALITY_HIGH)
        self.m_ts_c_b_stop.SetBitmap(wx.Bitmap(img,wx.BITMAP_SCREEN_DEPTH))
        

    def __del__(self):
        return super().__del__()

    def on_init_dialog(self, event):
        return super().on_init_dialog(event)

    def on_background_erase(self, event):
        return super().on_background_erase(event)

    def on_b_e_click(self, event):
        return super().on_b_e_click(event)

    def on_b_en_click(self, event):
        return super().on_b_en_click(event)

    def on_b_es_click(self, event):
        return super().on_b_es_click(event)

    def on_b_n_click(self, event):
        return super().on_b_n_click(event)

    def on_b_s_click(self, event):
        return super().on_b_s_click(event)

    def on_b_stop_click(self, event):
        return super().on_b_stop_click(event)

    def on_b_w_click(self, event):
        return super().on_b_w_click(event)

    def on_b_wn_click(self, event):
        return super().on_b_wn_click(event)

    def on_b_ws_click(self, event):
        return super().on_b_ws_click(event)