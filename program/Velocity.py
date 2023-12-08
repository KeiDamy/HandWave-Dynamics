#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

class Velocity:
    """物体の速度と方向を表すクラス"""
    def __init__(self, speed, direction):
        self.speed = speed
        self.direction = direction

    def getSpeed(self):
        return self.speed
    
    def getDirection(self):
        return self.direction
