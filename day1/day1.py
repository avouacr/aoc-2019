
# Part 1

def needed_fuel(mass):
    return mass // 3 - 2

with open('day1/input', 'r') as f:
    input = f.read().splitlines()

input = [int(x) for x in input]
total_fuel = sum([needed_fuel(x) for x in input])


# Part 2

def needed_fuel_rec(mass):
    fuel = needed_fuel(mass)
    fuels = []
    fuels.append(fuel)
    while fuel//3 - 2 > 0:
        fuel = needed_fuel(fuel)
        fuels.append(fuel)
    return sum(fuels)

total_fuel = sum([needed_fuel_rec(x) for x in input])