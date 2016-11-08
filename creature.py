import tkinter as tk

class Creature(object):
	level = 0
	experience = 0
	hp = 100
	moveScope = 1
    visionScope = 2

	def __init__(self,row,col,ch,cw):
		self.row = row
		self.col = col
		self.cellHeight = ch
		self.cellWidth = cw