# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import datetime
    
class SensorData:
    def __init__(self):
        self.datetime = datetime.datetime(2024, 1, 1, 0, 0, 0, 0)
        self.position_mm = 0.0
        self.current_mA = 0.0
        
    def getDatetime(self):
        """Get Datetime"""
        return self.datetime
    
    def getPosition(self):
        """Get Position[mm]"""
        return self.position_mm
    
    def getCurrent(self):
        """Get Current[mA]"""
        return self.current_mA