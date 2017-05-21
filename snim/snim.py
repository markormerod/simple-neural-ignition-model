from snim.snim_state import SnimState
from snim.cell import Cell

import time
import copy

class Snim:
    t = 0
    observers = []
    delta = 1

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.board = [[Cell(x, y) for x in range(w)] for y in range(h)]

    def run(self):
        while True:
            self.update()
            time.sleep(self.delta)

    def update(self):
        self.reset_count()

        new_board = copy.deepcopy(self.board)
        for row in new_board:
            for cell in row:
                cell.update(self)
                self.count_state(cell)

        self.board = new_board
        self.t += 1
        self.notify_observers()

    def reset_count(self):
        self.neurons = 0
        self.firing = 0
        self.resting = 0
        self.recovering = 0

    def count_state(self, cell):
        if cell.state is not SnimState.EMPTY:
            self.neurons += 1
        if cell.state is SnimState.FIRING:
            self.firing += 1
        if cell.state is SnimState.RESTING:
            self.resting += 1
        if cell.state is SnimState.RECOVERING:
            self.recovering += 1

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.notify(self)

    def get_diag_neighbours(self, x, y):
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i is not 0 and j is not 0:
                    # Prevent list wrap-around
                    if y + i < 0 or y + i >= self.height or x + j < 0 or x + j >= self.width:
                        neighbours.append(Cell(x + i, y + j))
                        continue
                    neighbours.append(self.board[y + i][x + j])
        return neighbours

    def set_state(self, x, y, state):
        self.board[y][x].state = state