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

import logging
from colorama import Fore,init
from os import mkdir, path
from time import strftime

# 初始化日志对象
logger = logging.getLogger(__name__)
fort = logging.Formatter('[%(asctime)s][%(levelname)s]%(message)s')
# 控制台日志参数
console_handle = logging.StreamHandler()
console_handle.setFormatter(fort)
logger.addHandler(console_handle)
# 文件日志
if not path.exists("./logs"):       # 若日志文件夹不存在，则创建一个
    mkdir("./logs")
file_handle = logging.FileHandler(filename=f"logs/{strftime('%Y-%m-%d#%H%M%S')}.log",encoding="utf-8",mode="w+")
file_handle.setFormatter(fort)
logger.addHandler(file_handle)
# 设置日志级别
logger.setLevel(logging.INFO)

init(autoreset=True)

class starlog():

    def __init__(self,name) -> (str):
        self.uname = name

    def __del__(self):
        pass

    #日志
    def log(self,msg) -> (str):
        logger.info(f"[{self.uname}] - {msg}")

    # 错误日志
    def loge(self,msg) -> (str):
        logger.info(f"[{self.uname}] - " + Fore.RED + f"{msg}" + Fore.RESET)

    # 警告日志
    def logw(self,msg) -> (str):
        logger.info(f"[{self.uname}] - " + Fore.YELLOW + f"{msg}" + Fore.RESET)

    # 调试日志
    def logd(self,msg) -> (str):
        logger.info(f"[{self.uname}] - " + Fore.MAGENTA + f"{msg}" + Fore.RESET)
