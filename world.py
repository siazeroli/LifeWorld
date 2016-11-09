import tkinter as tk
import random
from creature import Creature
from resource import Resource

class World(object):
	canHeight = 1000
	canWidth = 1000
	creatureNum = 0
	maxCreatureNum = 20
	resourceNum = 0
	maxResourceNum = 10
	names = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,\
	         'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0 ,'t': 0}
	creatures = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, \
	             'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0 ,'t': 0}
	resources = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0}
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

		for row in range(self.rows):
			for col in range(self.cols):
				x1 = col * self.cellWidth
				y1 = row * self.cellHeight
				x2 = x1 + self.cellWidth
				y2 = y1 + self.cellHeight
				self.cells[row,col] = self.space.create_rectangle(x1,y1,x2,y2)

	def runWorld(self,delay):

		# Count time
		self.month += 1
		if self.month % 13 == 0:
			self.year += 1
			self.month = 1
		print("\nCurrent year/month: " + str(self.year) + "/" + str(self.month))

        # Detect locations of all creatures and resources in the world
		creatureRowList = []
		creatureColList = []
		resourceRowList = []
		resourceColList = []

		for n in self.creatures:

			# Detect the dead creature from all current creature in the world
			if self.creatures[n] != 0 and self.creatures[n].isAlive() == 0:
				self.creatureNum -= 1
				self.creatures[n] = 0
				self.names[n] = 0
				continue

			if self.creatures[n] != 0:
				creatureRowList.append(self.creatures[n].row)
				creatureColList.append(self.creatures[n].col)

		for n in self.resources:

			# Decrease the duration of each resource at beginning of each year
			if self.resources[n] != 0 and self.year > 2 and self.month == 1:
				self.resources[n].existYear -= 1
				
			# Detect over-duration resources and delete
			if self.resources[n] != 0 and self.resources[n].isExist() == 0:
				print("Resource at (" + str(self.resources[n].row+1) + \
					  "," + str(self.resources[n].col+1) + ") exceeds the duration. Removed")
				self.space.delete(self.resources[n].resource)
				self.resourceNum -= 1
				self.resources[n] = 0
				continue

			if self.resources[n] != 0:
				resourceRowList.append(self.resources[n].row)
				resourceColList.append(self.resources[n].col)

		"""
		Release resource at a random location of the world each year if total number of
		resources are not larger than the allowable amount.
		In version 1.0, each resource cannot be released at occupied location.
		"""
		if self.resourceNum < self.maxResourceNum and self.month == 1 and self.year > 1:

			# Randomize location for new resource at non-occupied location
			randResourceRow = random.randint(0,self.rows-1)
			randResourceCol = random.randint(0,self.cols-1)

			while randResourceRow in creatureRowList and \
				  randResourceRow in resourceRowList and \
				  randResourceCol in creatureColList and \
				  randResourceCol in resourceColList:
					print("Location is occupied. Please rechoose new location for new resource")
					randResourceRow = random.randint(0,self.rows-1)
					randResourceCol = random.randint(0,self.cols-1)

			curResource = self.addResource(randResourceRow,randResourceCol)

			for key in self.resources:
				if self.resources[key] == 0:
					self.resources[key] = curResource
					break
				
			print("Resource nums: " + str(self.resourceNum))
			print("New Resource is released at (" + str(randResourceRow+1) + "," + str(randResourceCol+1) + ")")
		elif self.resourceNum >= self.maxResourceNum and self.month == 1 and self.year != 1:
			print("Cannot release more than " + str(self.maxResourceNum) + " resources.")
			
		"""
		Create new-born creature when creatures are not full and born prob is less than threshold
		In version 1.0, each month can have only one new-born creature
		"""
		# Randomize the born probability for new-born creature
		bornProb = random.random()
		bornThreshold = random.random()

		if self.creatureNum < self.maxCreatureNum and bornProb > bornThreshold:

            # Randomize location for new-born creature at non-occupied location
			# In version 1.0, new-born creature cannot be at occupied location (no birth competition now)
			randCreatureRow = random.randint(0,self.rows-1)
			randCreatureCol = random.randint(0,self.cols-1)
			while randCreatureRow in creatureRowList and \
			      randCreatureRow in resourceRowList and \
			      randCreatureCol in creatureColList and \
				  randCreatureCol in resourceColList:
				print("Location is occupied. Please rechoose new location for new-born creature")
				randCreatureRow = random.randint(0,self.rows-1)
				randCreatureCol = random.randint(0,self.cols-1)

            # Pick a name for new-born creature with non-occupied name
			for key in self.names:
				if self.names[key] == 0:
					curName = key
					self.names[key] = 1
					break

			# Create the new-born creature at given location with given name
			curCreature = self.addCreature(randCreatureRow,randCreatureCol,curName)

			# Add creature to creatures dictionary to keep track current alive creatures
			self.creatures[curName] = curCreature

			# Let new-born creature move
			curCreature.move(1000,self.space)

			print("Creature nums: " + str(self.creatureNum))
			print(curName + " is born at (" + str(randCreatureRow+1) + "," + str(randCreatureCol+1) + ")")

		if self.creatureNum == self.maxCreatureNum:
			print("lives full")

        # Keep the world runing
		self.world.after(delay, lambda: self.runWorld(delay))




	def addCreature(self,row,col,name):
		c = Creature(name,row,col,self.cellHeight,self.cellWidth,self.canHeight,self.canWidth,self.world,self.space)
		self.creatureNum += 1
		return c
	
	def addResource(self,row,col):
		r = Resource(row,col,self.cellHeight,self.cellWidth,self.canHeight,self.canWidth,self.world,self.space)
		self.resourceNum += 1
		return r
