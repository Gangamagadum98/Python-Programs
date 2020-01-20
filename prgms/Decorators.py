# Decorators - Add the extra features to the existing functions'

#suppose code is in another functioon , you dont want to change that function that time use decorators

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return  inner

div = smart_div(div)
div(2,4)


