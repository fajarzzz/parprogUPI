# Kelompok 5
# 1. Fajar Zuliansyah Trihutama
# 2. Khamidah A.S
# 3. Ade Ariyansyah
# 4. Qolbu
import json
import os
from datetime import datetime
ADRESS_FILE = 'D:/PERKULIAHAN/BelajarPython/pythonParprog/data.json'


def header():
    print("==============================================")
    print("       SISTEM MANAJEMEN KEUANGAN PRIBADI")
    print("==============================================")


def footer():
    print("==============================================")
    print("|        all rights reserved ©2020           |")
    print("==============================================")
def countData(data):
    hasil=len(data)
    return hasil

def validitas(pilih,data,status):
    while(True):
        if(status==1):
            batas= countData(data)
        elif(status == 4):
            batas = 4
        elif(status == 3):
            batas = 5
        if(pilih > batas):
            os.system('cls')
            input("Masukkan anda salah!! \nUlangi, Tekan enter...")
            break
        else:
            break


def akhir(x): return x-1


def totalSaldo(data):
    saldoAkhir = data["saldo"]["awal"]
    for value in data["saldo"]["pendapatan"].keys():
        saldoAkhir += data["saldo"]["pendapatan"][value]
    for value in data["saldo"]["pengeluaran"].keys():
        saldoAkhir -= data["saldo"]["pengeluaran"][value]
    return saldoAkhir
def totalArray(data):
    total=0
    for value in data:
        total+=value
    return total
def cekMoney(data,pengeluaran):
    if(totalSaldo(data)<pengeluaran):
        enough=False
    else:
        enough=True
    return enough
def simpanData(data):
    with open(ADRESS_FILE, "w") as b:
        b.write(json.dumps(data))
def notesTransaction(jenis,jumlah):
    a = datetime.now()
    b=(a.strftime("%d/%m/%Y, %H:%M:%S"))
    kamus={
        "times": "",
        "jenis": "",
        "jumlah": 0
    }
    kamus["times"]=b
    kamus["jenis"] = jenis
    kamus["jumlah"]=jumlah
    data["transaksi"].append(kamus)
    #hutang berkurang
    if(jenis=="Cicilan" and data["hutang"]!=0):
        data["hutang"]-=jumlah
    elif(jenis=="Cicilan" and data["hutang"]==0):
        print("Anda tidak punya hutang")
def printHistory(data):
    for value in data:
        print("{}++++++++++++++++++++++++++".format(value["times"]))
        print("  Jenis transaksi : {}".format(value["jenis"]))
        print("  Jumlah          : Rp{},00\n".format(value["jumlah"]))

# open file json dan parsing json ke dict
with open(ADRESS_FILE) as a:
    data = json.load(a)

finalIndex = akhir(len(data["saldo"])-1)
# jika belum ada data nama
if(data["nama"] == ""):
    # menu isi data diri
    os.system('cls')
    header()
    print("|              Isi Data Pribadi              |")
    print("==============================================")
    # input data diri
    data["nama"] = str(input("  Nama            : "))
    data["nik"] = str(input("  Nomor Identitas : "))
    data["hp"] = str(input("  No. Telepon     : "))
    data["surel"] = str(input("  Email           : "))
    data["saldo"]["awal"] = int(input("  Saldo Awal      : Rp "))
    notesTransaction("Saldo Awal", data["saldo"]["awal"])
    data["tabungan"] = int(input("  Tabungan        : Rp "))
    notesTransaction("Tabungan", data["tabungan"])
    footer()
    input()
    # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
    with open(ADRESS_FILE, "w") as b:
        b.write(json.dumps(data))
    os.system('cls')
