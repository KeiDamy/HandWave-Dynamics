#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

class VideoCapture:
    """ビデオキャプチャデバイスを表すクラス"""
    def __init__(self,source):
        self.source = source # カメラ

    def startCapture(self):
        """キャプチャを開始する"""
        return 0
    
    def stopCapture(self):
        """キャプチャを停止する"""
        return 0
    
    def getFrame():
        """現在のビデオフレームを取得する"""
        return 0
