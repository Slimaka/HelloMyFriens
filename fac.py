def factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result

if __name__ == "__main__":
    print(factorial(5))
