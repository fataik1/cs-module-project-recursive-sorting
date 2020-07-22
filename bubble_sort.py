def bubble_sort(arr):
    #we jbiw akk tghe elements are in sorted oreder when we do a full
    #pass throufh rhe array and perform no swaps
    swaps_occurred = True
    #iterate through the arr and look at elements two at a time
    #swap them if they're out of order
    while swaps_occurred:
        swaps_occurred = False
        #toggle swaps_occurred boolean to False
        # if we do this all the way through, all the elements will
        # eventually end up in a sorted order
        for i in range(len(arr) - 1):
            #we need to swap if arr[i] > arr[i+1]
            if arr[i] > arr[i+1]:
                #swap them
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True

    return arr
            #we know all the elements are sorted order when we do a full
    #pass through the array and perform no swaps

    #parallel to selection sort; build up the sorted portion of the array
    #start by putting the largest elements at the endof the array,
    # seond-largest at rhe second to last spot, etc.

    # the number of iterations through the array that we need to make is equal
    # to the number of the elements in the array

def recursive_bubble_sort(arr, unsorted_length):
        #base case
        #re use the swap_occured boolean idea
        # the boolean tells us when the "unsorted" portion of the list reaches 0
        # if the length of the unsorted portion is 0
    if unsorted_length > 0:
        recursive_bubble_sort(arr, unsorted_length - 1)
        #how do we get closer to a base case?
        # each pass shortens the unsorted portion by 1
        # each pass does the exact same thing as ehat it in the iterative implementation
    for i in range(unsorted_length - 1):
            # we need to swap if arr[i] > arr[i+1]
        if arr[i] > arr[i+1]:
            # swap them
            arr[i], arr[i+1] = arr[i+1], arr[i]
arr = [13, 15, 6, 18, 3, 27, 19, 22]
print(recursive_bubble_sort(arr, 3)) 