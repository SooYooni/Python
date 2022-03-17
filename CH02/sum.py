'''
number = 0
for num in range(0, 11):
    number = number+num
    print(number)
'''


number = 0
for num in range(1,11):
    if(num % 2 == 0):
     number = number+num

print(f"1부터 10까지 중 짝수의 합은 {number}입니다.")
