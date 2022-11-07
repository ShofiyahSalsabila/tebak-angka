import random

angkatebakan = random.randint(1,100)
peluang = 7

# while peluang > 0:
#     data = int(input("masukkan tebakan anda :"))
#     if data < angkatebakan:
#         print("Angka yang ditulis terlalu kecil")
#     if  > 10:
#         print("Angka yang anda masukkan terlalu besar")
#     if peluang == 10:
#         print("Selamat, jawaban anda benar")
#     if peluang < 10:
#         print("angka yang an55
# da masukkan terlalu kecil")


while True:
    jawaban = int(input("masukkan tebakan anda: "))
    peluang -= 1
    if peluang == 0:
        print("Anda kurang beruntung")
        break
    elif jawaban == angkatebakan:
        print('tebakan anda tepat, anda menebak sebanyak', (peluang+1), 'kali')
        break
    if jawaban > angkatebakan:
        print('Tidak tepat, angka terlalu besar')
    if jawaban < angkatebakan:
        print('Tidak tepat,angka  terlalu kecil')
