list1 = []
list2 = []
value = 1

for i in range(0, 3):
    for k in range(0, 4):
        list.append(value)
        value += 1
    list2.append(list1)
    list1 = []

for i in range(0, 3):
    for k in range(0, 4):
        print("%3d" %list2[i][k], end="")
    print("")

#-----------------------------------------------------

## aa 값을 지정해주고 그 합을 나타내는 코드 ##
aa = [[1, 2, 3, 4],
      [5, 6],
      [7, 8, 9]]

totalSum = 0
for i in range(len(aa)):
    sum = 0
    for j in range(len(aa[i])):
        sum += aa[i][j]
    print(sum)
    totalSum += sum
print("total : ", totalSum)