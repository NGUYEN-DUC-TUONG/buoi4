import array
# Mảng ban đầu
my_array = array.array('i', [1, 2, 3])
# Sử dụng list comprehension để chuyển đổi array thành list
my_list = [element for element in my_array]
# In list từ mảng
print("List từ mảng:", my_list)
# Sử dụng phương thức buffer_info() để lấy thông tin bộ đệm
buffer_info = my_array.buffer_info()
# In thông tin bộ đệm
print("Thông tin bộ đệm:", buffer_info)