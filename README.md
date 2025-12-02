# 1. Kalkulator Sederhana dengan Operasi Dasar
Struktur Program:
```python
def kalkulator_sederhana():
    # Menu dan logika utama
    while True:
        # Loop utama program
```
Bagian-bagian Penting:
a. Menu dan Input:
```python
print("=== Kalkulator Sederhana ===")
print("Operasi yang tersedia:")
print("1. Penjumlahan (+)")
# ... pilihan lainnya
pilihan = input("Pilih operasi (1-6) atau 0 untuk keluar: ")
Program menampilkan menu operasi
```
Pengguna memilih dengan angka 1-6

Input '0' untuk keluar dari program

# b. Try-Except untuk Error Handling:
python
try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
except ValueError:
    print("Error: Masukkan angka yang valid!")
try-except menangani error jika input bukan angka

float() mengkonversi input string menjadi bilangan desimal

Jika konversi gagal, muncul pesan error

c. Logika Operasi:
python
if pilihan == '1':
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")
elif pilihan == '2':
    # operasi pengurangan
# ... dst
Menggunakan if-elif untuk menentukan operasi

Setiap operasi memiliki rumus matematika tersendiri

f-string untuk format output yang rapi

d. Penanganan Kasus Khusus:
python
elif pilihan == '4':  # Pembagian
    if angka2 == 0:
        print("Error: Pembagian dengan nol!")
    else:
        hasil = angka1 / angka2
Memeriksa pembagian dengan nol

Mencegah error runtime dengan validasi

Keamanan:
Tidak menggunakan eval() - lebih aman dari injeksi kode

Validasi input manual

Error handling yang baik

2. Kalkulator dengan Input Ekspresi Langsung
Konsep Dasar:
python
hasil = eval(ekspresi)
Menggunakan fungsi eval() untuk mengevaluasi ekspresi matematika

Pengguna bisa langsung mengetik seperti: 2 + 3 * 4

Keuntungan:
python
# Pengguna bisa mengetik:
# "2 + 3"
# "5 * (10 - 3)"
# "2 ** 3 + 4"
Fleksibel - menerima ekspresi kompleks

Mendukung prioritas operasi matematika (BODMAS/PEMDAS)

Risiko dan Penanganan:
python
# PERHATIAN: eval() berbahaya!
# Contoh ekspresi berbahaya:
# __import__('os').system('rm -rf /')  # HAPUS FILE SYSTEM!
Risiko:

Code Injection: Pengguna bisa menjalankan kode Python berbahaya

Security Vulnerability: Membuka celah keamanan

Penanganan:

python
except SyntaxError:
    print("Error: Ekspresi tidak valid!")
except NameError:
    print("Error: Masukkan angka dan operator yang valid!")
Blok try-except menangani berbagai jenis error

Tapi tetap tidak sepenuhnya aman dari malicious code

Kapan menggunakan eval():
Hanya untuk program pribadi/edukasi

JANGAN gunakan untuk aplikasi web atau public-facing apps

Alternatif aman: gunakan parser matematika seperti ast.literal_eval() atau library khusus

3. Kalkulator Berbasis Fungsi
Arsitektur Modular:
python
def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

# ... fungsi lainnya
Keuntungan Desain:
Separation of Concerns: Setiap fungsi menangani satu tugas

Reusability: Fungsi bisa digunakan di tempat lain

Testability: Mudah di-test secara terpisah

Dictionary untuk Mapping:
python
operasi = {
    '+': tambah,
    '-': kurang,
    '*': kali,
    # ... mapping lainnya
}

# Pemanggilan dinamis
fungsi = operasi[operator]
hasil = fungsi(angka1, angka2)
Dictionary memetakan operator ke fungsi

Pemanggilan fungsi dinamis berdasarkan input

4. Kalkulator GUI dengan Tkinter
Komponen GUI:
a. Entry Widget:
python
entry = tk.Entry(root, font=('Arial', 20), justify='right')
Kotak input untuk menampilkan angka dan ekspresi

justify='right' untuk align kanan seperti kalkulator biasa

b. Tombol-tombol:
python
# Layout tombol menggunakan grid
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    # ... posisi tombol lainnya
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, font=('Arial', 18))
    btn.grid(row=row, column=col)
Menggunakan grid() untuk layout matrix

Loop untuk membuat tombol secara dinamis

c. Event Handling:
python
def tombol_click(angka):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(angka))
Fungsi dipanggil saat tombol ditekan

Mengambil nilai saat ini, menghapus, lalu memasukkan yang baru

d. Perhitungan:
python
def hitung():
    try:
        hasil = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(hasil))
    except:
        messagebox.showerror("Error", "Ekspresi tidak valid!")
Menggunakan eval() untuk perhitungan

messagebox untuk menampilkan error

Warning: Sama seperti versi CLI, menggunakan eval() berisiko

Perbandingan dan Rekomendasi
Fitur	Versi 1	Versi 2	Versi 3	Versi 4
Keamanan	⭐⭐⭐⭐⭐	⭐	⭐⭐⭐⭐⭐	⭐
Fleksibilitas	⭐⭐	⭐⭐⭐⭐⭐	⭐⭐	⭐⭐⭐⭐
Kemudahan	⭐⭐⭐⭐	⭐⭐⭐⭐⭐	⭐⭐⭐	⭐⭐⭐
UI/UX	CLI	CLI	CLI	GUI
Rekomendasi	Untuk pemula	Untuk eksperimen	Untuk struktur baik	Untuk GUI
Rekomendasi berdasarkan kebutuhan:
Untuk Pemula Belajar Python: Versi 1

Memahami logika dasar

Praktik control flow (if-else, while)

Error handling sederhana

Untuk Eksperimen Cepat: Versi 2

Prototyping cepat

Testing ekspresi matematika

Hanya untuk penggunaan lokal

Untuk Best Practices: Versi 3

Belajar modular programming

Separation of concerns

Code yang mudah di-maintain

Untuk Aplikasi Desktop: Versi 4

Butuh antarmuka grafis

Pengguna non-teknis

Tambah validasi input untuk keamanan

Tips Pengembangan Lanjutan:
1. Tambahkan Fitur:
python
# History perhitungan
history = []
history.append(f"{angka1} {operator} {angka2} = {hasil}")

# Memory functions
memory = 0
def memory_add(value):
    global memory
    memory += value

# Scientific functions
import math
def akar_kuadrat(x):
    return math.sqrt(x)
2. Validasi Input yang Lebih Baik:
python
import re

def is_valid_expression(expr):
    # Hanya izinkan angka, operator, dan spasi
    pattern = r'^[\d\s\+\-\*\/\(\)\.\%\^]+$'
    return bool(re.match(pattern, expr))
3. Alternatif Aman untuk eval():
python
# Menggunakan ast.literal_eval (lebih aman)
import ast

def safe_eval(expr):
    try:
        # Hanya izinkan ekspresi literal
        return ast.literal_eval(expr)
    except:
        return "Ekspresi tidak valid"
4. Unit Testing:
python
import unittest

class TestKalkulator(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3), 5)
    
    def test_bagi_nol(self):
        self.assertEqual(bagi(5, 0), "Error: Pembagian dengan nol!")

if __name__ == '__main__':
    unittest.main()
