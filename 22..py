from mcpi.minecraft import Minecraft



mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

def Tree(x,y,z):
    mc.setBlocks(x-1,y+5,z-1,x+1,y+3,z+1,49) 
    mc.setBlocks(x,y,z,x,y+4,z,1) 


for i in range(20):
    Tree(x+i*5,y,z)