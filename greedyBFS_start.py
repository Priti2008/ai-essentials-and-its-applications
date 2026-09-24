# import heapq
# def greedy_bfs(graph, heuristics, start,goal):
#     queue=[]
#     heapq.heappush(queue,(heuristics[start],start))
#     visited=set()
#     while queue:
#         current_h,current_node = heapq.heappop(queue)
#         print(f"Cheacking node: {current_node} Distance estimate: {current_h}")
#         if current_node==goal:
#             print("Goal Reached!")
#             return 
#         visited.add(current_node)
#         for neighbor in graph[current_node];
#             if neighbor not in visited:
#                 heapq.heappush(queue,(heuristics[neighbor],neighbor))
#                 graph = {
#                     'A':['B','C'],
#                     'B':['D'],
#                     'C':['G'],
#                     'D':[],
#                     'G':[]
#                 }
#                 heuristics={
#                     'A':10',
#                     'B':8,
#                     'C':3,
#                     'D':6,
#                     'G':0
#                 }
# greedy_bfs(graph, heuristics, start='A',goal='G')

import heapq
def greedy_bfs(graph, heuristics, start,goal):
    queue=[]
    heapq.heappush(queue,(heuristics[start],start))
    visited=set()
    while queue:
        current_h,current_node = heapq.heappop(queue)
        print(f"Cheacking node: {current_node} Distance estimate: {current_h}")
        if current_node==goal:
            print("Goal Reached!")
            return 
        visited.add(current_node)
        for neighbor in graph[current_node];
            if neighbor not in visited:
                heapq.heappush(queue,(heuristics[neighbor],neighbor))
                graph = {
                    'A':['B','C'],
                    'B':['D'],
                    'C':['G'],
                    'D':[],
                    'G':[]
                }
                heuristics={
                    'A':10',
                    'B':8,
                    'C':3,
                    'D':6,
                    'G':0
                }
greedy_bfs(graph, heuristics, start='A',goal='G')