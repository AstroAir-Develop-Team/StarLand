-- coding=utf-8

--[[

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

]]--

-- Load Library
local json = require("lib.json")
if json == nil then
    print("Failed to load json library")
end
-- Load Library
local httpc = require("lib.http").new()
if httpc == nil then
    print("Could not load http lib")
end

local ok, err, ssl_session = httpc:connect({
    scheme = "http",
    host = "127.0.0.1",
    port = 8080,
})

if not ok then
    ngx.log(ngx.ERR, "connection failed: ", err)
    return
end

