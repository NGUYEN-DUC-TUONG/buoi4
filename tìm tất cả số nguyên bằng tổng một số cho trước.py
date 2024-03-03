def find_pairs_with_sum(arr, target_sum):
    # Sử dụng list comprehension để tạo danh sách các cặp có tổng bằng target_sum
    pairs = [(arr[i], arr[j]) for i in range(len(arr)) for j in range(i+1, len(arr)) if arr[i] + arr[j] == target_sum]
    return pairs

input_array = [2, 6, 3, 9, 11]
target_sum = 9
result_pairs = find_pairs_with_sum(input_array, target_sum)
print(result_pairs)