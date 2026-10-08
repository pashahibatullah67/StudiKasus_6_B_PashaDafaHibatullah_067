# StudiKasus_6_B_PashaDafaHibatullah_067

Nama : Pasha Dafa Hibatullah

NIM : 2609116067

Kelas : B 

Pada Kesempatan kali ini saya akan menjelaskan tentang studi kasus 6 : sistem pencatatan nilai mahasiswa, yang dimana program digunakan untuk mencatat  dan melihat histori nilai dari mahasiswa. Didalam program ini, data yang dipakai disimpan menggunakan file json, yang dimana berfungsi jika program telah ditutup atau berakhir, data yang telah ditambahkan akan tetap tersimpan hingga saat program dijalankan kembali. Didalam program ini, pengguna dapat melihat data nilai dari mahasiswa tersebut ataupun menambahkan data nilai mahasiswa yang baru.

<img width="161" height="38" alt="Screenshot 2026-10-08 224515" src="https://github.com/user-attachments/assets/4a787f16-600d-4f87-be2c-ab4be9215167" />
 
Yang pertama ada screenshot dari import json. Import json ini digunakan ke dalam program ini untuk mengaktifkan file json yang tersimpan di folder yang sama dengan file phyton yang ingin digunakan. import json ini digunakan untuk membaca data dari file json itu serta untuk menyimpan data ke dalam file json.

<img width="222" height="24" alt="Screenshot 2026-10-08 224906" src="https://github.com/user-attachments/assets/14b4511a-fb11-41f3-b8e5-b4d12f93ea3c" />

Pada screenshot ini menampilkan nilai_json. nilai_json digunakan sebagai tempat untuk menaruh data nilai dari mahasiswa yang ada didalam program. Tanda [ ] atau kurung siku ini diguakan untuk menunjukkan kalau data itu awalnya hanya berupa list yang masih kosong. Data yang dibaca dari file JSOn nantinya akan dimasukkan ke dalam list kosong ini.

<img width="345" height="39" alt="Screenshot 2026-10-08 225251" src="https://github.com/user-attachments/assets/e542ecbb-fdf5-4f72-a23b-b4ee387ab76f" />

Pada screenshot ini menunjukkan bagian membuka dan juga membaca file Json tersebut. with open() digunakan untuk membuat file nilai_mahasiswa.json. Mode "r" atau "Read" digunakan seperti namanya, yaitu untuk membaca isi file nilai_mahassiwa.json tersebut. Setelah itu ada json.load(file) yang digunakan untuk mengambil data dari file nilai_mahasiswa.json tersebut dan dimasukkan ke dalam variabel nilai_json. Ada pula (file) itu diambil dari bagian "as file" yang dimana itu bekerja sebagai pengganti nama atau alias dari file nilai_mahasiswa.json tersebut.

<img width="404" height="121" alt="Screenshot 2026-10-08 230155" src="https://github.com/user-attachments/assets/423b2052-8b79-4552-8ad5-ee0b0fea0bf3" />
<img width="240" height="125" alt="Screenshot 2026-10-08 231642" src="https://github.com/user-attachments/assets/fbe45338-34c0-447a-8471-093ee86af128" />

Pada bagian screenshot ini menunjukkan def tampilkan(). Yang dimana def tampilkan() ini digunakan untuk menampilkan seluruh data nilai mahasiswa yang ada didalam nilai_json. Data nanti akan ditampilkan satu persatu dan pengguna dapat melihat nama, nim, dan nilai dari mahasiswa tersebut dengan cara dipanggil dari keys nya mereka yang ada di file JSON. Yang dimana akan dipanggil sesuai keys paling teratas lalu kebawah dan tertampil dari paling kiri sampai ke kanan.

<img width="417" height="206" alt="Screenshot 2026-10-08 230208" src="https://github.com/user-attachments/assets/431bd0b0-d9f6-42d3-b919-5f4529f79566" />
<img width="291" height="119" alt="Screenshot 2026-10-08 232419" src="https://github.com/user-attachments/assets/4aede229-640e-4753-a352-86345e265bc5" />

Pada bagian screenshot ini menunjukkan def tambah() beserta output nya. Fungsi dari tambah() itu sendiri digunakan untuk menambahkan data nilai mahasiswa yang baru. Pengguna diminta untuk menambahkan nama, nim, dan juga nilai dari mahasiswa yang ingin ditambahkan ke dalam data tersebut. yang kemudian data tersebut akan tersimpan ke dalam list menggunakan append(). setelah data tersimpan, program akan menyimpan kembali data tersebut masuk ke dalam file JSON mengunakan json.dump(). Yang dimana itu akan berfungsi menyimpan data yang telah diperbarui bahkan setelah program telah di berhentikan hingga di gunakan kembali

<img width="525" height="206" alt="Screenshot 2026-10-08 230505" src="https://github.com/user-attachments/assets/41e49475-102a-43e7-8b2b-49fc8609c8b9" />

Pada screenshot ini menunjukkan perulangan atau wile true. While true digunakan pada program ini supaya program dapat tetap digunakan berjalan bahkan saat pengguna memilih opsi untuk melihat data ataupun menambahkan data yang baru. Dan di while true ini juga menggunakan break jika pengguna meimilih untuk menghentikan program dengan cara memilih opsi ketiga, yaitu keluar. Walaupun pengguna telah keluar dan berhenti menggunakan prpogram, data nilai-niali dari para mahasiswa akan tetap tersimpan karena bantuan dari file json tersebut yang akan menyimpankan data yang telah diperbarui atau ditambahkan.
