def increment(*numbers, by=1):
    for number in numbers:
        print(number + by)

x = 9

increment(x, 2, 3)
increment(x, by=2)
increment(x, by=3)
