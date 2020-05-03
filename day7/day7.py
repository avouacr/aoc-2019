
from itertools import permutations

def solve_intcode(x, phase_setting, input_signal):
    x = x.copy()
    i = 0 # Initialize instruction pointer
    j = 0 # Initialize input counter
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

        if opcode in [1, 2, 5, 6, 7, 8]:
            # Second parameter not always needed
            if par_modes[1] == 0:
                x2 = x[x[i + 2]]
            elif par_modes[1] == 1:
                x2 = x[i + 2]

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
            if j == 0:
                result = phase_setting
            else:
                result = input_signal
            x[x[i + 1]] = result
            n_para = 1
            i += (n_para + 1)
            j += 1

        elif opcode == 4:
            return x1
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


def output_signal(intcode, phase_seq):
    out = 0
    for i in range(5):
        out = solve_intcode(intcode, phase_setting=phase_seq[i], input_signal=out)
    return out


def max_signal(intcode):
    all_combi = list(permutations([0,1,2,3,4]))
    all_signals = [output_signal(intcode, combi) for combi in all_combi]
    return max(all_signals)



with open('day7/input', 'r') as f:
    puzzle_input = f.read().splitlines()[0]

# puzzle_input = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'

puzzle_input = puzzle_input.split(',')
puzzle_input = [int(x) for x in puzzle_input]

# Part 1

max_signal(intcode=puzzle_input)
