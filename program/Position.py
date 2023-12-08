#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

class Position:
    """物体の位置を表すクラス"""
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getZ(self):
        return self.z
    