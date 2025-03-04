def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

alas = float(input("Masukkan alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))
print(f"Luas Segitiga: {luas_segitiga(alas, tinggi)}cm²")