# class 내부에 있는 메서드는 self를 무조건 적어주어야한다!!

class Post:  # self는 class가 메모리에 뜰때 class의 주소를 담음.
    def __init__(self, username, password):  # class가 실행될때 무조건 실행되는애
        self.usename = username  # self = java의 this와 같음.
        self.password = password


p = Post("ssar", "1234")

# class -> dict 변환
print(p.__dict__)
