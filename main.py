from Mouse1 import Mouse
from pathfind import pathf
from drive import drived


class Main:
    def __init__(self):
        self.start = (0, 0)
        self.position = self.start
        self.goal = (8, 8)
        self.yaw = 0
        self.visited = []
        self.MASSIV()

    def MASSIV(self):
        current_cell = self.start
        stack = []
        while True:
            self.maze = Path.return_maze()
            self.Sensor = Mouse().sensor()
            v, v1 = Path.get_cell(self.Sensor)
            print(self.position)
            self.maze[self.position] = v1
            Path.resize_maze(self.Sensor, self.position,v1)
            print(self.maze)
            self.visited.append(current_cell)

            next_cell = Path.check_neighbors(self.position, v1, self.visited)
            if next_cell:
                self.visited.append(next_cell)
                stack.append(current_cell)
                current_cell = next_cell
                self.position = drived().movement(self.position, v, current_cell, self.Sensor[5])
            elif stack:
                neighbors = Path.uncheck_neighbors(self.position, v1, stack)
                self.position = drived().movement(self.position, v, neighbors, self.Sensor[5])
                current_cell = stack.pop()
            else:
                break
        print(1)
        print(self.maze)
        start = Path.find_start()
        print(start)
        drived().drive(self.maze, start)




Path = pathf()
main = Main()

