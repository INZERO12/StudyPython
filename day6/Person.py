# Person 클래스
from operator import ge


class Person:
    name = '무명이'             # 아직 이름이 없다
    age = 0
    height = 0
    gender = ''
    feetsize = 230
    bloodtype = ''


    # 생성자
    def __init__(self, name, age, height, gender) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender
        print('Person이 생성되었습니다')

    def 소개한다(self):
        greeting = f'''안녕하세요. 저는 {self.name}입니다.
        {self.gender}구요. {self.age}살입니다.
        '''
        print(greeting)

    def 먹는다(self, food):
        print(f'{self.name}이(가) {food}을(를) 먹는다')

    def 일한다(self, drink):
        print(f'{self.name}이(가) {drink}을(를) 마시면서 일한다')


if __name__ =='__main__':
#     p = Person()               # p라는 이름의 Person 객체 생성
#     print(type(p))
    # print(id(p))               # id 값

    # p2 = Person()              # p2 객체 생성
    # print(type(p2))
    # print(id(p2))
    lin = Person('이인영', 26, 158, 'female')   # == __init__(self, name, age, height, gender): / self는 생략, 생성자를 쓸때는 항상 __문자__ 형태로 써야함
    # lin.name = '이인영'
    # lin.age = 26
    # lin.height = 158
    # lin.gender = 'female'
    # lin.feetsize = 230
    lin.bloodtype = 'AB'

    # cws = Person()
    # cws.name = '최우식'
    # cws.age = 31
    # cws.height = 181
    # cws.gender = 'male'
    # cws.feetsize = '275'
    # cws.bloodtype = 'O'

    lin.소개한다()
    lin.먹는다('돈까스')
    lin.일한다('콜드부르')

    
    lin.__doc