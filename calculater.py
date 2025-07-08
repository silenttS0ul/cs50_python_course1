# في السطر اعلاه قمنا بوضع اسم ملف للخليه حيث سوف يمكننا ان نستعملها كملف منفرد ونستدعي اي وظيفه نريدها
def main():
    x = int(input('what is the value of x'))
    print("x squard is ", square(x))


def square(n):
    return n + n # الاختبارات في الكودات القادمه مبنيه على لو ان هذا السطر كان
                #n + n
if __name__ == "__main__":
    main()
