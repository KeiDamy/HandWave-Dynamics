#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

from Position import Position

class RippleEffect:
    """手の位置から波紋エフェクトを生成するクラス"""
    def __init__(self):
        self.lastHandPosition = Position()  # 最後に検出された手の位置

    def generateRipple(self, handPosition):
        """波紋エフェクトを生成する"""
        # 波紋エフェクトのパラメータを設定（半径、速度、色など）
        ripple_params = {
            "radius": 0,
            "speed": 5,
            "color": (255, 255, 255),
            "opacity": 1.0
        }

        # handPosition から波紋の開始位置を設定
        self.lastHandPosition = handPosition

        # 波紋エフェクトを描画するロジックをここに実装
        # （具体的な描画コードは、使用するグラフィックライブラリに依存）

        return ripple_params  # 描画された波紋エフェクトを返す
