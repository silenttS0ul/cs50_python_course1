
import random

class Hat:
    #def __init__(self):# we remove init
    houses = ["Gry", "Huf" , "Rav", "Sly"]# we define a variable inside of my class


    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
        #OR
        # house = random.choice(self.houses)
        # print(name, "is in",  house)



# hat = Hat()
Hat.sort("Hatty")



