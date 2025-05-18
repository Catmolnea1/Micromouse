from Mouse1 import Mouse
from pathfind import pathf

class drived:

    def drive(self, maze):
        self.position = (15, 0)
        yaw1 = 0
        graph = pathf().en_mass(maze)
        path = pathf().dekstra(graph)
        for i in path[1:]:
            yaw = Mouse().sensor()[5] % 360
            if self.position[0] > i[0]:
                yaw1 = 0
                yaw2 = 0
            elif self.position[1] > i[1]:
                yaw1 = 270
                yaw2 = -90
            elif self.position[0] < i[0]:
                yaw1 = 180
                yaw2 = -180
            elif self.position[1] < i[1]:
                yaw1 = 90
                yaw2 = 90
            if abs(yaw - yaw1) == 180:
                Mouse().right()
                Mouse().right()
            elif yaw - yaw1 == -90 or yaw - yaw1 == 270:
                Mouse().right()
            elif yaw - yaw1 == 90 or yaw - yaw1 == -270:
                Mouse().left()
            Mouse().forward()
            self.position = pathf().shtoto_position(yaw2, self.position)

    def movement(self, position, v, current_cell, yaw0):
        yaw = yaw0 % 360
        if position[0] > current_cell[0]:
            yaw1 = 0
            yaw2 = 0
        elif position[1] > current_cell[1]:
            yaw1 = 270
            yaw2 = -90
        elif position[0] < current_cell[0]:
            yaw1 = 180
            yaw2 = -180
        elif position[1] < current_cell[1]:
            yaw1 = 90
            yaw2 = 90
        if abs(yaw - yaw1) == 180:
            Mouse().right()
            Mouse().right()
        elif yaw - yaw1 == -90 or yaw - yaw1 == 270:
            Mouse().right()
        elif yaw - yaw1 == 90 or yaw - yaw1 == -270:
            Mouse().left()
        Mouse().forward()
        position = pathf().shtoto_position(yaw2, position)
        return position