from asyncio.windows_events import NULL


f = open("C:/users/green/hello.txt", 'r')

for line in f.readlines():
    print(line)
