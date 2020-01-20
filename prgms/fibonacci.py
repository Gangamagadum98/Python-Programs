def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        if n>0:
            print(a)
            print(b)

            for i in range(2,n):
                c=a+b
                a=b
                b=c
                if c>n:
                    break
                else:
                    print(c)

        else:
            print('invalid no')
fib(100)