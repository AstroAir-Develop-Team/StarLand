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

from core.device.device import Device
from core.lib.starlog import starlog

log = starlog(__name__)

import gettext
_ = gettext.gettext

__api__ = "Filterwheel Basic API"
__api_version__ = "1.0.0"
__copyright__ = "Max Qian"
__license__ = "GPL3"

# #########################################################################
# 
# Filterwheel Info Class
#
# #########################################################################

class FilterwheelInfo(object):
    """Filterwheel info class"""

    """Basic Info"""
    _address = None # For ASCOM & INDI
    _name = None
    _api_version : str
    _description : str
    _id : int
    _timeout = 5
    _config_file : str

    """Property Info"""
    _filter_info : list

    """Current Info"""
    _current_position : int
    _offset_filter : list

    """Status Info"""
    _is_connected = False
    _is_operating = False

    def get_dict(self) -> dict:
        """Get the filterwheel info and return in dict format"""
        r = {
            "address": self._address,
            "api_version" : self._api_version,
            "description": self._description,
            "id": self._id,
            "timeout" : self._timeout,
            "properties" : {
                "filter" : self._filter_info
            },
            "current" : {
                "current_position" : self._current_position,
                "offset_filter" : self._offset_filter
            },
            "status" : {
                "is_connected" : self._is_connected
            }
        }
        return r


# #########################################################################
# 
# Basic Filterwheel Class
#
# #########################################################################

class BasicFilterwheel(Device):
    """Basic Filterwheel class"""

    # #########################################################################
    #
    # From Device Class | ????????????????????????
    #
    # #########################################################################

    def __init__(self) -> None:
        """Construct | ????????????"""

    def __del__(self) -> None:
        """Delete | ????????????"""

    def connect(self, params: dict) -> dict:
        """
            Connect to filterwheel and after success we can do anything else
            ??????????????????????????????????????????????????????????????????????????????????????????????????????
            @ params : {
                "count": int # the number of filterwheel
                "name" : string # the name of the filterwheel
            }
            @ return : {
                "status" : "success","error","warning","debug"
                "message": str
                "params" : {
                    "id" : int # the id of the device
                    "name" str # the name of the device
                }
            }
        """
        return super().disconnect(params)

    def disconnect(self, params: dict) -> dict:
        """
            Disconnect from the filterwheel after disconnection we can do nothing with filterwheel
            ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
            @ return : {
                "status" : "success","error","warning","debug",
                "message" : str,
                "params" : None
            }
        """
        return super().disconnect(params)

    def return_message(self, status: str, message: str, params={}) -> dict:
        """Return message just use parent class | ????????????"""
        return super().return_message(status, message, params)

    def update_config(self) -> dict:
        """
            Update filterwheel configuration and storage settings in filterwheel_Info\n
            Run this function when first initialize the filterwheel\n
            ?????????????????????????????????????????????????????????????????????????????????FilterwheelInfo???\n
            ???????????????????????????????????????\n
            @ params : None
            @ return : {
                "status" : "success","error","warning","debug",
                "message" : str,
                "params" : {
                    "info" : FilterwheelInfo object
                }
            }
            Note : This function needs to be called
        """
        return super().update_config()

    def load_config(self, params: dict) -> dict:
        """
            Load the configuration from file
            ????????????????????????
            @ params : {
                "filename" : filename
                "path" : path
            }
            @ return : {
                "status" : "success","error","warning","debug",
                "message" : str,
                "params" : configuration from file
            }
        """
        return super().load_config(params)

    def save_config(self) -> dict:
        """
            Save the configuration from filterwheel_Info as a JSON file
            ???filterwheel_Info??????????????????????????????JSON?????????
            @ params : None
            @ return : {
                "status" : "success","error","warning","debug",
                    # Success : save the configuration to file successfully
                    # Error : save the configuration to file with error
                    # Warning : save the configuration to file with warning
                    # Debug : save the configuration to file in debug mode
                "message" : str,
                "params" : None
            }
        """
        return super().save_config()

    def refresh_info(self) -> dict:
        """
            Refresh the Info from filterwheel_Info, other functions get information through this function
            ???????????????????????????????????????
            @ params : None
            @ return : {
                "status" : "success","error","warning","debug",
                    # Success : refresh filterwheel info successfully
                    # Error : refresh filterwheel info with error
                    # Warning : refresh filterwheel info with warning
                    # Debug : refresh filterwheel info in debug mode
                "message" : str,
                "params" : {
                    "info" : FilterwheelInfo object
                }
            }
        """
        return super().refresh_info()

    # #################################################################
    # 
    # Filterwheel Class | ???????????????????????????
    #
    # #################################################################

    # #############################################################
    # Goto functions
    # #############################################################

    def goto(self, params : dict) -> dict:
        """
            Goto the specified position | ??????????????????????????????
            Args:
                {
                    "position" : int 
                }
            Return: 
                {
                    "status" : "success","error","warning","debug"
                    "message" : "Goto the specified position successfully" # success
                                "Faild to goto the specified position" # error
                                "Goto the specified position with a warning" # warning
                    "params" : {
                        "info" : FilterwheelInfo object
                    }
                }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def get_position(self) -> dict:
        """
            Get the current position of the current Filterwheel | ???????????????????????????
            Return:
                {
                    "status" : "success","error","warning","debug",
                    "message" : str
                    "params" : {
                        "position" : int
                    }
                }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def get_position_offset(self) -> dict:
        """
            Get the offset of the each filter | ?
            Return:
                {
                    "status" : "success","error","warning","debug",
                    "message" : str,
                    "params" : {
                        "offset" : list
                    }
                }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))
