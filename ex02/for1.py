# for 문 연습

a = range(1, 10)  # 1부터 10전까지

for i in range(1, 11):
    print(i)

list = [1, 2, 3, 4]

for i in list:
    print(i)

tuple = [1, 2, 3, 4]

for i in tuple:
    print(i)
    
for i in tuple:
    for j in list:
        print(i*j)
