def fibonacci(index: int):
    if index < 2:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))