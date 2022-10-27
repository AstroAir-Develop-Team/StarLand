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

from lupa import LuaRuntime
import threading
import traceback
import os

from core.lib.starlog import starlog

log = starlog(__name__)

class lualoader(threading.Thread):

    def __init__(self, files,target,params) -> None:
        threading.Thread.__init__(self)
        self.params = params
        self.target = target
        self.file = files

    def __delattr__(self, __name: str) -> None:
        return super().__delattr__(__name)
    
    def run(self):
        """
            重写Thread.run，以适配lua环境
        """
        try:
            # 执行具体的函数,返回结果打印在屏幕上
            luaRuntime = self.getLuaRuntime()
            rel = luaRuntime(self.api, self.params)
            print (rel)
        except Exception as e:
            log.loge(f"Run {self.file} error , {e.message}")
            traceback.extract_stack()
 
 
    def getLuaRuntime(self):
        """
            从文件中加载要执行的lua脚本,初始化lua执行环境
        """

        if os.path.isfile(self.file):
            # 上锁,保证多个线程加载不会冲突
            if lualoader.lock.acquire():
                if lualoader.luaRuntime is None:
                    fileHandler = open(self.file)
                    content = ''
                    try:
                        content = fileHandler.read()
                    except Exception as e:
                        log.loge(f"Run {self.file} error , {e.message}")
                        traceback.extract_stack()
    
                    # 创建lua执行环境
                    lualoader.luaScriptContent = content
                    luaRuntime = LuaRuntime()
                    luaRuntime.execute(content)
    
                    # 从lua执行环境中取出全局函数functionCall作为入口函数调用,实现lua的反射调用
                    g = luaRuntime.globals()
                    function_call = g.FunctionCall
                    lualoader.luaRuntime = function_call
                lualoader.lock.release()
                log.loge(f"Run {self.file} successfully")
            return lualoader.luaRuntime
        else:
            log.loge(f"Failed to find {self.file}")
    