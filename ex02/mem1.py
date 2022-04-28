# 함수 (클래스 내부에 있는 것이 아닌 것들을 함수)
# 메서드는 클래스 내부에 있는 어떤 상태를 변경 = return값이 달라질수 있음
# 함수는 독단적으로 있는 자기만의 상태 = return값이 동일

def add():
    print("더하기")


def minus():
    return 1


add()
n = minus()
print(n)


def multi(n1, n2=3):
    print(f"곱하기 {n1}*{n2}")


multi(3, 2)

multi(2)


def my_dict(**data):  # dict 변환 문법
    print(data)
    pass  # 함수 내부를 비워두고 싶을때 사용


my_dict(id=1, username="ssar")  # dict라서 키값이 무조건 있어야함.

n1 = 1


def vartest():
    global n1  # 전역변수에 있는것을 선택해줌, 사용 안하면 지역변수 n1을 생성함 => 타입을 지정안하기때문
    n1 = 2


vartest()
print(n1)
