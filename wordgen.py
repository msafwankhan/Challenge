from random import *
from os import system

with open("sowpods.txt") as f:
    raw_dat = choice(f.readlines()).lower()

system("cls")
replay = True
word = raw_dat.rstrip("\n")
print(word)
count = len(word)
guess = ["_"] * count
chance = len(word)+3
print("\n{0}".format(" ".join(guess)))
print("\nNumber of alphabets are:", len(word))
used = []

while count >= 0 and chance > 0:
    print("\nThe number of chances left are: {0}".format(chance))
    letter = input("\nEnter a letter: ")
    indices = [i for i,j in enumerate(word) if j == letter]

    while(len(letter))!=1:
        letter = input("\nPlease enter only one alphabet at a time!: ")

    if letter.isalpha() and letter in word and letter not in used:
        print("\nThat's correct!")
        for i in indices:
            guess[i] = letter
        count -= word.count(letter)
        used.append(letter)
        if count == 0:
            print("\n{0} YOU WON! {0}\nThe word is: {1}" .format(("*"*5), word.upper()))
            break

    elif letter not in word or letter in used:
        if not letter.isalpha():
            print("\nEnter an alphabet")
        elif letter in used:
            print("\nThis alphabet has already been used!")
        else:
            print("\nWrong! Try again!!")
            used.append(letter)
            chance -= 1
            if chance == 0:
                print("\nYou Lose!\nThe word was:",word.upper())
                break


    print("\n{0}".format(" ".join(guess)))
    print("\nUsed letters are:"," ".join(used))

