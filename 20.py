from mcpi.minecraft import Minecraft



mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

for i in range(20):
    mc.setBlocks(x+1,y,z+1,x,y+1,z,1)


     