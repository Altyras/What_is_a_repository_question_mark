import random
import time

print("H")
time.sleep(1)
print(12345)
print(time.localtime())

print(time.localtime().tm_gmtoff)
print(time.localtime().tm_year)
print(time.localtime().tm_wday)
print(time.localtime().tm_mday)
print(time.localtime().tm_yday)
print(time.localtime().tm_year)
print(time.localtime().tm_zone)
print(time.localtime().tm_isdst)
print(time.localtime().tm_hour)
print(time.localtime().tm_sec)
a=1
b=1
for i in range(3):
    time.sleep(0.618)
    c=b
    b+=a
    a=c
    print(b)


for i in range(3):
    print(input())
