import tkinter as tk
import random

class Creature(object):
	level = 0
	experience = 0
	hp = 100
	power = 10
	moveScope = 1
	visionScope = 2
	creatureVision = []
	resourceVision = []

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
	def __init__(self,name,row,col,ch,cw,wh,ww,w,canvas):
		self.name = name
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

    In version 1.0, move strategy is random by generator

    More higher-level tech (Machine learning methods) will be used for later versions.
    """
	def move(self,delay,canvas):
		while True:
		  if self.isAlive() == 0:
		  	canvas.delete(self.creature)
		  	return
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
			  self.hp -= 5
			  if self.isAlive() == 0:
				  print("Creature " + self.name + " died because of escaping from the world")
		  else:
			  self.row = self.row + horizontalMove * self.moveScope
			  self.col = self.col + verticalMove * self.moveScope
			  canvas.coords(self.creature,self.x1,self.y1,self.x2,self.y2)
			  self.hp -= 2
			  if self.isAlive() == 0:
				  print("Creature " + self.name + " died on the way to move")
			  else:
			      self.levelUp()
			  break
		self.world.after(delay, lambda: self.move(delay,canvas))

	"""	
	View method: Creature can view and detect around the world in the vision scope.
	             Vision knowledge of creature may help it decide how to choose next move.
	input: clist: creature list in the world (use to compare with location of this creature)
	       rlist: resource list in the world (use to compare with location of this creature)
	"""
	def view(self,clist,rlist):

		self.creatureVision = []
		self.resourceVision = []
		
		for ckey in clist:
			if clist[ckey] != 0 and clist[ckey].isAlive() == 1 and \
			   self.name != clist[ckey].name and \
			   abs(clist[ckey].row - self.row) >= 0 and \
			   abs(clist[ckey].row - self.row) <= self.visionScope and \
			   abs(clist[ckey].col - self.col) >= 0 and \
			   abs(clist[ckey].col - self.col) <= self.visionScope:
			     print("Creature " + str(self.name) + " detect creture " + str(clist[ckey].name))
			     self.creatureVision.append(clist[ckey])
		

		for rkey in rlist:
			if rlist[rkey] != 0 and \
			   abs(rlist[rkey].row - self.row) >= 0 and \
			   abs(rlist[rkey].row - self.row) <= self.visionScope and \
			   abs(rlist[rkey].col - self.col) >= 0 and \
			   abs(rlist[rkey].col - self.col) <= self.visionScope:
			     print("Creature " + str(self.name) + " detect resource.")
			     self.resourceVision.append(rlist[rkey])


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
	  	if self.visionScope < 6:
	  	  self.visionScope += 1

	def isAlive(self):
		if self.hp <= 0:
			return 0
		else:
		    return 1 