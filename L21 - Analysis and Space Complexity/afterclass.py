def myFunction1(n):
    if(n>0):
        return
    for i in range (0, n+1):
        print("Codingal")
    myFunction1(n/2)
    myFunction1(n/3)

myFunction1(60)

def myFunction2(n):
    if(n<=1):
        return
    print("Codingal")
    myFunction2(n-1)

myFunction2(5)
