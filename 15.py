# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

mc=Minecraft.create()

a=0
while a< 1000:
    mc.setBlocks(x-30,y-1,z,x+30,z,19)
    z=z+6
    a=a+1