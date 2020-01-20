def smallest(numlist):
    numlist.sort()
    odd_flag=False
    even_flag=False
    for i in range(0,len(numlist)):
        i=len(numlist)-1-i
        num=numlist[i]
        if(num%2==0):
            if even_flag == False:
                print("largest even number is" + str(num))
                even_flag=True
            else:
                if odd_flag==False:
                    print("largest odd number is"+str(num))
                    odd_flag=True
smallest([4,5,7,2,1])