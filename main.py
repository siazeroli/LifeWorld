import tkinter as tk
from world import World

def main():
	newWorld = World(30,30)
	newWorld.createWorld()
	newWorld.addCreature(1,1)
	newWorld.creatures[1,1].move(1000,newWorld.space)
	newWorld.world.mainloop()

main()