
try:
    f = open("c:/hello.txt", "r")  # 파일오픈같은것도 무조건 try-catch로 넣어줘야함.
    print(2/0)
except Exception as e:  # 별칭을 붙이면 메세지가 찍힘
    print(e)
finally:  # 터지든 안터지든 무조건 실행
    print("무조건 실행됨")
