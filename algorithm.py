from init import np
from init import grid_x, grid_y, UNIT_BLOCK
init_cost = -1


# Node Class(Structure)
class Node:
	def __init__(self, node):
		self.x = node[0]
		self.y = node[1]


# Find Cost Around(4 Nearest Nodes) a given Node
def find_neighbors(cost_matrix, i_node, cost_value):
	nearest_neighbors = []
	# 4 nearest neighbours : Top, Down, Left, Right
	nodes = [Node([i_node.x - 1, i_node.y]), Node([i_node.x + 1, i_node.y]), Node([i_node.x, i_node.y - 1]), Node([i_node.x, i_node.y + 1])]

	for node in nodes:
		# Check if the node is within the grid size
		if (node.x >= 0) and (node.x < grid_x) and (node.y >= 0) and (node.y < grid_y):
			# Check if the node is unvisited (Cost Value = -1 : Unvisited Node)
			if cost_matrix[node.y, node.x] == cost_value:
				nearest_neighbors.append(node)

	return nearest_neighbors


# Find Cost Matrix : Iterate to Find the Cost for All Nodes in The Grid
def find_cost_mat(cost_matrix, i_node):
	iteration_list = [i_node]

	while len(iteration_list) != 0:
		for i_node in iteration_list:
			n_neighbors = find_neighbors(cost_matrix, i_node, init_cost)

			for i in n_neighbors:
				cost_matrix[i.y, i.x] = cost_matrix[i_node.y, i_node.x] + 1

			# Add new neighbour nodes and remove the existing node from iteration list
			iteration_list.extend(n_neighbors)
			iteration_list = iteration_list[1:]


def path_planner(cost_matrix, i_node, i_cost):
	g_path = np.array([i_node.x, i_node.y])
	n_neighbors = [i_node]

	while i_cost != 0:
		i_cost = i_cost - 1
		n_neighbors = find_neighbors(cost_matrix, n_neighbors[0], i_cost)
		g_path = np.vstack((g_path, np.array([n_neighbors[0].x, n_neighbors[0].y])))
	return g_path


def grassfire_path(n_start, n_end):
	# Check if start and end node is valid
	if (Node(n_start).x < 0) and (Node(n_start).x >= grid_x) and (Node(n_start).y < 0) and (Node(n_start).y >= grid_y):
		print("Cannot Start from this Node")

	if (Node(n_end).x < 0) and (Node(n_end).x >= grid_x) and (Node(n_end).y < 0) and (Node(n_end).y >= grid_y):
		print("Cannot End at this Node")

	# print("Start and End \n", n_start, n_end)
	cost_matrix = init_cost * np.ones([grid_y, grid_x])

	# Start Node = 0, 0
	cost_matrix[Node(n_end).y, Node(n_end).x] = 0

	find_cost_mat(cost_matrix, Node(n_end))
	total_cost = cost_matrix[Node(n_start).y, Node(n_start).x]

	if total_cost == init_cost:
		print(" No Route Exists ")
	else:
		path = path_planner(cost_matrix, Node(n_start), total_cost)
	return path

#if __name__ == "__main__":
#	grassfire_path(n_start, n_end)