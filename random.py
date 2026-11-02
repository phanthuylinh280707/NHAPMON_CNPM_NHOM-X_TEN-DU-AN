
import random

so_bi_mat = random.randint(1, 100)
so_lan_doan = 0

print("=== TRO CHOI DOAN SO ===")
print("Hay doan mot so tu 1 den 100")

while True:
    doan = int(input("Nhap so ban doan: "))
    so_lan_doan += 1

    if doan < so_bi_mat:
        print("So ban doan nho hon!")
    elif doan > so_bi_mat:
        print("So ban doan lon hon!")
    else:
        print("Chuc mung! Ban da doan dung!")
        print("So lan doan:", so_lan_doan)
        break

