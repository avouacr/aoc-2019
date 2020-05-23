
def solve_intcode(x, additional_memory):
    x = x + [0] * additional_memory
    outputs = []

    i = 0
    relative_base = 0

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
        elif par_modes[0] == 2:
            x1 = x[x[i + 1] + relative_base]

        if opcode in [1, 2, 5, 6, 7, 8]:
            # Second parameter not always needed
            if par_modes[1] == 0:
                x2 = x[x[i + 2]]
            elif par_modes[1] == 1:
                x2 = x[i + 2]
            elif par_modes[0] == 2:
                x2 = x[x[i + 2] + relative_base]

        if opcode == 1:
            result = x1 + x2
            x[x[i + 3]] = result
            n_para = 3
            i += (n_para + 1)

        elif opcode == 2:
            result = x1 * x2
            x[x[i + 3]] = result
            n_para = 3
            i += (n_para + 1)

        elif opcode == 3:
            result = int(input())
            x[x[i + 1]] = result
            n_para = 1
            i += (n_para + 1)

        elif opcode == 4:
            outputs.append(x1)
            n_para = 1
            i += (n_para + 1)

        elif opcode == 5:
            if x1 != 0:
                i = x2
            else:
                n_para = 2
                i += (n_para + 1)

        elif opcode == 6:
            if x1 == 0:
                i = x2
            else:
                n_para = 2
                i += (n_para + 1)

        elif opcode == 7:
            if x1 < x2:
                x[x[i + 3]] = 1
            else:
                x[x[i + 3]] = 0
            n_para = 3
            i += (n_para + 1)

        elif opcode == 8:
            if x1 == x2:
                x[x[i + 3]] = 1
            else:
                x[x[i + 3]] = 0
            n_para = 3
            i += (n_para + 1)

        elif opcode == 9:
            relative_base += x1
            n_para = 1
            i += (n_para + 1)

    return outputs


# puzzle_input = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'

with open('day9/input', 'r') as f:
    puzzle_input = f.read().splitlines()[0]

puzzle_input = puzzle_input.split(',')
puzzle_input = [int(x) for x in puzzle_input]
x = puzzle_input

# Part 1 & 2

solve_intcode(puzzle_input, 10000)
