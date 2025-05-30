# -*- coding: utf-8 -*-
"""Tugas4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1H2UtvyqRXNumHGLtC2TTh3Mf7NYa6D78
"""

# Fungsi rekursif untuk menghitung faktorial
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Input dari pengguna
angka = int(input("Masukkan angka untuk dihitung faktorialnya: "))

# Validasi input
if angka < 0:
    print("Faktorial tidak didefinisikan untuk bilangan negatif.")
else:
    hasil = faktorial(angka)
    print(f"Faktorial dari {angka} adalah {hasil}")