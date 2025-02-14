def get_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)
    return triangle


def pr_triangle(n):
    for i in range(n):
        # adjust space
        print(' ' * (n - i), end='')

        # compute each value in the row
        coef = 1
        for j in range(0, i + 1):
            print(coef, end=' ')
            coef = coef * (i - j) // (j + 1)
        print()

if __name__ == "__main__":
    it = int(input('Enter the row number: '))
    for row in get_triangle(it):
        print(row)
    pr_triangle(it)