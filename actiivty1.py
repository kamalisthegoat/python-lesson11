k = int(input("enter the number of rows u want: "))
num = 1

for i in range(k):
    for j in range(i+1):

        num = (num+1)

        print(num, end=" ")

    print()