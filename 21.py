from mcpi.minecraft import Minecraft
import random
import time
mc=Minecraft.create()

pos=mc.player.getTilePos()
while True:
   
    y=pos.y+30
    x=pos.x+random.uniform(-20,20)
    z=pos.z+random.uniform(-20,20)
    
    mc.spawnEntity(x,y,z,53)
    time.sleep(0.1)