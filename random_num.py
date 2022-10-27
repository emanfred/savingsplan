import datetime as dt
import time
import random

#lst = list(range(1, 101))
with open("lst.txt", "rU") as file:
    for line in file:
        lst.extend(line.split())

def pick_num(lst):
    now = dt.datetime.now()
    weekday = now.weekday()
    if weekday:
        num = random.choice(lst)
        print(num)
        lst.remove(num)
        with open("lst.txt", mode="w") as file:
            file.write(str(lst))
        print(lst)
        time.sleep(5)

while(True):
    if len(lst) > 0:
        pick_num(lst)
    else:
        f.close()
        break

