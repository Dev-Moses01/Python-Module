#Big O notation is a way of expressiong time complexity
#Big O(1) = constant time complexity eg, adding two numbers in one step, accessing an element/index in a list

def add(a,b):
    steps = 0
    print(a + b)
    steps += 1
    print("The number of steps taken is: ", steps)
add(100,100)


#Big O(n) = linear time complexity ==> the time taken increases proportionaly with the input size

def OnTime(n):
    steps = 0
    for i in range(1, n+1):
        print(i)
        steps += 1
    print("The number of steps is: ", n)

OnTime(1)

#Big O(n^2) => quadratic time complexity => time grows quadratically with the input size; the time doubles with the input, eg nested loop(loop inside another loop)

def oNsquaredTime(n):
    steps = 0
    for i in range(0, n):
        for i in range(0, n):
            print("*", end="")
            steps += 1
        print("")
    print("The number of steps is: ", steps)

oNsquaredTime(3)