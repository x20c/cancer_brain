import sys

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
    triangle = get_triangle(n)
    max_width = len("   ".join(str(num) for num in triangle[-1]))

    for row in triangle:
        row_str = "   ".join(str(num) for num in row)
        spaces = (max_width - len(row_str)) // 2
        print(" " * spaces + row_str)

def task_1():
    """

    Intersection and merge of two sorted lists

    a. Write a function that returns an intersection of two sorted lists of integers in non-decreasing order.

    b. Write a function that returns a merge of two sorted lists of integers  in non-decreasing order.

    """

    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_b = [1, 3, 4, 6, 7, 9]
    def sort_1(li1, li2):
        return sorted(li1 and li2)
    def sort_2(li1, li2):
        return sorted(li1 or li2)
    print('Task1')
    print(sort_1(list_a, list_b))
    print(sort_2(list_a, list_b))
def task_2():
    """

    Move zeroes

    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero

    elements.

    """
    a = [1,0,2,3,4,0,4]
    for i in range(len(a)):
        if a[i] == 0:
            a.remove(0)
            a.append(0)
    print('Task2\n', a)

def task_3():
    """

    Shuffle list

    Given a list, shuffle it so that the elements from the second half appear between the elements from the first half.

    """
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def shuffle(lst):
        centr = (len(lst)+1) // 2
        first_half, second_half = lst[:centr], lst[centr:]
        result = []
        for i in range(len(first_half)):
            result.append(first_half[i])
            if i < len(second_half):
                result.append(second_half[i])
        return result

    print('Task3\n' ,shuffle(list_a))

def task_4():
    """

    Greatest common divisor of list

    Given a list, find the greatest common divisor of all the elements in the list.

    """
    a = [4, 8, 16, 32]

    def find_gcd(lst):
        res = min(lst)
        while any(num % res for num in lst):
            res -= 1
        return res

    print('Task4\n', find_gcd(a))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <number_of_rows>")
        sys.exit(1)

    try:
        it = int(sys.argv[1])
        for row in get_triangle(it):
            print(row)
        pr_triangle(it)
        task_1()
        task_2()
        task_3()
        task_4()
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)