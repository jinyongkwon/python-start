from pymysql import connect, cursors  # cursor => rs.next처럼 딱 커서를 찝는것

conn = connect(
    host="localhost",
    user="green",
    password="green1234",
    db="greendb",
    charset="utf8"  # -가 없이 받음.
)

# 바로 파싱해서 주는데 파싱 타입의 디폴트 = tuple타입 그래서 Dict로 바꾸어줌
cursor = conn.cursor(cursors.DictCursor)
