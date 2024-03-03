def allFib(n):
    return [str(i) + ":, " + str(fib(i)) for i in range(n)]

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# Gọi hàm allFib với đối số là 5 và in kết quả
result = allFib(5)
print(result)