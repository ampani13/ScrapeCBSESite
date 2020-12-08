# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 00:54:19 2019

@author: Amiya
"""
import md5
userpwd=str("mySuperPassword")
hashedpw=md5.new(userpwd)
print(hashedpw)