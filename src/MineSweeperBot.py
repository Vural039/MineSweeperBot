import pyautogui
import time
import random

#(667, 222) = first tile expert 30x16
#(680,222) =first tile indermetiate 16x16
#(680,222) = first tile beginner 9x9
time.sleep(1)
Base_X=680
Base_Y=222
mouthX=680#control tile for begginer is:757,180 for the mouth and 757,171 for the glasses
mouthY=171#control tile for intermediate is:827,180 for the mouth and 827,171 for the glasses
glassesX=827#control tile for the expert is :954,180 for the mouth and 954,171 for the glasses
glassesY=171
Tile_Size=20
NumOfTilesX=16
NumOfTilesY=16

#Converting tiles to basic form, you give information to the bot via this func

def convTiles(x,y):
    return Base_X+x*Tile_Size, Base_Y+y*Tile_Size

#Information of tiles

def getValue(x,y):
    cx,cy=convTiles(x,y)
    color=pyautogui.pixel(cx,cy)
    colorCorner=pyautogui.pixel(cx-12,cy-15)
    colorFlagPoint=pyautogui.pixel(cx-4,cy-8)
    if colorCorner==(255,255,255):#Closed tile sittuation
        if colorFlagPoint==(255,0,0):#Flag sittuation
            return -3
        return -2
    elif color==(0,0,255)or color==(0,0,254):
        return 1
    elif color==(0,123,0) or color==(0,124,0) or color==(0,122,0):
        return 2
    elif color==(255,0,0) or color==(254,0,0):
        return 3
    elif color==(0,0,123) or color==(0,0,124) or color==(0,0,122):
        return 4
    elif color==(123,0,0) or color==(122,0,0) or color==(124,0,0):
        return 5
    elif color==(0,128,128) or color==(0,127,127):
        return 6
    elif color==(189,189,189):
        return 0
    elif color==(0,0,0):
        return -1
    
#Take neighbors
def getNeighbors(x,y):
    neighbors=[]

    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            nx,ny= x+dx, y+dy
            if (0<=nx and 0<=ny) and (nx<NumOfTilesX and ny<NumOfTilesY):
                neighbors.append((nx,ny))
    return neighbors

#Make field
grid=[]

for i in range(NumOfTilesY):
    grid.append([None]*NumOfTilesX)

#See how many flags around the tile
def countFlaggedNeighbors(grid, x, y):
    neighbors = getNeighbors(x, y)
    flagged_count = 0
    for (nx, ny) in neighbors:
        if grid[ny][nx] == -3: 
            flagged_count += 1
    return flagged_count

def click(x,y):#just click... you know
        pyautogui.click(*convTiles(x,y))

click(5,8)#start

#Main loop
condition=True
    
print(grid)
while condition:
    click(5,8)#start
    #Representing field vvvvvvv
    numberedTilesX=[]
    numberedTilesY=[]
    for x in range(NumOfTilesX):
        for y in range(NumOfTilesY):
            val= getValue(x,y)
            grid[y][x]=val #write x as y or y as x when calling array
            if grid[y][x] in [1,2,3,4,5,6,7,8]:
                numberedTilesX.append(x)
                numberedTilesY.append(y)
        print(grid)
    for x in numberedTilesX:#Puttin' flagss type shi
        for y in numberedTilesY:
            if grid[y][x] not in [0,1,2,3,4,5,6]:#Control the tile if its open 
                continue
            neighbors = getNeighbors(x,y)#take neighbors 
            closedNeighbors = []
            flaggedNeighbors = []
            for (nx,ny) in neighbors:#scanning neighbors for closed or flagged
                if grid[ny][nx] == -2: 
                    closedNeighbors.append((nx,ny))
                elif grid[ny][nx] == -3: 
                    flaggedNeighbors.append((nx,ny))
            if grid[y][x]== len(flaggedNeighbors):#if its already full flagged check
                continue
            if grid[y][x]== len(flaggedNeighbors)+len(closedNeighbors):#flag check
                for (nx, ny) in closedNeighbors:
                    if grid[ny][nx]!= -3:
                        pyautogui.rightClick(*convTiles(nx,ny))
                        grid[ny][nx]= -3
                        flaggedNeighbors.append((nx,ny))
                        time.sleep(0.3)
                        if grid[y][x]== len(flaggedNeighbors):
                            break
                        
    for x in numberedTilesX:
        for y in numberedTilesY:
            if grid[y][x] not in [1,2,3,4,5,6,7]:
                continue
            
            neighbors = getNeighbors(x,y)#take neighbors 
            closedNeighbors = []
            flaggedNeighbors = []
            for (nx,ny) in neighbors:#scanning neighbors for closed or flagged
                if grid[ny][nx] == -2: 
                    closedNeighbors.append((nx,ny))
                elif grid[ny][nx] == -3: 
                    flaggedNeighbors.append((nx,ny))
            flags= countFlaggedNeighbors(grid,x,y)
            if grid[y][x]==flags:
                for (nx,ny) in closedNeighbors:
                    click(nx,ny)
                    grid[ny][nx]=getValue(nx,ny)
    if pyautogui.pixel(mouthX,mouthY)!=(58,58,0):
        pyautogui.click(mouthX,mouthY)             
    elif pyautogui.pixel(glassesX,glassesY)!=(255,255,0):
        print("congrats")
        pyautogui.click(glassesX,glassesY)
        #condition=False

        

                     
                