a = int(input("Ro'yxatda nechta son bo'ladi: "))
ruyxat = []
for i in range (1, a+1):
    son = int(input(f"{i}-sonni kiriting: "))
    ruyxat.append(son)
print(f"Kiritilgan ro'yxat: {ruyxat}")
def replace(n:list):
    for i in n:
        if i == 0:
            ruyxat.remove(i)
            ruyxat.insert(len(n),i)
    return n
print(f"Chiqarilgan ro'yxat: {replace(ruyxat)}")