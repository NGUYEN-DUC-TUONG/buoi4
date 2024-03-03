from array import array
# Mảng ban đầu
my_array = array('i', [3, 4, 5])
# Danh sách chứa các giá trị mới
new_values = [6, 7, 8]
# Sử dụng list comprehension để thêm các giá trị từ danh sách vào mảng
my_array.extend(new_values)
# In mảng sau khi thêm giá trị từ danh sách
print("Mảng sau khi thêm giá trị từ danh sách:", my_array)