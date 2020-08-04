# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

   
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

width=10
height=20
length=15

block=1
air=0

mc.setBlocks(x,y,z,x+length,y+height,z+width,block)
mc.setBlocks(x+1,y+1,z+1,x+length-1,y+height-1,z+width-1,air)