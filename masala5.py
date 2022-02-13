son = int(input("Son kiriting: "))
jami = 0
for i in range(1, son):
    if son % i == 0:
        jami += i
if jami == son:
    print(son, " mukammal son")
else:
    print(son, " mukammal son emas")