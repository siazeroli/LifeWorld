import tkinter as tk

class Creature(object):
	level = 0
	experience = 0
	hp = 100
	moveScope = 1
	visionScope = 2

    # constructor to create the creature at certain position of the world
	def __init__(self,row,col,ch,cw,canvas):
		self.row = row
		self.col = col
		self.cellHeight = ch
		self.cellWidth = cw
		self.x1 = self.col * self.cellWidth + self.cellWidth/12
		self.y1 = self.row * self.cellHeight + self.cellHeight/12
		self.x2 = self.x1 + 10/12 * self.cellWidth
		self.y2 = self.y1 + 10/12 * self.cellHeight
		self.creature = canvas.create_oval(self.x1,self.y1,self.x2,self.y2,fill="black")

	def move(self,horizontal,vertical,canvas):
		self.x1 = self.x1 + horizontal * self.cellWidth
		self.y1 = self.y1 + vertical * self.cellHeight
		self.x2 = self.x2 + horizontal * self.cellWidth
		self.y2 = self.y2 + vertical * self.cellHeight
		canvas.coords(self.creature,self.x1,self.y1,self.x2,self.y2)