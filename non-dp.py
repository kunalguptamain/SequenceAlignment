'''
Takes two nucleotide sequences and does sequence alignment,
finding the largest substring, in O(m^2 * n)
'''
def longest_common_substring(sequence_1: str, sequence_2: str):
    smaller_sequence: str = sequence_1
    larger_sequence: str = sequence_2
    if(len(sequence_1) > len(sequence_2)): smaller_sequence, larger_sequence = larger_sequence, smaller_sequence

    for i in range(len(smaller_sequence) - 1):
        substring_length = len(smaller_sequence) - i - 1
        for index in range(len(smaller_sequence) - substring_length):
            substring = smaller_sequence[index: index + substring_length]
            if substring in larger_sequence:
                return substring, substring_length
            
    return "", 0

def substring_pairs(sequence_1: str, sequence_2: str):
    sequence_2_index = 0
    for i in range(len(sequence_1)):
        found = False
        for j in range(sequence_2_index, len(sequence_2)):
            sequence_2_index = j
            if(sequence_2[j] == sequence_1[i]): 
                found = True
                break
        if not found: return False
    return True

'''
Takes two nucleotide sequences and does sequence alignment, 
including gaps and insertions in the sequence in O(m^2 * (n + m))
'''
def longest_common_subsequence(sequence_1: str, sequence_2: str):
    smaller_sequence: str = sequence_1
    larger_sequence: str = sequence_2
    if(len(sequence_1) > len(sequence_2)): smaller_sequence, larger_sequence = larger_sequence, smaller_sequence

    for i in range(len(smaller_sequence) - 1):
        substring_length = len(smaller_sequence) - i - 1
        for index in range(len(smaller_sequence) - substring_length):
            substring = smaller_sequence[index: index + substring_length]
            if substring_pairs(substring, larger_sequence):
                return substring, substring_length
    return "", 0
            