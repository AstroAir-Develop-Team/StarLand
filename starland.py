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
import os,json,sys,importlib

from core.lib.starlog import starlog

import config
log = starlog(__name__)

# 加载材质配置
def load_assets():
    if os.path.isfile("assets/assets.json"):
        try:
            with open("assets/assets.json",mode="r",encoding="utf-8") as file:
                config.assets = json.load(file)
                log.log("Loaded asset config ,try to check all of the files")
            """
            此处有大问题，遍历多层字典
            for value in config.assets.values():
                dic = value.values()
                for i in range(len(dic)):
                    file = list(dic)[i]
                    if not os.path.isfile(file):
                        log.log(f"Could not find {file}")
                        raise FileNotFoundError(f"{file}")
                log.log("All file check passed")
            """
            return True
        except IOError:
            log.loge("IOError when loaded assets/asset.json")
        except BaseException:
            log.loge("Unknown error when loaded assets/assets.json")
    else:
        log.loge("Could not find assets/assets.json,please check it!")
        return False

# 加载本体配置
def load_config():
    if os.path.isfile("assets/config.json"):
        try:
            with open("assets/config.json",mode="r",encoding="utf-8") as file:
                config.config_data  = json.load(file)
            return True
        except IOError:
            log.loge("IOError when loaded assets/config.json")
        except BaseException:
            log.loge("Unknown error when loaded assets/config.json")
    else:
        log.loge("Could not find assets/config.json,please check it!")
    return False

def main():
    try:
        if load_assets() and load_config():
            log.log("Loading starland ui and server , please wait for a moment")
            log.log(f"System info : {sys.version}")
            log.log(f"Wx version : {wx.version()}")

            app = wx.App()
            exec("mod = importlib.import_module('core.starloader')")
            frame = eval("mod.starloader(None)")
            
            frame.Show()
            app.MainLoop()
        else:
            log.loge("Fail ,redo")
    except KeyboardInterrupt:
        log.loge("Shutdown by user,bye.")
        
if __name__ == "__main__":
    main()
else:
    log.log("Please run in main thread")