from random import choice
from sys import stderr
from string import ascii_uppercase


while True:
    try:
        K = int(input("Enter the number of lists: "))
        list_rec = {}
        while K > 0:
            list_name = choice(ascii_uppercase) + str(K)
            print("An empty list {0}[] has been created".format(list_name))
            size = int(input("Enter the size of the list {0}: ".format(list_name)))
            buffer = []
            for num in range(size):
                buffer.append(int(input("Enter the {0} element of the list {1}: ".format(num+1, list_name))))
            list_rec[list_name] = buffer
            K -= 1

        print("The following records have been created {0}".format(list_rec))

        S_max = 0
        max_of_lists = [max(x)**2 for x in list_rec.values()]
        M = 1000
        for m in max_of_lists:
            S_max += (m)

        print(S_max)
        print(S_max % M)
        break

    except Exception:

        stderr.write("\n"+"*"*5+"_"*2+" Enter numbers only "+"_"*2+"*"*5+"\n")