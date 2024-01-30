""" The idea is to use Karatsuba trick for computing the product of two polynomials"""
def karatsuba_mult(poly1, poly2):
    n = max(len(poly1), len(poly2))
 
    if n == 1:
        return [poly1[0] * poly2[0]]

    mid = n // 2

    a, b = poly1[:mid], poly1[mid:]
    c, d = poly2[:mid], poly2[mid:]

    ac = karatsuba_mult(a, c)
    bd = karatsuba_mult(b, d)

    ad_bc = karatsuba_mult([ai + bi for ai, bi in zip(a, b)], [ci + di for ci, di in zip(c, d)]) - ac - bd

    result = ac + [0] * (2 * mid) + ad_bc + [0] * mid + bd

    return result

if __name__ == "__main__":
    poly1 = [1, 2, 3]  # Coefficients of the first polynomial, e.g., 1 + 2x + 3x^2
    poly2 = [4, 5, 6]  # Coefficients of the second polynomial, e.g., 4 + 5x + 6x^2

    result = karatsuba_mult(poly1, poly2)
    print(result)

