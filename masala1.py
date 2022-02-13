import random
n = int(input("Nechta son kiritishingizni belgilang: "))

ruyxat = []
tanlangan = []
for i in range(1, n+1):
    sonlar = int(input(f"{i}-sonni kiriting: "))
    ruyxat.append(sonlar)
a = int(input("Bular ichidan nechtasini tanlab olasiz: "))
tanlangan.append(random.choices(ruyxat, k = a))

print(f"Sizga to'g'ri kelgan tasodifiy raqamlar: {tanlangan}")
print(tanlangan)