def differByOne(num):
    digits = str(num)
    start = 0
    for i in range(1,len(digits)):
        if int(digits[i]) - int(digits[start]) != 1:
            return False
        start += 1
    return True

num = int(input("Enter Number : "))
print("Valid") if differByOne(num) else print("Not-Valid")