# menu utama
pilih = 1
while(pilih != 0):
    os.system('cls')
    header()
    print("|                 Menu Utama                 |")
    print("==============================================")
    print("1. Info")
    print("2. Input Data Keuangan")
    print("3. Laporan Keuangan")
    print("4. Ambil Tabungan")
    print("5. Hapus Riwayat Transaksi")
    print("0. Keluar")
    
    pilih = int(input("Pilihan anda : "))
    # cek validitas pilihan
    validitas(pilih,data["saldo"],3)
    # jika pilihannya adalah info
    if(pilih == 1):
        # menu info
        pilih1 = 1
        while(pilih1 != 0):
            os.system('cls')
            header()
            print("|                  Menu Info                 |")
            print("==============================================")
            print("1. Data Diri")
            print("2. Info Saldo")
            print("3. Riwayat Transaksi")
            print("0. Kembali")
            pilih1 = int(input("Pilihan anda : "))
            # cek  pilihan
            validitas(pilih1,data["saldo"],3)
            # jika pilihannya adalah data diri
            if(pilih1 == 1):
                # tampilan profil
                os.system('cls')
                header()
                print("|                   Profil                   |")
                print("==============================================")
                print("  Nama            :", data["nama"])
                print("  Nomor Identitas :", data["nik"])
                print("  Nomor Telepon   :", data["hp"])
                print("  Email           :", data["surel"])
                print("  Saldo           : Rp{}{}".format(
                    totalSaldo(data), ",00"))
                print("  Tabungan        : Rp{}{}".format(data["tabungan"], ",00"))
                print("  Hutang          : Rp{}{}".format(data["hutang"], ",00"))
                footer()
                input("Tekan enter untuk kembali...")
            # jika pilihannya adalah info saldo
            elif (pilih1 == 2):
                # tampilan profil
                os.system('cls')
                header()
                print("|                 Info Saldo                 |")
                print("==============================================")
                print("  Saldo            : Rp{}{}".format(
                    totalSaldo(data), ",00"))
                print("       Saldo Awal  : Rp{}{}".format(
                      data["saldo"]["awal"], ",00"))
                print("       Pendapatan  : ")
                for key, value in data["saldo"]["pendapatan"].items():
                    print("              {}  : Rp{}{}".format(key.capitalize(), data["saldo"]["pendapatan"][key],",00"))
                print("       Pengeluaran : ")
                for key, value in data["saldo"]["pengeluaran"].items():
                    print("              {}  : Rp{}{}".format(key.capitalize(), data["saldo"]["pengeluaran"][key],",00"))
                print(
                    "\nCatatan :\n Saldo = pendapatan + saldo awal - pengeluaran")
                footer()
                input("Tekan enter untuk kembali...")
            # jika pilihannya adalah riwayat transaksi
            elif (pilih1 == 3):
                # tampilan riwayat transaksi
                os.system('cls')
                header()
                print("|              Riwayat Transaksi             |")
                print("==============================================")
                if(len(data["transaksi"])!=0):
                    printHistory(data["transaksi"])
                else:
                    print("-----------------Data Kosong------------------")
                footer()
                input("Tekan enter untuk kembali...")
    # jika pilihannya adalah input data maka
    elif (pilih == 2):
        # menu input data
        pilih2 = 1
        while(pilih2 != 0):
            os.system('cls')
            header()
            print("|          Menu Input Data Keuangan          |")
            print("==============================================")
            print("1. Pendapatan")
            print("2. Pengeluaran")
            print("3. Tabungan")
            print("4. Hutang")
            print("0. Kembali")
            pilih2 = int(input("Pilihan anda : "))
            # cek  pilihan
            validitas(pilih2,data["saldo"],4)
            # jika memilih menu pendapatan
            if(pilih2 == 1):
                pilihan1 = 1
                while(pilihan1 != 0):
                    # tampilan menu input pendapatan
                    os.system('cls')
                    header()
                    print("|            Menu Input Pendapatan           |")
                    print("==============================================")
                    print("1. Uang Saku")
                    print("2. Gaji")
                    print("0. Kembali")
                    pilihan1 = int(input("Pilihan anda : "))
                    # cek  pilihan
                    validitas(pilihan1,data["saldo"]["pendapatan"],1)
                    if(pilihan1 == 1):
                        os.system('cls')
                        header()
                        print("|               Input Uang Saku              |")
                        print("==============================================")
                        uangSaku = int(input("  Uang Saku : Rp "))
                        data["saldo"]["pendapatan"]["saku"]+=uangSaku
                        notesTransaction("Uang Saku",uangSaku)
                        footer()
                        # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                        simpanData(data)
                        input("Data berhasil diinputkan,Tekan enter...")
                    elif(pilihan1==2):
                        os.system('cls')
                        header()
                        print("|                 Input Gaji                 |")
                        print("==============================================")
                        gaji = int(input("  Gaji : Rp "))
                        data["saldo"]["pendapatan"]["gaji"]+=gaji
                        notesTransaction("Gaji",gaji)
                        footer()
                        # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                        simpanData(data)
                        input("Data berhasil diinputkan,Tekan enter...")
            elif(pilih2==2):
                pilihan2=1
                while(pilihan2 != 0):
                    os.system('cls')
                    header()
                    print("|           Menu Input Pengeluaran           |")
                    print("==============================================")
                    print("1. Pendidikan")
                    print("2. Makanan atau Minuman")
                    print("3. Kebutuhan diri")
                    print("4. Rumah Tangga")
                    print("5. Transportasi")
                    print("6. Cicilan")
                    print("7. Asuransi")
                    print("8. Lain-lain")
                    print("0. Kembali")
                    pilihan2 = int(input("Pilihan anda : "))
                    # cek validitas pilihan
                    validitas(pilihan2,data["saldo"]["pengeluaran"],1)
                    if(pilihan2 == 1):
                        os.system('cls')
                        header()
                        print("|           Pengeluaran Pendidikan           |")
                        print("==============================================")
                        uangPendidikan = int(input("  Biaya Pendidikan : Rp "))
                        if(cekMoney(data, uangPendidikan) == True):
                            data["saldo"]["pengeluaran"]["pendidikan"]+=uangPendidikan
                            notesTransaction("Pendidikan", uangPendidikan)
                            # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                            simpanData(data)
                            input("Data berhasil diinputkan,Tekan enter...")
                        else:
                            input("Uang anda tidak cukup, kerja!!!")
                        footer()
                    elif(pilihan2==2):
                        os.system('cls')
                        header()
                        print("|      Pengeluaran Makanan dan Minuman       |")
                        print("==============================================")
                        fd = int(input("  Biaya Makan/Minum : Rp "))
                        if(cekMoney(data, fd) == True):
                            data["saldo"]["pengeluaran"]["f&d"]+=fd
                            notesTransaction("Makan/Minum", fd)
                            # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                            simpanData(data)
                            input("Data berhasil diinputkan,Tekan enter...")
                        else:
                            input("Uang anda tidak cukup, kerja!!!")
                        footer()
                    elif(pilihan2==3):
                        os.system('cls')
                        header()
                        print("|        Pengeluaran Kebutuhan Diri          |")
                        print("==============================================")
                        kebdir = int(input("  Biaya Kebutuhan Diri: Rp "))
                        if(cekMoney(data, kebdir) == True):
                            data["saldo"]["pengeluaran"]["kebutuhan"]+=kebdir
                            notesTransaction("Kebutuhan", kebdir)
                            # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                            simpanData(data)
                            input("Data berhasil diinputkan,Tekan enter...")
                        else:
                            input("Uang anda tidak cukup, kerja!!!")
                        footer()
                    elif(pilihan2 == 4):
                        os.system('cls')
                        header()
                        print("|        Pengeluaran Rumah Tangga          |")
                        print("==============================================")
                        rt = int(input("  Biaya Rumah Tangga: Rp "))
                        if(cekMoney(data, rt) == True):
                            data["saldo"]["pengeluaran"]["rt"]+=rt
                            notesTransaction("Rumah Tangga", rt)
                            # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                            simpanData(data)
                            input("Data berhasil diinputkan,Tekan enter...")
                        else:
                            input("Uang anda tidak cukup, kerja!!!")
                        footer()
                    elif(pilihan2 == 5):
                        os.system('cls')
                        header()
                        print("|         Pengeluaran Transportasi           |")
                        print("==============================================")
                        transport = int(input("  Biaya Transportasi: Rp "))
                        if(cekMoney(data, transport) == True):
                            data["saldo"]["pengeluaran"]["transport"]+=transport
                            notesTransaction("Transportasi", trasnsport)
                            # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                            simpanData(data)
                            input("Data berhasil diinputkan,Tekan enter...")
                        else:
                            input("Uang anda tidak cukup, kerja!!!")
                        footer()
                    elif(pilihan2 == 6):
                        os.system('cls')
                        header()
                        print("|           Pengeluaran Cicilan              |")
                        print("==============================================")
                        cicil = int(input("  Bayar Cicilan : Rp "))
                        if(cekMoney(data, cicil) == True):
                            data["saldo"]["pengeluaran"]["cicilan"]+=cicil
                            notesTransaction("Cicilan", cicil)
                            # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                            simpanData(data)
                            input("Data berhasil diinputkan,Tekan enter...")
                        else:
                            input("Uang anda tidak cukup, kerja!!!")
                        footer()
                    elif(pilihan2 == 7):
                        os.system('cls')
                        header()
                        print("|           Pengeluaran Asuransi             |")
                        print("==============================================")
                        asuransi = int(input("  Bayar Asuransi: Rp "))
                        if(cekMoney(data, asuransi) == True):
                            data["saldo"]["pengeluaran"]["asuransi"]+=asuransi
                            notesTransaction("Asuransi", asuransi)
                            # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                            simpanData(data)
                            input("Data berhasil diinputkan,Tekan enter...")
                        else:
                            input("Uang anda tidak cukup, kerja!!!")
                        footer()
                    elif (pilihan2==8):
                        os.system('cls')
                        header()
                        print("|            Pengeluaran Lainnya             |")
                        print("==============================================")
                        lain = int(input("  Pengeluaran Lainnya : Rp "))
                        if(cekMoney(data, lain) == True):
                            data["saldo"]["pengeluaran"]["lain"]+=lain
                            notesTransaction("Lain", lain)
                            # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                            simpanData(data)
                            input("Data berhasil diinputkan,Tekan enter...")
                        else:
                            input("Uang anda tidak cukup, kerja!!!")
                        footer() 
            elif(pilih2 == 3):
                os.system('cls')
                header()
                print("|               Input Tabungan               |")
                print("==============================================")
                tabungan = int(input("  Tabungan : Rp "))
                data["tabungan"]+=tabungan
                notesTransaction("Tabungan",tabungan)
                # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                simpanData(data)
                footer()
                input("Data berhasil diinputkan,Tekan enter...")
            elif(pilih2 == 4):
                os.system('cls')
                header()
                print("|                Input Hutang                |")
                print("==============================================")
                hutang = int(input("  Hutang : Rp "))
                data["hutang"]+=hutang
                notesTransaction("Hutang", hutang)
                # open file json dan replace dengan format json yang didapatkan dengan parsing dict ke json
                simpanData(data)
                footer()
                input("Data berhasil diinputkan,Tekan enter...")

    # jika pilihannya adalah laporan keuangan
    elif (pilih == 3):
        # tampilan laporan keuangan
        os.system('cls')
        header()
        print("|              Laporan Keuangan              |")
        print("==============================================")
        print("Saldo          : Rp {},00".format(totalSaldo(data)))
        print("   Awal        : Rp {},00".format(data["saldo"]["awal"]))
        print("   Hutang      : Rp {},00".format(data["hutang"]))
        print("   Tabungan    : Rp {},00".format(data["tabungan"]))
        total = 0
        for key in data["saldo"]["pendapatan"].keys():
            total += data["saldo"]["pendapatan"][key]
        print("   Pendapatan  : Rp {},00".format(total))
        total2 = 0
        for key in data["saldo"]["pengeluaran"].keys():
            total2 += data["saldo"]["pengeluaran"][key]
        print("   Pengeluaran : Rp {},00".format(total2))
        print("++++++++++++++++++++++++++++++++++++++++++++++")
        print("Analisis       : ")

        if(total<total2 and data["saldo"]["pendapatan"]["lain"]!= 0 and data["hutang"]!=0):
            print("    Pengeluaran anda melebihi pendapatan yang anda terima, kurangi penggunaan uang kepada hal yang tidak penting,hutang anda juga belum lunas,bayar dan segera berhemat! Bahkan anda sudah pernah mengambil uang tabungan")
        elif(total<total2 and data["saldo"]["pendapatan"]["lain"]!= 0 and data["hutang"]==0):
            print("    Pengeluaran anda melebihi pendapatan yang anda terima, kurangi penggunaan uang kepada hal yang tidak penting,segera berhemat! Bahkan anda sudah pernah mengambil uang tabungan")
        elif(total<total2 and data["saldo"]["pendapatan"]["lain"]!=0 and data["hutang"]!=0):
            print("    Pengeluaran anda melebihi pendapatan yang anda terima, kurangi penggunaan uang kepada hal yang tidak penting,segera berhemat! Bahkan anda sudah pernah mengambil uang tabungan,tetapi masih saja hutang belum lunas")
        elif(total<total2 and data["saldo"]["pendapatan"]["lain"]==0 and data["hutang"]==0):
            print("    Pengeluaran anda melebihi pendapatan yang anda terima, kurangi penggunaan uang kepada hal yang tidak penting,segera berhemat! Tetapi anda belum pernah mengambil uang tabungan")
        elif(total > total2 and data["tabungan"] == 0 and data["hutang"] != 0):
            print("    Keuangan anda sehat tetapi anda tidak punya tabungan dan masih punya hutang")
        elif(total > total2 and data["tabungan"] == 0 and data["hutang"] == 0):
            print("    Keuangan anda sehat tetapi anda tidak punya tabungan")
        else:
            print("    Keuangan anda sehat,Maksimalkan!")
        footer()
        input("Tekan enter untuk kembali...")
    elif(pilih==4):
        os.system('cls')
        header()
        print("|           Pindah Uang Tabungan             |")
        print("==============================================")
        tarik=int(input("Jumlah : "))
        data["saldo"]["pendapatan"]["lain"]+=tarik
        data["tabungan"]-=tarik
        simpanData(data)
        footer()
        input("Data berhasil diinputkan,Tekan enter...")
    elif (pilih == 5):
        # tampilan hapus riwayat transaksi
        os.system('cls')
        header()
        print("|             Riwayat Transaksi              |")
        print("==============================================")
        yakin=input("Yakin hapus riwayat transaksi ? (Y/T) : ")
        if(yakin.upper()=='Y'):
            del data["transaksi"][:len(data["transaksi"])]
            simpanData(data)
            print("-------------Data sudah terhapus-------------")
        footer()
        input("Tekan enter untuk kembali...")
os.system('cls')  # clearscreen
