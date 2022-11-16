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

# #################################################################
#
# Focuser Info Class
#
# #################################################################

class FocuserInfo(object):
    """Focuser Info class for containing focuser information"""

    def get_dict(self) -> dict:
        """Return focuser information in a dictionary"""

        
# #################################################################
# 
# Base class for focuser control
#
# #################################################################

class Focuser(Device):
    """Focuser control class based on Device class"""

    def __init__(self) -> None:
        """Initial Class"""

    def __del__(self) -> None:
        """Delete Class"""

    def connect(self,params : dict) -> dict:
        """
            Connect to Focuser and finish all the initialization process
            连接电调并且完成所有的初始化
            @ params : {
                "count" : number of focuser # Default is 1
                "name" : string # To check if the focuser is you need
            }
        """
        return super().connect(params)     

    def disconnect(self) -> dict:
        """
            Disconnect from focuser and after execute this function we will lose connection with focuser.And should realize all the resources
            与电调断开连接，完成此步后就结束了任务，需要释放所有资源
        """
        return super().disconnect()

    def update_config(self) -> dict:
        """
            Update the configuration of the focuser . execute this function after "connect"
            更新电调配置，通常在连接成功后执行
        """
        return super().update_config()

    def set_config(self,params : dict) -> dict:
        """
            Set the configuration of the current Focuser
            设置电调参数
            @ params : {

            }
        """
        return super().set_config(params)

    def save_config(self) -> dict:
        """
            Save the configuration of the focuser . execute this function after "disconnect"
            保存电调配置，通常在断开连接后执行
        """
        return super().save_config()

    def refresh_info(self) -> dict:
        """
            Refresh the Focuser Information and return it to the function which called this function
            更新电调信息并且返回给调用此函数的函数
        """
        return super().refresh_info()

    def move(self,params : dict) -> dict:
        """
            Move the Focuser position 
            移动电调位置
            @ params : {
                "step" : int # step number
                "speed" : int # speed ? Will this be supported
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def moveto(self,params : dict) -> dict:
        """
            Move to the current you set position
            @ params : {
                "position" : int # position
                "speed" : int # speed ? Will this be supported
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def abort(self) -> dict:
        """
            Abort the current movement

        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def get_position(self) -> dict:
        """
            Get the current position of the current Focuser
            获取电调当前位置
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def get_temperature(self) -> dict:
        """
            Get the current temperature of the current Focuser
            获取电调当前温度
            Note: This function needs focuser support
            提示： 这个功能需要电调支持
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))