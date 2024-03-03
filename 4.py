def print_unordered_pairs(arrayA, arrayB):
    # Sử dụng list comprehension để tạo danh sách các cặp (i, j) từ hai mảng
    pairs = [(arrayA[i], arrayB[j]) for i in range(len(arrayA)) for j in range(len(arrayB))]
    # In các cặp
    for pair in pairs:
        print(','.join(map(str, pair)))

# INPUT
arrayA = [1, 2, 3]
arrayB = ['a', 'b', 'c']

print_unordered_pairs(arrayA, arrayB)