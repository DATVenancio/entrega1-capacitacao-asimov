# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:44:40 2021

@author: Daniel
"""

import winsound
import time



x = int(input("TEMPO X  :  "))
y = int(input("TEMPO Y  :  "))
escolha = str(input("QUER QUE TOQUE O AUDIO ?    y/n     :"))

if escolha.lower()[0] =='y':
    winsound.PlaySound("audio", winsound.SND_FILENAME)
    
    time.sleep(x)
    
    for i in range(y):
        winsound.PlaySound("audio", winsound.SND_FILENAME)
    
