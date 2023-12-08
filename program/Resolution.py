#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

class Resolution:
    """解像度を表すクラス"""
    def __init__(self,width,height):
        self.width = width   # 幅
        self.height = height # 高さ

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    