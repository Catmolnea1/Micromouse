from collections import deque
from random import choice
import numpy as np



class pathf:
    def __init__(self):
        self.x = []
        self.y = []
        self.start = (15,0)
        self.position = self.start
        self.maze = np.full((16, 16), "1111", dtype="<U4")



    def dekstra(self, graph, start=(15, 0), goal=(8, 8)):
        distances = {node: float("inf") for node in graph}
        distances[start] = 0
        previous_n = {start: None}
        queue = deque([start])

        while queue:
            current_node = queue.popleft()

            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = previous_n[current_node]
                return path[::-1]

            for neighbor in graph.get(current_node, []):
                if distances[neighbor] == float("inf"):
                    distances[neighbor] = distances[current_node] + 1
                    previous_n[neighbor] = current_node
                    queue.append(neighbor)

        return []

    def return_maze(self):
        return self.maze

    def resize_maze(self, Sensor, position):
        n, n1 = self.get_cell(Sensor)
        if n1[0] == "0" and abs(position[0]) + 1 == len(self.maze):
            self.maze = np.pad(self.maze, ((1, 0), (0, 0)), mode='constant', constant_values="1111")
        if n1[1] == "0" and position[1] + 1 == len(self.maze[0]):
            self.maze = np.pad(self.maze, ((0, 0), (0, 1)), mode='constant', constant_values="1111")






    def en_mass(self, maze):
        graph = {}
        for i in range(len(maze)):
            for l in range(len(maze[i])):
                n = []
                cell = maze[i][l]
                if cell[0] == "0" and i > 0:
                    n.append((i - 1, l))
                if cell[1] == "0" and l < len(maze[i]) - 1:
                    n.append((i, l + 1))
                if cell[2] == "0" and i < len(maze) - 1:
                    n.append((i + 1, l))
                if cell[3] == "0" and l > 0:
                    n.append((i, l - 1))
                graph[(i, l)] = n
        return graph


    def get_cell(self, Sensor):
        n = ""
        n1 = ""
        for i in range(4):
            if Sensor[i+1] <= 70:
                n +="1"
            else: n += "0"
        if Sensor[5] == 90:
            n1 = n[-1:]+n[:-1]
        elif Sensor[5] == -180:
            n1 = n[-2:]+n[:-2]
        elif Sensor[5] == -90:
            n1 = n[-3:]+n[:-3]
        else: n1 = n
        return (n,n1)

    def shtoto_position(self, yaw, position):
        if yaw == 0:
            self.position = (position[0]-1, position[1])
        if yaw == 90:
            self.position = (position[0], position[1]+1)
        if yaw == -180:
            self.position = (position[0]+1, position[1])
        if yaw == -90:
            self.position = (position[0], position[1]-1)
        return self.position

    def ret_pos(self):
        return self.position


    def uncheck_neighbors(self, position, v1, stack):
        top = (position[0]-1, position[1])
        right = (position[0], position[1]+1)
        bottom = (position[0]+1, position[1])
        left = (position[0], position[1]-1)
        if v1[0] == "0" and top in stack:
            neighbors = top
        if v1[1] == "0" and right in stack:
            neighbors = right
        if v1[2] == "0" and bottom in stack:
            neighbors = bottom
        if v1[3] == "0" and left in stack:
            neighbors = left
        return neighbors



    def check_neighbors(self, position, v1, visited):
        neighbors = []
        top = (position[0]-1, position[1])
        right = (position[0], position[1]+1)
        bottom = (position[0]+1, position[1])
        left = (position[0], position[1]-1)
        if v1[0] == "0" and not top in visited:
            neighbors.append(top)
        if v1[1] == "0" and not right in visited:
            neighbors.append(right)
        if v1[2] == "0" and not bottom in visited:
            neighbors.append(bottom)
        if v1[3] == "0" and not left in visited:
            neighbors.append(left)
        return choice(neighbors) if neighbors else False

