import random
from typing import NoReturn
r = random.randint(1, 100)
print(r)
count = 0

while True:
    count += 1 #count = count + 1
    number = int(input('請猜數字: '))
    if number == r:
        print('終於猜對了')
        print('你猜了', count, '次')
        break
    elif number > r:
        print('比答案大，猜小一點')
    elif number < r:
        print('比答案小，猜大一點')
    print('你猜了', count, '次')