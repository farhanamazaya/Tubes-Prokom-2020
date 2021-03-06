#
#
#
#
#
#




from datetime import datetime, date
from random import randint
import os
import sys
checkin, checkout = None, None
loop = True

def print_menu(): # tampilan menu awal
    print()
    print('\t','      HOTEL MELATI SOLO BARU ')
    print()
    print('\t','---------Selamat Datang----------')
    print()
    print('Jl.Solo baru No.900, kode pos 29112 No HP. 08232111')
    print('\t','      Solo Baru Surakarta')
    print()
    print('\t',' Hotel bintang 3 dengan keunggulan: ')
    print('\t','           Nyaman')
    print('\t','            Aman')
    print('\t','           Bersih')
    print('\t','            Asri')
    print()
    print('======================================================')
    print('Pilih yang Anda inginkan :')
    print()
    print('1. CHECK IN')
    print('2. keluar program')
    print()
    
#program dimulai

while loop:
    print_menu() #memanggil def menu diatas
    pilihan = int(input('Masukan pilihan [1/2]: '))
    print() 
    os.system('cls') #membersihkan layar dalam shell
    if (pilihan == 1):  #ketika memilih 'checkIn'
        print()
        print('\t','[ ISI BIODATA PENGINAP ]')
        print('------------------------------------')
        print()
        nama = input('Masukkan nama lengkap penginap : ').upper()
        nohp = input('Masukkan No HP penginap : +62 ')
        if len(nohp) != 11 and len (nohp) != 12: 
            # ketika no hp tidak sama dengan 11/12 digit, program akan menolak.
            os.system('cls')
            print('No Hp Anda tidak terdaftar')
            continue
        ktp = input ('Apakah Anda memiliki kartu identitas KTP/SIM (y/n) : ')
        if ktp == 'n':
            sys.exit('\nError : Anda harus memuliki kartu identitas untuk menginap')      
             # penginap/tamu harus memiliki kartu identitas untuk menginap, jika tidak punya, TIDAK boleh menginap.
        elif ktp == 'y':
            kk = input('Masukkan No identitas kartu : ')
            tl = input("Masukkan Tempat lahir Anda : ").upper()
            tt = input ('Masukkan tanggal lahir Anda (dd-mm-yyyy) : ')
            print()
            os.system('cls')
        else:
            os.system('cls')
            input('\nError : Anda harus memilih antara (y/n)')
            continue
    elif (pilihan == 2):
        sys.exit('\nInformasi : Anda telah keluar program')
    else:
        print('Pilihan yang Anda masukkan salah, silahkan coba lagi')
        continue
    #mengisi tipe kamar sesuai keinginan penginap/tamu
    print()
    print('\t','ISI TIPE KAMAR SESUAI DENGAN PILIHAN PENGINAP')
    print('======================================================')
    print()
    print('1. Regular')
    print('2. Deluxe')
    print('3. Suite')
    print('4. President suite')

    tipe = int(input('Masukkan tipe kamar yang Anda pilih : '))
    os.system('cls')
    if (tipe == 1):
        kamar = 'Regular'
        tarif = ['150.000','300.000','450.000','600.000','750.000','900.000','1.050.000']
        #tarif (harga permalam) dalam berbentuk list, yang akan dipanggil.
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn :  ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%d %m %Y")
                #format tanggal
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
                #ketika format tanggal yang dimasukkan tidak sesuai, akan memunculkan pesan tersebut.

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut :  ")

            try:
                checkout = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
        waktuMenginap = checkout - checkin
        #untuk menghitung rentang hari tamu menginap.
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            try:
                pass
            except NameError:
                print()            
            sys.exit('\nError : Maksimal hanya menginap 7 hari')
    elif (tipe == 2):
        kamar = 'Deluxe'
        tarif = ['200.000','400.000','600.000','800.000','1.000.000','1.200.000','1.400.000']
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn :  ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut : ")

            try:
                checkout = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            os.system('cls')   
            print('Waktu yang Anda isi salah')
            continue

    elif (tipe == 3):
        kamar = 'Suite'
        tarif = ['185.000','370.000','555.000','740.000','925.000','1.110.000','1.295.000']
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn : ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
                
         while checkout is None:
                tanggal = input("Masukkan tanggal CheckOut : ")
                
            try:
                checkout = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            os.system('cls')   
            print('Waktu yang Anda isi salah')
            continue

    elif (tipe == 4):
        kamar = 'President suite'
        tarif = ['355.000','710.000','1.065.000','1.420.000','1.775.000','2.130.000','2.485.000']
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn : ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut : ")

            try:
                checkout = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            os.system('cls')   
            print('Waktu yang Anda isi salah')
            continue

    else:
        print('Pilihan yang Anda pilih salah, silahkan coba lagi')
        #ketika resepsionis salah meng inputkan nomor (selain 1-4)
        continue
        
        break
    #masuk kebagian kwitansi pembayaran
    print()
    print()
    print('\t','KWITANSI PEMBAYARAN RESERVASI HOTEL')
    print('---------------------------------------------')
    print()
    print('\t','Nama : '+ str(nama))
    print()
    print('\t','No HP : (+62)'+ str(nohp))
    print()
    print('\t','No Identitas : '+ str(kk))
    print()
    print('\t','TTL : '+ str(tl) + ','+ str(tt))
    print()
    print('\t','Tipe kamar : '+ str(kamar))
    print()
    for _ in range(1):
        kamar = randint(1, 20)
        print('\t','Kunci kamar nomor :',kamar)
    print()
    print('\t','Waktu : '+ str(waktu)+ ' Malam')
    print()
    print('\t','Biaya : '+ 'Rp.' + str(tarif2)+',00-')
    print()
    print('\t','Bayar dengan uang pas')
    print()
    print()
    print('Terima kasih atas kepercayaan yang Anda berikan kepada kami, semoga Anda senang')
    print()

    print('=======================================================')

    def pengecekanUlang():
    #berfungsi agar memastikan data yang diinputkan oleh resepsionis benar
        print('Silahkan cek data diatas terlebih dahulu')
        pilih = input("Apakah data tersebut sudah sesuai? [y/n]: ")
        if pilih == 'y':
            print()
        else:
            os.system('cls')
            print('Silahkan ulang dari awal, pastikan data yang Anda isi BENAR')
            sys.exit()
            #ketika terjadi kesalahan dalam pengisian data, program akan mengulan dari awal

    pengecekanUlang()

    #masuk ke bagian pembayaran
    #resepsionis akan menawarkan 2 opsi pembayaran
    while loop: 
        print("[SILAHKAN MELAKUKAN PEMBAYARAN]")
        print()
        print("Pilih metode pembayaran yang akan Anda lakukan:")
        print('1. Cash')
        print('2. Debit Card') 
        
        pilih = input("Pilih yang Anda inginkan (1/2):  ")
        if pilih == "1":
            cash = int(input('Uang dari penginap: Rp. '))
            #resepsionis menginputkan uang yang diberikan oleh tamu/penginap
            tarif3 = int(input('Biaya hotel: Rp.'))
            #resepsionis menginputkan biaya hotel, sesuai pada kwitansi
            kurang = str(tarif3 - cash)
            kembali = str(cash - tarif3)
            if (cash > tarif3):
                print ('Jumlah kembalian adalah :'+ 'Rp.' + str(kembali)+',00-')
                #program akan menampilkan kembalian yang harus diberikan kepada tamu/penginap
                print("""
            Terima kasih telah melakukan reservasi di hotel kami
            Selamat menikmati penginapan yang nyaman
            Semoga hari Anda menyenangkan:)
            """)
            
            else:
                print ('Maaf uang Anda kurang sebesar :'+ 'Rp.' + str(kurang)+',00-')
                #program akan menampilkan kekurangan uang yang harus dibayarkan lagi oleh tamu/penginap
                os.sys('cls')
                print('Pastikan uang anda cukup')
                continue


        else:
            saldo = input('Apakah saldo mencukupi? [y/n]: ')
            if saldo == 'y':
            #respsionis akan mengambil kartu debit dari tamu/penginap
            #jika kartu debit dapat digunakan (saldo cukup) , resepsionis akan menginputkan 'y'
                print("""
                Terima kasih telah melakukan reservasi di hotel kami
                Selamat menikmati penginapan yang nyaman
                Semoga hari Anda menyenangkan:)
                """)
            else :
            #respsionis akan mengambil kartu debit dari tamu/penginap
            #jika kartu debit tidak dapat digunakan (saldo tidak cukup) , resepsionis akan menginputkan 'n'
                print ("""
                Mohon maaf sisa saldo Anda tidak mencukupi untuk melakukan reservasi ini.
                Silahkan gunakan debit card lain atau menggunakan metode pembayaran lain
                """)
                ubah = input ('Ingin mengubah metode pembayaran atau mengganti debit card? [y/n]: ')
                #tamu/penginap dapat mengubah metode pembayaran / mengganti karti debit
                if ubah == 'y':
                    change = input('Ubah metode pembayaran menjadi cash? [y/n]: ')
                    #menawarkan tamu/penginap untuk mengubah pembayaran menjadi cash
                    if change == 'y':
                        os.sys('cls')
                        continue
                    else :
                        ganti = input ('Ingin mengganti debit card? [y/n]: ')
                        #menawarkan tamu untuk mengganti debit card
                        if ganti == 'y':
                            saldo = input('Apakah saldo mencukupi? [y/n]: ')
                            if saldo == 'y':
                                print("""
                                Terima kasih telah melakukan reservasi di hotel kami
                                Selamat menikmati penginapan yang nyaman
                                Semoga hari Anda menyenangkan:)
                                """)
                            else:
                                os.sys('cls')
                                print('Gunakan pembayaran Cash saja')
                                #ketika kartu debit tamu/penginap yang ke 2 masih tetap kurang saldonya
                                #tamu/penginap akan disarankan untuk menggunakan metode cash saja
                        else :
                            os.sys('cls')
                else :
                    
                    sys.exit()
                    
        ulang =''
        while ulang!= 'y' and ulang!= 't':
            #resepsionis akan menanyakan kembali kepada tamu/penginap ,
            ulang = input('Apakah anda ingin memesan kamar lagi [y/t] : ')
            if ulang == 'y':
                os.system('cls')
                print ('Silahkan pilih lagi')
                #ketika ingin memesan lagi, program akan mengulang dari awal
            elif ulang =='t':
                print('Terimankasih telah melakukan reservasi di Hotel kami :)')
                sys.exit()
            #program selesai


exit()
   




