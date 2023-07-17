def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def selection(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                index = j
        swap(arr, i, index)


def insertion(arr):
    length = len(arr)
    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, leftarr, rightarr, left, right):
    i, j, k = 0, 0, 0
    while i < left and j < right:
        if leftarr[i] < rightarr[j]:
            arr[k] = leftarr[i]
            k += 1
            i += 1
        else:
            arr[k] = rightarr[j]
            k += 1
            j += 1

    while i < left:
        arr[k] = leftarr[i]
        i += 1
        k += 1

    while j < right:
        arr[k] = rightarr[j]
        j += 1
        k += 1


def mergesort(array, l):
    if l == 1:
        return
    l = 0
    h = l - 1
    mid = l + ((h - l) // 2)
    leftarr = [0] * (mid + 1)
    right = [0] * (l - mid - 1)
    for i in range(0, mid + 1):
        leftarr[i] = array[i]
    for i in range(mid + 1, l):
        right[i - (mid + 1)] = array[i]
    mergesort(leftarr, mid + 1)
    mergesort(right, l - mid - 1)
    merge(array, leftarr, right, mid + 1, l - mid - 1)