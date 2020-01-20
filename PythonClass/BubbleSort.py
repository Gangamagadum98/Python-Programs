def bubbleSort(unsorted_list):
    for i in range (0, len(unsorted_list)-1):
        for j in range (0, len(unsorted_list)-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = temp
    print(unsorted_list)








unsorted_list = [5,2,1,9,3,8,0]
bubbleSort(unsorted_list)