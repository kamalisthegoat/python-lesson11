num = int(input("Enter a number: "))
WAAH = 0

while num > 0:
    num = num // 10
    WAAH = WAAH + 1

print("number of digit in this number are =", WAAH)