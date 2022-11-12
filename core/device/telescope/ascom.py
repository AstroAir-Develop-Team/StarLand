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

from time import sleep
from requests import exceptions
import ephem

from core.lib.pyascom.exceptions import (DriverException,
                                         NotConnectedException,
                                         NotImplementedException,
                                         ParkedException)
from core.lib.pyascom.telescope import Telescope
from core.lib.starlog import starlog

log = starlog(__name__)

import gettext

import config

_ = gettext.gettext

class telescope_info():
    """Telescope Info from ASCOM"""
    _address = None # Address
    _api_version = None # API version
    _description = None # 赤道仪描述
    _coordinates_type = None # 赤道仪坐标类型

    _can_park = False       # 能否归为 from CanPark
    _can_unpark = False     # 能否取消归为 from CanUnpark
    _can_home = False       # 能否回家 from CanFindHome
    _can_guide = False      # 能否导星 from CanPulseGuide
    _can_tracking = False   # 能否跟踪 from CanTrack

    _can_slewing = False    # 能否转动 from CanSlewing
    _can_slewing_async = False      # 能否校准 from CanSlewingAsync

    _can_slewing_azalt = False       # 能否根据地平经纬度转动 from CanSlewAzalt
    _can_slewing_azalt_async = False # 能否根据地坪经纬度校准 from CanSlewAzaltAsync

    _can_set_park = False       # 能否设置归位位置
    _can_set_guide_rate = False # 能否设置导星速率
    _can_set_ra_rate = False    # 能否设置RA转动速度
    _can_set_dec_rate = False   # 能否设置DEC转动速度

    _is_guiding = False # 是否正在导星 from IsPulseGuiding
    _guide_ra_rate : float  # RA导星速率  from GuideRateRightAscension
    _guide_dec_rate : float # DEC导星速率 from GuideRateDeclination

    _is_tracking = False # 是否正在跟踪 from Tracking
    _tracking_ra_rate : float # RA跟踪速率 from RightAscensionRate
    _tracking_dec_rate : float # DEC跟踪速率 from DeclinationRate

    _is_slewing = False # 是否在转动
    _target_ra = 0.0 # 当前RA坐标
    _target_dec = 0.0 # 当前DEC坐标
    _convert_ra : str # 转化后的RA坐标
    _convert_dec : str # 转化后的DEC坐标
    _target_az = 0.0 # 当前AZ坐标
    _target_alt = 0.0 # 当前ALT坐标
    _convert_az = 0.0 # 转化后的AZ坐标
    _convert_alt = 0.0 # 转化后的ALT坐标

    _is_parked = False

    def return_dict(self) -> dict:
        """Return a dictionary"""
        dic = {
            "ADDRESS": self._address,
            "API_VERSION" : self._api_version,
            "Description": self._description,
            "Coordinates_Type" : self._coordinates_type,
            "Can" : {
                "Park" : self._can_park,
                "Unpark" : self._can_unpark,
                "Home" : self._can_home,
                "Guide" : self._can_guide,
                "Tracking" : self._can_tracking
            },
            "CanSet" : {
                "GuideRate" : self._can_set_guide_rate,
                "Park" : self._can_set_park,
                "RARate" : self._can_set_ra_rate,
                "DECRate" : self._can_set_dec_rate
            },
            "Slewing" : {
                "Can" : self._can_slewing,
                "Async" : self._can_slewing_async,
                "CanAzAlt" : self._can_slewing_azalt,
                "CanAzAltAsync" : self._can_slewing_azalt_async,
                "IsSlewing" : self._is_slewing
            },
            "Tracking" : {
                "IsTracking" : self._is_tracking,
                "TrackingRARate"  : self._tracking_ra_rate,
                "TrackingDECRate" : self._tracking_dec_rate,
            },
            "Guiding" : {
                "IsGuiding" : self._is_guiding,
                "GuideRARate" : self._guide_ra_rate,
                "GuideDecRate" : self._guide_dec_rate
            },
            "Target" : {
                "RA" : self._target_ra,
                "DEC" : self._target_dec,
                "ConvertRA" : self._convert_ra,
                "ConvertDEC" : self._convert_dec,
                "Az" : self._target_az,
                "Alt" : self._target_alt,
                "ConvertAz" : self._convert_az,
                "ConvertAlt" : self._convert_alt,
            }
        }
        return dic

