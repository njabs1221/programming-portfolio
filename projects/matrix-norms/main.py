import math


def matrix_one_norm(matrix):
    column_count = len(matrix[0])
    best = 0

    for column in range(column_count):
        column_sum = 0
        for row in matrix:
            column_sum += abs(row[column])
        best = max(best, column_sum)

    return best


def matrix_infinity_norm(matrix):
    best = 0

    for row in matrix:
        row_sum = sum(abs(value) for value in row)
        best = max(best, row_sum)

    return best


def frobenius_norm(matrix):
    total = 0

    for row in matrix:
        for value in row:
            total += value ** 2

    return math.sqrt(total)


def main():
    rows, cols = map(int, input().split())
    matrix = []

    for _ in range(rows):
        row = [float(value) for value in input().split()]
        if len(row) != cols:
            raise ValueError("Each row must contain the expected number of columns")
        matrix.append(row)

    print(f"{matrix_one_norm(matrix):.6f}")
    print(f"{matrix_infinity_norm(matrix):.6f}")
    print(f"{frobenius_norm(matrix):.6f}")


if __name__ == "__main__":
    main()
