import random

while True:
    reserve =random.randint(0,100)
    money = int(input("put a money on it: - "))
    counter = 0
    while counter < 3:
        num=int(input("guess the num: - "))

        if num ==reserve:
            print("correct")
            money = money*2
        elif num > reserve:
            print("guess lower")
            counter = counter + 1
        elif num < reserve:
            print("guess higher")
            counter = counter + 1
        elif ("correct,guess higher,guess lower")
            ask =input("game over \ndo u want to play again y/n -")
            if ask!="y":continue
            break