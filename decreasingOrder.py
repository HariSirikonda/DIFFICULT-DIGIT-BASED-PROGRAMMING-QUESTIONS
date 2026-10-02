def isDecreasing(num):
    digits = str(num)
    start = 0
    for i in range(1,len(digits)):
        if int(digits[start]) <= int(digits[i]):
            return False
        start += 1
    return True

num = int(input("Enter Number : "))
print("Decreasing") if isDecreasing(num) else print("Non-Decreasing")
