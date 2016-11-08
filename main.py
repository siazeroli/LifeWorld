import tkinter as tk
from world import World

def main():
	newWorld = World(100,100)
	newWorld.createWorld()
	newWorld.addCreature(50,50)
	newWorld.creatures[50,50].move(1000,newWorld.space)
	newWorld.world.mainloop()

main()