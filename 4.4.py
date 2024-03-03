# Tạo một mảng ban đầu
my_array = [1, 2, 3, 4]
# Chèn giá trị 5 vào vị trí thứ 3 (index 2) sử dụng list comprehension
insert_value = 5
position = 2
my_array = my_array[:position] + [insert_value] + my_array[position:]
# In mảng sau khi chèn giá trị
print("Mảng sau khi chèn giá trị:", my_array)