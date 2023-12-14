#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

from math import cos, sin
from program.Position import Position
from program.Velocity import Velocity

class Boid:
    """個々の生物を表すクラス"""
    def __init__(self, position, velocity):
        self.position = position  # 生物の位置
        self.velocity = velocity  # 生物の速度と方向

    def updatePosition(self):
        """生物の位置を更新する"""
        # 速度に基づいて位置を更新
        self.position.x += self.velocity.speed * cos(self.velocity.direction)
        self.position.y += self.velocity.speed * sin(self.velocity.direction)
