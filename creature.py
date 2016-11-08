import tkinter as tk
import random

class Creature(object):
	level = 0
	experience = 0
	hp = 100
	power = 10
	moveScope = 1
	visionScope = 2

	"""
	Constructor to create the creature at certain position of the world
	input: row: row position at the world
	       col: column position at the world
	       ch: cell height
	       cw: cell width
	       wh: world height
	       ww: world width
	       canvas: canvas of the world
	       w: world (use to call tkinter methods)
	"""
	def __init__(self,row,col,ch,cw,wh,ww,w,canvas):
		self.row = row
		self.col = col
		self.cellHeight = ch
		self.cellWidth = cw
		self.worldHeight = wh
		self.worldWidth = ww
		self.world = w
		self.x1 = self.col * self.cellWidth + self.cellWidth/12
		self.y1 = self.row * self.cellHeight + self.cellHeight/12
		self.x2 = self.x1 + 10/12 * self.cellWidth
		self.y2 = self.y1 + 10/12 * self.cellHeight
		self.creature = canvas.create_oval(self.x1,self.y1,self.x2,self.y2,fill="black")

	"""
	Move method: creature moves to certain position based on the move scope.

	A main activation function for the creature when it is alive until it is dead.

    In version 1.1, move strategy is random by generator

    More higher-level tech (Machine learning methods) will be used for later versions.
    """
	def move(self,delay,canvas):
		while True:
		  if self.isAlive() == 0:
		  	canvas.delete(self.creature)
		  	break
		  horizontalRandChoice = random.randint(1,10)
		  verticalRandChoice = random.randint(1,10)
		  randScope = random.randint(1,self.moveScope)
		  horizontalMove = 0
		  verticalMove = 0

		  if horizontalRandChoice < 5:
		  	horizontalMove = 1
		  elif horizontalRandChoice > 5:
		  	horizontalMove = -1
		  if verticalRandChoice < 5:
		  	verticalMove = 1
		  elif verticalRandChoice > 5:
		  	verticalMove = -1

		  x1old = self.x1
		  y1old = self.y1
		  x2old = self.x2
		  y2old = self.y2

		  self.x1 = self.x1 + horizontalMove * self.moveScope * self.cellWidth
		  self.y1 = self.y1 + verticalMove * self.moveScope * self.cellHeight
		  self.x2 = self.x2 + horizontalMove * self.moveScope * self.cellWidth
		  self.y2 = self.y2 + verticalMove * self.moveScope * self.cellHeight

		  if self.x1 < 0 or self.y1 < 0 or self.x2 > self.worldWidth or self.y2 > self.worldHeight:
		  	self.x1 = x1old
		  	self.y1 = y1old
		  	self.x2 = x2old
		  	self.y2 = y2old
		  	self.hp -= 10
		  else:
		  	canvas.coords(self.creature,self.x1,self.y1,self.x2,self.y2)
		  	self.levelUp()
		  	break
		self.world.after(delay, lambda: self.move(delay,canvas)) 

	def levelUp(self):
	  self.experience += 10
	  if self.experience == 1000:
	    self.level += 1
	    self.power += 2
	    self.hp += 20
	    self.experience = 0
	  if self.level % 10 == 0:
	  	if self.moveScope < 5:
	  	  self.moveScope += 1
	  	if self.visionScope < 10:
	  	  self.visionScope += 1

	def isAlive(self):
		if self.hp <= 0:
			return 0
		else:
		    return 1 