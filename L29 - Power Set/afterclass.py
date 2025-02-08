def find_all_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    return substrings

string = "abc"
print(find_all_substrings(string))
