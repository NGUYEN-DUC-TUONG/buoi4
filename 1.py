def foo(array):
    # Tính tổng của mảng sử dụng sum() và lưu vào biến sum_result
    sum_result = sum(array)

    # Sử dụng list comprehension để tính tích của mảng, nếu mảng rỗng thì giá trị mặc định là 0
    product_result = 1 if array else 0
    product_result = product_result if not array else product_result * array[0]
    # Sử dụng vòng lặp để tính tích của mảng, nếu mảng không rỗng thực hiện thêm một lần nhân với phần tử đầu tiên của mảng.
    for i in array[1:]:
        product_result *= i 
    # Sử dụng vòng lặp để tính tích của các phần tử còn lại của mảng (bắt đầu từ phần tử thứ hai vì đã nhân phần tử đầu tiên ở bước trước).
    print("Sum =", sum_result, ", Product =", product_result)

my_array = [1, 2, 3, 4, 5]
foo(my_array)