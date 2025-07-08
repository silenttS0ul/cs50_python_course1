
import random

cards = ["jack", "queen", "king"]

def main():
    #print(random.choices(cards, k=2))
    #print(random.sample(cards, k=2))
    random.seed(1)#random.seed(0)
    print(random.choices(cards, k=2))


main()
