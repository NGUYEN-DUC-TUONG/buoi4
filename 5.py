def print_unordered_pairs(arrayA, arrayB):
    # Sử dụng list comprehension để tạo danh sách các cặp (i, j) từ hai mảng và lặp 100,000 lần
    pairs = [(arrayA[i], arrayB[j]) for i in range(len(arrayA)) for j in range(len(arrayB)) for k in range(100000)]

    # In các cặp
    for pair in pairs:
        print(','.join(map(str, pair)))
# INPUT
arrayA = [1, 2, 3]
arrayB = ['a', 'b', 'c']
print_unordered_pairs(arrayA, arrayB)