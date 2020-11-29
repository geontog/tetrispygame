import pygame
import random
import math
pygame.init()

win = pygame.display.set_mode((250,500))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock() 



class block(object):
    def __init__(self, color):
        self.color = color
        self.phase = 1
        if color == "blue":
            self.parts = [[5,1], [4,0], [6,1], [4,1]]
            self.rgb = (3, 65, 174)
        elif color == "green":
            self.parts = [[4,1], [4,0], [5,2], [5,1]]
            self.rgb = (114, 203, 59)
        elif color == "yellow":
            self.parts = [[4,0], [5,1], [5,0], [4,1]]
            self.rgb = (255, 213, 0)
        elif color == "orange":
            self.parts = [[5,1], [4,1], [6,1], [6,0]]
            self.rgb = (255, 151, 28)
        elif color == "red":
            self.parts = [[4,1], [5,1], [5,0], [4,2]]
            self.rgb = (255, 50, 19)
        elif color == "teal":
            self.parts = [[4,3], [4,2], [4,1], [4,0]]
            self.rgb = (0,255,255)
        elif color == "purple":
            self.parts = [[5,1], [4,1], [5,0], [6,1]]
            self.rgb = (138,43,226)
        else: 
            self.parts = []
            self.color = ""
            self.rgb = ""

    def canMoveDown(self, size):
        canIt = True
        for part in self.parts:
            if part[1]+size >= floor[part[0]]:
                canIt = False
        return canIt

    def moveDown(self):
        for part in self.parts:
            part[1] = part[1]+1

    def canMoveLeft(self):
        canIt = True
        for part in self.parts:
            if part[0]-1 == -1:
                canIt = False
                break
            for ablock in blocks[:-1]:
                for parter in ablock.parts:
                    if parter[0] == part[0]-1 and parter[1] == part[1]:
                        canIt = False
                        break
        return canIt

    def moveLeft(self):
        for part in self.parts:
            part[0] = part[0]-1

    def canMoveRight(self):
        canIt = True
        for part in self.parts:
            if part[0]+1 == 10:
                canIt = False
                break
            for ablock in blocks[:-1]:
                for parter in ablock.parts:
                    if parter[0] == part[0]+1 and parter[1] == part[1]:
                        canIt = False
                        break
        return canIt

    def moveRight(self):
        for part in self.parts:
            part[0] = part[0]+1        

    def draw(self, win):
        for part in self.parts:
            pygame.draw.rect(win, self.rgb, (part[0]*25, part[1]*25, 25, 25), 0)
            pygame.draw.rect(win, (0,0,0), (part[0]*25, part[1]*25, 25, 25), 1)

    def rotate(self):
        if self.color == "purple":
            p = self.parts[0] #p = pivot
            self.parts.pop(1)
            if self.phase == 1:
                self.parts.append([p[0], p[1]+1])
            if self.phase == 2:
                self.parts.append([p[0]-1, p[1]])
            if self.phase == 3:
                self.parts.append([p[0], p[1]-1])
            if self.phase == 4:
                self.parts.append([p[0]+1, p[1]])
        elif self.color == "green":
            p = self.parts[0] #p = pivot
            self.parts.pop(1)
            self.parts.pop(1)
            if self.phase == 1:
                self.parts.append([p[0]-1, p[1]+1])
                self.parts.append([p[0], p[1]+1])
            if self.phase == 2:
                self.parts.append([p[0]-1, p[1]-1])
                self.parts.append([p[0]-1, p[1]])
            if self.phase == 3:
                self.parts.append([p[0]+1, p[1]-1])
                self.parts.append([p[0], p[1]-1])
            if self.phase == 4:
                self.parts.append([p[0]+1, p[1]+1])
                self.parts.append([p[0]+1, p[1]])
        elif self.color == "red":
            p = self.parts[0] #p = pivot
            self.parts.pop(1)
            self.parts.pop(1)
            if self.phase == 1:
                self.parts.append([p[0]+1, p[1]+1])
                self.parts.append([p[0]-1, p[1]])
            if self.phase == 2:
                self.parts.append([p[0]-1, p[1]+1])
                self.parts.append([p[0], p[1]-1])
            if self.phase == 3:
                self.parts.append([p[0]-1, p[1]-1])
                self.parts.append([p[0]+1, p[1]])
            if self.phase == 4:
                self.parts.append([p[0]+1, p[1]-1])
                self.parts.append([p[0], p[1]+1])
        elif self.color == "orange":
            p = self.parts[0] #p = pivot
            self.parts.pop()
            self.parts.pop()
            self.parts.pop()
            if self.phase == 1:
                self.parts.append([p[0], p[1]+1])
                self.parts.append([p[0], p[1]-1])
                self.parts.append([p[0]+1, p[1]+1])
            if self.phase == 2:
                self.parts.append([p[0]+1, p[1]])
                self.parts.append([p[0]-1, p[1]])
                self.parts.append([p[0]-1, p[1]+1])
            if self.phase == 3:
                self.parts.append([p[0], p[1]+1])
                self.parts.append([p[0], p[1]-1])
                self.parts.append([p[0]-1, p[1]-1])
            if self.phase == 4:
                self.parts.append([p[0]-1, p[1]])
                self.parts.append([p[0]+1, p[1]])
                self.parts.append([p[0]+1, p[1]+1])
        elif self.color == "blue":
            p = self.parts[0] #p = pivot
            self.parts.pop()
            self.parts.pop()
            self.parts.pop()
            if self.phase == 1:
                self.parts.append([p[0], p[1]+1])
                self.parts.append([p[0], p[1]-1])
                self.parts.append([p[0]+1, p[1]-1])
            if self.phase == 2:
                self.parts.append([p[0]+1, p[1]])
                self.parts.append([p[0]-1, p[1]])
                self.parts.append([p[0]+1, p[1]-1])
            if self.phase == 3:
                self.parts.append([p[0], p[1]+1])
                self.parts.append([p[0], p[1]-1])
                self.parts.append([p[0]+1, p[1]+1])
            if self.phase == 4:
                self.parts.append([p[0]-1, p[1]])
                self.parts.append([p[0]+1, p[1]])
                self.parts.append([p[0]-1, p[1]+1])
        elif self.color == "teal":
            p = self.parts[0] #p = pivot
            self.parts = []
            if self.phase == 1:
                self.parts.append([p[0]-1, p[1]-2])
                self.parts.append([p[0]+1, p[1]-2])
                self.parts.append([p[0], p[1]-2])
                self.parts.append([p[0]+2, p[1]-2])
            if self.phase == 2:
                self.parts.append([p[0]+2, p[1]-1])
                self.parts.append([p[0]+2, p[1]])
                self.parts.append([p[0]+2, p[1]+1])
                self.parts.append([p[0]+2, p[1]-2])
            if self.phase == 3:
                self.parts.append([p[0]+1, p[1]+2])
                self.parts.append([p[0]-1, p[1]+2])
                self.parts.append([p[0], p[1]+2])
                self.parts.append([p[0]-2, p[1]+2])
            if self.phase == 4:
                self.parts.append([p[0]-2, p[1]-2])
                self.parts.append([p[0]-2, p[1]-1])
                self.parts.append([p[0]-2, p[1]])
                self.parts.append([p[0]-2, p[1]+1])
        else:
            pass
        if self.phase == 4:
            self.phase = 1
        else:
            self.phase += 1

                



