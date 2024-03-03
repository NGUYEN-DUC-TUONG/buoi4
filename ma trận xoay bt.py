def rotate_matrix(matrix):
    # Lấy chiều dài của ma trận
    n = len(matrix)
    # Sử dụng list comprehension để tạo ma trận kết quả với tất cả giá trị ban đầu là 0
    rotated_matrix = [[0] * n for _ in range(n)]
    # Sử dụng list comprehension để xoay ma trận
    rotated_matrix = [[matrix[i][j] for i in range(n)] for j in range(n-1, -1, -1)]
    return rotated_matrix
# Test 
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result_matrix = rotate_matrix(original_matrix)
# In ma trận kết quả
for row in result_matrix:
    print(row)