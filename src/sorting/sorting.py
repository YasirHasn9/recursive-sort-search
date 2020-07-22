# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    index_left = index_right = 0
    for _ in range(elements):
        if index_left < len(arrA) and index_right < len(arrB):
            if arrA[index_left] <= arrB[index_right]:
                merged_arr.append(arrA[index_left])
                index_left += 1
            else:
                merged_arr.append(arrB[index_right])
                index_right += 1

        elif index_left == len(arrA):
            merged_arr.append(arrB[index_right])
            index_right += 1
        elif right_index == len(arrB):
             merged_arr.append(arrA[index_left])
             index_left += 1
    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

