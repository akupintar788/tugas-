#!/usr/bin/env python
# coding: utf-8

# In[14]:


import math

# Menampilkan pesan selamat datang dan daftar opsi
print("Selamat datang di kalkulator luas/volume!")
print("Pilih opsi yang Anda inginkan")
print("1. Menghitung luas 2 dimensi")
print("2. Menghitung volume 3 dimensi")

# Meminta pengguna untuk memilih opsi
pilihan = input("Masukkan pilihan Anda (1 atau 2): ")

# Memeriksa opsi yang dipilih oleh pengguna
if pilihan == "1":
    # Menampilkan daftar bentuk 2 dimensi yang dapat dihitung
    print("Pilihan bentuk 2 dimensi yang ingin dihitung:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar Genjang")
    print("6. Trapesium")
    
    # Meminta pengguna untuk memilih bentuk
    bentuk = input("Masukkan pilihan Anda (1-6): ")
    
    # Memeriksa bentuk yang dipilih oleh pengguna
    if bentuk == "1":
        sisi = float(input("Masukkan panjang sisi: "))
        luas = sisi * sisi  # Menghitung luas persegi
        print("Luas persegi adalah:", luas)
    elif bentuk == "2":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = panjang * lebar  # Menghitung luas persegi panjang
        print("Luas persegi panjang adalah:", luas)
    elif bentuk == "3":
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 0.5 * alas * tinggi  # Menghitung luas segitiga
        print("Luas segitiga adalah:", luas)
    elif bentuk == "4":
        jari_jari = float(input("Masukkan jari-jari: "))
        luas = math.pi * jari_jari**2  # Menghitung luas lingkaran
        print("Luas lingkaran adalah:", luas)
    elif bentuk == "5":
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = alas * tinggi  # Menghitung luas jajar genjang
        print("Luas jajar genjang adalah:", luas)
    elif bentuk == "6":
        sisi_a = float(input("Masukkan sisi A: "))
        sisi_b = float(input("Masukkan sisi B: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas = 0.5 * (sisi_a + sisi_b) * tinggi
        print ("Luas jajar genjang adalah: ", luas)
    
    else:
        print("Maaf, bentuk tidak dikenal.")
        
elif pilihan == "2":
    print("Pilihan bentuk 3 dimensi yang ingin dihitung:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Limas")
    print("6. Prisma")
    
    bentuk = input("Masukan pilhan anda (1-6):")

    if bentuk == "1":
        sisi = float(input("Masukan panjang sisi: "))
        volume = sisi**3
        print("Volume kubus adalah: ", volume)
    elif bentuk == "2":
        panjang =float(input("Masukan panjang balok: "))
        lebar =float(input("Masukan lebar balok: "))
        tinggi =float(input("Masukan tinggi balok: "))
        volume = panjang * lebar * tinggi
        print("Volume balok dengan panjang", panjang, ",lebar", lebar, ", dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "3":
        jari_jari =float(input("Masukan jari-jari tabung: "))
        tinggi = float(input("Masukan tinggi tabung: "))
        volume = math.pi * jari_jari * tinggi
        print("Volume tabung dengan jari-jari", jari-jari, "dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "4":
        jari_jari =float(input("Masukan jari-jari kerucut: "))
        tinggi =float(input("Masukan tinggi kerucut: "))
        volume = 1/3 * math.pi * jari_jari **2 * tinggi
        print("Volume kerucut dengan jari-jari", jari-jari, "dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "5":
        alas =float(input("Masukan alas limas: "))
        tinggi =float(input("Masukan tinggi limas: "))
        volume = 1/3 * alas * tinggi
        print("Volume limas dengan luas alas", alas, "dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "6":
        alas =float(input("Masukan alas segitiga prisma: "))
        tinggi =float(input("Masukan tinggi segita prisma: "))
        tinggi_prisma =float(input("Masukan tinggi prisma: "))
        volume = 1/2 * alas * tinggi * tinggi_prisma
        print("Volume prisma segita dengan alas", alas, ", tinggi", ", dan tinggi prisma", tinggi_prisma, "adalah", volume)
else:
    print("Bentuk tidak dikenali.")


# In[4]:




