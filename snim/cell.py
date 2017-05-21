from snim.snim_state import SnimState

class Cell:
    def __init__(self, x, y, state = SnimState.EMPTY):
        self.x = x
        self.y = y
        self.state = state

    def update(self, snim):
        neighbours = snim.get_diag_neighbours(self.x, self.y)
        neural_neighbours = sum(1 for n in neighbours if n.state is not SnimState.EMPTY)
        firing_neighbours = sum(1 for n in neighbours if n.state is SnimState.FIRING)

        if self.state is SnimState.EMPTY:
            # If all of the surrounding cells are living, spawn a new neuron
            if neural_neighbours is 4:
                self.state = SnimState.RESTING
                return

        if self.state is SnimState.FIRING:
            # If firing and there are no surrounding living cells, can't discharge so stay lit
            if neural_neighbours < 1:
                self.state = SnimState.FIRING
                return

            self.state = SnimState.RECOVERING
            return

        if self.state is SnimState.RECOVERING:
            # If recovering and over 2 neighbours are firing, reignite
            if firing_neighbours > 2:
                self.state = SnimState.FIRING
                return

            self.state = SnimState.RESTING
            return

        if self.state is SnimState.RESTING:
            # If resting and any neighbours fire, ignite
            if firing_neighbours >= 1:
                self.state = SnimState.FIRING
                return