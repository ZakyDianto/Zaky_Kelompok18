class MahasiswaTekkom:
    def __init__(self, nama, konsentrasi):
        self.nama = nama
        self.konsentrasi = konsentrasi

    def profil(self):
        print(f"Halo! Saya {self.nama}, mahasiswa Teknik Komputer dengan fokus di {self.konsentrasi}.")

    def deadline_tugas(self, hari):
        print("Waktu tersisa untuk pengumpulan project:")
        while hari > 0:
            print(f"{hari} hari lagi...")
            hari -= 1
        print("Waktu habis! Sistem ditutup.")

obj = MahasiswaTekkom("Jeki", "Backend Specialist")

obj.profil()
print("-" * 30)
obj.deadline_tugas(4)