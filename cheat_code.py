from init import *
import networkx as nx

grid_x = (width  // unit_block)
grid_y = (height  // unit_block)

class cheat_code:
	def __init__(self):
		self.astar_route = np.empty(shape = (0, 0))
		self.hack_key = "A"

	def route(self, start, end):
		g_grid = nx.grid_graph(dim = [grid_x, grid_y])  

		def distance(a, b):
			(x1, y1) = a
			(x2, y2) = b
			return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

		astar_list = nx.astar_path(g_grid, start, end, distance)
		if(len(astar_list) > 0):
			self.astar_route = ( np.vstack( (np.asarray(astar_list[1:]), np.array([0, 0])) ) - np.asarray(astar_list) )[:-1]
			#print(self.astar_route)

	def hack(self, snake, food):
		if(self.astar_route.shape[0] == 0):
			start = (snake[0][0] // unit_block, snake[0][1] // unit_block) 
			end   = (food[0] // unit_block, food[1] // unit_block) 
			self.route(start, end) 

		if(self.astar_route[0] == [1, 0]).all():
			self.hack_key = "D"

		elif(self.astar_route[0] == [-1, 0]).all():
			self.hack_key = "A"

		elif(self.astar_route[0] == [0, -1]).all():
			self.hack_key = "W"

		elif(self.astar_route[0] == [0, 1]).all():
			self.hack_key = "S"

		#print(self.astar_route[0], self.hack_key)
		self.astar_route = self.astar_route[1:, :]
		return ord(self.hack_key)
