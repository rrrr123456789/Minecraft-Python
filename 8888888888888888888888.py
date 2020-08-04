# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

mc.setBlock(x,y,z,11)
mc.setBlock(x,y+1,z,11)
mc.setBlock(x,y+2,z,11)
mc.setBlock(x,y+3,z,11)
mc.setBlock(x,y+4,z,11)
mc.setBlock(x,y+5,z,11)
mc.setBlock(x,y+6,z,11)
mc.setBlock(x,y+7,z,11)          