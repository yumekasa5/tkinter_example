# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import serial
import time

class SerialComControl(serial.Serial):
    """
    Serialクラスの派生クラスとして扱う
    """
    def __init__(self) -> None:
        super().__init__(self)
        
        self.port = "COM3"
        self.baudrate = 9600
        self.timeout = 0.5
        
    def Open(self):
        """Open処理"""
        self.open() 
        time.sleep(0.1)  
        message = self.read(256)
        
    def Close(self):
        self.write("syst:loc\n".encode("utf-8"))
        self.close()