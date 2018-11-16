from mine import *
import time
mc=Minecraft()
position=mc.player.getTilePos()


x=position.x
y=position.y
z=position.z
blockType=5
##Stone Slabs Entrance
def StoneSlabEntrance(x,y,z):
    mc.setBlocks(x,y,z-3,x,y,z+3,44,5)
    mc.setBlock(x+1,y,z-4,44,5)
    mc.setBlock(x+1,y,z+4,44,5)
    mc.setBlock(x+2,y,z+5,44,5)
    mc.setBlock(x+2,y,z-5,44,5)
    mc.setBlocks(x+3,y,z-6,x+6,y,z-6,44,5)
    mc.setBlocks(x+3,y,z+6,x+6,y,z+6,44,5)
##Wood Blocks Entrance
def WoodBlocksEntrance(x,y,z):
    mc.setBlocks(x+1,y,z-3,x+1,y,z+3,blockType)
    mc.setBlocks(x+2,y,z-4,x+2,y,z+4,blockType)
    mc.setBlocks(x+3,y,z-5,x+6,y,z+5,blockType)
##Sea Lanterns + Glass Entrance
def SeaLanternGlassEntrance(x,y,z):
    mc.setBlocks(x+4,y,z-2,x+4,y,z+2,95,3)
    mc.setBlocks(x+2,y,z,x+6,y,z,95,3)
    mc.setBlocks(x+4,y-1,z-2,x+4,y-1,z+2,169)
    mc.setBlocks(x+2,y-1,z,x+6,y-1,z,169)

##Front Wall
def FrontWall(x,y,z):
    ##Right Wall - Front
    mc.setBlocks(x+7,y,z+5,x+7,y+2,z+45,17)

    ##Left Wall - Front
    mc.setBlocks(x+7,y,z-5,x+7,y+2,z-45,17)

    ##Sea Lanterns - Front Walls
    mc.setBlock(x+7,y+1,z+9,138)
    mc.setBlock(x+7,y+1,z+17,138)
    mc.setBlock(x+7,y+1,z+25,138)
    mc.setBlock(x+7,y+1,z+33,138)
    mc.setBlock(x+7,y+1,z+41,138)

    mc.setBlock(x+7,y+1,z-9,138)
    mc.setBlock(x+7,y+1,z-17,138)
    mc.setBlock(x+7,y+1,z-25,138)
    mc.setBlock(x+7,y+1,z-33,138)
    mc.setBlock(x+7,y+1,z-41,138)

    ##Fence - Front Walls
    mc.setBlocks(x+7,y+3,z+5,x+7,y+3,z+45,85)
    mc.setBlocks(x+7,y+3,z-5,x+7,y+3,z-45,85)

##Main Path
def MainPath(x,y,z):
    ##Wood Blocks - Main Path
    mc.setBlocks(x+7,y,z-4,x+57,y,z+4,blockType)
    mc.setBlocks(x+7,y,z-4,x+57,y,z+4,blockType)


    ##Wood Blocks - Main Path
    mc.setBlocks(x+7,y,z-4,x+57,y,z+4,blockType)
    mc.setBlocks(x+7,y,z-4,x+57,y,z+4,blockType)

    ##Sea Lantern + Glass - Main Path
    mc.setBlocks(x+8,y,z,x+56,y,z,95,3)
    mc.setBlocks(x+8,y-1,z,x+56,y-1,z,169)

    ##Stone Slabs - Main Path
    mc.setBlocks(x+8,y+1,z-4,x+57,y+1,z-4,44,5)
    mc.setBlocks(x+8,y+1,z+4,x+57,y+1,z+4,44,5)

