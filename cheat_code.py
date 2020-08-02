from init import grid_x, grid_y, UNIT_BLOCK
from algorithm import grassfire_path
import numpy as np

# Uncomment This to Run in A-Star Algorithm
# import networkx as nx

class cheat_code:
	def __init__(self):
		self.hack_route = np.empty(shape=(0, 0))
		self.hack_key = "A"

	def route(self, start, end):
		# Uncomment This to Run in A-Star Algorithm
		# g_grid = nx.grid_graph(dim=[grid_x, grid_y])

		def distance(a, b):
			(x1, y1) = a
			(x2, y2) = b
			return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

		hack_list = grassfire_path(start, end)
		# Uncomment This to Run in A-Star Algorithm
		# hack_list = nx.astar_path(g_grid, start, end, distance)

		if len(hack_list) > 0:
			self.hack_route = (np.vstack((np.asarray(hack_list[1:]), np.array([0, 0]))) - np.asarray(hack_list))[:-1]

	def hack(self, snake, food):
		if self.hack_route.shape[0] == 0:
			start = (snake[0][0] // UNIT_BLOCK, snake[0][1] // UNIT_BLOCK) 
			end = (food[0] // UNIT_BLOCK, food[1] // UNIT_BLOCK)
			self.route(start, end) 

		if(self.hack_route[0] == [1, 0]).all():
			self.hack_key = "D"

		elif(self.hack_route[0] == [-1, 0]).all():
			self.hack_key = "A"

		elif(self.hack_route[0] == [0, -1]).all():
			self.hack_key = "W"

		elif(self.hack_route[0] == [0, 1]).all():
			self.hack_key = "S"

		self.hack_route = self.hack_route[1:, :]
		return ord(self.hack_key)
