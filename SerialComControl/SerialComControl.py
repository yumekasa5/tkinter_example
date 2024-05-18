# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import serial
import time

# class SerialComControl(serial.Serial):
#     """
#     Serialクラスの派生クラスとして扱う
#     """
    # def __init__(self, port="COM3", baudrate=9600, timeout=0.5) -> None:
    #     super().__init__(port=port, baudrate=baudrate, timeout=timeout)
        
    # def Open(self):
    #     """Open処理"""
    #     self.open() 
    #     time.sleep(0.1)  # デバイスの起動待ち時間
    #     message = self.read(256) # デバイスからのメッセージを取得
    #     return message
        
    # def Close(self, command="syst:loc\n"): # commandはデバイスによって異なる
    #     """Close処理"""
    #     self.write(command.encode("utf-8")) # デバイスにコマンドを送信
    #     self.close()