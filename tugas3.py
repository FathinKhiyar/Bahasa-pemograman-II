# Input dari user
nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan Status (Pegawai Tetap/Honor): ").strip().lower()
golongan = input("Masukkan Golongan (A/B/C): ").strip().upper()

# Data gaji pokok dan bonus berdasarkan status & golongan
gaji_pokok = {"pegawai tetap": 1000000, "pegawai honor": 750000}
data_gaji = {
    "pegawai tetap": {"A": 200000, "B": 400000, "C": 550000},
    "pegawai honor": {"A": 150000, "B": 275000, "C": 480000}
}

gaji = 0
bonus = 0

# Loop buat nyari gaji dan bonus yang sesuai
for key in data_gaji:
    if status == key:  # Cocokin status pegawai
        if golongan in data_gaji[key]:  # Cocokin golongan
            gaji = gaji_pokok[key]
            bonus = data_gaji[key][golongan]
            break  # Kalau udah ketemu, keluar loop

# Kalau gak ketemu gajinya, berarti input salah
if gaji == 0 and bonus == 0:
    print("Input status atau golongan tidak valid!")
    exit()

total = gaji + bonus  # Hitung total gaji

# Cetak hasilnya
print("\n==== Detail Gaji ====\n")
print("Nama       : ",nama)
print("NIK        : ",nik)
print("Status     : ", status)
print("Golongan   : ",golongan)
print("Gaji       : Rp. ",gaji)
print("Bonus      : Rp. ",bonus)
print("Total gaji : Rp. ",total)