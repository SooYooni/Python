while True:
    a = input("첫번째 숫자 입력")

    if a == "00000":
        break
    b = int(input("두번째 숫자 입력"))
    a = int(a)
    result = a + b
    print(a, "+", b, "=", result)
    #break

    result = a - b
    print(a, "-", b, "=", result)

    result = a * b
    print(a, "*", b, "=", result)

    result = a / b
    print(a, "/", b, "=", result)

print("end of block")
