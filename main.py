import tkinter as tk
from world import World

def main():
	newWorld = World(30,30)
	newWorld.createWorld()
	newWorld.addCreature()
	newWorld.world.mainloop()

main()