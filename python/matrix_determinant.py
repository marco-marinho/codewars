def determinant(matrix):
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    buff = 0
    for i in range(len(matrix)):
        sign = 1 if i % 2 == 0 else -1
        buff += (
            sign
            * matrix[0][i]
            * determinant([row[:i] + row[i + 1 :] for row in matrix[1:]])
        )
    return buff
