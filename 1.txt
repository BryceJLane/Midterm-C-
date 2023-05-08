import random

def bubble_sort(arr, n):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def random_list(length, start=1, end=100):
    return [random.randint(start, end) for _ in range(length)]

if __name__ == "__main__":
    my_list = random_list(10)
    print("Unsorted list:", my_list)
    bubble_sort(my_list, len(my_list))
    print("Sorted list:", my_list)
