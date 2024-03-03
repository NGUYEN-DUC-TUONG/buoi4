def reverse(array):
    # Sử dụng list comprehension để đảo ngược mảng
    array = [array[len(array) - i - 1] for i in range(len(array))]
# lấy mỗi phần tử của mảng cũ từ phần tử cuối cùng đến phần tử đầu tiên.
    # In mảng sau khi đảo ngược
    print(array)

# Mảng đầu vào
my_array = [1, 2, 3, 4, 5]

# Gọi hàm reverse với mảng đầu vào
reverse(my_array)