# Хусаинова Л. Р., 05-703, Сортировки
def insert_sort(A): #Функция сортировки вставками
    N = len(A) # вычисление длины массива А
    for top in range(1,N):
        k = top-1
        while k >- 1 and A[k] > A[k+1]:
            A[k], A[k+1] = A[k+1], A[k]
            k -= 1
def choise_sort(A):# Функция сортировки выбором
    N = len(A)
    for top in range(N):
        topmin = top
        for k in range(top+1, N):
            if A[topmin] > A[k]:
                A[topmin], A[k] = A[k], A[topmin]
def bubble_sort(A):# Функция сортировки пузырьком
    N = len(A)
    for top in range(N):
        i = top
        for k in range(1, N-i):
            if A[k-1] > A[k]:
                A[k-1], A[k] = A[k], A[k-1]

def test_array_sort(sort_algorithm): # Функция тестирования алгоритма
    # сортировки
    print("test#1")
    A = [5, 4, 3, 2, 1]
    A_sorted = [1, 2, 3, 4, 5] # отсортированный массив А
    sort_algorithm(A)
    print("Ok"if A == A_sorted else "Fail")# выводит ok, если массив
    # отсортировался после применения алгоритма, иначе fail
    print("test#2")
    A = [3, 4, 5, 2, 1]
    sort_algorithm(A)
    print("Ok"if A == A_sorted else "Fail")
    print("test#3")
    A = list(range(10,20))+list(range(1,10))
    A_sorted=list(range(1,20)) # создание списка целых чисел от 1 до 19
    sort_algorithm(A)
    print("Ok"if A == A_sorted else "Fail")
print("Insert sort")
test_array_sort(insert_sort)# проверка алгоритма сортитровки вставками
print("Choise sort")
test_array_sort(choise_sort)# проверка алгоритма сортировки выбором
print("Bubble sort")
test_array_sort(bubble_sort)# проверка алгоритма сортировки пузырьком