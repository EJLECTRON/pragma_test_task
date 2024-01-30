""" Solution is made by brute force. Firstly I discovered that solutions of first congruence are
 x = 4 + 7 * k and then tries to find solutions of second congruence by substituting x in second congruence.
 I found that there is no solution of first congruence that satisfies second congruence."""

def calculate_solutions_first_congruence_manual() -> list:
    solutions = []
    func = lambda x: x**4 + x**3 + 2

    for i in range(7):
        if func(i) % 7 == 0:
            solutions.append(i)

    return solutions

def calculate_general_solution() -> tuple:
    possible_solutions = calculate_solutions_first_congruence_manual()
    solutions = []
    for i in range(possible_solutions[0], 343, 7):
        if (i**7 + i + 1) % 343 == 0:
            solutions.append(i)

    if len(solutions) == 0:
        return None
    else:
        return solutions, 343

if __name__ == "__main__":
    solution = calculate_general_solution()
    if solution == None:
        print("There is no solution")
    else:
        print("General solution: x ≡", calculate_general_solution[0], "mod", calculate_general_solution[1])

