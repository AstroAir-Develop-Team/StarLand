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

import requests
import json,os
from concurrent.futures import ThreadPoolExecutor

from core.lib.starlog import starlog
import config

log = starlog(__name__)

class Qweather():

    def __init__(self) -> None:
        self.is_internet_connected = self.checkconnection()
        self.threadpool = ThreadPoolExecutor(max_workers=5)
        self.threadpool.submit(self.get_location())
        self.threadpool.submit(self.hitokoto())
        pass

    def __del__(self):
        pass

    def checkconnection(self):
        log.log("Starting checking internet connection")
        try:
            requests.get("https://www.baidu.com")
            return True
        except requests.exceptions.ConnectionError:
            log.log("Could not connect www.baidu.com , please check your internet connection")
        except requests.exceptions.HTTPError:
            log.log("Http Error when checked connection")
        except requests.exceptions.ConnectTimeout:
            log.log("Timeout")
        except:
            log.log("Unknown error during checking connection")
        return False

    # 获取定位
    def get_location(self):
        if self.is_internet_connected:
            # 如果没有文件夹就自己建一个
            if not os.path.exists("config/client"):
                os.mkdir("config/client")
            """
            此处是否有能代替以下两个网址的，以提高访问速度
            """
            try:
                # 获取基于互联网定位的本机IP
                ip = json.loads(requests.get("https://httpbin.org/ip").text)["origin"]
                log.log(f"Local Ip is {ip}")
                # 再通过IP解析网站获取较为准确的位置
                data = json.loads(requests.get(f"http://ip-api.com/json/{ip}?lang=zh-CN").text)
                # 将获取的坐标写入问价，以便后续读取
                with open(config.config_data["config"]["qweather"][0],"w+",encoding="utf-8") as file:
                    # 将数据格式化输出，默认4个空格
                    file.write(json.dumps(data,indent=4,ensure_ascii=False))
            # 连接错误
            except requests.exceptions.ConnectionError:
                log.log("Could not connect Location server,please check Internet connnection!")
            return data["country"] + data["regionName"] + data["city"]
        else:
            log.log("No internet connected,Could not use locate function")
    
    # 每日一言，有一部分是傻波语录
    def hitokoto(self):
        if self.is_internet_connected:
            try:
                # 获取每日一言
                response = requests.get("https://v1.hitokoto.cn/").json()
                speaker = response['from_who']
                text = response['hitokoto']
                # 如果没有明确的作者
                if not speaker:
                    speaker = "noname"
                log.log(f'A single sentence every day : {text}  --{speaker}')
            except requests.exceptions.ConnectionError:
                log.log("Could not connect Hitokoto server,please check Internet connnection!")
            return f'{text} -- {speaker}'
        else:
            log.log("No internet connected,Could not use hitokoto function")