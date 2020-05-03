
from itertools import permutations

def solve_intcode(x, phase_setting, input_signal):
    x = x.copy()
    i = 0 # Initialize instruction pointer
    j = 0 # Initialize input counter
    while i < len(x):

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

        if opcode == 99:
            return None

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
            if phase_setting is not None and j == 0:
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


def any_break(signals):
    for sig in signals:
        if sig is None:
            return True
    return False

def output_signal(intcode, phase_seq, feedback):
    out = 0

    for i in range(5):
        out = solve_intcode(intcode, phase_setting=phase_seq[i], input_signal=out)

    if feedback:
        all_signals = []
        output_signals = []
        while True:
            for i in range(5):
                out = solve_intcode(intcode, phase_setting=None, input_signal=out)
                all_signals.append(out)
                if i == 5:
                    output_signals.append(out)
                if any_break(all_signals):
                    return output_signals[-1]

    return out


def max_signal(intcode, range, feedback):
    all_combi = list(permutations(range))
    all_signals = [output_signal(intcode, combi, feedback) for combi in all_combi]
    return max(all_signals)



with open('day7/input', 'r') as f:
    puzzle_input = f.read().splitlines()[0]

puzzle_input = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'

puzzle_input = puzzle_input.split(',')
puzzle_input = [int(x) for x in puzzle_input]

# Part 1

# output_signal(intcode=puzzle_input, phase_seq=[4,3,2,1,0], feedback=False)
# max_signal(intcode=puzzle_input, range=[0,1,2,3,4], feedback=False)

# Part 2

output_signal(intcode=puzzle_input, phase_seq=[9,8,7,6,5], feedback=True)
# max_signal(intcode=puzzle_input, range=[5,6,7,8,9], feedback=True)
