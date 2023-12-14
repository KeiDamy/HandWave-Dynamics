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
        self.handDetector = HandDetector()     
        self.boidSimulation = BoidSimulation() 
        self.rippleEffect = RippleEffect()     
        self.view = View()                     

    def run(self):
        """プログラムの主要な実行を行う"""
        while True:
            # 手の検出
            hands = self.handDetector.detectHands()
            # Boidシミュレーションの更新
            self.boidSimulation.simulateBoids()
            # 波紋エフェクトの生成
            self.rippleEffect.generateRipple()
            # ビューの更新
            self.view.updateDisplay()
