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
import os,sys,importlib
from json import load , JSONDecodeError

import core.lib.i18n

from core.lib.starlog import starlog

import config

import gettext
_ = gettext.gettext

log = starlog(__name__)

def _load_(path : str,filename : str) -> dict:
    """Load Config File when preloading"""
    if os.path.isfile(os.path.join(path,filename)):
        try:
            with open(os.path.join(path,filename),mode="r",encoding="utf-8") as file:
                data = load(file)
                log.log(_(f"Loaded {filename} in {path}"))
                return data
        except IOError:
            log.loge(_(f"IOError when load {filename}"))
        except JSONDecodeError as error:
            log.loge(_(f"{filename} is not a json file , error code : {error.msg}"))
    else:
        log.loge(_(f"Could not find {filename} in {path}"))

def _check_(dic : dict) -> dict:
    """Check if the file is correct - Not Finish"""
    for item in dic.values():
        if os.path.isfile(item):
            log.log(f"Find {item}")

def main() -> None:
    """Main Function"""
    # 加载配置
    config.assets = _load_("assets","assets.json")
    config.config_data = _load_("data","data.json")
    config.mainconfig = _load_("assets","mainconfig.json")
    # 检查配置是否加载成功
    if config.assets is not None and config.config_data is not None and config.mainconfig is not None:
        # 输出一些基本信息
        log.log(_("Loading starland ui and server , please wait for a moment"))
        log.log(_(f"System info : {sys.version}"))
        log.log(_(f"Wx version : {wx.version()}"))
        # 创建实例
        app = wx.App()
        # 先加载模组界面
        try:
            mod = importlib.import_module('core.starloader')
        except ImportError:
            log.loge(_("Could not find core.starloader,please check it ,if there is any unknwon problem ,please contact the developer"))
        frame = mod.starloaderframe()
        frame.Show()
        # 主循环
        app.MainLoop()
    else:
        log.loge(_("Config data is empty,something is going wrong!"))
        raise IOError(_("Please check your config file!"))

if __name__ == "__main__":
    main()
else:
    log.loge(_("Please run in main thread"))