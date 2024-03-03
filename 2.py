def printPairs(array):
    # Sử dụng list comprehension để tạo danh sách các cặp (i, j)
    pairs = [(i, j) for i in array for j in array]
    # In các cặp
    for pair in pairs:
        print(','.join(map(str, pair)))

printPairs([1, 2, 3])