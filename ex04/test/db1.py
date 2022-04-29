from db import connect as db

# 바인딩을 %s로 함
inset_sql = "INSERT INTO my_member(username, password) VALUES(%s, %s)"
db.cursor.execute(inset_sql, ["love", "1234"])  # 버퍼로 쏘아줌
db.conn.commit()
