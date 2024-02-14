#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.0'
__date__ = '2023/12/08(Created: 2023/12/08)'

from VideoCapture import VideoCapture

import cv2
import mediapipe as mp

class HandDetector:
    """手の動きを検出するためのクラス"""
    def __init__(self):
        self.selfcaptureDevice = VideoCapture() # ビデオキャプチャデバイスを表す

    def detectHands(self):
        """ビデオフレームから手の位置を検出する"""
        video_capture = VideoCapture()
        video_capture.startCapture()
        return 0
