# Tạo một mảng
my_array = [1, 20, 3, 21, 5]

# Sử dụng list comprehension để truy cập các phần tử riêng lẻ và in giá trị
[print(f"Phần tử thứ {i+1}: {element}") for i, element in enumerate(my_array)]