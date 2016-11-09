import tkinter as tk
import random

class Resource(object):

	existYear = 5

	def __init__(self,row,col,ch,cw,wh,ww,w,canvas):
		self.hp = random.randint(10,30)
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
		self.resource = canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill="red")
	
	def isExist(self):
		if self.existYear == 0:
			return 0
		else:
			return 1
		
