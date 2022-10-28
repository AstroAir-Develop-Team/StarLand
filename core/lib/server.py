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
from numpy import degrees,rad2deg
from datetime import datetime,timedelta
from time import sleep
import gps3

from os import path
from json import load
from threading import Thread

import config
import ephem

from core.lib.starlog import starlog
from core.lib.exceptions import gps_timeout

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
app = Flask(__name__,static_folder=config.mainconfig["server"]["main"]["config"]["static"],template_folder=config.mainconfig["server"]["main"]["config"]["template"])
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
    return render_template(config.assets["web"]["index"])

# noVNC - 未来移植
@app.route("/novnc")
def novnc():
    return render_template(config.assets["web"]["novnc"])

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
        self.server = None
        
 
    def __del__(self):
        log.log("Server class deleted")

    # 运行服务器
    def runserver(self,host="127.0.0.1",port=8000):
        log.log(f"Start buildin server in {host} on {port}")
        socketio.run(app,host=host,port=port)


class astropanel():

    def __init__(self) -> None:
        pass

    def get_moon_phase(observer):
        target_date_utc = observer.date
        target_date_local = ephem.localtime( target_date_utc ).date()
        next_full = ephem.localtime( ephem.next_full_moon(target_date_utc) ).date()
        next_new = ephem.localtime( ephem.next_new_moon(target_date_utc) ).date()
        next_last_quarter = ephem.localtime( ephem.next_last_quarter_moon(target_date_utc) ).date()
        next_first_quarter = ephem.localtime( ephem.next_first_quarter_moon(target_date_utc) ).date()
        previous_full = ephem.localtime( ephem.previous_full_moon(target_date_utc) ).date()
        previous_new = ephem.localtime( ephem.previous_new_moon(target_date_utc) ).date()
        previous_last_quarter = ephem.localtime( ephem.previous_last_quarter_moon(target_date_utc) ).date()
        previous_first_quarter = ephem.localtime( ephem.previous_first_quarter_moon(target_date_utc) ).date()

        if target_date_local in (next_full, previous_full):
            return 'Full'
        elif target_date_local in (next_new, previous_new):
            return 'New'
        elif target_date_local in (next_first_quarter, previous_first_quarter):
            return 'First Quarter'
        elif target_date_local in (next_last_quarter, previous_last_quarter):
            return 'Last Quarter'
        elif previous_new < next_first_quarter < next_full < next_last_quarter < next_new:
            return 'Waxing Crescent'
        elif previous_first_quarter < next_full < next_last_quarter < next_new < next_first_quarter:
            return 'Waxing Gibbous'
        elif previous_full < next_last_quarter < next_new < next_first_quarter < next_full:
            return 'Waning Gibbous'
        elif previous_last_quarter < next_new < next_first_quarter < next_full < next_last_quarter:
            return 'Waning Crescent'

    def get_body_positions(observer, body):
        positions = []

        # test for always below horizon or always above horizon
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

    def get_sun_twilights(self,observer):
        results = []

        # remember entry observer horizon
        observer_horizon = observer.horizon

        # Twilights, their horizons and whether to use the centre of the Sun or not
        twilights = [('-6', True), ('-12', True), ('-18', True)]

        for twi in twilights:
            observer.horizon = twi[0]
            try:
                rising_setting = self.self.get_body_positions(observer,ephem.Sun(observer))
                results.append((rising_setting[0], rising_setting[2]))
            except ephem.AlwaysUpError:
                results.append(('n/a', 'n/a'))

        # reset observer horizon to entry
        observer.horizon = observer_horizon

        return results

    def get_polaris_data(self,observer):
        polaris_data = []

        j2000 = ephem.Date('2000/01/01 12:00:00')
        d = observer.date - j2000

        lon = rad2deg(float(repr(observer.lon)))

        utstr = observer.date.datetime().strftime("%H:%M:%S")
        ut = float(utstr.split(":")[0]) + float(utstr.split(":")[1])/60 + float(utstr.split(":")[2])/3600

        lst = 100.46 + 0.985647 * d + lon + 15 * ut
        lst = lst - int(lst / 360) * 360

        polaris = ephem.readdb("Polaris,f|M|F7,2:31:48.704,89:15:50.72,2.02,2000")
        polaris.compute()
        polaris_ra_deg = rad2deg(float(repr(polaris.ra)))

        # Polaris Hour Angle = LST - RA Polaris [expressed in degrees or 15*(h+m/60+s/3600)]
        pha = lst - polaris_ra_deg

        # normalize
        if pha < 0:
            pha += 360
        elif pha > 360:
            pha -= 360

        # append polaris hour angle
        polaris_data.append(pha)

        # append polaris next transit
        try:
            polaris_data.append(ephem.localtime( observer.next_transit(polaris) ).strftime("%H:%M:%S"))
        except (ephem.NeverUpError, ephem.AlwaysUpError):
            polaris_data.append('-')

        # append polaris alt
        polaris_data.append(polaris.alt)

        return polaris_data

    def get_gps(self):
        gps_data = []
        timeout = timedelta(seconds=10)
        loop_time = 1
        gps_start_time = datetime.utcnow()
        status = 'Trying GPS'

        gpsd_socket = gps3.GPSDSocket()
        gpsd_socket.connect()
        gpsd_socket.watch()
        data_stream = gps3.DataStream()

        for new_data in gpsd_socket:
            waiting_time = datetime.datetime.utcnow() - gps_start_time
            if waiting_time > timeout:
                raise gps_timeout("GPS timeout")
            if new_data:
                data_stream.unpack(new_data)
                if data_stream.TPV['lat'] != 'n/a' and int(data_stream.TPV['mode']) == 3:
                    gps_data.append(data_stream.TPV['lat'])
                    gps_data.append(data_stream.TPV['lon'])
                    gps_data.append(data_stream.TPV['alt'])
                    gps_data.append(data_stream.TPV['time'])
                    break
            else:
                sleep(loop_time)

        gpsd_socket.close()
        return gps_data

    def get_location(self):
        location = []
        try:
            gps_data = self.get_gps()
            latitude = "%s" % gps_data[0]
            longitude = "%s" % gps_data[1]
            elevation = "%.2f" % gps_data[2]
            city = 'GPS location'
            alias = 'GPS location'
            position_mode = 'gps'
            location.append(latitude)
            location.append(longitude)
            location.append(elevation)
            location.append(city)
            location.append(alias)
            location.append(position_mode)
        except gps_timeout:
            # no location data - loading defaults
            latitude = '120.212012'
            longitude = '30.208432'
            elevation = 0
            city = 'Hangzhou'
            alias = 'Demo location'
            position_mode = 'demo'
            location.append(latitude)
            location.append(longitude)
            location.append(elevation)
            location.append(city)
            location.append(alias)
            location.append(position_mode)

        return location

    def background_thread(self):
        while True:
            # update location
            location = self.get_location()

            # init observer
            home = ephem.Observer()

            # set geo position
            home.lat = location[0]
            home.lon = location[1]
            home.elevation = float(location[2])

            # update time
            t = datetime.datetime.utcnow()
            home.date = t

            polaris_data = self.get_polaris_data(home)

            astropanel_socketio.emit('celestialdata', {
            'latitude': "%s" % home.lat,
            'longitude': "%s" % home.lon,
            'elevation': "%.2f" % home.elevation,
            'city': location[3],
            'alias': location[4],
            'mode': location[5],
            'polaris_hour_angle': polaris_data[0],
            'polaris_next_transit': "%s" % polaris_data[1],
            'polaris_alt': "%.2f°" % degrees(polaris_data[2]),
            'moon_phase': "%s" % self.get_moon_phase(home),
            'moon_light': "%d" % ephem.Moon(home).phase,
            'moon_rise': "%s" % self.get_body_positions(home,ephem.Moon(home))[0],
            'moon_transit': "%s" % self.get_body_positions(home,ephem.Moon(home))[1],
            'moon_set': "%s" % self.get_body_positions(home,ephem.Moon(home))[2],
            'moon_az': "%.2f°" % degrees(ephem.Moon(home).az),
            'moon_alt': "%.2f°" % degrees(ephem.Moon(home).alt),
            'moon_ra': "%s" % ephem.Moon(home).ra,
            'moon_dec': "%s" % ephem.Moon(home).dec,
            'moon_new': "%s" % ephem.localtime(ephem.next_new_moon(t)).strftime("%Y-%m-%d %H:%M:%S"),
            'moon_full': "%s" % ephem.localtime(ephem.next_full_moon(t)).strftime("%Y-%m-%d %H:%M:%S"),
            'sun_at_start': self.get_sun_twilights(home)[2][0],
            'sun_ct_start': self.get_sun_twilights(home)[0][0],
            'sun_rise': "%s" % self.get_body_positions(home,ephem.Sun(home))[0],
            'sun_transit': "%s" % self.get_body_positions(home,ephem.Sun(home))[1],
            'sun_set': "%s" % self.get_body_positions(home,ephem.Sun(home))[2],
            'sun_ct_end': self.get_sun_twilights(home)[0][1],
            'sun_at_end': self.get_sun_twilights(home)[2][1],
            'sun_az': "%.2f°" % degrees(ephem.Sun(home).az),
            'sun_alt': "%.2f°" % degrees(ephem.Sun(home).alt),
            'sun_ra': "%s" % ephem.Sun(home).ra,
            'sun_dec': "%s" % ephem.Sun(home).dec,
            'sun_equinox': "%s" % ephem.localtime(ephem.next_equinox(t)).strftime("%Y-%m-%d %H:%M:%S"),
            'sun_solstice': "%s" % ephem.localtime(ephem.next_solstice(t)).strftime("%Y-%m-%d %H:%M:%S"),
            'mercury_rise': "%s" % self.get_body_positions(home,ephem.Mercury(home))[0],
            'mercury_transit': "%s" % self.get_body_positions(home,ephem.Mercury(home))[1],
            'mercury_set': "%s" % self.get_body_positions(home,ephem.Mercury(home))[2],
            'mercury_az': "%.2f°" % degrees(ephem.Mercury(home).az),
            'mercury_alt': "%.2f°" % degrees(ephem.Mercury(home).alt),
            'venus_rise': "%s" % self.get_body_positions(home,ephem.Venus(home))[0],
            'venus_transit': "%s" % self.get_body_positions(home,ephem.Venus(home))[1],
            'venus_set': "%s" % self.get_body_positions(home,ephem.Venus(home))[2],
            'venus_az': "%.2f°" % degrees(ephem.Venus(home).az),
            'venus_alt': "%.2f°" % degrees(ephem.Venus(home).alt),
            'mars_rise': "%s" % self.get_body_positions(home,ephem.Mars(home))[0],
            'mars_transit': "%s" % self.get_body_positions(home,ephem.Mars(home))[1],
            'mars_set': "%s" % self.get_body_positions(home,ephem.Mars(home))[2],
            'mars_az': "%.2f°" % degrees(ephem.Mars(home).az),
            'mars_alt': "%.2f°" % degrees(ephem.Mars(home).alt),
            'jupiter_rise': "%s" % self.get_body_positions(home,ephem.Jupiter(home))[0],
            'jupiter_transit': "%s" % self.get_body_positions(home,ephem.Jupiter(home))[1],
            'jupiter_set': "%s" % self.get_body_positions(home,ephem.Jupiter(home))[2],
            'jupiter_az': "%.2f°" % degrees(ephem.Jupiter(home).az),
            'jupiter_alt': "%.2f°" % degrees(ephem.Jupiter(home).alt),
            'saturn_rise': "%s" % self.get_body_positions(home,ephem.Saturn(home))[0],
            'saturn_transit': "%s" % self.get_body_positions(home,ephem.Saturn(home))[1],
            'saturn_set': "%s" % self.get_body_positions(home,ephem.Saturn(home))[2],
            'saturn_az': "%.2f°" % degrees(ephem.Saturn(home).az),
            'saturn_alt': "%.2f°" % degrees(ephem.Saturn(home).alt),
            'uranus_rise': "%s" % self.get_body_positions(home,ephem.Uranus(home))[0],
            'uranus_transit': "%s" % self.get_body_positions(home,ephem.Uranus(home))[1],
            'uranus_set': "%s" % self.get_body_positions(home,ephem.Uranus(home))[2],
            'uranus_az': "%.2f°" % degrees(ephem.Uranus(home).az),
            'uranus_alt': "%.2f°" % degrees(ephem.Uranus(home).alt),
            'neptune_rise': "%s" % self.get_body_positions(home,ephem.Neptune(home))[0],
            'neptune_transit': "%s" % self.get_body_positions(home,ephem.Neptune(home))[1],
            'neptune_set': "%s" % self.get_body_positions(home,ephem.Neptune(home))[2],
            'neptune_az': "%.2f°" % degrees(ephem.Neptune(home).az),
            'neptune_alt': "%.2f°" % degrees(ephem.Neptune(home).alt)
            })
            astropanel_socketio.sleep(10)

###########################################################################
"""

Astropanel 服务器，单独拆封出来
来自：Radek Kaczorek

"""
astropanel_server = Flask(__name__,static_folder=config.mainconfig["server"]["astropanel"]["config"]["static"],template_folder=config.mainconfig["server"]["astropanel"]["config"]["template"])
astropanel_socketio = SocketIO(astropanel_server)
astropanel_crfs = CSRFProtect()
astropanel_crfs.init_app(astropanel_server)
astropanel_run = astropanel()

thread = None

# Astropanel
@astropanel_server.route("/")
def astropanel():
    return render_template(config.assets["web"]["astropanel"])

@astropanel_socketio.on('/astropanel/connect')
def handle_connect():
	global thread
	if thread is None:
		thread = astropanel_socketio.start_background_task(target=astropanel_run.background_thread)

def run_astropanel():
    astropanel_socketio.run(app, host='127.0.0.1', port = 8626, debug=False)

###########################################################################