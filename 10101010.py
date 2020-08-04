# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
         
mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,11)