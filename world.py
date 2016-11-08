import tkinter as tk

class World(object):
	canHeight = 700
	canWidth = 700

	def __init__(self,rows,cols):
		self.rows = rows
		self.cols = cols
		self.cellHeight = self.canHeight / self.rows
		self.cellWidth = self.canWidth / self.cols
		self.creatures = []

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

	def addCreature(self):
		return