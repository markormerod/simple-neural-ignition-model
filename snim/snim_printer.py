from snim.snim_state import SnimState

import os

class SnimPrinter:
    clear_key = 'clear' # Clear keyword to send to terminal for a Unix-based OS

    def __init__(self, snim):
        snim.register_observer(self)

        # If Windows, change clear command
        if os.name is 'nt':
            self.clear_key = 'cls'

    def notify(self, snim):
        self.draw(snim)

    def draw(self, snim):
        os.system(self.clear_key)

        print("Time: {} Neurons: {} Firing: {} Resting: {} Recovering: {}".format(snim.t, snim.neurons, snim.firing, snim.resting, snim.recovering))
        for row in snim.board:
            for cell in row:
                print(self.get_symbol(cell.state) + " ", end='')
            print('')

    def get_symbol(self, state):
        return {
            SnimState.EMPTY: " ",
            SnimState.RESTING: u"\u2606",
            SnimState.FIRING: u"\u2605",
            SnimState.RECOVERING: u"\u2022",
        }[state]