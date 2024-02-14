#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

import sys

from ApplicationController import ApplicationController

if __name__ == '__main__':
    anApplicationController = ApplicationController()
    sys.exit(anApplicationController.run())
