
from calculater import square 
# هنا استطعنى استدعاء الوظيفه التي نريدها من الخليه السابقه
def main():
    test_square()


def test_square():
    if square(2) != 4:
        print('2 square was not 4')
    if square(3) != 9:
        print('3 squared was not 9')


if __name__ == "__main__":
    main()
