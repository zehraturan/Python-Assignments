fibo_list = []
a, b = 0, 1
while b <= 55:
    a, b = b, a+b
    fibo_list.append(a)
print("fibonacci -> ", fibo_list)