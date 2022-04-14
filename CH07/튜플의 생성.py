## 튜플의 생성 ##
tt1 = (10, 29, 39); tt1
tt2 = 10, 20, 30; tt2

print(tt1)
print(tt2)

tt3 = (10); tt3
tt4 = 10; tt4

tt5 = (10,); tt5
tt6 = 10,; tt6

print(tt3)
print(tt4)
print(tt5)
print(tt6)


## 튜플의 오류 ##
tt1.append(40)
tt1[0] = 40
del(tt1[0])


## 튜플의 삭제 ##
del(tt1)
del(tt2)


## 튜플의 사용 ##
# 튜플 항목에 접근 #
tt1 = (10, 20, 30, 40)
tt1[0]
tt1[0] + tt1[1] + tt1[2]


# 튜플 범위에 접근 #
tt1[1:3]
tt1[1:]
tt1[:3]


# 튜플의 덧셈 및 곱셈 연산 #
tt2 = ('A', 'B')
tt1 + tt2
tt2 * 3



# 튜플 > 리스트 > 튜플 변환 #
myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
myTuple

