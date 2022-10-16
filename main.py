n: int = int(input("Введите число: "))


def getFibonacci(n: int):
    if n == 1 or n == 2:
        return 1
    else:
        return getFibonacci(n - 1) + getFibonacci(n - 2)


print(getFibonacci(n))
