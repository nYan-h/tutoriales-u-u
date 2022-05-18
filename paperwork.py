def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return n * m

print(paperwork(5, 5))

# return n * m if n > 0 and m > 0 else 0