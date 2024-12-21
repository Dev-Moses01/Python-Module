def myFunction(n):
    total = 0
    steps = 0
    for i in range(0,n+1):
        print("First Loop")
        steps += 1
    print("The number of steps is:", steps)
    #Constant time complexity
        
    j=1
    steps = 0
    while(j<=n+1):
        print("Second Loop", j)
        j=j*2
        steps += 1
    print("The number of steps is:", steps)
    #Constant time complexity
    
    steps = 0
    for i in range(0, 100):
        print("Third Loop")
        steps +=1
    print("The number of steps is: ", steps)
    #Linear time complexity
    total += 1
    print("The total steps taken is: ", total)
myFunction(2)