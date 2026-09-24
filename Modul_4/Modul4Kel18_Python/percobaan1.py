# 1. Non-return function (Void)
def sapa_pengunjung(nama, asal_daerah):
    print(f"Selamat datang {nama} dari {asal_daerah} di sistem pemantauan Desa Patakbanteng.")

# 2. Return function (Mengembalikan nilai yang sebenarnya)
def cek_status_suhu(suhu):
    print(f"Suhu yang tercatat: {suhu}°C")
    if suhu < 20:
        return "Status: Suhu terpantau dingin."
    else:
        return "Status: Suhu normal atau hangat."
    
# 3. Arbitrary function (Jumlah argumen bebas)
def catat_titik_cctv(*titik_lokasi):
    print("Lokasi CCTV yang sedang aktif:")
    for lokasi in titik_lokasi:
            print(f"- {lokasi}")

# 4. Anonymous function (Lambda)
# Misalnya untuk menghitung selisih data
hitung_selisih = lambda x, y: x - y
# Main program
sapa_pengunjung("Dafa", "Semarang")
print("-" * 30)

hasil_suhu = cek_status_suhu(18)
print(hasil_suhu)
print("-" * 30)

catat_titik_cctv("Gerbang Utama", "Balai Desa", "Area Parkir")
print("-" * 30)

print("Selisih pengunjung hari ini dan kemarin:",
hitung_selisih(150, 120))