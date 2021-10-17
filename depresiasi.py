import pandas as pd

def straightLine():
    hargaPerolehan = float(input("Masukkan harga perolehan: Rp "))
    nilaiResidu = float(input("Masukkan nilai residu: Rp "))
    umurEkonomis = float(input("Masukkan umur ekonomis (dalam tahun): "))
    depresiasi = akumulasiDepresiasi = (hargaPerolehan - nilaiResidu) / umurEkonomis

    dataDepresiasi = {
        "Akhir Tahun": [],
        "Biaya Depresiasi": [],
        "Akumulasi Depresiasi": [],
        "Nilai Buku": []
    }

    mulai = 1
    while mulai <= umurEkonomis:
        dataDepresiasi["Akhir Tahun"].append(mulai)
        dataDepresiasi["Biaya Depresiasi"].append(f"Rp {depresiasi}")
        dataDepresiasi["Akumulasi Depresiasi"].append(f"Rp {akumulasiDepresiasi}")
        dataDepresiasi["Nilai Buku"].append(f"Rp {hargaPerolehan - akumulasiDepresiasi}")

        akumulasiDepresiasi += depresiasi
        mulai += 1

    dfDataDepresiasi = pd.DataFrame(dataDepresiasi)
    print(f"\nNilai depresiasi per tahun = Rp {depresiasi}")
    print(dfDataDepresiasi)

print("+++PROGRAM MENGHITUNG DEPRESIASI+++\n")

while True:
    straightLine()

    ulang = input("\nUlang? y|n: ")
    if ulang == "y" or ulang == "Y":
        pass
    elif ulang == "n" or ulang == "N":
        print("Terima Kasih!")
        break
    else:
        print("Pilihan tidak ada!")
        break