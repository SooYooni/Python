# 글자 출력 #
inStr = 'happy'
outStr = ''

# 글자 거꾸로 출력 #
'''
#j = len(inStr)
for i in range(len(inStr)):
    #outStr += outStr + inStr[i]
    outStr += inStr[j-i-1]
print(outStr)
'''
print(inStr[::-1])
