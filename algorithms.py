from random import sample
import time

program_start_time = time.time()

a = sample(range(1000000), 10000)

b = a.copy()

c = a.copy()

d = a.copy()

e = a.copy()

print('a =', a)


def selection_sort(a):
    for i in range(len(a) - 1):
        m_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m_index]:
                m_index = j
        a[i], a[m_index] = a[m_index], a[i]

    return a


start_time = time.time()

print(selection_sort(a))
print("Time taken by selection sort = ", time.time() - start_time)

print('b = ', b)


def bubble_sort(b):
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            if b[j] < b[i]:
                b[j], b[i] = b[i], b[j]
    return b


start_time = time.time()
print(bubble_sort(b))
print("Time taken by bubble sort = ", time.time() - start_time)

print('c = ', c)


def insertion_sort(c):
    for i in range(1, len(c)):
        value = c[i]
        hole = i
        while hole > 0 and c[hole - 1] > value:
            c[hole] = c[hole - 1]
            hole -= 1
        c[hole] = value
    return c


start_time = time.time()
print(insertion_sort(c))
print("Time taken by insertion sort = ", time.time() - start_time)


def merge(L, R, d):
    nL = len(L)
    nR = len(R)
    i = j = k = 0
    while i < nL and j < nR:
        if L[i] <= R[j]:
            d[k] = L[i]
            i += 1
        else:
            d[k] = R[j]
            j += 1
        k += 1
    while i < nL:
        d[k] = L[i]
        i += 1
        k += 1
    while j < nR:
        d[k] = R[j]
        j += 1
        k += 1


print('d = ', d)


def merge_sort(d):
    n = len(d)
    if n < 2:
        return d
    mid = n // 2
    l = [d[i] for i in range(mid)]
    r = [d[i] for i in range(mid, n)]
    merge_sort(l)
    merge_sort(r)
    merge(l, r, d)
    return d


start_time = time.time()
print(merge_sort(d))
print("Time taken by merge sort= ", time.time() - start_time)

print('e = ',e)


def partition(a, start, end):
    pivot = a[end]
    part_index = start - 1
    for i in range(start, end):
        if a[i] <= pivot:
            part_index += 1
            a[i], a[part_index] = a[part_index], a[i]

    a[part_index + 1], a[end] = a[end], a[part_index + 1]
    return part_index+1


def quick_sort(a, start, end):
    if start < end:
        part_index = partition(a, start, end)
        quick_sort(a, start, part_index - 1)
        quick_sort(a, part_index + 1, end)
    return a

start_time = time.time()
print(quick_sort(e,0,len(e)-1))
print("Time taken by quick sort= ", time.time() - start_time)



print('The program executed in ', time.time() - program_start_time)