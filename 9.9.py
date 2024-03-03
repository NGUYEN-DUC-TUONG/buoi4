# Mảng ban đầu
my_array = [1, 2, 3, 4, 5]
# Giá trị cần tìm chỉ mục
value_to_find = 3
# Sử dụng list comprehension để tạo một danh sách chỉ mục của giá trị trong mảng
indices_of_value = [index for index, value in enumerate(my_array) if value == value_to_find]
# In danh sách chỉ mục của giá trị
print(f"Chỉ mục của giá trị {value_to_find} trong mảng là {indices_of_value}")