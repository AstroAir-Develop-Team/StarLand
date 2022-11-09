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
from core.lib.astropanel import run_astropanel_s
from core.lib.gpspanel import run_gpspanel_s

import gettext
_ = gettext.gettext

log = starlog(__name__)

###########################################################################

# 初始化Flask服务器
app = Flask(__name__,static_folder=config.mainconfig.get("server").get("main").get("config").get("static"),template_folder=config.mainconfig.get("server").get("main").get("config").get("template"))
app.config.update(
    SECRET_KEY = config.mainconfig["server"]["main"]["config"]["key"],
    SESSION_COOKIE_NAME = config.mainconfig["server"]["main"]["config"]["cookie_name"]
)
# Websocket服务
socketio = SocketIO(app)
# 不知道是什么的推荐的保护
crfs = CSRFProtect()
crfs.init_app(app)

# 主页
@app.route("/")
def index():
    return render_template(config.assets.get("web").get("index"))

# noVNC
@app.route("/novnc")
def novnc():
    return render_template(config.assets.get("web").get("novnc"))

# Astropanel
@app.route("/astropanel")
def astropanel_():
    return render_template(config.assets.get("web").get("astropanel"))

# GPSPanel
@app.route("/gpspanel")
def gpspanel():
    return render_template(config.assets.get("web").get("gpspanel"))

# 403
@app.errorhandler(403)
def not_allow(error):
    return render_template(config.assets.get("web").get("403"))

# 404
@app.errorhandler(404)
def not_found(error):
    return render_template(config.assets.get("web").get("404"))

# 500
@app.errorhandler(500)
def server_error(error):
    return render_template(config.assets.get("web").get("500"))

@socketio.on("client",namespace="/client")
def client(ws):
    """Web server"""


class starserver():
    """Buildin server"""
    # 运行服务器
    def runserver(self,host="127.0.0.1",port=8000) -> None:
        """Run native server"""
        log.log(_(f"Start buildin server in {host} on {port}"))
        socketio.run(app,host=host,port=port)
    
    def run_astropanel(self,host = "127.0.0.1",port = 8626) -> None:
        """Run astropanel server"""
        log.log(_(f"Start astropanel server in {host} on {port}"))
        run_astropanel_s()
    
    def run_gpspanel(self,host = "127.0.0.1" , port = 8625) -> None:
        log.log(_(f"Start gpspanel server in {host} on {port}"))
        run_gpspanel_s()

