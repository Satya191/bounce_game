import pygame
import time

pygame.init()

choosed = False

red = (255, 0, 0)
light_blue = (51, 255, 255)

x = 1000
y = 900

screen = pygame.display.set_mode((x, y))

pygame.display.set_caption('Simple Game')

running = True

font = pygame.font.Font('freesansbold.ttf', 48) 
font1 = pygame.font.Font('freesansbold.ttf', 28)
text = font.render('Do you want to be a boy or a girl?', True, red)
text1 = font.render('Boy', True, (0, 0, 0))
text2 = font.render('Girl', True, (0, 0, 0))
textRect = text.get_rect()
textRectb = text1.get_rect()
textRectg = text2.get_rect()
textRectb.center = (200, 500)
textRectg.center = (800, 500)
textRect.center = (500, 100)

player_img = 0
playerX=0
playerY=0

def show_player():
	screen.blit(player_img, (playerX, playerY))

def show_background():
	grass1 = pygame.image.load('grass.png')
	grass_img = pygame.transform.scale(grass1, (1000, 280))
	screen.blit(grass_img, (0, 640))

while not(choosed):
	screen.fill((0, 0, 0))
	pygame.draw.circle(screen, red, (200, 500), 80)
	pygame.draw.circle(screen, red, (800, 500), 80)
	screen.blit(text1, textRectb)
	screen.blit(text2, textRectg)
	screen.blit(text, textRect)
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			choosed = True	
		if event.type == pygame.MOUSEBUTTONDOWN:
  			if(pygame.mouse.get_pos()[0] > 120) and (pygame.mouse.get_pos()[0] < 280):
  				if(pygame.mouse.get_pos()[1] > 420) and (pygame.mouse.get_pos()[1] < 580):
  					player_img1 = pygame.image.load('brown_boy.png')
  					player_img = pygame.transform.scale(player_img1, (250, 300))
  					playerX = 380
  					playerY = 470
  					choosed = True
  			elif(pygame.mouse.get_pos()[0] > 720) and (pygame.mouse.get_pos()[0] < 880):
  				if(pygame.mouse.get_pos()[1] > 420) and (pygame.mouse.get_pos()[1] < 580):
  					player_img1 = pygame.image.load('blonde_girl.png')
  					player_img = pygame.transform.scale(player_img1, (250, 300))
  					playerX = 380
  					playerY = 470
  					choosed = True
	pygame.display.update()


while running:

	screen.fill(light_blue)	

	show_background()

	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			running = False	

	show_player()
	pygame.display.update()
