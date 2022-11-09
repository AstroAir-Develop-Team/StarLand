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

from flask import Flask
from flask_socketio import SocketIO,emit

app = Flask(__name__)
wsserver = SocketIO(app)

@wsserver.on('connect', namespace='/ws')
# 函数名在内核事件中没有要求，只要不和关键字重复
def connect():
    """Connect"""

@wsserver.on('disconnect', namespace='/ws')
def disconnect():
    """Disconnect"""