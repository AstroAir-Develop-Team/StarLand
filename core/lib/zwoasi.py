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
the Free Software Foundation, Inctypes., 51 Franklin Street, Fifth Floor,
Boston, MA 02110-1301, USA.

"""

import ctypes
from dataclasses import dataclass
import os
import sys

from core.lib.exceptions import ZWO_IOError
from core.lib.starlog import starlog

log = starlog(__name__)

# ASI_BAYER_PATTERN
ASI_BAYER_RG = 0
ASI_BAYER_BG = 1
ASI_BAYER_GR = 2
ASI_BAYER_RB = 3

# ASI_IMGTYPE
ASI_IMG_RAW8 = 0
ASI_IMG_RGB24 = 1
ASI_IMG_RAW16 = 2
ASI_IMG_Y8 = 3
ASI_IMG_END = -1

# ASI_GUIDE_DIRECTION
ASI_GUIDE_NORTH = 0
ASI_GUIDE_SOUTH = 1
ASI_GUIDE_EAST = 2
ASI_GUIDE_WEST = 3

ASI_GAIN = 0
ASI_EXPOSURE = 1
ASI_GAMMA = 2
ASI_WB_R = 3
ASI_WB_B = 4
ASI_BRIGHTNESS = 5
ASI_OFFSET = 5
ASI_BANDWIDTHOVERLOAD = 6
ASI_OVERCLOCK = 7
ASI_TEMPERATURE = 8  # return 10*temperature
ASI_FLIP = 9
ASI_AUTO_MAX_GAIN = 10
ASI_AUTO_MAX_EXP = 11
ASI_AUTO_MAX_BRIGHTNESS = 12
ASI_HARDWARE_BIN = 13
ASI_HIGH_SPEED_MODE = 14
ASI_COOLER_POWER_PERC = 15
ASI_TARGET_TEMP = 16  # not need *10
ASI_COOLER_ON = 17
ASI_MONO_BIN = 18  # lead to less grid at software bin mode for color camera
ASI_FAN_ON = 19
ASI_PATTERN_ADJUST = 20

# ASI_CAMERA_MODE
ASI_MODE_NORMAL = 0 
ASI_MODE_TRIG_SOFT_EDGE = 1
ASI_MODE_TRIG_RISE_EDGE = 2
ASI_MODE_TRIG_FALL_EDGE = 3
ASI_MODE_TRIG_SOFT_LEVEL = 4
ASI_MODE_TRIG_HIGH_LEVEL = 5
ASI_MODE_TRIG_LOW_LEVEL = 6
ASI_MODE_END = -1

# ASI_TRIG_OUTPUT
ASI_TRIG_OUTPUT_PINA = 0
ASI_TRIG_OUTPUT_PINB = 1
ASI_TRIG_OUTPUT_NONE = -1

# ASI_EXPOSURE_STATUS
ASI_EXP_IDLE = 0
ASI_EXP_WORKING = 1
ASI_EXP_SUCCESS = 2
ASI_EXP_FAILED = 3

# Mapping of error numbers to exceptions. Zero is used for success.
zwo_errors = [None,
              ZWO_IOError('Invalid index', 1),
              ZWO_IOError('Invalid ID', 2),
              ZWO_IOError('Invalid control type', 3),
              ZWO_IOError('Camera closed', 4),
              ZWO_IOError('Camera removed', 5),
              ZWO_IOError('Invalid path', 6),
              ZWO_IOError('Invalid file format', 7),
              ZWO_IOError('Invalid size', 8),
              ZWO_IOError('Invalid image type', 9),
              ZWO_IOError('Outside of boundary', 10),
              ZWO_IOError('Timeout', 11),
              ZWO_IOError('Invalid sequence', 12),
              ZWO_IOError('Buffer too small', 13),
              ZWO_IOError('Video mode active', 14),
              ZWO_IOError('Exposure in progress', 15),
              ZWO_IOError('General error', 16),
              ZWO_IOError('Invalid mode', 17)
              ]

class _ASI_CAMERA_INFO(ctypes.Structure):
    """ASI camera info"""
    _fields_ = [
        ('Name', ctypes.c_char * 64),
        ('CameraID', ctypes.c_int),
        ('MaxHeight', ctypes.c_long),
        ('MaxWidth', ctypes.c_long),
        ('IsColorCam', ctypes.c_int),
        ('BayerPattern', ctypes.c_int),
        ('SupportedBins', ctypes.c_int * 16),
        ('SupportedVideoFormat', ctypes.c_int * 8),
        ('PixelSize', ctypes.c_double),  # in um
        ('MechanicalShutter', ctypes.c_int),
        ('ST4Port', ctypes.c_int),
        ('IsCoolerCam', ctypes.c_int),
        ('IsUSB3Host', ctypes.c_int),
        ('IsUSB3Camera', ctypes.c_int),
        ('ElecPerADU', ctypes.c_float),
        ('BitDepth', ctypes.c_int),
        ('IsTriggerCam', ctypes.c_int),

        ('Unused', ctypes.c_char * 16)
    ]
    
    def get_dict(self) -> dict:
        r = {}
        for k, _ in self._fields_:
            v = getattr(self, k)
            if sys.version_info[0] >= 3 and isinstance(v, bytes):
                v = v.decode()
            r[k] = v
        del r['Unused']
        
        r['SupportedBins'] = []
        for i in range(len(self.SupportedBins)):
            if self.SupportedBins[i]:
                r['SupportedBins'].append(self.SupportedBins[i])
            else:
                break
        r['SupportedVideoFormat'] = []
        for i in range(len(self.SupportedVideoFormat)):
            if self.SupportedVideoFormat[i] == ASI_IMG_END:
                break
            r['SupportedVideoFormat'].append(self.SupportedVideoFormat[i])

        for k in ('IsColorCam', 'MechanicalShutter', 'IsCoolerCam',
                  'IsUSB3Host', 'IsUSB3Camera'):
            r[k] = bool(getattr(self, k))
        return r


class _ASI_CONTROL_CAPS(ctypes.Structure):
    _fields_ = [
        ('Name', ctypes.c_char * 64),
        ('Description', ctypes.c_char * 128),
        ('MaxValue', ctypes.c_long),
        ('MinValue', ctypes.c_long),
        ('DefaultValue', ctypes.c_long),
        ('IsAutoSupported', ctypes.c_int),
        ('IsWritable', ctypes.c_int),
        ('ControlType', ctypes.c_int),
        ('Unused', ctypes.c_char * 32),
        ]

    def get_dict(self) -> dict:
        r = {}
        for k, _ in self._fields_:
            v = getattr(self, k)
            if sys.version_info[0] >= 3 and isinstance(v, bytes):
                v = v.decode()
            r[k] = v
        del r['Unused']
        for k in ('IsAutoSupported', 'IsWritable'):
            r[k] = bool(getattr(self, k))
        return r


class _ASI_ID(ctypes.Structure):
    _fields_ = [('id', ctypes.c_char * 8)]

    def get_id(self) -> dict:
        # return self.id
        v = self.id
        if sys.version_info[0] >= 3 and isinstance(v, bytes):
            v = v.decode()
        return v


class _ASI_SUPPORTED_MODE(ctypes.Structure):
    _fields_ = [('SupportedCameraMode', ctypes.c_int * 16)]

    def get_dict(self)  -> dict:
        base_dict = {k: getattr(self, k) for k, _ in self._fields_}
        base_dict['SupportedCameraMode'] = [int(x) for x in base_dict['SupportedCameraMode']]
        return base_dict

class _ASI_INFO():
    """ASI Camera info for better storage"""
    _count : int        # 数量
    _id : int           # ID
    _name : str         # 名称
    _found = False       # 是否发现
    _connected = False   # 是否连接
    _in_exposure = False # 是否曝光
    _in_video = False    # 是否在录制视频

    _max_width : int   # 最大宽度
    _max_height : int   # 最大高度
    _bayer : int        # 拜尔类型
    _pixel : float      # 像素大小
    _bitdepth : int     # 位深
    _bin = int          # 像素合并

    _is_cool : bool
    _is_color : bool
    _is_guide : bool
    _is_usb3 : bool

class _EXPOSURE_INFO():
    """Exposure info"""
    _exp = 1
    _bin = 1
    _gain = 20
    _offset = 20
    _is_save = True
    _filename : str

class zwoasi():
    """ASI Camera class"""

    def __init__(self) -> None:
        self.zwolib = None
        self.zwoinfo = _ASI_INFO()
        self.exposureinfo = _EXPOSURE_INFO()
        self.init()

    def __del__(self) -> None:
        self.disconnect()

    def init(self) -> None:
        # 如果已经加载库则跳过初始化
        if self.zwolib is not None:
            return
        _p = os.path.join
        libpath = _p(_p(os.getcwd(),"lib"),"zwoasi")
        # 判断系统位数 - 32/64
        if 'PROGRAMFILES(X86)' in os.environ:
            libpath = _p(_p(libpath,"x64"),"ASICamera2.dll")
        else:
            libpath = _p(_p(libpath,"x86"),"ASICamera2.dll")
        # 检查库是否存在
        if os.path.isfile(libpath):
            log.log(f"Find {libpath}")
        else:
            log.loge(f"Failed to find {libpath}")
        # 加载动态库
        self.zwolib = ctypes.cdll.LoadLibrary(libpath)
        self.init_dll()
        
    def init_dll(self) -> None:
        """Init dll for next step"""
        self.zwolib.ASIGetNumOfConnectedCameras.argtypes = []
        self.zwolib.ASIGetNumOfConnectedCameras.restype = ctypes.c_int

        self.zwolib.ASIGetCameraProperty.argtypes = [ctypes.POINTER(_ASI_CAMERA_INFO), ctypes.c_int]
        self.zwolib.ASIGetCameraProperty.restype = ctypes.c_int

        self.zwolib.ASIOpenCamera.argtypes = [ctypes.c_int]
        self.zwolib.ASIOpenCamera.restype = ctypes.c_int

        self.zwolib.ASIInitCamera.argtypes = [ctypes.c_int]
        self.zwolib.ASIInitCamera.restype = ctypes.c_int

        self.zwolib.ASICloseCamera.argtypes = [ctypes.c_int]
        self.zwolib.ASICloseCamera.restype = ctypes.c_int

        self.zwolib.ASIGetNumOfControls.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        self.zwolib.ASIGetNumOfControls.restype = ctypes.c_int

        self.zwolib.ASIGetControlCaps.argtypes = [ctypes.c_int, ctypes.c_int,
                                            ctypes.POINTER(_ASI_CONTROL_CAPS)]
        self.zwolib.ASIGetControlCaps.restype = ctypes.c_int

        self.zwolib.ASIGetControlValue.argtypes = [ctypes.c_int,
                                            ctypes.c_int,
                                            ctypes.POINTER(ctypes.c_long),
                                            ctypes.POINTER(ctypes.c_int)]
        self.zwolib.ASIGetControlValue.restype = ctypes.c_int

        self.zwolib.ASISetControlValue.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_long, ctypes.c_int]
        self.zwolib.ASISetControlValue.restype = ctypes.c_int

        self.zwolib.ASIGetROIFormat.argtypes = [ctypes.c_int,
                                        ctypes.POINTER(ctypes.c_int),
                                        ctypes.POINTER(ctypes.c_int),
                                        ctypes.POINTER(ctypes.c_int),
                                        ctypes.POINTER(ctypes.c_int)]
        self.zwolib.ASIGetROIFormat.restype = ctypes.c_int

        self.zwolib.ASISetROIFormat.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.zwolib.ASISetROIFormat.restype = ctypes.c_int

        self.zwolib.ASIGetStartPos.argtypes = [ctypes.c_int,
                                        ctypes.POINTER(ctypes.c_int),
                                        ctypes.POINTER(ctypes.c_int)]
        self.zwolib.ASIGetStartPos.restype = ctypes.c_int

        self.zwolib.ASISetStartPos.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.zwolib.ASISetStartPos.restype = ctypes.c_int

        self.zwolib.ASIGetDroppedFrames.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        self.zwolib.ASIGetDroppedFrames.restype = ctypes.c_int

        self.zwolib.ASIEnableDarkSubtract.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char)]
        self.zwolib.ASIEnableDarkSubtract.restype = ctypes.c_int

        self.zwolib.ASIDisableDarkSubtract.argtypes = [ctypes.c_int]
        self.zwolib.ASIDisableDarkSubtract.restype = ctypes.c_int

        self.zwolib.ASIStartVideoCapture.argtypes = [ctypes.c_int]
        self.zwolib.ASIStartVideoCapture.restype = ctypes.c_int

        self.zwolib.ASIStopVideoCapture.argtypes = [ctypes.c_int]
        self.zwolib.ASIStopVideoCapture.restype = ctypes.c_int

        self.zwolib.ASIGetVideoData.argtypes = [ctypes.c_int,
                                        ctypes.POINTER(ctypes.c_char),
                                        ctypes.c_long,
                                        ctypes.c_int]
        self.zwolib.ASIGetVideoData.restype = ctypes.c_int

        self.zwolib.ASIPulseGuideOn.argtypes = [ctypes.c_int, ctypes.c_int]
        self.zwolib.ASIPulseGuideOn.restype = ctypes.c_int

        self.zwolib.ASIPulseGuideOff.argtypes = [ctypes.c_int, ctypes.c_int]
        self.zwolib.ASIPulseGuideOff.restype = ctypes.c_int

        self.zwolib.ASIStartExposure.argtypes = [ctypes.c_int, ctypes.c_int]
        self.zwolib.ASIStartExposure.restype = ctypes.c_int

        self.zwolib.ASIStopExposure.argtypes = [ctypes.c_int]
        self.zwolib.ASIStopExposure.restype = ctypes.c_int

        self.zwolib.ASIGetExpStatus.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        self.zwolib.ASIGetExpStatus.restype = ctypes.c_int

        self.zwolib.ASIGetDataAfterExp.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char), ctypes.c_long]
        self.zwolib.ASIGetDataAfterExp.restype = ctypes.c_int

        self.zwolib.ASIGetID.argtypes = [ctypes.c_int, ctypes.POINTER(_ASI_ID)]
        self.zwolib.ASIGetID.restype = ctypes.c_int

        self.zwolib.ASISetID.argtypes = [ctypes.c_int, _ASI_ID]
        self.zwolib.ASISetID.restype = ctypes.c_int


        self.zwolib.ASIGetGainOffset.argtypes = [ctypes.c_int,
                                            ctypes.POINTER(ctypes.c_int),
                                            ctypes.POINTER(ctypes.c_int),
                                            ctypes.POINTER(ctypes.c_int),
                                            ctypes.POINTER(ctypes.c_int)]
        self.zwolib.ASIGetGainOffset.restype = ctypes.c_int

        self.zwolib.ASISetCameraMode.argtypes = [ctypes.c_int, ctypes.c_int]
        self.zwolib.ASISetCameraMode.restype = ctypes.c_int

        self.zwolib.ASIGetCameraMode.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        self.zwolib.ASIGetCameraMode.restype = ctypes.c_int

        self.zwolib.ASIGetCameraSupportMode.argtypes = [ctypes.c_int, ctypes.POINTER(_ASI_SUPPORTED_MODE)]
        self.zwolib.ASIGetCameraSupportMode.restype = ctypes.c_int

        self.zwolib.ASISendSoftTrigger.argtypes = [ctypes.c_int, ctypes.c_int]
        self.zwolib.ASISendSoftTrigger.restype = ctypes.c_int

        self.zwolib.ASISetTriggerOutputIOConf.argtypes = [ctypes.c_int,
                                                    ctypes.c_int,
                                                    ctypes.c_int,
                                                    ctypes.c_long,
                                                    ctypes.c_long]
        self.zwolib.ASISetTriggerOutputIOConf.restype = ctypes.c_int

        self.zwolib.ASIGetTriggerOutputIOConf.argtypes = [ctypes.c_int,
                                                    ctypes.c_int,
                                                    ctypes.POINTER(ctypes.c_int),
                                                    ctypes.POINTER(ctypes.c_long),
                                                    ctypes.POINTER(ctypes.c_long)]
        self.zwolib.ASIGetTriggerOutputIOConf.restype = ctypes.c_int

        log.log(f"Processing ASILib completed")

    def return_message(self,tpye : str,message : str,advice : str = "") -> dict:
        """Return message in dict format"""
        r = {
            "status" : tpye,
            "message" : message,
            "advice" : advice
        }
        return r

    def connect(self,name) -> dict:
        """Connect to camera & return false when error happens"""
        self.zwoinfo._count = self.zwolib.ASIGetNumOfConnectedCameras()
        if self.zwoinfo._count == 0:
            log.loge(f"No ASI camera been found,please check connection")
            return self.return_message("error","no camera found","check connection")
        # 在所有相机中搜索需要连接的相机
        for _id in enumerate(self.zwoinfo._count):
            # 获取相机信息
            prop = _ASI_CAMERA_INFO()
            r = self.zwolib.ASIGetCameraProperty(prop, _id)
            prop_dict = prop.get_dict()
            if r:
                log.loge(f"Fail to get camera property ,error code : {zwo_errors[r]}") 
            # 找到对应名称相机
            if prop_dict["Name"] == name:
                log.log(f"Found ASI camera : {name}")
                self.zwoinfo._found = True
                self.zwoinfo._id = prop_dict["CameraID"]
                self.zwoinfo._name = prop_dict["Name"]
                break
        if self.zwoinfo._found:
            # 打开相机
            r = self.zwolib.ASIOpenCamera(_id)
            if r:
                log.loge(f"Fail to open camera ,error code : {zwo_errors[r]}") 
                return self.return_message("error","fali to open camera","restart")
            r = self.zwolib.ASIInitCamera(_id)
            if r:
                log.loge(f"Fail to initialize camera ,error code : {zwo_errors[r]}") 
                return self.return_message("error","fali to initialize camera","restart")
            log.log(f"Connect to {self.zwoinfo._name} successfully")
            return self.return_message("success","connected")
        log.loge(f"Failed to find {name}")
        return self.return_message("error","no appoint camera found","Reconnect the camera")

    def disconnect(self) -> dict:
        """Disconnect from camera"""
        if self.zwoinfo._connected:
            if self.zwoinfo._in_exposure:
                log.log("Stop exposure")
                self.abort_exposure()
            if self.zwoinfo._in_video:
                log.log("Stop wideo capture")
            # 关闭相机
            r = self.zwolib.ASICloseCamera(self.zwoinfo._id)
            if r:
                log.loge(f"Fail to disconnect from {self.zwoinfo._name} , error code : {zwo_errors[r]}")
                return self.return_message("error","fail to disconnect camera","gg")
            log.log(f"Success to disconnect from {self.zwoinfo._name}")
            return self.return_message("success",f"disconnect from {self.zwoinfo._name}")

    def update_config(self) -> dict:
        """Get camera settings & status"""
        # 获取相机信息
        prop = _ASI_CAMERA_INFO()
        r = self.zwolib.ASIGetCameraProperty(prop, self.zwoinfo._id)
        prop_dict = prop.get_dict()
        if r:
            log.loge(f"Fail to get camera property ,error code : {zwo_errors[r]}") 
            return self.return_message("error","fail to get camera settings","reconnect")
        # 获取相机类型
        self.zwoinfo._is_color = prop_dict["IsColorCam"]
        self.zwoinfo._is_cool = prop_dict["IsCoolerCam"]
        self.zwoinfo._is_usb3 = prop_dict["IsUSB3Camera"]
        # 获取相机参数
        self.zwoinfo._max_height = prop_dict["MaxHeight"]
        self.zwoinfo._max_width = prop_dict["MaxWidth"]
        self.zwoinfo._bayer = prop_dict["BayerPattern"]
        self.zwoinfo._bin = prop_dict["SupportedBins"]
        self.zwoinfo._pixel = prop_dict["PixelSize"]
        self.zwoinfo._bitdepth = prop_dict["BitDepth"]

        log.log(f"Get {self.zwoinfo._name} info successfully")
        return self.return_message("success",f"get {self.zwoinfo._name} info")

    def start_exposure(self,params : dict) -> dict:
        """
        Start exposure & create image
        @ params : {
            "exp" : int # time of exposure in seconds
            "bin" : int # pixel merge
            "gain" : int # gain
            "offset" : int # offset

            "is_save" : bool # whether to save the image
            "filename" : str # filename to save
        }
        """
        if not self.zwoinfo._connected:
            log.loge("Camera not connected,please do not start exposure")
            return self.return_message("error","no camera connected","run after connected")
        
    def abort_exposure(self) -> dict:
        """Abort camera exposure"""
        log.log("Aborting camera exposure ...")
        if not self.zwoinfo._connected:
            log.loge("Camera not connected,please do not abort exposure")
            return self.return_message("error","no camera connected","run after connected")
        r = self.zwolib.ASIStopExposure(self.zwoinfo._id)
        if r:
            log.loge(f"Fail to abort {self.zwoinfo._name} exposure")
            return self.return_message("error","fail to abort exposure","try again")
        log.log(f"Aborted {self.zwoinfo._name} exposure")
        return self.return_message("success","aborted exposure")

    def set_camera_config(self,params) -> dict:
        """
        Set camera config
        @ params : {
            "bin" : int # pixel merge
            "gain" : int # gain
            "offset" : int # offset
        }
        """
