
def fibonacci(numero: int):
    if numero <= 0:
        return 0
    if numero in [1, 2]:
        return 1

    two = [1, 1]

    def recursao(N: int):
        if N == 2:
            return

        two.append(sum(two))
        two.pop(0)
        recursao(N - 1)

    recursao(numero)
    return two[-1]


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(20))
