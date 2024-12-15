# algorithm = steps
#psuedo code = 
#time complexity = the time taken to complete an algorithm/step
#space complexity = the space required to complete an algorithm

def funct1(m):
    return m*(m+1)/2

#iteration m*(m+1)/2

print(funct1(100000000000))

def funct2(m):
    sum = 0
    for i in range(1,m+1):
        sum += i
    return sum

#iteration for a loop is longer

print(funct2(100000000000))
