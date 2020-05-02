
# Part 1

def solve_intcode(x):
    i = 0
    while x[i] != 99:
        pos1 = x[i + 1]
        pos2 = x[i + 2]
        pos_overwrite = x[i + 3]
        if x[i] == 1:
            result = x[pos1] + x[pos2]
        elif x[i] == 2:
            result = x[pos1] * x[pos2]
        x[pos_overwrite] = result
        i += 4
    return x[0]

def init_problem(input, noun, verb):
    init = input.copy()
    init[1] = noun
    init[2] = verb
    return init

with open('day2/input', 'r') as f:
    input = f.read().splitlines()[0]

input = input.split(',')
input = [int(x) for x in input]

init = init_problem(input, 12, 2)
result = solve_intcode(init)
print(result)

# Part 2

def guess_init(output):
    for i in range(100):
        for j in range(100):
            init = init_problem(input, i, j)
            result = solve_intcode(init)
            if result == output:
                return 100*i + j

guess_init(19690720)
