#here are the formulas we are using in our quiz
#import them with * or a function at a time when needed
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    #for div we have to handle a division by zero as not defined
    if b == 0:
        return "Not Defined"
    else:
        return a/b
def mod(a,b):
    return a/b
def pow(a,b):
    return a**b
