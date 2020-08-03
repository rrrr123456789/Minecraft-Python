# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x=200
y=150
z=-100

mc.player.setTilePos(x,y,z)