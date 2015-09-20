from .. import maze_generator
import math

class Environment:
    def __init__(self, size=(9, 9)):
        self.size = size
        self.maze = maze_generator.Maze(self.size)
        self.current_coordinate = (0, 0)
        self.move_count = 0
        self.history = [self.current_coordinate]
        self.novelty = 0

    def coordinate_id(self):
        return self.current_coordinate[0] + self.current_coordinate[1] * self.size[1]

    def get_coordinate_from_id(self, cid):
        x = cid % self.size[1]
        y = (cid - x) / self.size[1]
        return (x, y)

    def wall(self, cid=None):
        if cid is None:
            cid = self.coordinate_id()
        return self.maze.wall(self.get_coordinate_from_id(cid))

    def move(self, direction):
        neighbor = [ \
            (self.current_coordinate[0] + 1, self.current_coordinate[1]    ), \
            (self.current_coordinate[0] - 1, self.current_coordinate[1]    ), \
            (self.current_coordinate[0]    , self.current_coordinate[1] + 1), \
            (self.current_coordinate[0]    , self.current_coordinate[1] - 1)]
        if self.wall()[direction] == 0:
            self.current_coordinate = neighbor[direction]
        self.move_count += 1
        self._Environment__check_novelty()

    def __check_novelty(self):
        flag = False
        for coordinate in self.history:
            if coordinate == self.current_coordinate:
                flag = True
                break
        if flag:
            self.novelty = 0
        else:
            self.novelty = 10
            self.history.append(self.current_coordinate)

    def exit(self):
        return self.maze.is_exit(self.current_coordinate)

    def optical_targets(self):
        return [ \
            (          -1,           -1), \
            (self.size[0],           -1), \
            (          -1, self.size[1]), \
            (self.size[0], self.size[1])]

    def optical_params(self):
        distance = []
        for target in self.optical_targets():
            distance.append(math.sqrt( \
                (self.current_coordinate[0] - target[0]) ** 2 + \
                (self.current_coordinate[1] - target[1]) ** 2))
        return distance

    def reset(self):
        self.current_coordinate = (0, 0)
        self.move_count = 0
        self.history = [self.current_coordinate]
        self.novelty = 0
