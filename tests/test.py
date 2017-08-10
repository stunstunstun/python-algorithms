
def fibonacci(n: int):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


def test_fibonacci():
    """
    0 1 1 2 3 ...
    n = 3, output = 2
    """
    value = fibonacci(3)
    print(value)

if __name__ == "__main__":
    test_fibonacci()
