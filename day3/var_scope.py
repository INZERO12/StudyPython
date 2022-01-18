# 변수 라이프스코프\
a = 10             # 전역변수

def vartest(a):    # a가 살아있는 부분은 def 안 -> 지역변수(그 지역에서만 쓸 수 있다)
    a = a + 1      # 지역변수
    return a       # 여기까지 선언

a = vartest(a)   # def밖은 전역변수 / 여기서 부터 실행라인
print(a)