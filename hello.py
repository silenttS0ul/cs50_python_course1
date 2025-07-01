# package if you want make an import


def main():
    name = input("what is your name? ")
    hello(name)

def hello(to="world"):
    print("hello, ", to)

if __name__ == "__main__":
    main()