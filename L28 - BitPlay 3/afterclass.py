def longest_consecutive_ones(n):
    # Convert number to binary and remove '0b' prefix
    binary_representation = bin(n)[2:]
    
    # Split by '0' to get sequences of consecutive '1's
    ones_sequences = binary_representation.split('0')
    
    # Find the maximum length of sequences of '1's
    max_ones = max(map(len, ones_sequences))
    
    return max_ones

num = int(input("Enter a number: "))
print("Longest consecutive 1's:", longest_consecutive_ones(num))