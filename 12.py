# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time
import random    
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
while True:
    color=random.randrange(16)
    mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,95,color)
    time.sleep(0.5)