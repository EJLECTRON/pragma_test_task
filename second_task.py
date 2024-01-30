from sympy.ntheory.modular import solve_congruence
from math import gcd

def solve_congruence_with_x(first_coefficient: int, second_coefficient: int, third_coefficient: int) -> int:
    first_coefficient, second_coefficient = coprime(first_coefficient, second_coefficient)
    temp_multiplier = find_inverse_of_number(first_coefficient, third_coefficient)
    first_coefficient *= temp_multiplier
    second_coefficient *= temp_multiplier
    first_coefficient %= third_coefficient
    second_coefficient %= third_coefficient

    return second_coefficient

def coprime(first_coefficient: int, second_coefficient: int) -> tuple:
    temp_coef = gcd(first_coefficient, second_coefficient)

    return first_coefficient // temp_coef, second_coefficient // temp_coef

def find_inverse_of_number(number: int, modulo: int) -> int:
    return pow(number, -1, modulo)

if __name__ == "__main__":
    first_modulo = 5
    second_modulo = 6
    third_modulo = 7
    fourth_modulo = 11

    solution_first_pol = solve_congruence_with_x(2, 1, first_modulo)
    solution_second_pol = solve_congruence_with_x(3, 9, second_modulo)
    solution_third_pol = solve_congruence_with_x(4, 1, third_modulo)
    solution_fourth_pol = solve_congruence_with_x(5, 9, fourth_modulo)

    # print("Solution of first polynomial: x ≡", solution_first_pol, "mod", first_modulo)
    # print("Solution of second polynomial: x ≡", solution_second_pol, "mod", second_modulo)
    # print("Solution of third polynomial: x ≡", solution_third_pol, "mod", third_modulo)
    # print("Solution of fourth polynomial: x ≡", solution_fourth_pol, "mod", fourth_modulo)

    all_possible_solutions = solve_congruence((solution_first_pol, 5), (solution_second_pol, 6), (solution_third_pol, 7), (solution_fourth_pol, 11))

    print("All possible solutions: x ≡", all_possible_solutions[0], "mod", all_possible_solutions[1])
