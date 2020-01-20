#reverse string
s1="hi hello"
def reverse(s):
    s2 = ""         # empty string since string is immutable
    for i in s:
        print(i)    # we are iterating over characters in a string
        s2=i+s2
    return s2
# palindrome string
# if("NAN" == reverse("NAN")):
#     print("Is a palindrome")

result = reverse(s1)
print(result)

# perfect square

def perfect(a):
    sum1 = 0
    for i in range(1,a):
        if(a%i==0):
            sum1=sum1+i
    if(a==sum1):
        print("It is perfect square")
    else:
        print("not perfect square")
perfect(6)

# Leap year
def leap(year):
    if(year%4 == 0 and year%100!=0 or year%400==0):
        print("It is leap year")
    else:
        print("It's not leap year")
leap(2023)

# bitwise

def clearRightBit(n):
    return n & n-1
print(clearRightBit(6))

# reverse no

def reversenum(n):
    while(n>0):
        rem = n % 10
        num = n//10
        res1 = (rem *10)+num
        return res1


res = reversenum(65)
print(res)


# factorial no


def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact



result = fact(4)
print(result)

# smallest divisor of any no

def divisor(n):
    for i in range(2,n):
        if(n%i==0):
            print(i)
            break;
divisor(6)

# or

def smallestDivisor(n):
    a=[]
    for i in range(2,n):
        if(n%i==0):
            a.append(i)
    return a
print(smallestDivisor(21).pop(0))