#------------------------------------------

fruit = ['apple', 'banana', 'mango', 'melon']
j = 0
for i in fruit:
    print('Hello')
    print(j, fruit[j])
    j = j + 1
    print(i)

#------------------------------------------

fruit = ['apple', 'banana', 'mango', 'melon']
for i in fruit:
    print(fruit.index(i), i)

    if 'apple' in fruit:
        print('buy')
    else:
        print('not buy')

#------------------------------------------

fruit = ['apple', 'banana', 'mango', 'melon']
fruit.append("strawberry")
print(len(fruit))
fruit.pop()
print(len(fruit))
fruit.pop()
print(len(fruit))

for i in fruit:
    print(fruit.index(i), i)

    #if 'blueberry' in fruit:
    #    print('buy')
    #else:
    #    print('not buy')

#------------------------------------------

fruit = ['apple',True, 250, 10.99]
fruit.append("strawberry")
print(len(fruit))
fruit.pop()
print(len(fruit))
fruit.pop()
print(len(fruit))

for i in fruit:
    print(fruit.index(i), i)

    #if 'blueberry' in fruit:
    #    print('buy')
    #else:
    #    print('not buy')