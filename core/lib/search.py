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

from dataclasses import dataclass
from json import load
from os import path

import config

from core.lib.starlog import starlog

log = starlog(__name__)

@dataclass
class search_result:
    
    def __init__(self) -> None:
        self.name = ""
        self.number = ""
        self.con = {}
        self.ra = ""
        self.dec = ""
        self.vmag = 0.0
        self.type = ""
        self.describtion = ""
        self.starbase = {}

class search():

    def __init__(self):
        self._check_()
        self.result = search_result()

    def __del__(self):
        pass

    def search(self,target = None,ra = None,dec = None,stardata = "All") -> str:

        pass
    
    # 检查数据库是否存在
    def _check_(self) -> dict:
        """
        Check starbase when initialization\n
        Default starbase is ["Messier.json","NGCIC.json","SAC.json"]\n
        If failed return a dict {"status" : "error"}\n
        """
        flag = True
        try:
            for item in config.config_data["data"]["stardata"]:
                if path.isfile(item):
                    log.log(f"Found {item} & Loaded it to memory")
                    with open(item,mode="r",encoding="utf-8") as file:
                        data = load(file)
                    name = item.split("/").split(".")[0]
                    self.result.starbase[name] = data
                else:
                    log.loge(f"Failed to find {item}")
                    flag = False
        except KeyError:
            log.loge("KeyError when checked starbase")
        return flag

            