# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # i = j = k = 0 
    # for _ in range(0, len(merged_arr)):
    #     if i < len(arrA) and j < len(arrB):
    #         if arrA[i] < arrB[j]:
    #             merged_arr[k] == arrA[i]
    #             i =+ 1
    #         else:
    #             merged_arr[k] == arrB[j]
    #             j += 1
    #         k += 1
    #     elif i < len(arrA):
    #          merged_arr[k] == arrB[j]
    #          j += 1
    #          k += 1
    #     elif j < len(arrB):
    #          merged_arr[k] == arrA[i]
    #          i += 1
    #          k += 1

            



    # Your code here
    left_index = right_index = sorted_index = 0
    while left_index < len(arrA) and right_index < len(arrB):
        # check the first element in each list
        if arrA[left_index] < arrB[right_index]:
            # make the sorted index == correct one
            merged_arr[sorted_index] = arrA[left_index]
            left_index += 1
        else:
            merged_arr[sorted_index] = arrB[right_index]
            right_index += 1
        sorted_index += 1

    while left_index < len(arrA):
        merged_arr[sorted_index] = arrA[left_index]
        left_index += 1
        sorted_index += 1

    while right_index < len(arrB):
        merged_arr[sorted_index] = arrB[right_index]
        right_index += 1
        sorted_index += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        middle = len(arr)//2
        LHS = merge_sort(arr[:middle])
        RHS = merge_sort(arr[middle:])

        arr = merge(LHS, RHS)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

