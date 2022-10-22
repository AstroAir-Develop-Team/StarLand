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
import os,json,sys,importlib,signal

import core.lib.i18n

from core.lib.starlog import starlog

import config

import gettext
_ = gettext.gettext

log = starlog(__name__)

# 加载文件
def _load_(path,filename) -> (str):
    if os.path.isfile(os.path.join(path,filename)):
        try:
            with open(os.path.join(path,filename),mode="r",encoding="utf-8") as file:
                data = json.load(file)
                log.log(_(f"Loaded {filename} in {path}"))
                return data
        except IOError:
            log.loge(_(f"IOError when load {filename}"))
    else:
        log.loge(_(f"Could not find {filename} in {path}"))

# 检查目录下文件是否完整
# 此处未写完，仅限占位
def _check_(dic={}):
    for i in dic.values():
        if os.path.isfile(i):
            log.log(f"Find {i}")

# 停止运行
def shutdown():
    log.log(_("Shutdown by user,good bye!"))
    exit(0)

# 终端句柄
def term_handler(signum, frame):
	raise KeyboardInterrupt
# 事件绑定 - 有问题，没有效果
signal.signal(signal.SIGTERM, term_handler)

# 主函数
def main():
    # 加载配置
    config.assets = _load_("assets","assets.json")
    config.config_data = _load_("assets","config.json")
    if len(config.assets) != 0 and len(config.config_data) != 0:
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
        raise IOError("Please check your config file!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        shutdown()
else:
    log.loge(_("Please run in main thread"))