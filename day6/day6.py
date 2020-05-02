
# input = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN""".splitlines()

with open('day6/input', 'r') as f:
    input = f.read().splitlines()
input = [x.split(')') for x in input]
tuples = [(x[0], x[1]) for x in input]

all_planets = []
for l1, l2 in tuples:
    all_planets.extend([l1, l2])
all_planets = list(set(all_planets))


def get_directs(planets):
    all_directs = []
    for l in planets:
        directs_l = [x[0] for x in tuples if x[1] == l]
        all_directs.extend(directs_l)
    return all_directs

def n_steps(start, end):
    encountered = [end]
    steps = 0
    while start not in encountered:
        encountered = get_directs(encountered)
        steps += 1
    return steps

def total_steps():
    counter = 0
    for l in all_planets:
        counter += n_steps('COM', l)
    return counter

def all_ancestors(p):
    encountered = [p]
    trajectory = []
    while 'COM' not in encountered:
        encountered = get_directs(encountered)
        trajectory.extend(encountered)
    return trajectory

def n_transfers_required(p1, p2):
    ancestors_p1 = all_ancestors(p1)
    ancestors_p2 = all_ancestors(p2)
    for p in ancestors_p1:
        if p in ancestors_p2:
            lowest_common_ancestor = p
            break
    return n_steps(lowest_common_ancestor, p1) + n_steps(lowest_common_ancestor, p2) - 2


# Part 1
total_steps()

# Part 2
n_transfers_required('YOU', 'SAN')
