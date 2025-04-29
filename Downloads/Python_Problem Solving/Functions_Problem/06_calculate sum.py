def cal_sum(n):
    total = 0
    if n == 0:
        return total
    return n + cal_sum(n-1)


print(cal_sum(int(input("Enter a number: "))))
