def days_above_average():
    # Nhập số ngày
    num_days = int(input("How many day's temperature? "))
    # Sử dụng list comprehension để nhập nhiệt độ từng ngày
    temperatures = [float(input(f"Day {day}'s high temp: ")) for day in range(1, num_days + 1)]
    # Tính trung bình nhiệt độ
    average_temp = sum(temperatures) / num_days
    print(f"Average = {average_temp}")
    # Sử dụng list comprehension để đếm số ngày có nhiệt độ cao hơn trung bình
    above_average_days = sum(1 for temp in temperatures if temp > average_temp)
    print(f"{above_average_days} day(s) above average")
# Gọi hàm để thực thi chương trình
days_above_average()