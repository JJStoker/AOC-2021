import os
from collections import defaultdict

INPUT_FILE = "./sample.txt" if False else "./input.txt"

grid = defaultdict(str)
coordinates = []
instructions = []
with open(INPUT_FILE, "r") as input_file:
    for row in map(str.strip, input_file.readlines()):
        if ',' in row:
            coord = tuple(list(map(int, row.split(','))))
            coordinates.append(coord)
        elif row:
            instruction, amount = row.split('=')
            instructions.append((instruction.split(' ')[-1], int(amount)))
        
def initialize_grid():
    for y in range(max([c[1] for c in coordinates]) + 1):
        for x in range(max([c[0] for c in coordinates]) + 1):
            grid[(x, y)] = '.'
    for coord in coordinates:
        grid[coord] = '#'

def get_max_y():
    return max([c[1] for c in grid])

def get_max_x():
    return max([c[0] for c in grid])

def fold_grid(d='x', n=0):
    deleted = []
    if d == 'x':
        for x in range(get_max_x() + 1):
            if x < n: continue
            for y in range(get_max_y() + 1):
                val = grid[(x, y)]
                dx = (n - x) + n
                if 0 <= dx and val == '#':
                    grid[(dx, y)] = '#'
                del grid[(x, y)]
    else:
        for y in range(get_max_y() + 1):
            if y < n: continue
            for x in range(get_max_x() + 1):
                val = grid[(x, y)]
                dy = (n - y) + n
                if 0 <= dy and val == '#':
                    grid[(x, dy)] = '#'
                del grid[(x, y)]
    
def dump_grid():
    os.system("clear")
    for y in range(get_max_y() + 2):
        print (''.join([grid[(x, y)] for x in range(get_max_x() + 2)]), end='\n')

def count_dots():
    return len(list(filter(lambda x: x == '#', grid.values())))

def part_1():
    initialize_grid()
    x_or_y, n = instructions[0]
    fold_grid(d=x_or_y, n=n)
    dump_grid()
    print(f'Part 1: {count_dots()}')

part_1()