class telescope():
    """Telescope based on ASCOM"""

    def __init__(self) -> None:
        """Construct"""
        self.info = telescope_info()

    def __del__(self) -> None:
        """delete"""

    def return_message(self,tpye : str,message : str,advice : str = "") -> dict:
        """Return message in dict format"""
        r = {
            "status" : tpye,
            "message" : message,
            "advice" : advice
        }
        return r

    def connect(self, host = "127.0.0.1", port = "11111",device_number=0) -> dict:
        """
        Connect to the specified Telescope
        @params
            @host : host address that will be used
            @port : port number that will be used
            @device_number : device number default value is 0

        @return : dict
            @status : status code
            @message : message
            @advice : advice
        """
        try:
            self.device = Telescope(host + ':' + port,device_number)
            self.device.Connected = True
        except DriverException as exception:
            log.loge(_("Failed to connect to telescope , error: %s"), exception)
            return self.return_message("error",_("Failed to connect to Telescope"),_("try again"))
        except exceptions.ConnectionError as exception:
            log.loge(_(f"Remote connection error: {exception}"))
            return self.return_message("error",_("Remote connection error"),_("try again"))
        log.log(_("Connected to telescope successfully"))

        res = self.update_telescope_configuration()
        if res.get("status") != "success":
            return res

        return self.return_message("success",_("Connected to Telescope successfully"),"")

    def disconnect(self) -> dict:
        """
        Disconnect
        @return: dict
            @status: status code
            @message: message
            @advice: advice
        """
        try:
            self.device.Connected = False
        except DriverException as e:
            log.loge(_("Failed to disconnect from telescope , error : %s"),e)
            return self.return_message("error",_("Failed to disconnect from Telescope"),_("Try again"))
        except exceptions.ConnectionError as exception:
            log.loge(_(f"Remote connection error: {exception}"))
            return self.return_message("error",_("Remote connection error"),_("try again"))
        log.log(_("Disconnect from Telescope successfully"))
        return self.return_message("success",_("Disconnect from Telescope successfully"),"")

    def update_telescope_configuration(self) -> dict:
        """Update the Telescope configuration"""
        try:
            self.info._address = self.device.address
            self.info._api_version = self.device.api_version
            self.info._description = self.device.Description

            self.info._coordinates_type = self.device.EquatorialSystem.value
            self.updatecoordinates()

            self.info._can_park = self.device.CanPark
            self.info._can_unpark = self.device.CanUnpark
            self.info._can_home = self.device.CanFindHome
            self.info._can_guide= self.device.CanPulseGuide
            self.info._can_tracking = self.device.CanSetTracking

            self.info._can_slewing = self.device.CanSlew
            self.info._can_slewing_async = self.device.CanSlewAsync
            self.info._can_slewing_azalt = self.device.CanSlewAltAz
            self.info._can_slewing_azalt_async = self.device.CanSlewAltAzAsync
            
            self.info._can_set_park = self.device.CanSetPark
            self.info._can_set_dec_rate = self.device.CanSetDeclinationRate
            self.info._can_set_ra_rate = self.device.CanSetRightAscensionRate
            self.info._can_set_guide_rate = self.device.CanSetGuideRates

            self.info._is_guiding = self.device.IsPulseGuiding
            self.info._guide_ra_rate = self.device.GuideRateRightAscension
            self.info._guide_dec_rate = self.device.GuideRateDeclination

            self.info._is_tracking = self.device.Tracking
            self.info._tracking_ra_rate = self.device.RightAscensionRate
            self.info._tracking_dec_rate = self.device.DeclinationRate

            self.info._target_ra = self.device.RightAscension
            self.info._target_dec = self.device.Declination

        except NotConnectedException as exception:
            log.loge(_("Telescope hadn't connected,please connect before continuing"))
            return self.return_message("error",_("Telescope had not connected"),_("Connected before continuing"))
        except DriverException as exception:
            log.loge(_("Could not get device information for telescope"))
            return self.return_message("error",_("Could not get device information"),_("Try again"))
        except exceptions.ConnectionError as exception:
            log.loge(_(f"Remote connection error: {exception}"))
            return self.return_message("error",_("Remote connection error"),_("try again"))
        
        log.log(_("Update Telescope configuration successfully"))
        return self.return_message("success",_("Update Telescope configuration successfully"),"")

    def slew(self,params : dict) -> dict:
        """
        Slewing to coordinates
        @params : {
            "J2000": boolean # for coordinates convert
            "RA" : string # target ra coordinate
            "DEC" : string # target dec coordinate
        }
        """
        if not self.info._can_tracking:
            log.loge(_("Telescope had no tracking mode and could not use slewing function"))
            return self.return_message("error",_("Failed to slew"),_("Change a telescope"))
        coord = []
        if params.get("J2000") is True:
            """Convert J2000 coordinates to JNow coordinates"""
            coord = self.convert_J2000_to_JNow(params.get("RA"),params.get("DEC"))
        else:
            coord = [params.get("RA"),params.get("DEC")]
        # 切换至跟踪模式，准备执行Goto
        try:
            self.device.Tracking = True
        except NotImplementedException as exception:
            log.loge(_(f"Telescope slew error : {exception}"))
            return self.return_message("error",_("Telescope slew error"),_("No tracking mode available"))
        except NotConnectedException as exception:
            log.loge(_("Telescope hadn't connected,please connect before continuing"))
            return self.return_message("error",_("Telescope had not connected"),_("Connected before continuing"))
        except DriverException as exception:
            log.loge(_(f"Failed to start tracking , error : {exception}"))
            return self.return_message("error",_("Failed to start tracking"),_("Try again"))
        except exceptions.ConnectionError as exception:
            log.loge(_(f"Remote connection error: {exception}"))
            return self.return_message("error",_("Remote connection error"),_("try again"))
        
        if not self.info._can_slewing_async:
            log.loge(_("Telescope had no async mode available"))
            self.device.Tracking = False
            return self.return_message("error",_("Telescope had no async mode available"),_("Change a Telescope"))

        log.log(_(f"Start slewing to {coord}"))
        self.info._is_slewing = True
        try:
            self.device.SlewToCoordinatesAsync(coord[0], coord[1])
            log.log(_("Waiting for telescope slewing to complete"))
        except ParkedException as exception:
            log.loge(_("Telescope had already parked"))
            self.info._is_slewing = False
            return self.return_message("error",_("Telescope had already parked"),_("Unpark"))
        
        while(self.device.Slewing):
            sleep(1)
        
        log.log(_(f"Successfully slew to coordinates [params.get('RA',params.get('DEC')]"))
        self.info._is_slewing = False
        self.device.Tracking = False
        return self.return_message("success",_("Telescope slew successfully"),"")

    def abort_slew(self) -> dict:
        """Abort Slewing"""
        if not self.info._can_slewing:
            log.loge(_("Telescope have no slewing function available"))
            return self.return_message("error",_("Telescope have no slewing function available"),_("GG"))
        if not self.info._is_slewing:
            log.logw(_("Telescope is not slewing , please do not execute this command"))
            return self.return_message("warning",_("Telescope is not slewing"),"Please do not execute this command")
        try:
            self.device.Slewing = False
        except NotConnectedException as exception:
            log.loge(_("Telescope hadn't connected,please connect before continuing"))
            return self.return_message("error",_("Telescope had not connected"),_("Connected before continuing"))
        except DriverException as exception:
            log.loge(_(f"Error abort slewing , error : {exception}"))
            return self.return_message("error",_("Error abort slewing"),_("Try again"))
        log.log(_("Abort slewing successfully"))
        self.info._is_slewing = False
        return self.return_message("success",_("Abort slewing successfully"),"")

    def Park(self,timeout = 5) -> dict:
        """Park"""
        if self.info._is_slewing:
            log.logw(_("Telescope is still slewing,waiting for final"))
            self.abort_slew()
            while self.info._is_slewing:
                sleep(1)
        if self.info._is_tracking:
            log.logw(_("Telescope is still tracking,waiting for final"))
            # TODO: abort tracking
        log.log(_("Attempting to park telescope"))
        try:
            self.device.Park(True)
        except NotConnectedException as exception:
            log.loge(_("Telescope hadn't connected,please connect before continuing"))
            return self.return_message("error",_("Telescope had not connected"),_("Connected before continuing"))
        except DriverException as exception:
            log.loge(_(f"Error park telescope , error : {exception}"))
            return self.return_message("error",_("Error when park telescope"),_("Try again"))
        log.log(_("Waiting for telescope parked"))
        time = 0
        while not self.device.AtPark and time <= int(timeout):
            sleep(1)
            time += 1
        if not self.device.AtPark and time >= int(timeout):
            log.loge(_("Timeout while waiting for telescope parking"))
            return self.return_message("error",_("Timeout while waiting for telescope parking"),_("Unable to"))
        log.log(_("Telescope parked"))
        self.info._is_parked = True
        return self.return_message("success",_("Telescope parked successfully"),"")
        
    def unpark(self) -> dict:
        """Unpark"""
        if not self.is_parked:
            log.loge(_("Telescope isn't parked , please do not execute this command"))
            return self.return_message("error",_("Telescope isn't parked"),_("Please do not execute this command"))
        try:
            self.device.Unpark()
        except NotConnectedException as exception:
            log.loge(_("Telescope hadn't connected,please connect before continuing"))
            return self.return_message("error",_("Telescope had not connected"),_("Connected before continuing"))
        except DriverException as exception:
            log.loge(_(f"Error unpark telescope ,error : {exception}"))
            return self.return_message("error",_("Error when unpark telescope"),_("Try again"))
        self.info._is_parked = False
        log.log(_("Unpark telescope successfully"))
        return self.return_message("success",_("Unpark telescope successfully"),"")

    def updatecoordinates(self) -> dict:
        """Update coordinates"""
        try:
            self.info._target_ra = self.device.RightAscension
            self.info._target_dec = self.device.Declination
            self.info._target_az = self.device.Azimuth
            self.info._target_alt = self.device.Altitude
        except NotConnectedException as exception:
            log.loge(_(f"Telescope hadn't connected,please connect before continuing , error : {exception}"))
            return self.return_message("error",_("Telescope had not connected"),_("Connected before continuing"))
        except DriverException as exception:
            log.loge(_(f"Could not update coordinates for telescope , error : {exception}"))
            return self.return_message("error",_("Could not get device information"),_("Try again"))
        except exceptions.ConnectionError as exception:
            log.loge(_(f"Remote connection error: {exception}"))
            return self.return_message("error",_("Remote connection error"),_("Start again"))
        
        def convert_coordinates(coord) -> str:
            """Convert coordinates for people better to read"""
            coord_h = int(coord)
            coord_m = int((coord - coord_h) * 60)
            coord_s = int((coord - coord_h - coord_m / 60) * 3600)
            coord_h,coord_m,coord_s = map(str,[coord_h,coord_m,coord_s])
            return coord_h + ":" + coord_m + ":" + coord_s

        self.info._convert_ra = convert_coordinates(self.info._target_ra)
        self.info._convert_dec = convert_coordinates(self.info._target_dec)
        self.info._convert_az = convert_coordinates(self.info._target_az)
        self.info._convert_alt = convert_coordinates(self.info._target_alt)
        
        log.log(_("Refresh telescope coordinates successfully"))
        return self.return_message("success",_("Update Telescope coordnaties successfully"),"")

    def convert_J2000_to_JNow(self,ra_coord : str,dec_coord : str) -> list:
        """
        Convert a J2000 coordinates to a JNow coordinates
        @ra_coord : RA J2000 coordinates ; format "xx:xx:xx"
        @dec_coord : DEC J2000 coordinates ; format "xx:xx:xx" ; Must with +/-
        @return : list of JNow coordinates ; format ["xx:xx:xx", "xx:xx:xx"]
        """
        l = []
        """TODO: When DEC is negative number what should I do here"""

        center_J2000 = ephem.Equatorial(ra_coord,dec_coord,epoch = ephem.J2000)
        center_JNow = ephem.Equatorial(center_J2000, epoch=ephem.now())
        
        ra_h,ra_m,ra_s = str(center_JNow.ra).split(":")
        ra_s = str(int(round(float(ra_s))))
        ra = ra_h + ":" + ra_m + ":" + ra_s        
        
        dec_h,dec_m,dec_s = str(center_JNow.dec).split(":")
        dec_s = str(int(round(float(dec_s))))
        dec = dec_h + ":" + dec_m + ":" + dec_s

        return [ra,dec]
    
    def convert_coordinates_h_to_s(self,coordinates : str) -> str | None:
        """Convert coordinates from hourangle to string"""
        if not isinstance(coordinates,str):
            log.loge(_(f"Unknown coordinates type: {coordinates}"))
            return 
        coord_h,coord_m,coord_s = map(int,coordinates.split(":"))
        coord = coord_h + coord_m / 60 + coord_s / 3600
        return "%.14f"%coord
