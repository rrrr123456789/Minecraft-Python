# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
try:
    block=int(input('Block id?'))

    mc.setBlock(x,y,z,block)
except:
    mc.postToChat('You are a idiot')