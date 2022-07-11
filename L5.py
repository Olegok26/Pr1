def print_number(limit):
    for i in range(limit):
        print(i)


n = int(input("n="))
print_number(n)
print()


def hello():
    print("Hello, World")
    print("(This text get printed from a function)")
    print()


def add_number(x1, x2):
    return x1 * x2


def main():
    hello()
    add_number(3, 2)
    result=add_number(8, add_number(5, 2))
    print(result)


main()
