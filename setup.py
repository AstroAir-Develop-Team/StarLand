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

from setuptools import setup, find_packages

DESCRIPTION = """StarHunter is a new generation of astronomical photography terminal"""

setup(
    name="starhunter",
    version="1.0.0",
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author='Max Qian',
    author_email='astro_air@126.com',
    url="astroair.cn",
    packages=find_packages('.', exclude=[]),
    include_package_data=True,
    install_requires=['numpy', 'wxpython', 'Flask','Flask-WTF','Flask-SocketIO','ephem','requests','Pillow','lupa',"colorama"],
    license="GPL-3",
    zip_safe=False,
    platforms="any"
)