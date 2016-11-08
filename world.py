import tkinter as tk
import random
from creature import Creature

class World(object):
	canHeight = 700
	canWidth = 700
	creatureNum = 0
	names = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0}

	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols
		self.cellHeight = self.canHeight / self.rows
		self.cellWidth = self.canWidth / self.cols

	def createWorld(self):
		self.world = tk.Tk()
		self.world.title("Life World")
		self.space = tk.Canvas(self.world, bg="white", height=self.canHeight, width=self.canWidth)
		self.space.pack()

		self.cells = {}
		#self.creatureNumAtPt = {}

		for row in range(self.rows):
			for col in range(self.cols):
				x1 = col * self.cellWidth
				y1 = row * self.cellHeight
				x2 = x1 + self.cellWidth
				y2 = y1 + self.cellHeight
				self.cells[row,col] = self.space.create_rectangle(x1,y1,x2,y2)

	def runWorld(self,delay):
		bornProb = random.random()
		bornThreshold = random.random()

		if self.creatureNum < 10 and bornProb > bornThreshold:
			randRow = random.randint(0,self.rows-1)
			randCol = random.randint(0,self.cols-1)
			for key in self.names:
				if self.names[key] == 0:
					curName = key
					self.names[key] = 1
					break
			print(curName)
			curCreature = self.addCreature(randRow,randCol,curName)
			curCreature.move(1000,self.space)
		self.world.after(delay, lambda: self.runWorld(delay))




	def addCreature(self,row,col,name):
		c = Creature(name,row,col,self.cellHeight,self.cellWidth,self.canHeight,self.canWidth,self.world,self.space)
		self.creatureNum += 1
		return c