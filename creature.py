import tkinter as tk

class Creature(object):
	level = 0
	experience = 0
	hp = 100
	moveScope = 1
	visionScope = 2

	def __init__(self,row,col,ch,cw,canvas):
		self.row = row
		self.col = col
		self.cellHeight = ch
		self.cellWidth = cw
		x1 = self.col * self.cellWidth + self.cellWidth/12
		y1 = self.row * self.cellHeight + self.cellHeight/12
		x2 = x1 + 10/12 * self.cellWidth
		y2 = y1 + 10/12 * self.cellHeight
		self.creature = canvas.create_oval(x1,y1,x2,y2,fill="black")