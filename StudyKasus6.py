import json
import os

os.system("cls")

nilai_json = []

with open("Nilai_Mahasiswa.json", "r") as file:
    nilai_json = json.load(file)

def tampilkan_data():
    if len(nilai_json) == 0:
        print("Belum ada data nilainya bosku")
    else:
        print("\n=== DATA NILAI MAHASISWA ===")
        for i in nilai_json:
            print(i["Nama"], i["Nim"], i["Nilai"])

def tambah_data():
    nama_mahasiswa = input("Masukkan nama mahasiswa: ")
    nim_mahasiswa = input("Masukkan Nim mahasiswa: ")
    nilai_mahasiswa = int(input("Masukkan nilai dari mahasiswa: "))

    nilai_json.append({
        "Nama": nama_mahasiswa,
        "Nim": nim_mahasiswa,
        "Nilai": nilai_mahasiswa
    })

    with open("Nilai_Mahasiswa.json", "w") as file:
        json.dump(nilai_json, file, indent = 4)

while True:
    print("PILIH ANGKA DARI 1-3. \n1. LIHAT DATA. \n2. MENAMBAHKAN DATA. \n3 KELUAR")
    pilihan = input("Pilihan angka: ")

    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        break
    else:
        print("Pilihan anda tidak valid bos, piilh lagi.")
