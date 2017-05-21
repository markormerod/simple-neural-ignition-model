from snim.snim import Snim
from snim.snim_state import SnimState
from snim.snim_printer import SnimPrinter

import random
import argparse

parser = argparse.ArgumentParser(description='Run a Simple Neutral Ignition Model!')
parser.add_argument('--delta', dest='delta', default=1, type=float,
                    help='Specifies the time in seconds between each update (default: 1)')
parser.add_argument('--width', dest='width', default=20, type=int,
                    help='Specifies the width of the board (default: 20)')
parser.add_argument('--height', dest='height', default=20, type=int,
                    help='Specifies the height of the board (default: 20)')
parser.add_argument('--empty', dest='empty', default=50, type=float,
                    help='Chance of a given cell having initial state empty (0-100) (default: 50)')
parser.add_argument('--firing', dest='firing', default=50, type=float,
                    help='Chance of a given living cell having initial state firing (0-100) (default: 50)')

args = parser.parse_args()

snim = Snim(args.width, args.height)
snim.delta = args.delta
snim_print = SnimPrinter(snim)

for i in range(args.height):
    for j in range(args.width):

        if random.random() < args.empty / 100:
            state = SnimState.EMPTY

        else:
            if random.random() < args.firing / 100:
                state = SnimState.FIRING
            else:
                state = SnimState.RESTING

        snim.set_state(j, i, state)

snim.run()