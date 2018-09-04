#prime = [x for x in range(2,100) if all(x%y!=0 for y in range(2,x//2))]


l = [4,8,3,2,6,9,2,4,1]

l.append(7)
for a in l:
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            a = l[i]
            l[i] = l[i+1]
            l[i+1] = a
print(l)

'''
l1=[4,8,3,2,2,6,9]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

'''

my_dict = {}
for i in range(50):
    my_dict[i] = 2**i

print(my_dict)