# coding=utf-8

"""

Copyright(c) 2019 Radek Kaczorek  <rkaczorek AT gmail DOT com>

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

class astrometry():
    """Astrometry"""

    default_url = 'https://nova.astrometry.net/api/'

    def __init__(self) -> None:
        """Construct"""
        self.session = None

    def __del__(self) -> None:
        """Destroy"""

    def online_solver(self,params : dict) -> dict:
        """
        Online solver
        @params : {
            
        }
        """

