dict = {
    "1": "one",
    "2": "two", 
    "3": "three", 
    "4": "four", 
    "5": "five", 
    "6": "six", 
    "7": "seven", 
    "8": "eight", 
    "9": "nine"
}

nums = input("Number: ")
for num in nums:
    print(dict[num], end=' ')
