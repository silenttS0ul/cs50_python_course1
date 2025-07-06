
#make_package  (file)
def hello(name):
    print("hello, ", name)
def goodbey(name):
    print("goodbey, ", name)
def main():
    hello('would')
    goodbey('wourld')

if __name__ == '__main__':

    main()#من الخطا استعمال هذه هنا عند صنع اي حزمه لانها سوف تسبب مشكله و تقوم بطباعه الوظائف التي بداخلها وليس \\
      #الوظائف التي يريدها المستخدم
