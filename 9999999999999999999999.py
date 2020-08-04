# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

mc.setBlock(x-1,y,z+1,2)
mc.setBlock(x,y,z+2,2)
mc.setBlock(x+1,y,z,2)
mc.setBlock(x+1,y,z-1,2)
mc.setBlock(x,y,z-1,11)
mc.setBlock(x-1,y,z-1,2)
mc.setBlock(x-1,y,z,2)
mc.setBlock(x-1,y,z+1,2)          