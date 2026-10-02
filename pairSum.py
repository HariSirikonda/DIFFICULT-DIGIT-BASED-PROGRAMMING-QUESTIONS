def pairSum(num):
    digits = str(num)
    count = 0
    for i in range(len(digits)-1):
        sum = int(digits[i])+int(digits[i+1])
        if sum == 10:
            count += 1
    return count

num = int(input("Enter the number : "))
print(pairSum(num))