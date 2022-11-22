import datetime as dt
import time
import random

list = list(range(1, 101))
removedList = open("removed_nums.txt").read().splitlines()
list = [str(e) for e in list]

res = [i for i in list if i not in removedList]


num = random.choice(res)
print(num)
with open("removed_nums.txt", "a") as file:
    file.write(str(num)+"\n")
    file.close
#time.sleep(5)

#while(True):
#    if len(list) > 0:
#        pick_num()
#    else:
#       print("All done!") 
#       break