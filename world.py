import tkinter as tk
import random
from creature import Creature
from resource import Resource

class World(object):
	canHeight = 700
	canWidth = 700
	creatureNum = 0
	maxCreatureNum = 10
	names = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0}
	creatures = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0}
	month = 0
	year = 1

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
		self.month += 1
		if self.month % 13 == 0:
			self.year += 1
			self.month = 1
		print("Current year/month: " + str(self.year) + "/" + str(self.month))
		for n in self.creatures:
			if self.creatures[n] != 0 and self.creatures[n].isAlive() == 0:
				self.creatureNum -= 1
				print("creature " + self.creatures[n].name + " was dead")
				self.creatures[n] = 0
				self.names[n] = 0
		bornProb = random.random()
		bornThreshold = random.random()

		if self.creatureNum < self.maxCreatureNum and bornProb > bornThreshold:
			# In version 1.0, new-born creature cannot be at occupied location (no birth competition now)
			rowList = []
			colList = []
			for n in self.creatures:
				if self.creatures[n] != 0:
				  rowList.append(self.creatures[n].row)
				  colList.append(self.creatures[n].col)
			randRow = random.randint(0,self.rows-1)
			randCol = random.randint(0,self.cols-1)
			while randRow in rowList and randCol in colList:
				print("Location is occupied. Please rechoose new location for new-born creature")
				randRow = random.randint(0,self.rows-1)
				randCol = random.randint(0,self.cols-1)

			for key in self.names:
				if self.names[key] == 0:
					curName = key
					self.names[key] = 1
					break
			curCreature = self.addCreature(randRow,randCol,curName)
			self.creatures[curName] = curCreature
			curCreature.move(1000,self.space)
			print("Creature nums: " + str(self.creatureNum))
			print(curName + " is born")

		if self.creatureNum == self.maxCreatureNum:
			print("lives full")

		self.world.after(delay, lambda: self.runWorld(delay))




	def addCreature(self,row,col,name):
		c = Creature(name,row,col,self.cellHeight,self.cellWidth,self.canHeight,self.canWidth,self.world,self.space)
		self.creatureNum += 1
		return c
	
	def addResource(self,row,col):
		r = Resource(row,col,self.cellHeight,self.cellWidth,self.canHeight,self.canWidth,self.world,self.space)
		return r
