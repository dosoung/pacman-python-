def cal_factorial(x):
    if x == 1 :
        return x
    else :
        return (x * cal_factorial(x-1))
x = int(input())
print(cal_factorial(x))