##Middle Circle
def MiddleCircle(x,y,z):
    ##Middle Circle Rim
    mc.setBlocks(x+53,y+1,z-4,x+53,y+1,z+4,17)
    mc.setBlocks(x+54,y+1,z-5,x+54,y+1,z+5,17)
    mc.setBlocks(x+55,y+1,z-6,x+55,y+1,z+6,17)
    mc.setBlocks(x+56,y+1,z-7,x+56,y+1,z+7,17)
    mc.setBlocks(x+57,y+1,z-8,x+57,y+1,z+8,17)
    mc.setBlocks(x+58,y+1,z-9,x+58,y+1,z+9,17)
    mc.setBlocks(x+59,y+1,z-10,x+59,y+1,z+10,17)
    mc.setBlocks(x+60,y+1,z-11,x+60,y+1,z+11,17)
    mc.setBlocks(x+61,y+1,z-12,x+61,y+1,z+12,17)
    mc.setBlocks(x+61,y+1,z-12,x+69,y+1,z+12,17)
    mc.setBlocks(x+70,y+1,z-11,x+70,y+1,z+11,17)
    mc.setBlocks(x+71,y+1,z-10,x+72,y+1,z+10,17)
    mc.setBlocks(x+72,y+1,z-9,x+72,y+1,z+9,17)
    mc.setBlocks(x+73,y+1,z-8,x+72,y+1,z+8,17)
    mc.setBlocks(x+74,y+1,z-7,x+72,y+1,z+7,17)
    mc.setBlocks(x+75,y+1,z-6,x+72,y+1,z+6,17)
    mc.setBlocks(x+76,y+1,z-5,x+72,y+1,z+5,17)
    mc.setBlocks(x+77,y+1,z-4,x+72,y+1,z+4,17)

    mc.setBlocks(x+54,y+1,z-4,x+54,y+1,z+4,9)
    mc.setBlocks(x+55,y+1,z-5,x+55,y+1,z+5,9)
    mc.setBlocks(x+56,y+1,z-6,x+56,y+1,z+6,9)
    mc.setBlocks(x+57,y+1,z-7,x+57,y+1,z+7,9)
    mc.setBlocks(x+58,y+1,z-8,x+58,y+1,z+8,9)
    mc.setBlocks(x+59,y+1,z-9,x+59,y+1,z+9,9)
    mc.setBlocks(x+60,y+1,z-10,x+60,y+1,z+10,9)
    mc.setBlocks(x+61,y+1,z-11,x+69,y+1,z+11,9)
    mc.setBlocks(x+70,y+1,z-10,x+70,y+1,z+10,9)
    mc.setBlocks(x+71,y+1,z-9,x+71,y+1,z+9,9)
    mc.setBlocks(x+72,y+1,z-8,x+72,y+1,z+8,9)
    mc.setBlocks(x+73,y+1,z-7,x+73,y+1,z+7,9)
    mc.setBlocks(x+74,y+1,z-6,x+74,y+1,z+6,9)
    mc.setBlocks(x+75,y+1,z-5,x+75,y+1,z+5,9)
    mc.setBlocks(x+76,y+1,z-4,x+76,y+1,z+4,9)

    ##Middle Circle Bottom
    mc.setBlocks(x+53,y,z-4,x+53,y,z+4,2)
    mc.setBlocks(x+54,y,z-5,x+54,y,z+5,2)
    mc.setBlocks(x+55,y,z-6,x+55,y,z+6,2)
    mc.setBlocks(x+56,y,z-7,x+56,y,z+7,2)
    mc.setBlocks(x+57,y,z-8,x+57,y,z+8,2)
    mc.setBlocks(x+58,y,z-9,x+58,y,z+9,2)
    mc.setBlocks(x+59,y,z-10,x+59,y,z+10,2)
    mc.setBlocks(x+60,y,z-11,x+60,y,z+11,2)
    mc.setBlocks(x+61,y,z-12,x+61,y,z+12,2)
    mc.setBlocks(x+61,y,z-12,x+69,y,z+12,2)
    mc.setBlocks(x+70,y,z-11,x+70,y,z+11,2)
    mc.setBlocks(x+71,y,z-10,x+72,y,z+10,2)
    mc.setBlocks(x+72,y,z-9,x+72,y,z+9,2)
    mc.setBlocks(x+73,y,z-8,x+72,y,z+8,2)
    mc.setBlocks(x+74,y,z-7,x+72,y,z+7,2)
    mc.setBlocks(x+75,y,z-6,x+72,y,z+6,2)
    mc.setBlocks(x+76,y,z-5,x+72,y,z+5,2)
    mc.setBlocks(x+77,y,z-4,x+72,y,z+4,2)

