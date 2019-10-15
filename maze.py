import pygame
pygame.init()
scrwidth = 500
scrheight = 500
win = pygame.display.set_mode((scrwidth, scrheight))

pygame.display.set_caption("MAZE OF DEATH!")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
walkUp = [pygame.image.load('U1.png'), pygame.image.load('U2.png'), pygame.image.load('U3.png'), pygame.image.load('U4.png'), pygame.image.load('U5.png'), pygame.image.load('U6.png'), pygame.image.load('U7.png'), pygame.image.load('U8.png'), pygame.image.load('U9.png')]
walkDown = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png'), pygame.image.load('D4.png'), pygame.image.load('D5.png'), pygame.image.load('D6.png'), pygame.image.load('D7.png'), pygame.image.load('D8.png'), pygame.image.load('D9.png')]
bg3 = pygame.image.load('bg3.png')
bg = pygame.image.load('win.jpg')
char = pygame.image.load('standing.png')
background = False
clock = pygame.time.Clock()

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 2
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        elif self.up:
            win.blit(walkUp[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        elif self.down:
            win.blit(walkDown[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        
        else:
            win.blit(char, (self.x,self.y))
def maze():
    if not background:
    #main boundaries
        pygame.draw.rect(win, (0,0,0), (50,80,320,4))
        pygame.draw.rect(win, (0,0,0), (420,80,50,4))
        pygame.draw.rect(win, (0,0,0), (50,80,4,280))
        pygame.draw.rect(win, (0,0,0), (50,430,4,50))
        pygame.draw.rect(win, (0,0,0), (50,480,420,4))
        pygame.draw.rect(win, (0,0,0), (470,80,4,404))
        
    #left
        pygame.draw.rect(win, (0,0,0), (50, 150, 150, 4))
        pygame.draw.rect(win, (0,0,0), (110, 115, 4, 35))
        pygame.draw.rect(win, (0,0,0), (110, 220, 4, 110))
        pygame.draw.rect(win, (0,0,0), (110, 330, 20, 4))
        pygame.draw.rect(win, (0,0,0), (130, 330, 4, 100))
        pygame.draw.rect(win, (0,0,0), (110, 426, 200, 4))
        pygame.draw.rect(win, (0,0,0), (110, 430, 4, 50))
        pygame.draw.rect(win, (0,0,0), (170, 80, 4, 30))
    #mid
        pygame.draw.rect(win, (0,0,0), (170, 110, 70, 4))
        pygame.draw.rect(win, (0,0,0), (240, 110, 4, 150))
        pygame.draw.rect(win, (0,0,0), (170, 260, 154, 4))
        pygame.draw.rect(win, (0,0,0), (324, 230, 4, 34))
        pygame.draw.rect(win, (0,0,0), (200, 220, 4, 110))
        pygame.draw.rect(win, (0,0,0), (200, 330, 40, 4))
        pygame.draw.rect(win, (0,0,0), (310, 380, 4, 50))
        pygame.draw.rect(win, (0,0,0), (130, 390, 25, 4))
        pygame.draw.rect(win, (0,0,0), (230, 400, 4, 30))
        pygame.draw.rect(win, (0,0,0), (240, 190, 120, 4))
        pygame.draw.rect(win, (0,0,0), (370, 80, 4, 60))
        pygame.draw.rect(win, (0,0,0), (320, 140, 54, 4))
    #right
        pygame.draw.rect(win, (0,0,0), (420, 80, 4, 40))
        pygame.draw.rect(win, (0,0,0), (430, 165, 40, 4))
        pygame.draw.rect(win, (0,0,0), (380, 425, 90, 4))
        pygame.draw.rect(win, (0,0,0), (380, 335, 4, 90))
        pygame.draw.rect(win, (0,0,0), (310, 335, 70, 4))
        pygame.draw.rect(win, (0,0,0), (380, 380, 40, 4))
        pygame.draw.rect(win, (0,0,0), (430, 320, 40, 4))
        pygame.draw.rect(win, (0,0,0), (430, 220, 4, 100))
        pygame.draw.rect(win, (0,0,0), (380, 270, 50, 4))   
    

def GameWindowRedraw():
    if background:
        win.blit(bg, (0,0))
    else:
        win.blit(bg3, (0,0))
    man.draw(win)
    maze()
    pygame.display.update()

man = player(370, 20,35,50)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and man.x > man.vel:
        if (50 <= man.x <= 372 and 31 <= man.y <= 83) or (man.x <= 56 and 79 <= man.y <= 360) or (man.x <= 55 and 379 <= man.y <= 482): ##boundaries
            man.x += 0
        elif (50 <= man.x <= 200 and 100 <= man.y <= 153) or (110 <= man.x <= 114 and 170 <= man.y <= 330) or (130 <= man.x <= 134 and 280 <= man.y <= 430): ##left
            man.x += 0
        elif (240 < man.x < 244 and 60 < man.y < 260) or (170 < man.x < 324 and 210 < man.y < 264) or (324 < man.x < 328 and 180 < man.y < 264) or (200 < man.x < 204 and 170 < man.y < 330) or (200 < man.x < 240 and 280 < man.y < 334) or (310 < man.x < 314 and 330 < man.y < 430) or (130 < man.x < 155 and 340 < man.y < 394) or (240 < man.x < 360 and 140 < man.y < 194) or (370 < man.x < 374 and 30 < man.y < 140): ##mid
            man.x += 0
        elif 380 < man.x < 384 and 285 < man.y < 400: ##right
            man.x += 0
        else:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.up = False
            man.down = False


    elif keys[pygame.K_RIGHT] and man.x < (scrwidth-man.width-man.vel):
        if (49 <= man.x+33 <= 369 and 31 <= man.y <= 83) or (man.x+33 >= 420 and 29 <= man.y <= 85) or (man.x+33 >= 470 and 80 <= man.y <= 484): ##boundaries
            man.x += 0
        elif (110 <= man.x+33 <=114 and 170 <= man.y <= 330) or (130 <= man.x+33 <= 134 and 280 <= man.y <= 430): ##left
            man.x += 0
        elif (205 < man.x < 209 and 60 < man.y < 260) or (135 < man.x < 324 and 210 < man.y < 264) or (289 < man.x < 293 and 180 < man.y < 264) or (165 < man.x < 169 and 170 < man.y < 330) or (275 < man.x < 279 and 330 < man.y < 430): ##mid
            man.x += 0
        elif (385 < man.x < 389 and 50 < man.y < 120) or (395 < man.x < 440 and 115 < man.y < 169) or (345 < man.x < 470 and 375 < man.y < 429) or (345 < man.x < 349 and 285 < man.y < 425) or (275 < man.x < 370 and 285 < man.y < 339) or (345 < man.x < 430 and 220 < man.y < 274): ##right
            man.x += 0
        else:
            man.x += man.vel
            man.left = False
            man.right = True
            man.up = False
            man.down = False


    elif keys[pygame.K_UP] and man.y > man.vel:
        if (50 <= man.x <= 370 and man.y <= 85) or (man.x + 33 >= 420 and 79 <= man.y <= 87): ##boundaries
            man.y += 0
        elif (50 <= man.x <= 200 and 150 <= man.y <= 154) or (77 <= man.x <= 113 and 220 <= man.y <= 330) or (170 < man.x < 275 and 110 < man.y < 114): ##left
            man.y += 0
        elif (205 < man.x < 244 and 110 < man.y < 260) or (135 < man.x < 324 and 260 < man.y < 264) or (165 < man.x < 204 and 220 < man.y < 330) or (165 < man.x < 240 and 330 < man.y < 334) or (300 < man.x < 374 and 140 < man.y < 144): ##mid
            man.y += 0
        elif (385 < man.x < 424 and 80 < man.y < 120) or (395 < man.x < 440 and 165 < man.y < 169): ##right
            man.y += 0
        else:
            man.y -= man.vel
            man.left = False
            man.right = False
            man.up = True
            man.down = False


    elif keys[pygame.K_DOWN] and man.y < (scrheight-man.height-man.vel):
        if (50 <= man.x <= 370 and 30 <= man.y <= 83) or (man.x+33 >= 420 and 25 <= man.y <= 83) or (49 <= man.x <= 470 and man.y >= 428): ##boundaries
            man.y += 0
        elif (77 <= man.x <= 114 and 170 <= man.y <= 330) or (80 < man.x < 135 and 280 < man.y < 430) or (110 < man.x < 310 and 376 < man.y < 430): ##left
            man.y += 0
        elif (135 < man.x < 324 and 210 < man.y < 214) or (289 < man.x < 329 and 180 < man.y < 260) or (165 < man.x < 204 and 170 < man.y < 330) or (200 < man.x < 240 and 280 < man.y < 284) or (275 < man.x < 314 and 330 < man.y < 430) or (95 < man.x < 155 and 340 < man.y < 344) or (240 < man.x < 360 and 140 < man.y < 144): ##mid
            man.y += 0
        elif (345 < man.x < 470 and 375 < man.y < 379) or (345 < man.x < 384 and 285 < man.y < 425) or (275 < man.x < 350 and 285 < man.y < 339) or (345 < man.x < 430 and 220 < man.y < 274): ##right
            man.y += 0
        else:
            man.y += man.vel
            man.left = False
            man.right = False
            man.up = False
            man.down = True
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
    if man.x < 40 and man.y > 360:
        background = True
    GameWindowRedraw()
pygame.quit()
