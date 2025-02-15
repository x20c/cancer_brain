from typing import List, Tuple

def find_max(li: List[int]) -> int:
    return li[-1]
print("O(1)")

def find_max(li: List[int]) -> int:
    max_el = li[0]
    for el in li:
        if el > max_el:
            max_el = el
    return max_el
print("O(n)")

n = 100

a = 1
b = n

def game(n: int):
    l, h = 1, n
    while l <= h:
        val = (l + h) // 2
        print(f'Is your numer {val}?')
        resp = input().strip().lower()
        if resp == 'bingo':
            print('Correct!')
            return val
        elif resp == '<':
            h = val - 1
        elif resp == '>':
            l = val + 1
    return None

gamer_num = game(n)
print(game)
print("O(log n)")