colors = ["blue", "green", "yellow", "orange", "red", "teal", "purple"]

def redrawGameWindow():
    win.fill((0,0,0))
    for block in blocks:
        block.draw(win)
    if hasntLost == False:
        win.blit(text, (40,200))
        win.blit(text2, (15,250))
    pygame.display.update()

font = pygame.font.SysFont('comicsans', 50, True)
font2 = pygame.font.SysFont('comicsans', 25, True)
text = font.render('You Lose', 1, (170,170,170))
text2 = font2.render('Press enter to play again', 1, (170,170,170))
firstBlock = block(colors[random.randint(0,6)])
blocks = [firstBlock]
floor = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
speed = 5
speedCounter = 0
hasntLost = True
run = True 
pygame.key.set_repeat(1000000, 120000)
while run:
    clock.tick(speed) 
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    print(keys, "\n")


    speedCounter = speedCounter + 1
    if speedCounter == 1500:
        speedCounter = 0
        speed = speed + 1
    activeBlock = blocks[-1]

    if hasntLost: 
        #IF ITS MOVING             
        if activeBlock.canMoveDown(1): 
            if keys[pygame.K_SPACE]:
                activeBlock.rotate()

            if keys[pygame.K_DOWN]:
                if activeBlock.canMoveDown(2):
                    activeBlock.moveDown()
            activeBlock.moveDown()

            if keys[pygame.K_LEFT]:
                if activeBlock.canMoveLeft():
                    activeBlock.moveLeft()
            if keys[pygame.K_RIGHT]:
                if activeBlock.canMoveRight():
                    activeBlock.moveRight()
        #IF IT AINT MOVING
        else:
            for part in activeBlock.parts:
                if floor[part[0]] > part[1]:
                    floor[part[0]] = part[1]
            floorsToCheck = [part[1] for part in activeBlock.parts]
            for floorNo in set(floorsToCheck):
                counter = 0
                for block1 in blocks:
                    for part1 in block1.parts:
                        if part1[1] == floorNo:
                            counter = counter + 1
                if counter == 10:   
                    for blockk in blocks:
                        toBeKept = []
                        for partt in blockk.parts:
                            if partt[1] != floorNo:
                                toBeKept.append(partt)  
                        blockk.parts = toBeKept
                    floor = [x+1 for x in floor]
                    for blockkk in blocks:
                        if blockkk.parts == []:
                            blocks.remove(blockkk)
                            continue
                        for parttt in blockkk.parts:
                            if parttt[1] < floorNo: 
                                parttt[1] = parttt[1] + 1 
            newBlock = block(colors[random.randint(0, 6)])  
            # newBlock = block(colors[5])  
            if newBlock.canMoveDown(1):
                blocks.append(newBlock)
            else:
                hasntLost = False     
    else:
        if keys[pygame.K_RETURN]:
            hasntLost = True
            newBlock = block(colors[random.randint(0,6)])  
            blocks = [newBlock]
            floor = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
            speed = 10
            speedCounter = 0
            
    redrawGameWindow()

pygame.quit()
