nama = str(input("Masukkan Nama: "))
nik = int(input("Masukkan NIK: "))
status = str(input("Masukkan Status (Pegawai Tetap/Honor): ")).strip().lower()
golongan = str(input("Masukkan Golongan (A/B/C): ")).strip().upper()

gaji=0
bonus=0

if (status=="pegawai tetap"):
   gaji=1000000
   if(golongan=="A"):
      bonus=200000
   elif(golongan=="B"):
      bonus=400000
   elif(golongan=="C"):
      bonus=550000
   else:
      print("Pilihan tidak valid")
      exit()


elif(status=="pegawai honor"):
   gaji=750000
   if(golongan=="A"):
      bonus=150000
   elif(golongan=="B"):
      bonus=275000
   elif(golongan=="C"):
      bonus=480000
   else:
      print("Pilihan tidak valid")
      exit()

else:
    print("Status tidak valid!")
    exit()

total=int (gaji+bonus)

print("\n ==== Detail Gaji ====\n")

print("Nama       : ",nama)
print("NIK        : ",nik)
print("Status     : ",status)
print("Gologan    : ",golongan)
print("Gaji       :  Rp.", gaji)
print("Bonus      :  Rp.", bonus)
print("Total gaji :  Rp.", total)

      
    

   