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

from dataclasses import dataclass
from requests import get,exceptions
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import json,os

from core.lib.starlog import starlog

import config

log = starlog(__name__)

@dataclass
class QweatherInfo():
    def __init__(self) -> None:
        self.key = ""           # 密钥
        self.license = ""       # 证书
        self.city_id = ""       # 城市ID
        self.name = ""          # 城市名称
        self.full_name = ""     # 城市全名（国家+省+城市）
        self.time = datetime.now().strftime("%Y%m%d")       # 当天日期
        self.data = {
            "status" : "",
            "content" : {}
        }          # 天气数据
        
class Qweather():

    def __init__(self) -> None:
        self.is_internet_connected = config.threadpool.submit(self.checkconnection())
        
        config.threadpool.submit(self.get_location())
        config.threadpool.submit(self.hitokoto())
        pass

    def __del__(self):
        pass

    # 检查互联网连接
    def checkconnection(self):
        log.log("Starting checking internet connection")
        try:
            get("https://www.baidu.com")
            return True
        except exceptions.ConnectionError:
            log.loge("Could not connect www.baidu.com , please check your internet connection")
        except exceptions.HTTPError:
            log.loge("Http Error when checked connection")
        except exceptions.ConnectTimeout:
            log.loge("Timeout")
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
                ip = json.loads(get("https://httpbin.org/ip").text)["origin"]
                log.log(f"Local Ip is {ip}")
                # 再通过IP解析网站获取较为准确的位置
                data = json.loads(get(f"http://ip-api.com/json/{ip}?lang=zh-CN").text)
                # 将获取的坐标写入问价，以便后续读取
                with open(config.config_data["config"]["qweather"][0],"w+",encoding="utf-8") as file:
                    # 将数据格式化输出，默认4个空格
                    file.write(json.dumps(data,indent=4,ensure_ascii=False))
                return data["country"] + data["regionName"] + data["city"]    
            # 连接错误
            except exceptions.ConnectionError:
                log.loge("Could not connect Location server,please check Internet connnection!")
        else:
            log.loge("No internet connected,Could not use locate function")
    
    # 每日一言，有一部分是傻波语录
    def hitokoto(self):
        if self.is_internet_connected:
            try:
                # 获取每日一言
                response = get("https://v1.hitokoto.cn/").json()
                speaker = response['from_who']
                text = response['hitokoto']
                # 如果没有明确的作者
                if not speaker:
                    speaker = "noname"
                log.log(f'A single sentence every day : {text}  --{speaker}')
                return f'{text} -- {speaker}'
            except exceptions.ConnectionError:
                log.loge("Could not connect Hitokoto server,please check Internet connnection!")
            except exceptions.ProxyError:
                log.loge("Proxy error when got hitotoko")
        else:
            log.loge("No internet connected,Could not use hitokoto function")

    # 获取天气数据 - 来自和风天气
    def get_weather_qweater(self):
        # 如果互联网未连接则不会执行任何操作
        if self.is_internet_connected:
            info = QweatherInfo()
            # 如果还未获取天气数据
            if len(info.data["content"]) == 0:
                path = [config.config_data["config"]["qweather"][0],config.config_data["config"]["qweather"][1]]
                if os.path.isfile(path[1]):
                    try:
                        # 读取所需的配置信息 - 密钥 + 证书
                        with open(path[1],mode="r",encoding="utf-8") as file:
                            data = json.load(file)
                            info.key = data.get("key")
                            info.license = data.get("license")
                        log.log(f"Loaded {path[1]}")
                        # 判断密钥和证书是否为空
                        if len(info.key) != 0 and len(info.license) != 0:
                            # 如果还没有获取位置信息则定位
                            if len(info.city_id) == 0:
                                log.logw("Location is unknown , try to get from internet")
                                # 检查文件是否存在
                                if os.path.isfile(path[0]):
                                    # 读取位置信息
                                    with open(path[0],mode="r",encoding="utf-8") as file:
                                        try:
                                            data = json.load(file)
                                            info.name = data["city"]
                                            info.full_name = data["country"] + data["regionName"] + data["city"]
                                        except KeyError:
                                            log.loge("Could not read inneed infomation for getting location")
                                    # 和风天气API - 地理位置
                                    geourl = "https://geoapi.qweather.com/v2/city/lookup?location=" + info.name + "&key=" + info.key
                                    try:
                                        response = get(geourl).json()
                                        if response['code'] != "200":
                                            log.loge(f"Unable to get weather infomation , error code is {data['code']}")
                                        else:
                                            info.city_id = response["location"][0]["id"]
                                        log.log("Get location from https://geoapi.qweather.com/v2/city")
                                    except exceptions.ConnectionError:
                                        log.loge("Could not connect Qweather server,please check Internet connnection!")
                                else:
                                    log.loge(f"Could not find {path[0]}")
                        # 和风天气所有天气API
                        url_list = [
                            f'https://devapi.qweather.com/v7/weather/now?key={info.key}&location={info.city_id}',
                            f'https://devapi.qweather.com/v7/astronomy/sun?key={info.key}&location={info.city_id}&date={info.time}',
                            f'https://devapi.qweather.com/v7/astronomy/moon?key={info.key}&location={info.city_id}&date={info.time}',
                            f'https://devapi.qweather.com/v7/warning/now?key={info.key}&location={info.city_id}',
                        ]
                        # 太阳高度角需要商业证书才能获取
                        # 此处需要补太阳高度角url
                        if info.license == "business":
                            url_list.append(f"")
                        # 多线程
                        weather_thread = ThreadPoolExecutor(max_workers=5)
                        weather_thread.map(self._load_from_internet_,url_list)
                        # 此处需要增加获取返回值
                        info.data["status"] = "successful"
                        return info.data
                    except IOError:
                        log.loge("IOError when load Qweather")
                        return {"status":"error"}
                else:
                    log.loge(f"Could not find {config.config_data['config']['qweather'][1]}")
                    return {"status":"error"}
            else:
                log.logw("Had already got weather info,please do not load it again!")
                return info.data
        else:
            log.loge("No internet connected,Could not use Qweather function")
            return {"status":"error"}

    # 获取天气数据 - 来自OpenWeather
    def get_weather_openweather(self):
        if self.is_internet_connected:
            pass
        else:
            log.loge("No internet connected,Could not use Openweather function")
            return {"status":"error"}
    
    # 从网络中下载数据
    def _load_from_internet_(self,url) -> (str):
        try:
            response = get(url).json()
            return response
        except exceptions.ConnectionError:
            log.loge(f"Failed to get from {url}")
