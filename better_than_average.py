def better_than_average(class_points, your_points):
    sum = 0
    num = 1
    for x in class_points:
        sum += x
        num += 1
    sum += your_points
    return True if (sum / num) < your_points else False 

print(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50))

# return your_points > sum(class_points) / len(class_points)