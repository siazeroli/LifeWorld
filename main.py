import tkinter as tk
from world import World

def main():
	newWorld = World(30,30)
	newWorld.createWorld()
	newWorld.addCreature(0,0)
	newWorld.creatures[0,0].move(1,1,newWorld.space)
	newWorld.world.mainloop()

main()