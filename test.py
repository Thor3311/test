def kalkulator_sederhana():
    print("=== Kalkulator Sederhana ===")
    print("Operasi yang tersedia:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Modulus (%)")
    print("6. Pangkat (^)")
    print("0. Keluar")
    
    while True:
        try:
            print("\n" + "="*30)
            pilihan = input("Pilih operasi (1-6) atau 0 untuk keluar: ")
            
            if pilihan == '0':
                print("Terima kasih telah menggunakan kalkulator!")
                break
            
            if pilihan not in ['1', '2', '3', '4', '5', '6']:
                print("Pilihan tidak valid!")
                continue
            
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            
            if pilihan == '1':
                hasil = angka1 + angka2
                print(f"{angka1} + {angka2} = {hasil}")
            
            elif pilihan == '2':
                hasil = angka1 - angka2
                print(f"{angka1} - {angka2} = {hasil}")
            
            elif pilihan == '3':
                hasil = angka1 * angka2
                print(f"{angka1} × {angka2} = {hasil}")
            
            elif pilihan == '4':
                if angka2 == 0:
                    print("Error: Pembagian dengan nol!")
                else:
                    hasil = angka1 / angka2
                    print(f"{angka1} ÷ {angka2} = {hasil}")
            
            elif pilihan == '5':
                hasil = angka1 % angka2
                print(f"{angka1} % {angka2} = {hasil}")
            
            elif pilihan == '6':
                hasil = angka1 ** angka2
                print(f"{angka1} ^ {angka2} = {hasil}")
                
        except ValueError:
            print("Error: Masukkan angka yang valid!")
        except Exception as e:
            print(f"Error: {e}")

# Jalankan kalkulator
kalkulator_sederhana()

def kalkulator_ekspresi():
    print("=== Kalkulator Ekspresi ===")
    print("Contoh: 2 + 3, 5 * 4, 10 / 2")
    print("Gunakan: +, -, *, /, %, ** untuk pangkat")
    print("Ketik 'quit' untuk keluar")
    
    while True:
        ekspresi = input("\nMasukkan ekspresi: ").strip()
        
        if ekspresi.lower() == 'quit':
            print("Terima kasih!")
            break
        
        if not ekspresi:
            continue
        
        try:
            # Menggunakan eval untuk menghitung ekspresi
            # PERHATIAN: eval() bisa berbahaya jika digunakan untuk input tidak terpercaya
            hasil = eval(ekspresi)
            print(f"Hasil: {hasil}")
        except ZeroDivisionError:
            print("Error: Pembagian dengan nol!")
        except SyntaxError:
            print("Error: Ekspresi tidak valid!")
        except NameError:
            print("Error: Masukkan angka dan operator yang valid!")
        except Exception as e:
            print(f"Error: {e}")

# Jalankan kalkulator
kalkulator_ekspresi()

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol!"
    return a / b

def modulus(a, b):
    return a % b

def pangkat(a, b):
    return a ** b

def kalkulator_fungsi():
    print("=== Kalkulator Berbasis Fungsi ===")
    
    operasi = {
        '+': tambah,
        '-': kurang,
        '*': kali,
        '/': bagi,
        '%': modulus,
        '^': pangkat
    }
    
    while True:
        print("\nOperasi yang tersedia: +, -, *, /, %, ^")
        print("Ketik 'exit' untuk keluar")
        
        operator = input("Masukkan operator: ")
        
        if operator.lower() == 'exit':
            print("Terima kasih!")
            break
        
        if operator not in operasi:
            print("Operator tidak valid!")
            continue
        
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            
            fungsi = operasi[operator]
            hasil = fungsi(angka1, angka2)
            
            print(f"\n{angka1} {operator} {angka2} = {hasil}")
            
        except ValueError:
            print("Error: Masukkan angka yang valid!")
        except Exception as e:
            print(f"Error: {e}")

# Jalankan kalkulator
kalkulator_fungsi()

import tkinter as tk
from tkinter import messagebox

def buat_kalkulator_gui():
    def tombol_click(angka):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + str(angka))
    
    def clear():
        entry.delete(0, tk.END)
    
    def hitung():
        try:
            hasil = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(hasil))
        except:
            messagebox.showerror("Error", "Ekspresi tidak valid!")
            entry.delete(0, tk.END)
    
    # Buat window
    root = tk.Tk()
    root.title("Kalkulator GUI")
    root.geometry("300x400")
    
    # Entry untuk menampilkan angka
    entry = tk.Entry(root, font=('Arial', 20), justify='right')
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)
    
    # Tombol-tombol
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]
    
    for (text, row, col) in buttons:
        if text == '=':
            btn = tk.Button(root, text=text, font=('Arial', 18), 
                          command=hitung, bg='orange', fg='white')
        elif text in ['/', '*', '-', '+']:
            btn = tk.Button(root, text=text, font=('Arial', 18), 
                          command=lambda t=text: tombol_click(t), bg='lightgray')
        else:
            btn = tk.Button(root, text=text, font=('Arial', 18), 
                          command=lambda t=text: tombol_click(t))
        
        btn.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)
    
    # Tombol clear
    clear_btn = tk.Button(root, text='C', font=('Arial', 18), 
                         command=clear, bg='red', fg='white')
    clear_btn.grid(row=5, column=0, columnspan=4, sticky='ew', padx=5, pady=5, ipady=10)
    
    root.mainloop()

# Jalankan kalkulator GUI
# buat_kalkulator_gui()
