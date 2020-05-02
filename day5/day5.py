
def solve_intcode(x):
    i = 0
    while x[i] != 99:

        x_i_str = str(x[i])
        # Handle multiple parameter modes
        if len(x_i_str) < 5:
            # Add trailing zeros
            x_i_str = (5 - len(x_i_str)) * '0' + x_i_str
        opcode = int(x_i_str[-2:]) # Extract opcode
        par_modes = x_i_str[:-2][::-1] # Put parameter modes in right order
        par_modes = [int(x) for x in par_modes]

        if par_modes[0] == 0:
            x1 = x[x[i + 1]]
        elif par_modes[0] == 1:
            x1 = x[i + 1]

        if opcode in [1, 2]:
            # Second parameter not always needed
            if par_modes[1] == 0:
                x2 = x[x[i + 2]]
            elif par_modes[1] == 1:
                x2 = x[i + 2]

        if opcode == 1:
            result = x1 + x2
            x[x[i + 3]] = result
            n_para = 3

        elif opcode == 2:
            result = x1 * x2
            x[x[i + 3]] = result
            n_para = 3

        elif opcode == 3:
            result = int(input())
            x[x[i + 1]] = result
            n_para = 1

        elif opcode == 4:
            print(x1)
            n_para = 1

        i += (n_para + 1)

    return True



with open('day5/input', 'r') as f:
    puzzle_input = f.read().splitlines()[0]

puzzle_input = puzzle_input.split(',')
puzzle_input = [int(x) for x in puzzle_input]

# Part 1

solve_intcode(puzzle_input)

# Part 2

