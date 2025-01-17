print(10 << 3)
#left shift (<<) multiplies the number by 2 with each shift

print(10 >> 1)
#right shift (>>) divides the number by 2 with each shift

print(bin(15))
#set bit is the number of '1's in the binary digits and 15 has 4 set bits / 1's
def totalsetbits(n):
    count = 0
    while(n):
        if (n & 1 == 1):
            count += 1
        n = n >> 1
    return count

print(totalsetbits(10))

def onesandzeros(n):
    ones = 0
    zeroes = 0
    while(n):
        if (n & 1 == 1):
            ones += 1
    else:
        zeroes +=1
    n = n >> 1
    return ones, zeroes
print(onesandzeros(5))