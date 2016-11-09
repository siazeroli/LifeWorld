from world import World

def main():
	newWorld = World(200,200)
	newWorld.createWorld()
	newWorld.runWorld(1000)
	newWorld.world.mainloop()

main()