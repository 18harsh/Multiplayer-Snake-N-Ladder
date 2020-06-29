import pygame
import random

pygame.init()
from network import Network

width = 1100
height = 700
board_size = 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake-N-Ladder")
dice_img = [pygame.image.load('assets/dice1.png'),pygame.image.load('assets/dice2.png'), pygame.image.load('assets/dice3.png'), pygame.image.load('assets/dice4.png'), pygame.image.load('assets/dice5.png'), pygame.image.load('assets/dice6.png')]
board_img = pygame.image.load('assets/Snakes-and-Ladders-Bigger.jpg')
green = pygame.image.load('assets/greengoti.png')
red = pygame.image.load('assets/redgoti.png')
blue = pygame.image.load('assets/bluegoti.png')
yellow = pygame.image.load('assets/yellowgoti.png')

board_x = width/2- board_img.get_width()/2
board_y = height/2 - board_img.get_height()/2

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

	def draw(self):
		win.blit(dice_img[self.value-1],(board_x+board_size+150-dice_img[0].get_width()/2,height/2-dice_img[0].get_height()))	

	def update(self):
		self.value = random.randint(1,6)

class Player():
	def __init__(self,name,color,x=250,y=550):
		self.score = 0
		self.playername = name
		self.x = x
		self.y = y
		self.color = color
		self.turncount = 0
		self.count = 0

	def drawcoin(self,win):
		win.blit(self.color,(getCoordinate(self.score)))

	# def drawname(self):
	# 	font = pygame.font.SysFont('comicsans',30)
	# 	label = font.render(self.playername+"'s turn",1,(255,0,0))
	# 	win.blit(label,(board_x+board_size+150-dice_img[0].get_width()/2,height/2-dice_img[0].get_height()+150))

	def move(self,dice):
		keys = pygame.key.get_pressed()
		if pygame.mouse.get_pressed()[0]==1:
			Mouse_x, Mouse_y = pygame.mouse.get_pos()
			if board_x+board_size+150-dice_img[0].get_width()/2<Mouse_x<board_x+board_size+275-dice_img[0].get_width()/2:
				if height/2-dice_img[0].get_height()<Mouse_y<height/2-dice_img[0].get_height()+125:
					if self.count==0:
						self.count+=1
						dice.update()
						self.score += dice.value
						if climbladder(self.score) != 0:
							self.score = climbladder(self.score)
						elif snake(self.score)!=0:
							self.score = snake(self.score)
						return dice.value
		else:
			self.count=0
			return None


def read_pos(str):
    return int(str[0])


def make_pos(tup):
    return str(tup[0])

def redrawWindow(win,playerlist,dice,n):
	global turn
	win.fill((0,255,0))
	win.blit(board_img,(board_x,board_y))

	for j in reversed(playerlist):
		j.drawcoin(win)

	rply = (n.send((str(playerlist[1].score))))
	playerlist[0].score=int(rply)
	# playerlist[0].drawname()
	if playerlist[1].move(dice) != None:

		turn+=1

	dice.draw()

	pygame.display.update()

clientNumber = 0
turn=0
def main():
	n = Network()
	run = True
	clock = pygame.time.Clock()
	playerlist = [Player("player1",red),Player("player2",blue)]
	dice = Dice()
	score = read_pos(n.getPos())
	# print(score)
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		# n.send(make_pos())
		# scorelist = read_pos(n.send(make_pos((playerlist[1].score))))
		# playerlist[1].score = scorelist
		redrawWindow(win,playerlist,dice,n)

	pygame.quit()

main()