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

from os import remove,close,write,openpty,path,ttyname,symlink
from datetime import datetime
from time import sleep
from re import split
from json import load

from core.lib.starlog import starlog

import config

log = starlog(__name__)

class virtualgps():

    def __init__(self):
        self.path = config.config_data["config"]["virtualgps"]
        self.latitude = 0.0
        self.longitude = 0.0
        self.elevation = 0.0

    def __del__(self):
        remove(self.path[1])
        close(self.master)
        close(self.slave)

    # 转化为六十进制
    def convert_to_sexagesimal(self,coord):

        elements = split(r'[\u00ba\':\"]', coord)

        degrees = float(elements[0])
        if (len(elements) - 1) > 0:
            # 将分转化为度
            degrees += float(elements[1]) / 60
        if (len(elements) - 1) > 1:
            # 将秒转化为分
            degrees += float(elements[2]) / 3600
        return degrees

    # 检查卫星数据是否正确
    def nmea_checksum(self,sentence):
        chsum = 0
        for s in sentence:
            chsum ^= ord(s)
        return hex(chsum)[2:]
    
    # 启动虚拟GPS服务
    def virtualgps(self):
        # 初始化虚拟终端
        self.master, self.slave = openpty()
        self.pty = ttyname(self.slave)
        # 如果已经存在文件则移除
        if path.isfile(self.path[1]):
            remove(self.path[1])
        # 创建一个虚拟的终端设备
        symlink(self.pty,self.path[1])
        # 读取配置文件
        if path.isfile(self.path[0]):
            try:
                with open(self.path[0],mode="r",encoding="utf-8") as file:
                    data = load(file)
                log.log(f"Loaded {self.path[0]}")
                self.latitude = self.convert_to_sexagesimal(data["latitude"])
                self.longitude = self.convert_to_sexagesimal(data["longitude"])
                self.elevation = float(data["elevation"])   
            except IOError:
                log.loge(f"Could not open {self.path[0]}")
        else:
            log.loge(f"Failed to find {self.path[0]}")
        
        NS = "N" if self.latitude > 0 else "S"      # 南/北
        WE = "E" if self.longitude > 0 else "W"     # 东/西

        # format for NMEA
        self.latitude = abs(self.latitude)
        self.longitude = abs(self.longitude)

        lat_deg = int(self.latitude)
        lon_deg = int(self.longitude)

        lat_min = (self.latitude - lat_deg) * 60
        lon_min = (self.longitude - lon_deg) * 60

        self.latitude = "%02d%07.4f" % (lat_deg, lat_min)
        self.longitude = "%03d%07.4f" % (lon_deg, lon_min)
        while True:
            try:
                now = datetime.utcnow()
                date_now = now.strftime("%d%m%y")
                time_now = now.strftime("%H%M%S")

                gpgga = "GPGGA,%s,%s,%s,%s,%s,1,12,1.0,%s,M,0.0,M,," % (time_now, self.latitude, NS, self.longitude, WE, self.elevation)
                gpgsa = "GPGSA,A,3,,,,,,,,,,,,,1.0,1.0,1.0"
                gprmc = "GPRMC,%s,A,%s,%s,%s,%s,,,%s,000.0,W" % (time_now, self.latitude, NS, self.longitude, WE, date_now)

                gpgga = "$%s*%s\n" % (gpgga, self.nmea_checksum(gpgga))
                gpgsa = "$%s*%s\n" % (gpgsa, self.nmea_checksum(gpgsa))
                gprmc = "$%s*%s\n" % (gprmc, self.nmea_checksum(gprmc))

                write(self.master, gpgga.encode())
                write(self.master, gpgsa.encode())
                write(self.master, gprmc.encode())

                sleep(1)
            except IOError:
                log.loge("IOError during virtualgps running")
