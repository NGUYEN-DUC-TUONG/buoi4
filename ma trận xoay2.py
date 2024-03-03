def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n // 2):
        # Sử dụng list comprehension để hoán đổi giá trị của top và bottom
        matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
    # Sử dụng list comprehension để xoay ma trận
    matrix = [[matrix[j][i] for j in range(n)] for i in range(n)]
    return matrix
# Test với ma trận ví dụ
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result_matrix = rotate_matrix(original_matrix)
# In ma trận kết quả
for row in result_matrix:
    print(row)