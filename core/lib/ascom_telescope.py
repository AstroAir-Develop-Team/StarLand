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

from core.lib.pyascom.telescope import Telescope
from core.lib.pyascom.exceptions import NotConnectedException,InvalidOperationException

from core.lib.socket import check_port_in_use

from core.lib.starlog import starlog

log = starlog(__name__)

import gettext
_ = gettext.gettext

@dataclass
class telescope_info():
    """Telescope info"""
    _connected = False
    _description = None

class ascom_telescope():
    """Telescope class based on ASCOM"""

    def __init__(self,device_number : int,host = "127.0.0.1",port = 11111,ipv6 = False) -> dict:
        self.info = telescope_info()
        url = host + ":" + str(port)
        if not check_port_in_use(url):
            log.loge(_("The remote server is not started. Please start it and try to connect again"))
            return self.return_message("error",_("The remote server is not started."),_("Please start it and try to connect again"))
        try:
            self.telescope = Telescope(address=url,device_number=device_number)
        except NotConnectedException as exp:
            log.loge(_("Failed to connect the telescope"))
            return self.return_message("error",_("Failed to connect the telescope"),_("GG"))

    def __del__(self) -> None:
        if self.info._connected:
            self.disconnect()

    def return_message(self,tpye : str,message : str,advice : str = "") -> dict:
        """Return message in dict format"""
        r = {
            "status" : tpye,
            "message" : message,
            "advice" : advice
        }
        return r

    def connect(self) -> dict:
        """Connect to telescope"""
        try:
            self.telescope.Connected = True
            self.info._connected = True
            self.info._description = self.telescope.Description
        except InvalidOperationException as exp:
            log.loge(_("Unable to connect the telescope, please check the connection"))
            return self.return_message("error",_("Unable to connect the telescope"),_("Please check the connection"))
        log.log(_("Telescope connected successfully"))
        return self.return_message("success",_("Telescope connected successfully"),"")

    def disconnect(self) -> dict:
        """Disconnect from telescope"""
        self.telescope.Connected = False
        self.info._connected = False
        self.info._description = None
        log.log(_("Successfully disconnected the telescope"))

    
