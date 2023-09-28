import random

cases = {}

def permute_case(case, n):
    cases = [case.copy()]
    for i in range(n):
        random.shuffle(case)
        cases.append(case.copy())
    return cases

def generate_case(size, case_length):
    case = []
    for i in range(case_length):
        case.append(random.randint(1, size))
    return case

def generate_cases(size, case_length, num_cases, num_permutations):
    cases = []
    for i in range(num_cases):
        case = generate_case(size, case_length)
        perms = permute_case(case, num_permutations)
        cases += perms
    return cases


def get_cases(size):
    if size not in cases:
        cases[size] = generate_cases(size, 100, 10, 10)
    return cases[size]