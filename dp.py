def global_alignment(sequence_1: str, sequence_2: str, gap:int, substitution_matrix):
    game_board = [0] * len(sequence_2)
    for i in range(len(sequence_1)):
        row_i = [0]
        for j in range(len(sequence_2)):
            row_i.append(substitution_matrix[sequence_1[i]][sequence_2[j]])
        game_board.append(row_i)

    dynamic_cost_array = []
    for i in range(len(sequence_1)):
        row_i = []
        for j in range(len(sequence_2)):
            if i == 0 and j == 0: 
                row_i.append(0)
                break
            if i == 0:
                row_i.append(row_i[i][j - 1] - gap)
                break
            if j == 0:
                row_i.append(dynamic_cost_array[i - 1][j] - gap)
                break
            row_i.append(max(row_i[i][j - 1] - gap, dynamic_cost_array[i - 1][j] - gap, \
                             dynamic_cost_array[i - 1][j - 1] + game_board[i][j]))
        dynamic_cost_array.appennd(row_i)
            
    
    