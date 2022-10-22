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

from flask import Flask,render_template
from flask_wtf import CSRFProtect
from flask_socketio import SocketIO

import config

from core.lib.starlog import starlog

# 初始化Flask服务器
app = Flask(__name__,static_folder="../../assets/",template_folder="../../assets/templates/")
app.config.update(
    SECRET_KEY = "starland",
    SESSION_COOKIE_NAME = "starland"
)
# Websocket服务
socketio = SocketIO(app)
# 不知道是什么的推荐的保护
crfs = CSRFProtect()
crfs.init_app(app)

log = starlog(__name__)

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

class starserver():

    def __init__(self):
        log.log("Init server and load config")
        self.server = None

    def __del__(self):
        log.log("Server class deleted")

    # 运行服务器
    def runserver(self,host="127.0.0.1",port=8000):
        log.log(f"Start buildin server in {host} on {port}")
        app.run(host=host,port=port,threaded=True)
          