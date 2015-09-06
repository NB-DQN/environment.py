class Environment:
    def __init__(self):
        self.__size = (9, 9)
        self.__maze = maze_generator.Maze(self.size)
        self.__current_coordinate = (0, 0)
        self.__move_count = 0
        self.__history = [self.current_coordinate]
        self.__novelty = 0

    def wall(self):
        return self.maze.wall(self.current_coordinate)

    def move(direction):
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
        flag = false
        for coordinate in self.history:
            if coordinate == self.current_coordinate:
                flag = true
                break
        if flag:
            self.novelty = 0
        else:
            self.novelty = 10
            self.history.append(self.current_coordinate)

    def reset(self):
        self.current_coordinate = (0, 0)
        self.move_count = 0
        self.history = [self.current_coordinate]
        self.novelty = 0
