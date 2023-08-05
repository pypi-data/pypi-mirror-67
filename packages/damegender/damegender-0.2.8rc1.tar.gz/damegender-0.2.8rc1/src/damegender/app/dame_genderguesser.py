#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import csv
import requests
import json
import gender_guesser.detector as gender
from app.dame_gender import Gender


class DameGenderGuesser(Gender):
    def guess(self, name, binary=False):
        # guess method to check names dictionary
        genderguesserlist = []
        d = gender.Detector()
        get = d.get_gender(name)
        if (((get == 'female') or (get == 'mostly_female')) and binary):
            guess = 0
        elif (((get == 'male') or (get == 'mostly_male')) and binary):
            guess = 1
        elif (((get == 'unknown') or (get == 'andy')) and binary):
            guess = 2
        else:
            guess = get
        return guess

    # def print_confusion_matrix_gender(self, path='files/names/partial.csv', dimensions="2x3"):
    #     cmd = self.confusion_matrix_gender(path, dimensions)
    #     print("[[ %s, %s, %s]" % (cmd[0][0], cmd[0][1], cmd[0][2]))
    #     print(" [ %s, %s, %s]]\n" % (cmd[1][0], cmd[1][1], cmd[1][2]))
    #     return ""
