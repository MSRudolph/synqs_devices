#####################################################################
#                                                                   #
# /labscript_devices/MakoCamera/labscript_devices.py               #
#                                                                   #
# Copyright 2019, Monash University and contributors                #
#                                                                   #
# This file is part of labscript_devices, in the labscript suite    #
# (see http://labscriptsuite.org), and is licensed under the        #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
"""Import labscript devices"""
from labscript_devices.IMAQdxCamera.labscript_devices import IMAQdxCamera


class Mako_Camera(IMAQdxCamera):
    """Sub-class IMAQdxCamera"""

    description = "Mako Camera"
