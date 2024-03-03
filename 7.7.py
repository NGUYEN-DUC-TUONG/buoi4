# Mảng ban đầu
my_array = [1, 2, 3, 4, 5]
# Giá trị cần loại bỏ
value_to_remove = 3
# Sử dụng list comprehension để tạo mảng mới không chứa giá trị cần loại bỏ
my_array = [x for x in my_array if x != value_to_remove]
# In mảng sau khi loại bỏ
print("Mảng sau khi loại bỏ giá trị:", my_array)