
import numpy as np

def path_to_coords(path):
    movements = path.split(',')
    coords = [(0,0)]

    for m in movements:
        x_start = coords[-1][0]
        y_start = coords[-1][1]

        if m[0] == 'U':
            y_end = y_start + int(m[1:])
            y_range = list(range(y_start + 1, y_end + 1))
            x_range = [x_start] * len(y_range)
        if m[0] == 'D':
            y_end = y_start - int(m[1:])
            y_range = list(range(y_end, y_start))[::-1]
            x_range = [x_start] * len(y_range)
        if m[0] == 'L':
            x_end = x_start - int(m[1:])
            x_range = list(range(x_end, x_start))[::-1]
            y_range = [y_start] * len(x_range)
        if m[0] == 'R':
            x_end = x_start + int(m[1:])
            x_range = list(range(x_start+1, x_end+1))
            y_range = [y_start] * len(x_range)

        coords.extend(list(zip(x_range, y_range)))

    return coords

def man_dist_origin(x):
    return abs(x[0]) + abs(x[1])

def min_mast_dist_intersection(path1, path2):
    coords1, coords2 = path_to_coords(path1), path_to_coords(path2)
    intersections = set(coords1) & set(coords2)
    intersections.remove((0,0))
    man_distances = [man_dist_origin(x) for x in intersections]
    return min(man_distances)

def min_steps_intersection(path1, path2):
    coords1, coords2 = path_to_coords(path1), path_to_coords(path2)
    intersections = set(coords1) & set(coords2)
    intersections.remove((0, 0))
    intersections = list(intersections)
    n_steps = [coords1.index(x) + coords2.index(x) for x in intersections]
    return min(n_steps)


path1, path2 = 'R8,U5,L5,D3', 'U7,R6,D4,L4'
path1, path2 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'
path1, path2 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'

with open('day3/input', 'r') as f:
    input = f.read().splitlines()

# Part 1

path1, path2 = input[0], input[1]
min_mast_dist_intersection(path1, path2)

# Part 2

min_steps_intersection(path1, path2)
