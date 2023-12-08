#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

from program.Position import Position

class RippleEffect:
    """手の位置から波紋エフェクトを生成するクラス"""
    def __init__(self):
        self.lastHandPosition = Position # 最後に検出された手の位置

    def generateRipple():
        """波紋エフェクトを生成する"""
        return 0
