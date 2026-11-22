Class Kenalan:
    Def __init__(self, nama, alamat, hobi):
        Self.nama = nama
        Self.alamat = alamat
        Self.hobi = hobi

    Def perkenalan_diri(self, lawan_bicara):
        Print(f”{self.nama}: Halo {lawan_bicara.nama}, kenalkan aku {self.nama}. Aku tinggal di {self.alamat} dan hobiku {self.hobi}.”)

    Def balas_sapaan(self, lawan_bicara):
        Print(f”{self.nama}: Hai juga {lawan_bicara.nama}! Aku {self.nama}, aku tinggal di {self.alamat}. Kalo Hobiku {self.hobi}, senang berkenalan denganmu!”)

# Membuat data objek dengan tambahan atribut hobi
P1 = Kenalan(“Fifah”, “Tangerang”, “Bermain Gitar”)
P2 = Kenalan(“Siti”, “Serang”, “Membaca Buku”)

# Memanggil method dari class
P1.perkenalan_diri(p2)
P2.balas_sapaan(p1)
