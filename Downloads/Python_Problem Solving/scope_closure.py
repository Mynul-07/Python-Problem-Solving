def chai_coder(num):
    def actual(x):
        return num + x
    return actual


f = chai_coder(10)
g = chai_coder(20)

print(f(5))  # 15
print(g(5))  # 25
