import pygame
from network import Network
import random
import time

def climbladder(score):
	if score == 1:return 38
	elif score == 4:return 14
	elif score == 9:return 31
	elif score == 21:return 42
	elif score == 28:return 84
	elif score == 51:return 67
	elif score == 72:return 91
	elif score == 80:return 99
	else:return 0

def snake(score):
	if score == 17:return 7
	elif score == 54:return 34
	elif score == 62:return 19
	elif score == 64:return 60
	elif score == 87:return 36
	elif score == 93:return 73
	elif score == 95:return 75
	elif score == 98:return 79
	else:return 0

pygame.init()

W, H = 1100, 700
board_size = 500

win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Snake-N-Ladder')
clock = pygame.time.Clock()

dice_img = [pygame.image.load('assets/dice1.png'),pygame.image.load('assets/dice2.png'), pygame.image.load('assets/dice3.png'), pygame.image.load('assets/dice4.png'), pygame.image.load('assets/dice5.png'), pygame.image.load('assets/dice6.png')]
board_img = pygame.image.load('assets/Snakes-and-Ladders-Bigger.jpg')
green = pygame.image.load('assets/greengoti.png')
red = pygame.image.load('assets/redgoti.png')
blue = pygame.image.load('assets/bluegoti.png')
yellow = pygame.image.load('assets/yellowgoti.png')

board_x = W/2- board_img.get_width()/2
board_y = H/2 - board_img.get_height()/2

def drawboard(win=win):
	win.blit(board_img,(board_width,board_height))

def getCoordinate(score):
	if score < 1:
		return (250,550)
	elif 0 < score < 11:
		return (250+score*50,550)
	elif 10 < score < 21:
		return (800-(score-10)*50,500)
	elif 20 < score < 31:
		return (250+(score-20)*50,450)
	elif 30 < score < 41:
		return (800-(score-30)*50,400)
	elif 40 < score < 51:
		return (250+(score-40)*50,350)
	elif 50 < score < 61:
		return (800-(score-50)*50,300)
	elif 60 < score < 71:
		return (250+(score-60)*50,250)
	elif 70 < score < 81:
		return (800-(score-70)*50,200)
	elif 80 < score < 91:
		return (250+(score-80)*50,150)
	elif 90 < score < 101:
		return (800-(score-90)*50,100)
	elif score >= 100:
		return (300,100)

class Dice():
	def __init__(self):
		self.value = 6

	def dicedraw(self):
		win.blit(dice_img[self.value-1],(board_width+board_size+150-dice_img[0].get_width()/2,H/2-dice_img[0].get_height()))	

	def diceupdate(self):
		self.value = random.randint(1,6)

class Player():
	def __init__(self,name,color,x=250,y=550):
		self.score = 0
		self.playername = name
		self.x = x
		self.y = y
		self.value = 6
		self.color = color
		self.turncount = 0
	
	def draw(self):
		win.blit(self.color,(getCoordinate(self.score)))

	def drawname(self):
		font = pygame.font.SysFont('comicsans',30)
		label = font.render(self.playername+"'s turn",1,(255,0,0))
		win.blit(label,(board_width+board_size+150-dice_img[0].get_width()/2,H/2-dice_img[0].get_height()+150))

def main(win):
	global playerlist
	run = True
	dice = Dice()
	playerlist = [Player("player1",red),Player("player2",blue)]
	turns = 0
	while run:
		win.fill((0,255,0))
		turn = turns%len(playerlist)
		drawboard()
		dice.dicedraw()
		playerlist[turn].drawname()

		for i in reversed(playerlist):
			i.draw()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
				Mouse_x, Mouse_y = pygame.mouse.get_pos()
				if board_width+board_size+150-dice_img[0].get_width()/2<Mouse_x<board_width+board_size+275-dice_img[0].get_width()/2:
					if H/2-dice_img[0].get_height()<Mouse_y<H/2-dice_img[0].get_height()+125:
						dice.diceupdate()
						playerlist[turn].turncount +=1

						if playerlist[turn].score+dice.value<=100:
							playerlist[turn].score +=dice.value
						if playerlist[turn].score == 100:
							run = False
						print(f"{playerlist[turn].playername} {dice.value}")
						
						up = climbladder(playerlist[turn].score)
						down = snake(playerlist[turn].score)

						if up !=0 or down !=0:
							playerlist[turn].score =(up+down)

						if playerlist[turn].turncount >=3 or down!=0:
							playerlist[turn].turncount = 0
						print(playerlist[turn].score)
						if (dice.value !=6 or down !=0) and up==0 and playerlist[turn].score != 100:
							playerlist[turn].turncount=0
							turns+=1
						print(turn)
		pygame.display.update()

	pygame.time.delay(3000)	
	win.fill((0,255,0))
	winner_font = pygame.font.SysFont("comicsans",50)
	won = winner_font.render(f"{playerlist[turn].playername} won the game",1,(100, 20, 50))
	win.blit(won,(W /2 -(won.get_width()/2),H/2 - won.get_height()/2))
	pygame.display.flip()	
	pygame.time.delay(3000)	

def main_menu():
	def draw_text_middle(text,color,size,win):
		font = pygame.font.SysFont('comicsans',size)
		label = font.render(text,1,color)
		win.blit(label,(W /2 -(label.get_width()/2),H/2 - label.get_height()/2))
	run = True
	while run:
		win.fill((0,255,0))
		draw_text_middle("Press any key to start...",(100, 20, 50),60,win)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				main(win)
main_menu()	