##Main Tree
def MainTree(x,y,z):
    ##Main Tree

    ##Tree Marker
    mc.setBlock(x+62,y+1,z,52,1)

    mc.setBlocks(x+63,y+2,z-1,x+63,y+2,z+1,17)
    mc.setBlocks(x+64,y+2,z+2,x+66,y+2,z+2,17)
    mc.setBlocks(x+66,y+2,z+2,x+66,y+2,z+1,17)
    mc.setBlock(x+67,y+2,z,17)
    mc.setBlocks(x+66,y+2,z-1,x+63,y+2,z-1,17)
    mc.setBlock(x+64,y+2,z-2,17)

    mc.setBlocks(x+64,y+3,z-1,x+65,y+3,z+1,17)
    mc.setBlocks(x+66,y+3,z,x+66,y+3,z+1,17)
    mc.setBlock(x+65,y+3,z+2,17)
    mc.setBlocks(x+64,y+4,z,x+66,y+4,z+1,17)
    mc.setBlocks(x+65,y+4,z-1,x+66,y+4,z+1,17)
    mc.setBlock(x+65,y+4,z+2,17)

    mc.setBlocks(x+65,y+5,z+1,x+67,y+5,z-1,17)
    mc.setBlock(x+66,y+5,z-2,17)
    mc.setBlock(x+61,y+5,z-3,18)

    mc.setBlocks(x+65,y+6,z,x+67,y+6,z+1,17)
    mc.setBlock(x+66,y+6,z+1,17)
    mc.setBlocks(x+66,y+6,z-1,x+67,y+6,z-1,17)

    mc.setBlocks(x+62,y+7,z,x+68,y+7,z-2,17)
    mc.setBlocks(x+62,y+7,z-2,x+64,y+7,z-2,17)
    mc.setBlocks(x+68,y+7,z-3,x+66,y+7,z-3,18)
    mc.setBlocks(x+63,y+7,z+1,x+64,y+7,z+1,18)
    mc.setBlock(x+66,y+7,z+1,17)
    mc.setBlocks(x+61,y+7,z-1,x+60,y+7,z-4,18)
    mc.setBlock(x+60,y+7,z-5,18)
    mc.setBlock(x+59,y+7,z-1,18)
    mc.setBlocks(x+62,y+7,z-2,x+64,y+7,z-2,18)

    mc.setBlocks(x+62,y+8,z,x+68,y+8,z-2,17)
    mc.setBlocks(x+64,y+8,z-2,x+65,y+8,z-2,18)
    mc.setBlocks(x+66,y+8,z-3,x+68,y+8,z-3,17)
    mc.setBlocks(x+69,y+8,z-1,x+70,y+8,z-1,17)
    mc.setBlocks(x+70,y+8,z-2,x+71,y+8,z-2,17)
    mc.setBlock(x+66,y+8,z-3,17)
    mc.setBlocks(x+62,y+8,z+1,x+68,y+8,z+1,18)
    mc.setBlocks(x+61,y+8,z,x+59,y+8,z-6,18)
    mc.setBlocks(x+66,y+8,z+1,x+67,y+8,z+1,17)
    mc.setBlock(x+67,y+8,z+2,17)
    mc.setBlock(x+68,y+8,z+1,18)
    mc.setBlock(x+65,y+8,z+2,18)
    mc.setBlock(x+66,y+8,z+2,18)
    mc.setBlocks(x+65,y+8,z+1,x+62,y+8,z+1,18)
    mc.setBlocks(x+62,y+8,z-1,x+60,y+8,z-1,17)
    mc.setBlock(x+62,y+8,z+1,18)
    mc.setBlocks(x+61,y+8,z-1,x+61,y+8,z-4,17)
    mc.setBlocks(x+60,y+8,z-4,x+60,y+8,z-5,17)
    mc.setBlock(x+59,y+8,z-6,0)
    mc.setBlock(x+58,y+8,z-2,18)

    mc.setBlocks(x+62,y+9,z,x+61,y+9,z-4,18)
    mc.setBlocks(x+60,y+9,z-1,x+60,y+9,z-2,18)
    mc.setBlocks(x+60,y+9,z-4,x+60,y+9,z-5,18)
    mc.setBlocks(x+63,y+9,z,x+63,y+9,z-3,18)
    mc.setBlocks(x+64,y+9,z,x+64,y+9,z-2,18)
    mc.setBlocks(x+64,y+9,z-1,x+66,y+9,z-1,17)
    mc.setBlocks(x+65,y+9,z+1,x+65,y+9,z-1,17)
    mc.setBlocks(x+65,y+9,z-3,x+65,y+9,z-8,18)
    mc.setBlocks(x+65,y+9,z-6,x+65,y+9,z-7,17)
    mc.setBlocks(x+64,y+9,z-6,x+64,y+9,z-8,18)
    mc.setBlocks(x+66,y+9,z+2,x+66,y+9,z+1,18)
    mc.setBlocks(x+67,y+9,z,x+67,y+9,z+3,18)
    mc.setBlocks(x+67,y+9,z,x+67,y+9,z+3,18)
    mc.setBlocks(x+67,y+9,z+2,x+67,y+9,z+1,17)
    mc.setBlocks(x+67,y+9,z-3,x+67,y+9,z-2,18)
    mc.setBlocks(x+67,y+9,z-4,x+67,y+9,z-6,17)
    mc.setBlocks(x+67,y+9,z+4,x+67,y+9,z-6,18)
    mc.setBlocks(x+67,y+9,z+3,x+67,y+9,z+1,17)
    mc.setBlocks(x+67,y+9,z-3,x+67,y+9,z-5,17)
    mc.setBlocks(x+68,y+9,z-5,x+68,y+9,z+3,18)
    mc.setBlocks(x+68,y+9,z+1,x+68,y+9,z+2,17)
    mc.setBlock(x+68,y+9,z-4,17)
    mc.setBlocks(x+69,y+9,z-5,x+69,y+9,z+1,18)
    mc.setBlock(x+69,y+9,z-4,17)
    mc.setBlocks(x+70,y+9,z-4,x+70,y+9,z-1,18)
    mc.setBlock(x+70,y+9,z-2,17)
    mc.setBlocks(x+71,y+9,z-3,x+71,y+9,z-1,18)
    mc.setBlock(x+71,y+9,z-1,17)
    mc.setBlocks(x+72,y+9,z-3,x+72,y+9,z,18)
    mc.setBlock(x+72,y+9,z-2,17)

    mc.setBlocks(x+72,y+9,z-3,x+72,y+9,z,18)


