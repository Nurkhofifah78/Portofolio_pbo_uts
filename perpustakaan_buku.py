class Buku:
    def __init__(self, judul, penulis, dipinjam=False):
        self.judul = judul
        self.penulis = penulis
        self.dipinjam = dipinjam

    def pinjam(self):
        if not self.dipinjam:
            self.dipinjam = True
            return f"Buku '{self.judul}' berhasil dipinjam."
        return f"Buku '{self.judul}' sedang dipinjam."

    def kembalikan(self):
        if self.dipinjam:
            self.dipinjam = False
            return f"Buku '{self.judul}' sudah dikembalikan."
        return f"Buku '{self.judul}' memang tersedia di rak."

    def info(self):
        status = "Dipinjam" if self.dipinjam else "Tersedia"
        return f"[{status}] {self.judul} — {self.penulis}"


class Perpustakaan:
    def __init__(self, nama_ruang):
        self.nama_ruang = nama_ruang
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_koleksi(self):
        print(f"=== Koleksi {self.nama_ruang} ===")
        for buku in self.daftar_buku:
            print("-", buku.info())


# Pembuatan objek Buku
buku1 = Buku("Dasar Sistem Informasi", "Budi Santoso")
buku2 = Buku("Pemrograman Python Praktis", "Siti Rahma")

# Pembuatan objek Perpustakaan
ruang1 = Perpustakaan("Ruang Baca Utama")
ruang2 = Perpustakaan("Ruang Referensi")

# Menghubungkan objek ke perpustakaan
ruang1.tambah_buku(buku1)
ruang1.tambah_buku(buku2)
ruang2.tambah_buku(buku2)

# Menjalankan method pada objek
print(buku1.pinjam())
ruang1.tampilkan_koleksi()
ruang2.tampilkan_koleksi()

