from world import World

def main():
	newWorld = World(100,100)
	newWorld.createWorld()
	newWorld.runWorld(1000)
	newWorld.world.mainloop()

main()