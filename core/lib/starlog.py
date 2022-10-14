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

logger = logging.getLogger(__name__)
console_handle = logging.StreamHandler()
logger.addHandler(console_handle)
fort = logging.Formatter('[%(asctime)s][%(levelname)s]%(message)s')
console_handle.setFormatter(fort)
logger.setLevel(logging.INFO)

class starlog():

    def __init__(self,name) -> None:
        self.uname = name

    def log(self,msg) -> (str):
        logger.info(f"[{self.uname}] - {msg}")