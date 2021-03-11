# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:56:53 2021

@author: Daniel
"""

import sys    
import winsound
import time



    
x=int(sys.argv[1])
y=int(sys.argv[2])

escolha = str(input("QUER QUE TOQUE O AUDIO ?    y/n     :"))

if escolha.lower()[0] =='y':
    winsound.PlaySound("audio", winsound.SND_FILENAME)
    
    time.sleep(x)
    
    for i in range(y):
        winsound.PlaySound("audio", winsound.SND_FILENAME)