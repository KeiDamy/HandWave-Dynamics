#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

from program.HandDetector import HandDetector
from program.BoidSimulation import BoidSimulation
from program.RippleEffect import RippleEffect
from program.View import View

class ApplicationController:
    """コントローラー。他のコンポーネント間の調整を行う。"""
    def __init__(self):
        self.handDetector = HandDetector()     #手の動きを検知するためのオブジェクト
        self.boidSimulation = BoidSimulation() #Boidアルゴリズムに基づく生物群の動きをシミュレートするオブジェクト
        self.rippleEffect = RippleEffect()     #波紋エフェクトを生成するオブジェクト
        self.view = View()                     #システムの視覚的出力を担当するオブジェクト

    def run(self):
        """プログラムの主要な実行を行う"""
        return 0
