def alternatingEvenOdd(num):
    digits = str(num)
    for i in range(len(digits) - 1):
        if int(digits[i]) % 2 == int(digits[i + 1]) % 2:
            return False
    return True

num = int(input("Enter a number: "))
print("Valid") if alternatingEvenOdd(num) else print("Not-valid")
