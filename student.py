
import sys

class Student:
    def __init__(self, name, house):# we should but self as a third argument and you can call it any thing you want
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gry", "Huf" , "Rav", "Sly"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
