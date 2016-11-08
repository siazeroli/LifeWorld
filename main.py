from world import World
from resource import Resource

def main():
	newWorld = World(100,100)
	newWorld.createWorld()
	newWorld.runWorld(1000)
	newWorld.world.mainloop()

main()