def print_unordered_pairs(array):
    # Sử dụng list comprehension để tạo danh sách các cặp (i, j)
    pairs = [(array[i], array[j]) for i in range(len(array)) for j in range(i+1, len(array))]

    # In các cặp
    for pair in pairs:  # Duyệt qua danh sách các cặp và in mỗi cặp, sử dụng 
        print(','.join(map(str, pair))) # để chuyển mỗi cặp thành một chuỗi có dạng "i,j" và in ra màn hình.

my_array = [1, 2, 3, 4, 5]
print_unordered_pairs(my_array)