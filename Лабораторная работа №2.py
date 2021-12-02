#швидке сортування:
def bubble_sort(array):
    trigger = True
    while trigger:
        trigger = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                trigger = True
list1 = [int(s) for s in input("Введите масив целых чисел: ") .split()]
bubble_sort(list1)
print (list1)

#пошук елементу за значенням:
h = int(input("Введите индекс числа для пошуку значение: "))
def value_search(list1, h):
    for i in list1:
        if list1.index(i):
                return list1[h]
print ("значение: ", value_search(list1,h))

#пошук послідовності елементів:
k = int(input("Введите число для пошуку индекса: "))
def index_search(list1, k):
    for i in list1:
        if i == k:
                return list1.index(i)
print ("индекс: ", index_search(list1,k))

#пошук перших п`яти мінімальних елементів:
add = list1
def first_min(list1, add):
    bubble_sort(list1)
    return add[:5]
print ("5 наименьшие значения: ", first_min(list1,add))

#пошук перших п`яти максимальних елементів:
add = list1
def first_max(list1, add):
    bubble_sort(list1)
    list1.reverse()
    return add[:5]
print ("5 наибольшие значение: ", first_max(list1,add))

#пошук середнього арифметичного:
def average(a):
    return (sum(list1)/len(list1))
print ("середне арифметичне масыва: ", average(list1))

#повернення списку, що сформований з початкового списку, але не містить повторів (залишая лише перший з однакових елементів):
def without_repeating(list1):
    m = []
    for i in list1:
        if i not in  m:
            m.append(i)
    return m
print (without_repeating(list1))