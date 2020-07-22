# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    #set the index value to iterate through the sorted arrays and merged the array
    k = 0
    i = 0
    j = 0

    #while index values are within the range
    while (i < len(arrA)) and (j < len(arrB)):
        #if the value at the index of the first array is <= to the value at the index
        #in the 2nd array, add it to the merged array and increasy i by 1
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1

        #otherwise, add the value in the 2nd array to merge array since it is smaller, increment j by 1
        else:
            merged_arr[k] = arrB[j]
            j += 1

        # increment k by 1 no matter what
        k += 1

    # account for when arrB is empty and arrA still has values
    while (i < len(arrA)):

        #each element gets added to merged_arr until index is out of range
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    # same thing for when arrA is empty and arrB still has values
    while (j < len(arrB)):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr

hi = [1, 2, 3, 7]
ih = [2, 5, 6, 8]
print(merge(hi, ih))
# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:

        # find the mid index so we can dlice into left and rigfht sublists
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        #recur on the left
        left = merge_sort(left)
        # recur on the right
        right = merge_sort(right)

        arr = merge(left, right)


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here

