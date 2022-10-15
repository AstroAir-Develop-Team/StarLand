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
import threading

from gevent import pywsgi

import config

app = flask.Flask(__name__,static_folder="../../assets/",template_folder="../../assets/templates/")
socketio = flask_socketio.SocketIO(app)
crfs = flask_wtf.csrf.CSRFProtect()
crfs.init_app(app)
app.config['WTF_CSRF_ENABLED'] = False

@app.route("/")
@crfs.exempt
def index():
    return flask.render_template(config.assets["web"]["index"])

class starserver():

    def __init__(self):
        self.server = None

    def __del__(self):
        pass

    def runserver(self,host="127.0.0.1",port=8000):
        self.server = pywsgi.WSGIServer(('127.0.0.1',port),app).serve_forever()
          