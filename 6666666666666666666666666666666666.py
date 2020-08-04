# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
   x,y,z=mc.player.getTilePos()
   mc.postToChat('You are located on x:'+str(x)+',y:'+str(y)+',z:'+str(z))