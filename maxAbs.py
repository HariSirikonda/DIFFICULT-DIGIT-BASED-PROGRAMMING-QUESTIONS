def maxAbs(num):
    digits = str(num)
    res = 0
    for i in range(len(digits)-1):
        diff = int(digits[i+1])-int(digits[i])
        if diff > res:
            res = diff
    return res

num = int(input("Enter the number : "))
print(maxAbs(num))