
A = [2, 5, 3, 1, 4, 7, 6]

def reversed_selection_sort(list):
    for i in range(len(A) - 1):
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] < A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

reversed_selection_sort(A)
print("Sorted array:")
for i in range(len(A)):
    print(A[i], end=" ")
print("\n")
#2:

list = [2, 5, 3, 1, 4, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]


def average_even_nums(alist):
    result = 0
    num_of_evens = 0
    for num in alist:

        if num % 2 == 0:
            result = result + num
            num_of_evens = num_of_evens + 1
    return result / num_of_evens

average = average_even_nums(list)
print("Average of even elements:", average)

