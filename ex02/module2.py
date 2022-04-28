# 파이썬은 파일 하나를 module라고 한다.
# from hello import say_goodbye, say_hello  # hello파일안에 say_hello,say_goodbye를 정해서 가져옴
from hello import *  # hello파일안에 모든것을 가져옴 하지만 파일이름이 충돌날수 있음.

say_hello()
say_goodbye()
