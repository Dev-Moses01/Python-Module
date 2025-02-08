def totalflip(number1, number2):
    flips = 0
    while(number1 > 0 or number2 > 0):
        t1 = (number1 & 1)
        t2 = (number2 & 1)
        if (t1 != t2):
            flips += 1
        #right shift - remove the last digit
        number1 >>= 1
        number2 >>= 1
    return flips

print(totalflip(2, 10))

#Power Set
def power_set_bitwise(s):
    n = len(s)
    power_set = []
    for i in range(1 << n):  # 2^n subsets
        subset = [s[j] for j in range(n) if (i & (1 << j)) > 0]
        power_set.append(subset)
    return power_set

print(power_set_bitwise([1, 2, 3]))
