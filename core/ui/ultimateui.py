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

###########################################################################

"""Py shell terminal based on wx.py"""

import wx.py

def run_shell(frame,nb):
    intro = 'Welcome To PyCrust %s - The Flakiest Python Shell' % wx.py.version.VERSION
    return wx.py.shell.Shell(nb, -1, introText=intro)

###########################################################################

###########################################################################

"""Advanced Py shell based on wx.py"""

def run_a_shell(frame, nb):
    intro = 'Welcome To PyCrust %s - The Flakiest Python Shell' % wx.py.version.VERSION
    win = wx.py.crust.Crust(nb, intro=intro)
    return win

###########################################################################

###########################################################################

"""Basic music player based on wx.media"""

import wx
import wx.media
import os

class StaticText(wx.StaticText):
    """
    A StaticText that only updates the label if it has changed, to
    help reduce potential flicker since these controls would be
    updated very frequently otherwise.
    """
    def SetLabel(self, label):
        if label != self.GetLabel():
            wx.StaticText.SetLabel(self, label)

class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1,
                          style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)

        # Create some controls
        try:
            backend = "" # let MediaCtrl choose default backend
            self.mc = wx.media.MediaCtrl()
            ok = self.mc.Create(self, style=wx.SIMPLE_BORDER,
                                szBackend=backend)
            if not ok:
                raise NotImplementedError
        except NotImplementedError:
            self.Destroy()
            raise

        # the following event is not sent with the Windows default backend
        # MEDIABACKEND_DIRECTSHOW
        # choose above e.g. MEDIABACKEND_WMP10 if this is a problem for you
        self.Bind(wx.media.EVT_MEDIA_LOADED, self.OnMediaLoaded)

        btn1 = wx.Button(self, -1, "Load File")
        self.Bind(wx.EVT_BUTTON, self.OnLoadFile, btn1)

        btn2 = wx.Button(self, -1, "Play")
        self.Bind(wx.EVT_BUTTON, self.OnPlay, btn2)
        self.playBtn = btn2

        btn3 = wx.Button(self, -1, "Pause")
        self.Bind(wx.EVT_BUTTON, self.OnPause, btn3)

        btn4 = wx.Button(self, -1, "Stop")
        self.Bind(wx.EVT_BUTTON, self.OnStop, btn4)

        slider = wx.Slider(self, -1, 0, 0, 10)
        self.slider = slider
        slider.SetMinSize((150, -1))
        self.Bind(wx.EVT_SLIDER, self.OnSeek, slider)

        self.st_size = StaticText(self, -1, size=(100,-1))
        self.st_len  = StaticText(self, -1, size=(100,-1))
        self.st_pos  = StaticText(self, -1, size=(100,-1))


        # setup the layout
        sizer = wx.GridBagSizer(5,5)
        sizer.Add(self.mc, (1,1), span=(5,1))#, flag=wx.EXPAND)
        sizer.Add(btn1, (1,3))
        sizer.Add(btn2, (2,3))
        sizer.Add(btn3, (3,3))
        sizer.Add(btn4, (4,3))
        sizer.Add(slider, (6,1), flag=wx.EXPAND)
        sizer.Add(self.st_size, (1, 5))
        sizer.Add(self.st_len,  (2, 5))
        sizer.Add(self.st_pos,  (3, 5))
        self.SetSizer(sizer)

        wx.CallAfter(self.DoLoadFile, os.path.abspath("data/testmovie.mpg"))

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        self.timer.Start(100)



    def OnLoadFile(self, evt):
        dlg = wx.FileDialog(self, message="Choose a media file",
                            defaultDir=os.getcwd(), defaultFile="",
                            style=wx.FD_OPEN | wx.FD_CHANGE_DIR )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.DoLoadFile(path)
        dlg.Destroy()


    def DoLoadFile(self, path):

        if not self.mc.Load(path):
            wx.MessageBox("Unable to load %s: Unsupported format?" % path,
                          "ERROR",
                          wx.ICON_ERROR | wx.OK)
            self.playBtn.Disable()
        else:
            self.mc.SetInitialSize()
            self.GetSizer().Layout()
            self.slider.SetRange(0, self.mc.Length())
            self.playBtn.Enable()

    def OnMediaLoaded(self, evt):
        self.playBtn.Enable()

    def OnPlay(self, evt):
        if not self.mc.Play():
            wx.MessageBox("Unable to Play media : Unsupported format?",
                          "ERROR",
                          wx.ICON_ERROR | wx.OK)
        else:
            self.mc.SetInitialSize()
            self.GetSizer().Layout()
            self.slider.SetRange(0, self.mc.Length())

    def OnPause(self, evt):
        self.mc.Pause()

    def OnStop(self, evt):
        self.mc.Stop()


    def OnSeek(self, evt):
        offset = self.slider.GetValue()
        self.mc.Seek(offset)

    def OnTimer(self, evt):
        offset = self.mc.Tell()
        self.slider.SetValue(offset)
        self.st_size.SetLabel('size: %s' % self.mc.GetBestSize())
        self.st_len.SetLabel('length: %d seconds' % (self.mc.Length()/1000))
        self.st_pos.SetLabel('position: %d' % offset)

    def ShutdownDemo(self):
        self.timer.Stop()
        del self.timer

def runTest(frame, nb, log):
    try:
        win = TestPanel(nb, log)
        return win
    except NotImplementedError:
        from wx.lib.msgpanel import MessagePanel
        win = MessagePanel(nb, 'wx.MediaCtrl is not available on this platform.',
                           'Sorry', wx.ICON_WARNING)
        return win

###########################################################################