def summation(num):
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    return sum

print(summation(100))

# return sum(range(num + 1))