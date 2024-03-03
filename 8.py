n = 5
factorial = 1

# Sử dụng list comprehension để tính giai thừa
factorial_list = [factorial := factorial * i for i in range(1, n+1)][-1]

# In kết quả giai thừa
print(factorial_list)