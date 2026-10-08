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
