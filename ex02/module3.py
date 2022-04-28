# 같은라인, 폴더내부, 위폴더, 파이썬 라이브러리로 이동가능
import sys

# 내장 라이브러리 import 없이 사용할 수 있음.
print(sys.modules)  # 디폴트 class path를 보여줌
print("="*50)

# 외장 라이브러리 built-in 모듈 import를 해야 사용가능.
print(sys.path)  # 여기 들어가지 않은 것들은 사용이 불가능.
