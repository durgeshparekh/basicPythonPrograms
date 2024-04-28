# Program to calculate factorial

# 3! = 3 * 2 * 1
# 2! = 2 * 1
# 6! = 6 * 5 * 4 * 3 * 2 * 1
def factorial_value(num):
    factorial_val = 1

    if num < 0:
        return 'Error: Factorial of a negative number is not defined'
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial_val = factorial_val * i

    return factorial_val


if __name__ == '__main__':
    print("Enter the number")
    number = int(input())
    print("The factorial of", str(number), "is", factorial_value(number))
    a = input()
