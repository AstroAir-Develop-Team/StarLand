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
from numpy import degrees
from datetime import datetime
import ephem

import config

@dataclass
class sun():
    def __init__(self) -> None:
        self.ra = None          # 赤经
        self.dec = None         # 赤纬
        self.az = None          # 地平经度
        self.alt = None         # 方位角
        self.rise = None        # 升起
        self.transmit = None    # 中天
        self.set = None         # 落下
        self.ct_start = None    # 民用黄昏开始
        self.ct_end = None      # 民用黄昏结束
        self.at_start = None    # 天文黄昏开始
        self.at_end = None      # 天文黄昏结束
        self.equinox = None     # 春分
        self.solstice = None    # 冬至
        self.data = {}          # 数据

class starinfo():

    def __init__(self) -> None:

        self.home = ephem.Observer()

        self.sun = sun()

        self.get_sun()

    def __del__(self) -> None:
        pass

    def get_sun(self):

        t = datetime.utcnow()

        self.sun.ra = str(ephem.Sun(self.home).ra)
        self.sun.dec = str(ephem.Sun(self.home).dec)
        self.sun.az = ("%.2f°"%degrees(ephem.Sun(self.home).az))
        self.sun.alt = ("%.2f°"%degrees(ephem.Sun(self.home).alt))
        self.sun.rise = str(self.get_body_positions(self.home,ephem.Sun(self.home))[0])
        self.sun.transmit = str(self.get_body_positions(self.home,ephem.Sun(self.home))[1])
        self.sun.set = str(self.get_body_positions(self.home,ephem.Sun(self.home))[2])
        self.sun.ct_start = self.get_sun_twilights(self.home)[0][0]
        self.sun.ct_end = self.get_sun_twilights(self.home)[0][1]
        self.sun.at_start = self.get_sun_twilights(self.home)[2][0]
        self.sun.at_end = self.get_sun_twilights(self.home)[2][1]
        self.sun.equinox = str(ephem.localtime(ephem.next_equinox(t)).strftime("%Y-%m-%d %H:%M:%S"))
        self.sun.solstice = str(ephem.localtime(ephem.next_solstice(t)).strftime("%Y-%m-%d %H:%M:%S"))
        
    # 获取黄昏信息 - 天文 + 民用
    def get_sun_twilights(self,observer):
        results = []
        observer_horizon = observer.horizon
        twilights = [('-6', True), ('-12', True), ('-18', True)]
        for twi in twilights:
            observer.horizon = twi[0]
            try:
                rising_setting = self.get_body_positions(observer,ephem.Sun(observer))
                results.append((rising_setting[0], rising_setting[2]))
            except ephem.AlwaysUpError:
                results.append(('n/a', 'n/a'))
        observer.horizon = observer_horizon
        return results

    def get_body_positions(self,observer, body):
        positions = []
        try:
            if ephem.localtime(observer.previous_rising(body)).date() == ephem.localtime(observer.date).date() and observer.previous_rising(body) < observer.previous_transit(body) < observer.previous_setting(body) < observer.date:
                positions.append(observer.previous_rising(body))
                positions.append(observer.previous_transit(body))
                positions.append(observer.previous_setting(body))
            elif ephem.localtime(observer.previous_rising(body)).date() == ephem.localtime(observer.date).date() and observer.previous_rising(body) < observer.previous_transit(body) < observer.date < observer.next_setting(body):
                positions.append(observer.previous_rising(body))
                positions.append(observer.previous_transit(body))
                positions.append(observer.next_setting(body))
            elif ephem.localtime(observer.previous_rising(body)).date() == ephem.localtime(observer.date).date() and observer.previous_rising(body) < observer.date < observer.next_transit(body) < observer.next_setting(body):
                positions.append(observer.previous_rising(body))
                positions.append(observer.next_transit(body))
                positions.append(observer.next_setting(body))
            elif ephem.localtime(observer.previous_rising(body)).date() == ephem.localtime(observer.date).date() and  observer.date < observer.next_rising(body) < observer.next_transit(body) < observer.next_setting(body):
                positions.append(observer.next_rising(body))
                positions.append(observer.next_transit(body))
                positions.append(observer.next_setting(body))
            else:
                positions.append(observer.next_rising(body))
                positions.append(observer.next_transit(body))
                positions.append(observer.next_setting(body))
        except (ephem.NeverUpError, ephem.AlwaysUpError):
            try:
                if ephem.localtime(observer.previous_transit(body)).date() == ephem.localtime(observer.date).date() and observer.previous_transit(body) < observer.date:
                    positions.append('-')
                    positions.append(observer.previous_transit(body))
                    positions.append('-')
                elif ephem.localtime(observer.previous_transit(body)).date() == ephem.localtime(observer.date).date() and observer.next_transit(body) > observer.date:
                    positions.append('-')
                    positions.append(observer.next_transit(body))
                    positions.append('-')
                else:
                    positions.append('-')
                    positions.append('-')
                    positions.append('-')
            except (ephem.NeverUpError, ephem.AlwaysUpError):
                positions.append('-')
                positions.append('-')
                positions.append('-')

        if positions[0] != '-':
            positions[0] = ephem.localtime( positions[0] ).strftime("%H:%M:%S")
        if positions[1] != '-':
            positions[1] = ephem.localtime( positions[1] ).strftime("%H:%M:%S")
        if positions[2] != '-':
            positions[2] = ephem.localtime( positions[2] ).strftime("%H:%M:%S")

        return positions
        