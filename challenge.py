from math import factorial

def task_1():
    number = input("Input your number: ")
    result = 0
    for i in range(len(number)):
        result += int(number[i])
    return result

def task_2():
    number = input("Input your number: ")

    result = factorial(int(number))

    return result

def task_3():
    number = int(input("Input your number: "))
    if number < 2:
        return 'Not prime!'
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return 'Not prime!'
    return 'Prime!'
#Variant 1 FIBB
def task_4():
    number = int(input("Input your number: "))
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

    return fibonacci(number)
#Variant 2 FIBB
def task_5():
    number = int(input("Input your number: "))
    def fibonacci(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
    return fibonacci(number)

def process_data():
    while True:
        try:
            data = input("Choose task 1, 2, 3, 4, 5, 6 - for exit: ")
            match data:
                case '1':
                    return print(task_1())
                case '2':
                    return print(task_2())
                case '3':
                    return print(task_3())
                case '4':
                    return print(task_4())
                case '5':
                    return print(task_5())
                case '6':
                    exit()
            raise ValueError
        except ValueError:
            print("Wrong input!")
if __name__ == '__main__':
    process_data()