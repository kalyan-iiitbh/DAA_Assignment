from math import floor
import random
import time
import sys
import matplotlib.pyplot as plot
from cProfile import label
from statistics import mean

# Defining all algorithms

def insertionSort(array):
    for i in range(1, len(array)):
        j = i-1
        key = array[i]
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j-1

    array[j+1] = key


def merge_sort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        leftArr = arr[:m]
        rightArr = arr[m:]

        merge_sort(leftArr)
        merge_sort(rightArr)

        i = 0
        j = 0
        k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i = i+1
            else:
                arr[k] = rightArr[j]
                j = j+1
            k = k+1

        while i < len(leftArr):
            arr[k] = leftArr[i]
            i = i+1
            k = k+1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j = j+1
            k = k+1
    return (arr)


def bubble_Sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[random.randint(low, high)]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def quick_sort(numbers):
    arr = numbers
    quickSort(arr, 0, len(arr) - 1)
    return arr


if __name__ == '__main__':
    _programStartTime = time.time()
    sys.setrecursionlimit(10**6)

    arr = [180, 280, 380, 480, 580]  # x-axis ticks for input quantity
    yTicks_insertion_sort = []  # plot y axis ticks
    yTicks_merge_sort = []
    yTicks_bubble_Sort = []
    yTicks_inplaceQuick_sort = []

    for index in range(0, len(arr)):
        runs = 1
        time_insertion_sort = []
        time_merge_sort = []
        time_bubble_Sort = []
        time_inplaceQuick_sort = []

        while runs < 4:
            randomArray = []
            for a in range(0, arr[index]):
                randomArray.append(random.randint(1, arr[index]+1))

            _startTime = time.time()
            insersionSort(randomArray[:])
            _endTime = time.time()
            time_insertion_sort.append((_endTime-_startTime)*1000)

            _startTime = time.time()
            merge_sort(randomArray[:])
            _endTime = time.time()
            time_merge_sort.append((_endTime-_startTime)*1000)

            _startTime = time.time()
            bubble_Sort(randomArray[:])
            _endTime = time.time()
            time_bubble_Sort.append((_endTime-_startTime)*1000)

            _startTime = time.time()
            quick_sort(randomArray[:])
            _endTime = time.time()
            time_inplaceQuick_sort.append((_endTime-_startTime)*1000)

            runs = runs+1

        yTicks_insertion_sort.append(mean(time_insertion_sort))
        yTicks_merge_sort.append(mean(time_merge_sort))
        yTicks_bubble_Sort.append(mean(time_bubble_Sort))
        yTicks_inplaceQuick_sort.append(mean(time_inplaceQuick_sort))

#     print("Program end time : ",(time.time()-_programStartTime)*1000)

    print("Array size: ,", "insertion Sort: ,", "Merge Sort: ,",
          "bubble Sort: ,", "InplaceQuick Sort: ")
    for i in range(0, len(arr)):
        print(arr[i], ",", yTicks_insertion_sort[i], ",", yTicks_merge_sort[i],
              ",", yTicks_bubble_Sort[i], ",", yTicks_inplaceQuick_sort[i])
    plot.plot(arr, yTicks_insertion_sort, 'g', label='Insertion Sort')
    plot.plot(arr, yTicks_merge_sort, 'y', label='Merge Sort')
    plot.plot(arr, yTicks_bubble_Sort, 'r', label='bubble Sort')
    plot.plot(arr, yTicks_inplaceQuick_sort, 'b', label='In-Place Quick Sort')

    plot.xlabel('Input Data Size')
    plot.ylabel('Time for sorting(milli seconds)')
    plot.legend(loc='upper left')

    plot.show()
