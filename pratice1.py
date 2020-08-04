# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos() 
    rr=random.randrange(9)
    mc.setBlock(x,y,z,38,rr)  
    