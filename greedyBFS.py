# def greedy_best_first_search(graph, heuristic, start, goal):
# 	# open_nodes contains nodes that we still need to visit.
# 	open_nodes = [start]
# 	visited = set()
# 	parent = {start: None}

# 	while open_nodes:
# 		# Choose the node that looks closest to the goal.
# 		current = min(open_nodes, key=lambda node: heuristic[node])
# 		open_nodes.remove(current)
# 		visited.add(current)

# 		if current == goal:
# 			path = []
# 			while current is not None:
# 				path.append(current)
# 				current = parent[current]
# 			return path[::-1]

# 		for neighbor in graph.get(current, []):
# 			if neighbor not in visited and neighbor not in open_nodes:
# 				parent[neighbor] = current
# 				open_nodes.append(neighbor)

# 	return None


# if __name__ == "__main__":
# 	graph = {
# 		"A": ["B", "C"],
# 		"B": ["D", "E"],
# 		"C": ["F"],
# 		"D": [],
# 		"E": ["G"],
# 		"F": ["G"],
# 		"G": [],
# 	}

# 	heuristic = {
# 		"A": 6,
# 		"B": 4,
# 		"C": 3,
# 		"D": 5,
# 		"E": 2,
# 		"F": 1,
# 		"G": 0,
# 	}

# 	path = greedy_best_first_search(graph, heuristic, "A", "G")
# 	print("Path found:", " -> ".join(path) if path else "No path found")
# def greedy_best_first_search(graph, heuristic, start, goal):
# 	# open_nodes contains nodes that we still need to visit.
# 	open_nodes = [start]
# 	visited = set()
# 	parent = {start: None}

# 	while open_nodes:
# 		# Choose the node that looks closest to the goal.
# 		current = min(open_nodes, key=lambda node: heuristic[node])
# 		open_nodes.remove(current)
# 		visited.add(current)

# 		if current == goal:
# 			path = []
# 			while current is not None:
# 				path.append(current)
# 				current = parent[current]
# 			return path[::-1]

# 		for neighbor in graph.get(current, []):
# 			if neighbor not in visited and neighbor not in open_nodes:
# 				parent[neighbor] = current
# 				open_nodes.append(neighbor)

# 	return None


# if __name__ == "__main__":
# 	graph = {
# 		"A": ["B", "C"],
# 		"B": ["D", "E"],
# 		"C": ["F"],
# 		"D": [],
# 		"E": ["G"],
# 		"F": ["G"],
# 		"G": [],
# 	}

# 	heuristic = {
# 		"A": 6,
# 		"B": 4,
# 		"C": 3,
# 		"D": 5,
# 		"E": 2,
# 		"F": 1,
# 		"G": 0,
# 	}

# 	path = greedy_best_first_search(graph, heuristic, "A", "G")
# 	print("Path found:", " -> ".join(path) if path else "No path found")
ef greedy_best_first_search(graph, heuristic, start, goal):
	# open_nodes contains nodes that we still need to visit.
	open_nodes = [start]
	visited = set()
	parent = {start: None}

	while open_nodes:
		# Choose the node that looks closest to the goal.
		current = min(open_nodes, key=lambda node: heuristic[node])
		open_nodes.remove(current)
		visited.add(current)

		if current == goal:
			path = []
			while current is not None:
				path.append(current)
				current = parent[current]
			return path[::-1]

		for neighbor in graph.get(current, []):
			if neighbor not in visited and neighbor not in open_nodes:
				parent[neighbor] = current
				open_nodes.append(neighbor)

	return None


if __name__ == "__main__":
	graph = {
		"A": ["B", "C"],
		"B": ["D", "E"],
		"C": ["F"],
		"D": [],
		"E": ["G"],
		"F": ["G"],
		"G": [],
	}

	heuristic = {
		"A": 6,
		"B": 4,
		"C": 3,
		"D": 5,
		"E": 2,
		"F": 1,
		"G": 0,
	}

	path = greedy_best_first_search(graph, heuristic, "A", "G")
	print("Path found:", " -> ".join(path) if path else "No path found")
