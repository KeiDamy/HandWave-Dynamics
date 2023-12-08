#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

from program.Resolution import Resolution

class Projector:
    """プロジェクター装置を表すクラス"""
    def __init__(self,resolution):
        self.resolution = resolution # 解像度
        self.brightness = int        # 明るさ

    def projectImage(self,Image):
        """画像を投影する"""
        return 0
    
    def adjustSettings():
        """設定を調整する"""
        return 0
