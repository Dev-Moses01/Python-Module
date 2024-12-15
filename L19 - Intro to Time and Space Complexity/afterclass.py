def funct1(N, M):
    return N*(N+1)/2 * M

print(funct1(4, 2))

def funct2(N, M):
    total = 0
    for m in range(1, N+1 * M):
        total += m
    return total

print(funct2(4, 2))
