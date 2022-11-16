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
from core.device.device import Device
from core.lib.starlog import starlog

log = starlog(__name__)

import gettext
_ = gettext.gettext

# #################################################################
#
# CameraInfo class used to contain information about camera
#
# #################################################################

@dataclass
class CameraInfo():

    def get_dict(self) -> dict:
        """Return camera infomation in a dictionary"""

    

# #################################################################
# 
# Base class for camera control
#
# #################################################################

class Camera(Device):
    """
    Base class for camera control based on Device class
    """

    # #################################################################
    #
    # Base Device class
    #
    # #################################################################

    def __init__(self) -> None:
        """Initialize"""

    def __del__(self) -> None:
        """Destructor"""

    def connect(self,params : dict) -> dict:
        """
            Connect to camera
            Args:
                params (dict): camera parameters
        """

    def disconnect(self) -> dict:
        """
            Disconnect from camera
            Args:
                None
        """

    def update_config(self) -> dict:
        """
            Update camera configuration
            Args:
                None
            Return:
                Camera_Info object
        """

    def set_config(self,params : dict) -> dict:
        """
            Set camera configuration
            Args:
                params (dict): camera parameters
            Return:
                Status about set_config
        """
        
    def save_config(self) -> dict:
        """
            Save camera configuration
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : None
            }
        """

    def refresh_info(self) -> dict:
        """
            Refresh camera information
            Args:
                None
            @ return : {
                "status": "success","error","warning","debug"
                "message" : str
                "params" : {
                    "info": CameraInfo object
                }
            }
        """

    # #############################################################
    #
    # Camera control
    #
    # #############################################################

    # #############################################################
    # Exposure functions
    # #############################################################

    def start_exposure(self,params : dict) -> dict:
        """
            Start exposure | 开始曝光
            Args:
                params (dict): camera parameters
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {

                }
            }
            Note : Must make sure camera is safely configured
        """

    def abort_exposure(self) -> dict:
        """
            Abort exposure | 停止曝光
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params: None
            }
        """

    def get_exposure_status(self) -> dict:
        """
            Get exposure status | 获取曝光信息
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "status" : boolean # True if camera is exposuring
                    "error" : str # None if success
                }
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def get_exposure_data(self) -> dict:
        """
            Get exposure data | 获取图像数据
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "data" : {
                        "img" : bufferarray
                        "width" : int
                        "height" : int
                        "size" : int
                        "bayer" : {
                            "enable" : boolean
                            "mode" : str # Like RGB or RGBA
                        }
                    }
                }
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def save_image(self, params : dict) -> dict:
        """
            Save exposure image
            Args:
                params (dict): image parameters
                {
                    "filename": str
                    "type": str # Like FITS or JPEG or TIFF
                    "img" : bufferarray
                    "width" : int
                    "height" : int
                    "size" : int
                    "bayer" : {
                        "enable" : boolean
                        "mode" : str # Like RGB or RGBA
                    },
                    "info" : list # For Fits title
                }
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : None
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))
    
    # #############################################################
    # Video functions
    # #############################################################

    def start_video(self,params : dict) -> dict:
        """
            Start video | 开始视频拍摄
            Args:
                params (dict): camera parameters
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {

                }
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))
    
    def abort_video(self) -> dict:
        """
            Abort the video capture | 停止视频拍摄
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params: None
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def get_video_status(self) -> dict:
        """
            Get video capture status | 获取视频录制状态
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "drop_frames" : int
                    "size" : int
                    "fps" : int
                }
            }
            Note : This function is not surely can be called
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def get_video_data(self) -> dict:
        """
            Get video data | 获取视频数据
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "drop_frames" : int
                    "size" : int
                    "data" : bufferarray
                }
            }
            TODO : I'm not sure how to save a video file
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def save_video(self,params : dict) -> dict:
        """
            Save video | 开始视频拍摄
            Args:
                params (dict): video parameters
                {
                    "filename": str
                    "type": str # Like MP4
                    "fps": int
                }
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : None
            }
            TODO : What parameters does saving video need?
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    # #############################################################
    # Cooler functions
    # #############################################################

    def cool(self,params : dict) -> dict:
        """
            Cool on/off | 开始或停止制冷 
            Args:
                params (dict): camera parameters
                {
                    "enable" : boolean
                }
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : None
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def get_cool_status(self) -> dict:
        """
            Get the status of the cooler
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "enable" : boolean
                }
            }
            Note : This is only available for the cooler camera !
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def get_temperature(self) -> dict:
        """
            Get camera temperature | 获取相机温度
            Note : This is available for almost all cameras
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "temperature" : float
                }
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    def set_temperature(self,params : dict) -> dict:
        """
            Set camera temperature | 设置相机温度
            Note : This is available for almost all cameras
            Args:
                params (dict): camera parameters
                {
                    "temperature" : float
                }
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : None
            }
            Note : This is only available for cooler cameras !
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    # #############################################################
    # Information functions
    # #############################################################

    @property
    def gain(self) -> dict:
        """
            Get camera gain | 获取相机增益
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "gain" : float
                }
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))
    
    @gain.setter
    def gain(self,params : dict) -> dict:
        """
            Set camera gain | 设置相机增益
            Args:
                params (dict): gain parameters
                {
                    "gain" : float
                }
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : None
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    @property
    def offset(self) -> dict:
        """
            Get camera offset | 获取相机偏置
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "offset" : float
                }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))
    
    @offset.setter
    def offset(self,params : dict) -> dict:
        """
            Set the offset | 设置相机偏置
            Args:
                params (dict): offset parameters
                {
                    "offset" : float
                }
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : None
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    @property
    def gamma(self) -> dict:
        """
            Get camera gamma | 获取相机伽马值
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "gamma" : float
                }
            }
            Note : This function need camera support , ASI camera is surely support.
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    @gamma.setter
    def gamma(self,params : dict) -> dict:
        """
            Set camera gamma | 设置相机伽马值
            Args:
                params (dict): gamma parameters
                {
                    "gamma" : int
                }
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : None
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    @property
    def binning(self) -> dict:
        """
            Get the binning mode | 获取像素合成模式
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "binning" : int # 1 or 2 or 4
                    Note : If bin is bigger than 4 , everyone will thank you
                }
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    @binning.setter
    def binning(self,params : dict) -> dict:
        """
            Set the binning mode | 设置像素合成
            Args:
                params (dict): binning parameters
                {
                    "binning" : int # 1 or 2 or 4
                }
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : None
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    @property
    def roi(self) -> dict:
        """
            Get the roi | 获取相机画幅
            Args:
                None
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : {
                    "roi" : {
                        "start_x" : int
                        "start_y" : int
                        "height" : int
                        "width" : int
                        "is_filp" : boolean # This need camera support
                    }
                }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

    @roi.setter
    def roi(self, params : dict) -> dict:
        """
            Set the roi | 设置相机画幅
            Args:
                params (dict): roi parameters
                {
                    "roi" : {
                        "start_x" : int
                        "start_y" : int
                        "height" : int
                        "width" : int
                        "is_filp" : boolean # This need camera support
                    }
                }
            @ return : {
                "status" : "success","error","warning","debug"
                "message" : str
                "params" : None
            }
        """
        log.loge(_("The parent function should not be called"))
        return self.return_message("error",_("The parent function should not be called"))

