from typing import List, Tuple, Dict
from collections import Counter


def find_sum(target: int, li: List[int]) -> Tuple[int, int]:
    #O(n^2)
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] + li[j] == target:
                return li[i], li[j]

    raise ValueError("No valid pair found")


def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    #O(n)
    seen = set()
    for num in li:
        complement = target - num
        if complement in seen:
            return complement, num
        seen.add(num)

    raise ValueError("No valid pair found")


def word_frequency(text: str) -> Dict[str, int]:
    #O(n)
    words = text.split()
    frequency = Counter(words)
    return dict(frequency)


def are_anagrams(str1: str, str2: str) -> bool:
    #O(n)
    return Counter(str1) == Counter(str2)

print(find_sum(5, [1, 2, 3, 4, 5]))
print(find_sum_fast(5, [1, 2, 3, 4, 5]))
print(word_frequency("This is a sample text. This text is a good example."))
print(are_anagrams("listen", "silent"))