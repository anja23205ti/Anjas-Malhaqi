Kendaraan=['S','avanza',2500,'merah']
print(Kendaraan)
Kendaraan.append(300)
Kendaraan.append(4)
Kendaraan.insert(2,'Toyota')
Kendaraan.insert(3, 'Veloz')
print(Kendaraan)
print("Pilih bangun datar:")
print("1. Persegi")
print("2. Lingkaran")
print("3. Segitiga")

menu = int(input("Masukkan pilihan (1/2/3): "))

match menu:
    case 1:
        sisi = float(input("Masukkan sisi persegi: "))
        luas = sisi*sisi
    case 2:
        jari_jari = float(input("Masukkan jari-jari lingkaran: "))
        luas = 3,14*jari_jari*jari_jari
    case 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = alas*tinggi/2
    case _:
        print("Pilihan tidak valid.")
        luas = None

if luas is not None:
    print(f"Luas bangun datar adalah: {luas}")