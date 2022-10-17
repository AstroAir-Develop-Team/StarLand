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

import flask
import flask_wtf
import flask_socketio

from gevent import pywsgi

import config

# 初始化Flask服务器
app = flask.Flask(__name__,static_folder="../../assets/",template_folder="../../assets/templates/")
# Websocket服务
socketio = flask_socketio.SocketIO(app)
# 不知道是什么的推荐的保护
crfs = flask_wtf.csrf.CSRFProtect()
crfs.init_app(app)

@app.route("/")
@crfs.exempt
def index():
    return flask.render_template(config.assets["web"]["index"])

@app.route("/novnc")
def novnc():
    return flask.render_template(config.assets["web"]["novnc"])

@app.route("/astropanel")
def astropanel():
    return flask.render_template(config.assets["web"]["astropanel"])

@app.route("/gpspanel")
def gpspanel():
    return flask.render_template(config.assets["web"]["gpspanel"])

@app.errorhandler(404)
def not_found(_):
    return flask.render_template(config.assets["web"]["404"])

@app.errorhandler(500)
def server_error(_):
    return flask.render_template(config.assets["web"]["500"])

class starserver():

    def __init__(self):
        self.server = None

    def __del__(self):
        pass

    def runserver(self,port=8000):
        self.server = pywsgi.WSGIServer(('127.0.0.1',port),app).serve_forever()
          