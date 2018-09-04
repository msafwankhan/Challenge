from time import sleep
from sys import stderr
while True:

    entry = input("Enter a number(To quit simply type quit or exit): ")

    try:
        f = bool
        num = int(entry)
        if num == 1 or num == 2: f = False

        for i in range(2, num+1 // 2):

            if num % i == 0:
                f = True
                break
            else:
                f = False
                break
        if f:
            print("{0} is not prime".format(num))
        else:
            print("{0} is prime".format(num))

    except ValueError as e:
        if entry.lower() == "exit" or entry.lower() == 'quit' :
            print("\n***\tExiting\t***")
            sleep(2)
            break
        else:
            stderr.writelines("Your value threw the following error: {0}.\nPlease enter a correct value!".format(e))


