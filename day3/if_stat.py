# if구문 - 흐름제어
name = '인영'
name = ('인영', 'inzero', '명건', '태경', '다정')

# if name == '인영' or name =='inzero':
if '인영' in name:
    print('준호를 만나러 갑니다.')
    print('준호에게 인사합니다.')
elif name == '다정':
    print('송강을 만나러 갑니다.')
else:
    print('호출할때까지 대기합니다.')

x = 2
if x != 10:
    pass
else:
    pass