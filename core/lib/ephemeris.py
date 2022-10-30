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
the Free Software Foundation, Inctypes., 51 Franklin Street, Fifth Floor,
Boston, MA 02110-1301, USA.

"""

import requests
from concurrent.futures import ThreadPoolExecutor
import os

from core.lib.starlog import starlog

log = starlog(__name__)

_p = os.path.join

def messier():

    def check() -> bool:
        dirs = _p(_p(os.getcwd(),"data"),"messier")
        if not os.path.exists(dirs):
            os.mkdir(dirs)
            return False
        flag = True
        for id in range(1,111):
            path = _p(_p(os.getcwd(),"data"),f"m{id}.jpg") 
            if not os.path.isfile(path):
                flag = False
                log.loge(f"Failed to find {path}")
            else:
                log.log(f"Find {path}")
        return flag

    def download(id) -> None:
        url = f"http://messier.seds.org/Jpg/m{id}.jpg"
        log.log(f"Download image from {url}")
        with open(f"data/m{id}.jpg",mode="wb+") as file:
            file.write(requests.get(url).content)

    if not check():
        log.logw("Some images are found missing, start downloading")
        thread = ThreadPoolExecutor(max_workers=20)
        thread.map(download,range(1,111))
    else:
        log.log("All messier image files are checked!")

def apod():
    url = "https://apod.nasa.gov/apod/astropix.html"