import os

import datetime

lama_hari=0

def waktuinap():
    x=datetime.datetime.now()
    
def print_menu():
    print(1* "-")
    print()
    print('\t','      HOTEL MELATI SOLO BARU ')
    print()
    print('\t','---------Selamat Datang----------')
    print()
    print('Jl.Solo baru No.900, kode pos 29112 No HP. 0001122')
    print('\t','      Solo baru Surakarta')
    print()
    print('\t',' Hotel bintang 3 dengan keunggulan: ')
    print('\t','           Nyaman')
    print('\t','            Aman')
    print('\t','           Bersih')
    print('\t','            Asri')
    print()
    print(50* "-")
    print('Pilih yang anda inginkan ?')
    print()
    print('1. CHECK IN')
    print('2. keluar program')
    print()
    
    tanggalmasuk = int(input("Masukkan TANGGAL (1-31):"))
    bulanmasuk = int(input("Masukkan BULAN (1-12):"))
    tahunmasuk = int(input("Masukkan TAHUN (2020-2050):"))
    
    keluar = datetime.datetime.now()
    masuk = datetime.datetime(tahunmasuk, bulanmasuk, tanggalmasuk)
    lama = keluar - masuk


print_menu()

pilihan = Input("Pilih yang anda inginkan:  ")
if pilihan == "1.CHECK IN":

