#Task 1
class Interval:
    def __init__(self, start: int | float, end: int | float):
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise TypeError("Start and end must be numeric (int or float)")
        if start > end:
            raise ValueError("Start must be smaller than end")
        self.start = start
        self.end = end


    def __str__(self):
        return f'{self.start}, {self.end}'

interval = Interval(1, 5)
print(interval) # [1, 5]
#Task 2
class Interval:
    def __init__(self, start: int | float, end: int | float):
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise TypeError("Start and end must be numeric (int or float)")
        if start > end:
            raise ValueError("Start must be smaller than end")
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.start}, {self.end}'

    def is_overlapping(self, other_interval):
        if self.start > other_interval.end:
            return False
        elif self.end < other_interval.start:
            return False
        return self.start <= other_interval.start and self.end <= other_interval.end

interval1 = Interval(1, 5)
interval2 = Interval(3, 8)

overlap_result = interval1.is_overlapping(interval2)
print("Do intervals overlap?", overlap_result) # Do intervals overlap? True
#Task 3
class Interval:
    def __init__(self, start: int | float, end: int | float):
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise TypeError("Start and end must be numeric (int or float)")
        if start > end:
            raise ValueError("Start must be smaller than end")
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.start}, {self.end}'

    def is_overlapping(self, other_interval):
        if self.start > other_interval.end:
            return False
        elif self.end < other_interval.start:
            return False
        return self.start <= other_interval.start and self.end <= other_interval.end

    @staticmethod
    def intersection_static(interval1, interval2):
        start = max(interval1.start, interval2.start)
        end = min(interval1.end, interval2.end)
        if start <= end:
            return Interval(start, end)
        return None


interval1 = Interval(1, 5)
interval2 = Interval(3, 8)

intersection_result_static = Interval.intersection_static(interval1, interval2)
print("Intersection result (static method):", intersection_result_static) # Intersection result (static method): [3, 5]
#Task 4
class Interval:
    def __init__(self, start: int | float, end: int | float):
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise TypeError("Start and end must be numeric (int or float)")
        if start > end:
            raise ValueError("Start must be smaller than end")
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.start}, {self.end}'

    def is_overlapping(self, other_interval):
        if self.start > other_interval.end:
            return False
        elif self.end < other_interval.start:
            return False
        return self.start <= other_interval.start and self.end <= other_interval.end

    @staticmethod
    def intersection_static(interval1, interval2):
        start = max(interval1.start, interval2.start)
        end = min(interval1.end, interval2.end)
        if start <= end:
            return Interval(start, end)
        return None

    def __and__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented  # Підтримка тільки для об'єктів Interval
        return Interval.intersection_static(self, other)

interval1 = Interval(1, 5)
interval2 = Interval(3, 8)

intersection_result = interval1 & interval2
print("Intersection result:", intersection_result) # Intersection result: [3, 5]
#Task 5
class Interval:
    def __init__(self, start: int | float, end: int | float):
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise TypeError("Start and end must be numeric (int or float)")
        if start > end:
            raise ValueError("Start must be smaller than end")
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.start}, {self.end}'

    def is_overlapping(self, other_interval):
        if self.start > other_interval.end:
            return False
        elif self.end < other_interval.start:
            return False
        return self.start <= other_interval.start and self.end <= other_interval.end

    @staticmethod
    def intersection_static(interval1, interval2):
        start = max(interval1.start, interval2.start)
        end = min(interval1.end, interval2.end)
        if start <= end:
            return Interval(start, end)
        return None

    def __and__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented  # Підтримка тільки для об'єктів Interval
        return Interval.intersection_static(self, other)

    @staticmethod
    def union_static(interval1, interval2):
        if Interval.intersection_static(interval1, interval2) is None:
            return None

        start = min(interval1.start, interval2.start)
        end = max(interval1.end, interval2.end)
        return Interval(start, end)

interval1 = Interval(1, 5)
interval2 = Interval(3, 8)

union_result_static = Interval.union_static(interval1, interval2)
print("Union Result (Static method):", union_result_static) # Union Result (Static method): [1, 8]
#Task 6
class Interval:
    def __init__(self, start: int | float, end: int | float):
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise TypeError("Start and end must be numeric (int or float)")
        if start > end:
            raise ValueError("Start must be smaller than end")
        self.start = start
        self.end = end

    def __str__(self):
        return f'{self.start}, {self.end}'

    def is_overlapping(self, other_interval):
        if self.start > other_interval.end:
            return False
        elif self.end < other_interval.start:
            return False
        return self.start <= other_interval.start and self.end <= other_interval.end

    @staticmethod
    def intersection_static(interval1, interval2):
        start = max(interval1.start, interval2.start)
        end = min(interval1.end, interval2.end)
        if start <= end:
            return Interval(start, end)
        return None

    def __and__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented  # Підтримка тільки для об'єктів Interval
        return Interval.intersection_static(self, other)

    @staticmethod
    def union_static(interval1, interval2):
        if Interval.intersection_static(interval1, interval2) is None:
            return None

        start = min(interval1.start, interval2.start)
        end = max(interval1.end, interval2.end)
        return Interval(start, end)

    def __or__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        return Interval.union_static(self, other)


interval1 = Interval(1, 5)
interval2 = Interval(3, 8)

union_result = interval1 | interval2
print("Union Result:", union_result) # Union Result: [1, 8]
#Task 7
class Interval:
    def __init__(self, start: int | float, end: int | float):
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise TypeError("Start and end must be numeric (int or float)")
        if start > end:
            raise ValueError("Start must be smaller than end")
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Interval({self.start}, {self.end})"

    def __str__(self):
        return f'{self.start}, {self.end}'

    def is_overlapping(self, other_interval):
        if self.start > other_interval.end:
            return False
        elif self.end < other_interval.start:
            return False
        return self.start <= other_interval.start and self.end <= other_interval.end

    @staticmethod
    def intersection_static(interval1, interval2):
        start = max(interval1.start, interval2.start)
        end = min(interval1.end, interval2.end)
        if start <= end:
            return Interval(start, end)
        return None

    def __and__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented  # Підтримка тільки для об'єктів Interval
        return Interval.intersection_static(self, other)

    @staticmethod
    def union_static(interval1, interval2):
        if Interval.intersection_static(interval1, interval2) is None:
            return None

        start = min(interval1.start, interval2.start)
        end = max(interval1.end, interval2.end)
        return Interval(start, end)

    def __or__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        return Interval.union_static(self, other)

    def __sub__(self, other):
        if not isinstance(other, Interval):
            return NotImplemented
        intersection = Interval.intersection_static(self, other)

        if intersection is None:
            return [self]

        result = []

        if self.start < intersection.start:
            result.append(Interval(self.start, intersection.start))

        if self.end > intersection.end:
            result.append(Interval(intersection.end, self.end))

        return result


interval1 = Interval(1, 5)
interval2 = Interval(3, 8)

print("Difference Result:", interval1 - interval2) # Union Result: [1, 3]
print("Difference Result:", interval2 - interval1) # Union Result: [5, 8]