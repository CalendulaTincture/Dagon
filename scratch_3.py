import random
import time

typing_speed = 10**8
n = 0
i = 0
while True:
    n = random.randint(0, 12)
    i = random.randint(0, 9)
    print(f'{i: >{n}}', end='')
    #time.sleep(random.random() * 10.0 / typing_speed)
