def factorial(input):
    if (input == 1) | (input == 0):
        return 1
    return input*factorial(input-1)

num = int(input())
print(factorial(num))