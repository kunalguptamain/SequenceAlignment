'''
Takes two nucleotide sequences and does sequence alignment,
finding the largest substring, in O(s1 * s2^2) time
'''
def longest_common_substring(s1: str, s2: str):
    a: str = s1
    b: str = s2
    if(len(s1) > len(s2)): a, b = b, a

    for i in range(len(a) - 1):
        substring_length = len(a) - i - 1
        for index in range(len(a) - substring_length):
            substring = a[index: index + substring_length]
            if substring in b:
                return substring, substring_length
            
    return "", 0

def substring_pairs(s1: str, s2: str):
    s2_index = 0
    for i in range(len(s1)):
        found = False
        for j in range(s2_index, len(s2)):
            s2_index = j
            if(s2[j] == s1[i]): 
                found = True
                break
        if not found: return False
    return True

def longest_common_subsequence(s1: str, s2: str):
    a: str = s1
    b: str = s2
    if(len(s1) > len(s2)): a, b = b, a

    for i in range(len(a) - 1):
        substring_length = len(a) - i - 1
        for index in range(len(a) - substring_length):
            substring = a[index: index + substring_length]
            if substring_pairs(substring, b):
                return substring, substring_length
    return "", 0
            