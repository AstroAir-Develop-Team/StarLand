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

import gettext
_ = gettext.gettext

log = starlog(__name__)

@dataclass
class QweatherInfo():
    """Weather Info"""
    def __init__(self) -> None:
        self.key = ""           # 密钥
        self.license = ""       # 证书
        self.city_id = ""       # 城市ID
        self.name = ""          # 城市名称
        self.full_name = ""     # 城市全名（国家+省+城市）
        self.time = datetime.now().strftime("%Y%m%d")       # 当天日期
        self.alt = ""           # 海拔
        self.timezone = ""      # 时区
        self.data = {
            "status" : "",
            "content" : {}
        }          # 天气数据
        
class Qweather():
    """All Weather Function"""
    def __init__(self) -> None:
        """Init"""
        threadpool = ThreadPoolExecutor(max_workers=5)
        self.is_internet_connected = self.checkconnection()
        threadpool.submit(self.get_location)
        threadpool.submit(self.hitokoto)
        threadpool.submit(self.get_weather_qweather)

    # 检查互联网连接
    def checkconnection(self) -> bool:
        """Check Internet Connection based on wheather www.baidu.com is accessible"""
        log.log(_("Starting checking internet connection"))
        try:
            get("https://www.baidu.com")
            return True
        except exceptions.ConnectionError:
            log.loge(_("Could not connect www.baidu.com , please check your internet connection"))
        except exceptions.ConnectTimeout:
            log.loge(_("Timeout"))
        finally:
            log.log(_("Finish Internet checking"))
        return False

    # 获取定位
    def get_location(self) -> dict:
        """Get location via internet"""
        if not self.is_internet_connected:
            log.loge(_("No internet connected,Could not use locate function"))
            return self.return_message("error",_("no internet connected"),_("check"))
        try:
            # 获取基于互联网定位的本机IP
            ip = json.loads(get("https://httpbin.org/ip").text).get("origin")
            log.log(_(f"Local Ip is {ip}"))
            # 再通过IP解析网站获取较为准确的位置
            response = json.loads(get(f"http://ip-api.com/json/{ip}?lang=zh-CN").text)
            config.mainconfig["weather"]["location"] = response
            r_msg = response.get("country") + response.get("regionName") + response.get("city")    
            return self.return_message("success",r_msg,"")
        # 连接错误
        except exceptions.ConnectionError:
            log.loge(_("Could not connect Location server,please check Internet connnection!"))
            return self.return_message("error",_("connection error"),_("unknown"))            
    
    # 每日一言，有一部分是傻波语录
    def hitokoto(self) -> dict:
        if not self.is_internet_connected:
            log.loge(_("No internet connected,Could not use hitokoto function"))
            return self.return_message("error",_("no internet connected"),_("check"))
        try:
            # 获取每日一言
            response = get(config.mainconfig.get("weather").get("hitokoto").get("url")).json()
            if response.get("from_who") is None:
                config.mainconfig["weahter"]["hitokoto"]["data"]["from"] = _("noname")
            config.mainconfig["weahter"]["hitokoto"]["data"]["word"] = response.get('hitokoto')
            return self.return_message("success","","")
        except exceptions.ConnectionError:
            log.loge(_("Could not connect Hitokoto server,please check Internet connnection!"))
            return self.return_message("error",_("connection error"),_("unknown"))  

    # 获取天气数据 - 来自和风天气
    def get_weather_qweather(self):
        # 如果互联网未连接则不会执行任何操作
        if not self.is_internet_connected:
            log.loge(_("No internet connected,Could not use Qweather function"))
            return self.return_message("error",_("no internet connected"),_("check"))
        info = QweatherInfo()
        # 如果还未获取天气数据
        if info.data.get("content") is None:
            info.key = config.mainconfig.get("weather").get("qweather").get("key")
            info.license = config.mainconfig.get("weather").get("qweather").get("license")
            # 获取密钥和证书
            if info.key is None or info.license is None:
                log.loge(_(f"Failed to load Qweather key and license"))
                return self.return_message("error",_("empty key or license"),_("register"))
            # 未获得城市定位
            if len(info.city_id) == 0:
                log.log(_("Get location via internet"))

                info.name = config.mainconfig.get("weather").get("location").get("city")
                country = config.mainconfig.get("weather").get("location").get("country")
                region = config.mainconfig.get("weather").get("location").get("regionName")
                city = config.mainconfig.get("weather").get("location").get("city")
                if country is None or region is None or city is None:
                    log.loge(_("Failed to get city name,Can't run locating function"))
                    return self.return_message("error",_("empty city name"),_("relocate"))

                info.full_name = country + region + city
                # 和风天气API - 地理位置
                geourl = "https://geoapi.qweather.com/v2/city/lookup?location=" + info.name + "&key=" + info.key
                try:
                    response = get(geourl).json()
                    if response.get("code") != "200":
                        log.loge(_(f"Unable to get weather infomation , error code is {response['code']}"))
                        return self.return_message("error",_("fail to locate"),_("check"))
                    info.city_id = response.get("location")[0].get("id")
                    log.log("Get location from https://geoapi.qweather.com/v2/city")
                except exceptions.Timeout:
                    log.loge(_("Could not connect Qweather server,please check Internet connnection!"))
                    return self.return_message("error",_("timeout"),_("try again"))
                    
            # 和风天气所有天气API
            url_list = []
            if info.license == "dev":
                url_list = [
                    f'https://devapi.qweather.com/v7/weather/now?key={info.key}&location={info.city_id}',
                    f'https://devapi.qweather.com/v7/astronomy/sun?key={info.key}&location={info.city_id}&date={info.time}',
                    f'https://devapi.qweather.com/v7/astronomy/moon?key={info.key}&location={info.city_id}&date={info.time}',
                    f'https://devapi.qweather.com/v7/warning/now?key={info.key}&location={info.city_id}',
                    f'https://devapi.qweather.com/v7/weather/7d?key={info.key}&location={info.city_id}'
                ]
                log.log("Chose developer key & license")
            elif info.license == "business":
                url_list = [
                    f'https://api.qweather.com/v7/weather/now?key={info.key}&location={info.city_id}',
                    f'https://api.qweather.com/v7/astronomy/sun?key={info.key}&location={info.city_id}&date={info.time}',
                    f'https://api.qweather.com/v7/astronomy/moon?key={info.key}&location={info.city_id}&date={info.time}',
                    f'https://api.qweather.com/v7/warning/now?key={info.key}&location={info.city_id}',
                    f'https://api.qweather.com/v7/weather/7d?key={info.key}&location={info.city_id}',
                    f"https://api.qweather.com/v7/astronomy/solar-elevation-angle?key={info.key}&location={info.city_id}&date={info.time}&tz={info.timezone}&alt={info.alt}"
                ]
                log.log(_("Chose business key & license"))
            else:
                log.logw(_("Unknown license,choose default key & license"))
            # 多线程
            weather_thread = ThreadPoolExecutor(max_workers=5)
            results = weather_thread.map(self._load_from_internet_,url_list)
            # 读取返回的结果
            result_name = ["now","sun","moon","warning","7d"]
            for item,result_type in zip(results,result_name):
                info.data["content"][result_type] = item
            info.data["status"] = "success"
            config.mainconfig["weather"]["weather"] = info.data

    # 获取天气数据 - 来自OpenWeather
    def get_weather_openweather(self):
        if not self.is_internet_connected:
            log.loge(_("No internet connected,Could not use Openweather function"))
            return self.return_message("error",_("no internet connected"),_("check"))

    def return_message(self,status : str,message : str ,advice : str) -> dict:
        """Return message in dict format"""
        return {
            "status" : status,
            "message" : message,
            "advice" : advice
        }
    
    # 从网络中下载数据
    def _load_from_internet_(self,url) -> str:
        """Download"""
        try:
            response = get(url).json()
            return response
        except exceptions.ConnectionError:
            log.loge(f"Failed to get from {url}")
