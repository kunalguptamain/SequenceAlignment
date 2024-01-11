SEQUENCE_1_TEST = "CCCCCCATGCGTAGTCGTCAGCTAGCCCCCCC"
SEQUENCE_2_TEST = "ACTATCTAACGGTC"
GAP = 1
#    A  T  C  G
SUBSTITUTION_MATRIX = {
    "A" : {"A": 1, "T": -.5, "C": -1, "G": -1},
    "T" : {"A": -.5, "T": 1, "C": -1, "G": -1},
    "C" : {"A": -1, "T": -1, "C": 1, "G": -.5},
    "G" : {"A": -1, "T": -1, "C": -.5, "G": 1}
}

############################################################################

def print_2d_array(r):
    for i in range(len(r)):
        for j in range(len(r[i])):
            print("%3d" % r[i][j], end="")
        print()

############################################################################

def global_alignment(sequence_1: str, sequence_2: str, gap:int, substitution_matrix):
    #setting gameboard
    game_board = [[0] * (len(sequence_2) + 1)]
    for i in range(len(sequence_1)):
        row_i = [0]
        for j in range(len(sequence_2)):
            row_i.append(substitution_matrix[sequence_1[i]][sequence_2[j]])
        game_board.append(row_i)

    #print_2d_array(game_board)

    #choosing best path
    dynamic_cost_array = []
    for i in range(len(sequence_1)):
        row_i = []
        for j in range(len(sequence_2)):
            if i == 0 and j == 0: 
                row_i.append(0)
                continue
            if i == 0:
                row_i.append(row_i[j - 1] - gap)
                continue
            if j == 0:
                row_i.append(dynamic_cost_array[i - 1][j] - gap)
                continue
            row_i.append(max(row_i[j - 1] - gap, dynamic_cost_array[i - 1][j] - gap, \
                             dynamic_cost_array[i - 1][j - 1] + game_board[i][j]))
        dynamic_cost_array.append(row_i)

    #print_2d_array(dynamic_cost_array)

    #backtracking
    row = len(sequence_1) - 1
    col = len(sequence_2) - 1
    aligned_sequence_1 = sequence_1[row]
    aligned_sequence_2 = sequence_2[col]
    while not (row == 0 and col == 0):
        if row != 0 and dynamic_cost_array[row - 1][col] - dynamic_cost_array[row][col] == gap:
            aligned_sequence_1 += sequence_1[row - 1]
            aligned_sequence_2 += "-"
            row -= 1
        elif col != 0 and dynamic_cost_array[row][col - 1] - dynamic_cost_array[row][col] == gap:
            aligned_sequence_1 += "-"
            aligned_sequence_2 += sequence_2[ col- 1]
            col -= 1
        else:
            aligned_sequence_1 += sequence_1[row - 1]
            aligned_sequence_2 += sequence_2[col - 1]
            row -= 1
            col -= 1
            
    return aligned_sequence_1[::-1], aligned_sequence_2[::-1]

############################################################################

def semi_global_alignment(sequence_1: str, sequence_2: str, gap:int, substitution_matrix):
    #setting gameboard
    game_board = [[0] * (len(sequence_2) + 1)]
    for i in range(len(sequence_1)):
        row_i = [0]
        for j in range(len(sequence_2)):
            row_i.append(substitution_matrix[sequence_1[i]][sequence_2[j]])
        game_board.append(row_i)

    #print_2d_array(game_board)

    #choosing best path
    dynamic_cost_array = []
    for i in range(len(sequence_1)):
        row_i = []
        for j in range(len(sequence_2)):
            if i == 0 and j == 0: 
                row_i.append(0)
                continue
            if i == 0:
                row_i.append(row_i[j - 1])
                continue
            if j == 0:
                row_i.append(dynamic_cost_array[i - 1][j])
                continue
            row_i.append(max(row_i[j - 1] - gap, dynamic_cost_array[i - 1][j] - gap, \
                             dynamic_cost_array[i - 1][j - 1] + game_board[i][j]))
        dynamic_cost_array.append(row_i)

    #print(dynamic_cost_array)

    #backtracking
    row = len(sequence_1) - 1
    col = len(sequence_2) - 1

    for i in range(len(sequence_1)):
        if dynamic_cost_array[i][len(sequence_2) - 1] > dynamic_cost_array[row][col]:
            row = i
            col = len(sequence_2) - 1

    for i in range(len(sequence_2)):
        if dynamic_cost_array[len(sequence_1) - 1][i] > dynamic_cost_array[row][col]:
            row = len(sequence_1) - 1
            col = i

    aligned_sequence_1 = sequence_1[row]
    aligned_sequence_2 = sequence_2[col]
    while  row != 0 and col != 0 :
        if row != 0 and dynamic_cost_array[row - 1][col] - dynamic_cost_array[row][col] == gap:
            aligned_sequence_1 += sequence_1[row - 1]
            aligned_sequence_2 += "-"
            row -= 1
        elif col != 0 and dynamic_cost_array[row][col - 1] - dynamic_cost_array[row][col] == gap:
            aligned_sequence_1 += "-"
            aligned_sequence_2 += sequence_2[ col- 1]
            col -= 1
        else:
            aligned_sequence_1 += sequence_1[row - 1]
            aligned_sequence_2 += sequence_2[col - 1]
            row -= 1
            col -= 1
            
    return aligned_sequence_1[::-1], aligned_sequence_2[::-1]

############################################################################

global_sequences = global_alignment(SEQUENCE_1_TEST, SEQUENCE_2_TEST, GAP, SUBSTITUTION_MATRIX)
print(global_sequences[0])
print(global_sequences[1])

semi_global_sequences = semi_global_alignment(SEQUENCE_1_TEST, SEQUENCE_2_TEST, GAP, SUBSTITUTION_MATRIX)
print(semi_global_sequences[0])
print(semi_global_sequences[1])