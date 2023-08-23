import pygame,sys 
pygame.init()
size=(900,700)
pant=pygame.display.set_mode(size)
clock=pygame.time.Clock()
dt=0
surface=pygame.image.load('image1.jpg').convert()
player_pos=pygame.Vector2(pant.get_width()/2,pant.get_height()/2)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    pant.fill("blue")
    
   
    
    pygame.display.flip()
    clock.tick(60)/1000
    

             