##Fireworks
def Fireworks(x,y,z):
    ##Fireworks
    mc.setBlock(x+4,y,z+4,178)
    mc.setBlock(x+4,y,z-4,178)

    mc.setBlock(x+5,y,z+4,149,5)
    mc.setBlock(x+5,y,z-4,149,5)

    mc.setBlocks(x+5,y,z+5,x+6,y,z+5,55)
    mc.setBlocks(x+5,y,z-5,x+6,y,z-5,55)

    mc.setBlock(x+6,y,z+4,55)
    mc.setBlock(x+6,y,z-4,55)

    mc.setBlocks(x+7,y,z+4,x+46,y,z+4,55)
    mc.setBlocks(x+7,y,z-4,x+46,y,z-4,55)

    mc.setBlock(x+9,y,z+4,93,1)
    mc.setBlock(x+9,y,z-4,93,1)
    mc.setBlock(x+14,y,z+4,93,1)
    mc.setBlock(x+14,y,z-4,93,1)
    mc.setBlock(x+17,y,z+4,93,1)
    mc.setBlock(x+17,y,z-4,93,1)
    mc.setBlock(x+20,y,z+4,93,1)
    mc.setBlock(x+20,y,z-4,93,1)
    mc.setBlock(x+22,y,z+4,93,1)
    mc.setBlock(x+22,y,z-4,93,1)
    mc.setBlock(x+24,y,z+4,93,1)
    mc.setBlock(x+24,y,z-4,93,1)
    mc.setBlock(x+26,y,z+4,93,1)
    mc.setBlock(x+26,y,z-4,93,1)
    mc.setBlock(x+29,y,z+4,93,1)
    mc.setBlock(x+29,y,z-4,93,1)
    mc.setBlock(x+31,y,z+4,93,1)
    mc.setBlock(x+31,y,z-4,93,1)
    mc.setBlock(x+33,y,z+4,93,1)
    mc.setBlock(x+33,y,z-4,93,1)
    mc.setBlock(x+35,y,z+4,93,1)
    mc.setBlock(x+35,y,z-4,93,1)
    mc.setBlock(x+37,y,z+4,93,1)
    mc.setBlock(x+37,y,z-4,93,1)
    mc.setBlock(x+39,y,z+4,93,1)
    mc.setBlock(x+39,y,z-4,93,1)
    mc.setBlock(x+41,y,z+4,93,1)
    mc.setBlock(x+41,y,z-4,93,1)
    mc.setBlock(x+43,y,z+4,93,1)
    mc.setBlock(x+43,y,z-4,93,1)
    mc.setBlock(x+45,y,z+4,93,1)
    mc.setBlock(x+45,y,z-4,93,1)

    mc.setBlock(x+8,y-1,z+5,23,1)
    mc.setBlock(x+8,y-1,z-5,23,1)
    mc.setBlock(x+16,y-1,z+5,23,1)
    mc.setBlock(x+16,y-1,z-5,23,1)
    mc.setBlock(x+23,y-1,z+5,23,1)
    mc.setBlock(x+23,y-1,z-5,23,1)
    mc.setBlock(x+30,y-1,z+5,23,1)
    mc.setBlock(x+30,y-1,z-5,23,1)
    mc.setBlock(x+38,y-1,z+5,23,1)
    mc.setBlock(x+38,y-1,z-5,23,1)
    mc.setBlock(x+46,y-1,z+5,23,1)
    mc.setBlock(x+46,y-1,z-5,23,1)

    mc.setBlock(x+7,y+1,z+4,44,5)
    mc.setBlock(x+7,y+1,z-4,44,5)
    mc.setBlocks(x+6,y+1,z+4,x+4,y+1,z+5,44,5)
    mc.setBlocks(x+6,y+1,z-4,x+4,y+1,z-5,44,5)

    mc.setBlock(x+7,y+1,z,94)

    
def thezoo(x,y,z):

    StoneSlabEntrance(x,y,z)
    
    WoodBlocksEntrance(x,y,z)

    SeaLanternGlassEntrance(x,y,z)

    FrontWall(x,y,z)

    MainPath(x,y,z)

    MiddleCircle(x,y,z)

    MainTree(x,y,z)

    Fireworks(x,y,z)
    
thezoo(x,y,z)
