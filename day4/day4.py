
def has_double(x):
    x = str(x)
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            return True
    return False

def never_decreases(x):
    x = str(x)
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            return False
    return True

def count_meet_criteria(low, high):
    meet = []
    for x in range(low, high+1):
        if has_double(x) and never_decreases(x):
            meet.append(x)
    return len(meet)

def double_only(x):
    x = str(x)
    if has_double(x):
        x_list = list(x)
        for d in x_list:
            if x_list.count(d) == 2:
                return True
    return False

def count_meet_criteria2(low, high):
    meet = []
    for x in range(low, high+1):
        if never_decreases(x) and double_only(x):
            meet.append(x)
    return len(meet)


# Part 1
count_meet_criteria(130254, 678275)

# Part 2
count_meet_criteria2(130254, 678275)
