def f2(x):
    x = x + 1 
    return x  
def f1(x):
    x = x * 2 
    y = f2(x)
    return y 


if __name__ =="__main__":
    y = 5 
    z = f1(y)