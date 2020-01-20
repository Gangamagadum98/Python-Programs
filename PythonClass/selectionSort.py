# selection sort searches the smallest element each time and puts in the starting index of an array.

def select_sort(unsorted_list):

 # Outer loop to sort the entire list
 for i in range(0, len(unsorted_list)):
    # Inner loop to find the smallest number
    for j in range(i+1, len(unsorted_list)):
        if unsorted_list[i] > unsorted_list[j]:
            temp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[j]
            unsorted_list[j] = temp
 print(unsorted_list)

unsorted_list = [4, 9, 1, 2, 5]
select_sort(unsorted_list)


