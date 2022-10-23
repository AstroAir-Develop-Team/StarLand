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
from flask import Flask,render_template
from flask_wtf import CSRFProtect
from flask_socketio import SocketIO

from os import path
from json import load

import config

from core.lib.starlog import starlog

log = starlog(__name__)

###########################################################################

# 读取配置文件
def _load_config_():
    _path = config.config_data["config"]["server"]
    if path.isfile(_path[0]):
        with open(_path[0],mode="r",encoding="utf-8") as file:
            data = load(file)
        log.log(f"Loaded server config from file")
        return data
    else:
        log.loge(f"Failed to load {_path[0]}")
    return False
config.mainconfig["server"] = _load_config_()

###########################################################################

# 初始化Flask服务器
app = Flask(__name__,static_folder=config.mainconfig["server"]["config"]["static"],template_folder=config.mainconfig["server"]["config"]["template"])
app.config.update(
    SECRET_KEY = config.mainconfig["server"]["config"]["key"],
    SESSION_COOKIE_NAME = config.mainconfig["server"]["config"]["cookie_name"]
)
# Websocket服务
socketio = SocketIO(app)
# 不知道是什么的推荐的保护
crfs = CSRFProtect()
crfs.init_app(app)

###########################################################################

@dataclass
class server_info():
    def __init__(self) -> None:
        self.astropanel = None
        self.gpspanel = None
info = server_info()

###########################################################################

# 主页
@app.route("/")
def index():
    return render_template(config.assets["web"]["index"])

# noVNC - 未来移植
@app.route("/novnc")
def novnc():
    return render_template(config.assets["web"]["novnc"])

# Astropanel
@app.route("/astropanel")
def astropanel():
    return render_template(config.assets["web"]["astropanel"])

# GPSPanel
@app.route("/gpspanel")
def gpspanel():
    return render_template(config.assets["web"]["gpspanel"])

# 404
@app.errorhandler(404)
def not_found(_):
    return render_template(config.assets["web"]["404"])

# 500
@app.errorhandler(500)
def server_error(_):
    return render_template(config.assets["web"]["500"])

###########################################################################

def astropanel_thread():
    pass

@socketio.on("/astropanel/connect")
def handle_connect():
    if info.astropanel is None:
        info.astropanel = socketio.start_background_task(target=astropanel_thread)


class starserver():

    def __init__(self):
        self.server = None
 
    def __del__(self):
        log.log("Server class deleted")

    # 运行服务器
    def runserver(self,host="127.0.0.1",port=8000):
        log.log(f"Start buildin server in {host} on {port}")
        socketio.run(app,host=host,port=port)

          