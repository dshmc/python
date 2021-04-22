n = int(input())

ov = [0, 5,6,7,8,9]
sta = [2, 3, 4]
if 0 <= n <= 1000:
    if n == 0 or n ==11 or (n%100)//10 == 1 or n % 10 in ov:
        print(str(n) + ' программистов')
    elif n % 10 == 1 and n != 11:
        print(str(n) + ' программист')
    elif n%10 in sta and (n%100)//10!=1:
        print(str(n) + ' программиста')
