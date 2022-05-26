ss = '  파  이  썬  '
ss.strip()
ss.rstrip()
ss.lstrip()


# 앞뒤의 특정문자 삭제
ss = '---- 파 --- 이 --- 썬 ----'
print(ss.strip('-'))
ss = '<<< 파 << 이 >> 썬 >>>'
print(ss.strip('<>'))


#문자열 중간의 공백까지 삭제해주는 코드
inStr = "  한글 Python 프로그래밍  "
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] != ' ':
        outStr += inStr[i]

print("원래 문자열 ==> " + '[' + inStr + ']')
print("공백 삭제 문자열 ==> " + '[' + outStr + ']')