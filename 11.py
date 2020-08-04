# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
    
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
         
mc.setBlocks(x+25,y+11,z+25,x-125,y-1,z-25,0)