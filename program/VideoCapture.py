#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""HandWave_Dynamics：手の動きに対応した画像を出力する"""
__author__ = 'Yokokawa Kotaro'
__version__ = '1.0.1'
__date__ = '2024/2/15(Created: 2023/12/08)'

import cv2
import mediapipe as mp

class VideoCapture:
    """ビデオキャプチャデバイスを表すクラス"""
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands()

    def startCapture(self):
        """キャプチャを開始する"""
        while True:
            success, image = self.cap.read()
            if not success:
                break

            # Mediapipeを使用して手の検出を実行
            results = self.hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # 手のランドマークを画像に描画
                    self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

            # 画像を表示
            cv2.imshow('Hand Tracking', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.stopCapture()
        return 0
    
    def stopCapture(self):
        """キャプチャを停止する"""
        self.cap.release()
        cv2.destroyAllWindows()
        return 0
    
    def getFrame(self):
        """現在のビデオフレームを取得する"""
        success, image = self.cap.read()
        if success:
            return image
        else:
            return None
