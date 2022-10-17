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

__author__ = "Max Qian"

class m_ahout_ui(wx.adv.AboutDialogInfo):

    def __init__(self, *args, **kwargs):
        super(m_ahout_ui, self).__init__(*args, **kwargs)

    def OnAboutBox(self):

        description = """Star Hunter is a new generation of astronomical photography terminal. 
            It is lightweight, yet rich in functions, simple and beautiful. 
            It is your good helper on the astronomical photography road
            """

        licence = """Star Hunter is free software; you can redistribute
            it and/or modify it under the terms of the GNU General Public License as
            published by the Free Software Foundation; either version 3 of the License,
            or (at your option) any later version.

            Star Hunter is distributed in the hope that it will be useful,
            but WITHOUT ANY WARRANTY; without even the implied warranty of
            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
            See the GNU General Public License for more details. You should have
            received a copy of the GNU General Public License along with Star Hunter;
            if not, write to the Free Software Foundation, Inc., 59 Temple Place,
            Suite 330, Boston, MA  02111-1307  USA
        """
        
        info = wx.adv.AboutDialogInfo()

        info.SetName('Star Hunter')
        info.SetVersion('Indev')
        info.SetDescription(description)
        info.SetCopyright(f'(C) 2022 {__author__}')
        info.SetWebSite('https://astroair.cn')
        info.SetLicence(licence)
        info.AddDeveloper(__author__)
        info.AddDocWriter(__author__)
        info.AddArtist(__author__)
        info.AddTranslator(__author__)

        wx.adv.AboutBox(info)