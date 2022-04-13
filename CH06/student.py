#--------------------------------------------------------
# 생성
student1 = {'학번' : 1000, '이름' : '홍길동', '학과' : '컴퓨터학과'}
print(student1)
# 추가
student1['연락처'] = '010-1111-1111'
print(student1)

# 수정
student1['학과'] = '파이썬학과'
print(student1)

# 삭제
del(student1['학과'])
print(student1)

# 마지막에 있는 키가 적용
student1 = {'학번' : 1000, '이름' : '홍길동', '학과' : '파이썬학과', '학번' : 2000}
print(student1)
#--------------------------------------------------------


# 접근
student1 = {}
student1['학번']
student1['이름']
student1['학과']
print(student1)

student1.get('이름')
print()


student1['주소']
student1.get('주소')

student1.keys()


list(student1.keys())

#--------------------------------------------------------




