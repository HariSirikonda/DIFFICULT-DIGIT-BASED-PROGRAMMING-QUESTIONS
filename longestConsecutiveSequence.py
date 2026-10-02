def longestConsequtiveSequence(num):
    digits = str(num)
    dict = {}
    for digit in digits:
        dict[digit] = dict.get(digit, 0) + 1
    maxlen = 0
    res = 0
    for p, q in dict.items():
        if q > maxlen:
            maxlen = q
            res = p
    return [res, maxlen]

num = int(input("Enter a number : "))
res = longestConsequtiveSequence(num)
print(f"Digit = {res[0]} Length = {res[1]}")