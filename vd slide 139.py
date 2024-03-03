def two_sum(nums, target):
    # Tạo một từ điển để lưu trữ giá trị và chỉ số của các số đã xem xét
    seen = {}
    # Sử dụng list comprehension để tìm cặp số có tổng bằng target
    indices = [seen.get(target - num, -1) for num in nums]
    # Lọc ra chỉ số hợp lệ (không phải -1)
    valid_indices = [i for i in indices if i != -1]
    if len(valid_indices) == 2:
        # Trả về chỉ số của cặp số
        return valid_indices
    else:
        # Trường hợp không có giải pháp (theo đề bài, giả định rằng mỗi đầu vào sẽ có chính xác một giải pháp)
        return []
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)