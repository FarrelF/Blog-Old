# Farrel Franqois Blog
[![Netlify Status](https://api.netlify.com/api/v1/badges/edc59a5f-e63a-426c-ae65-cffe9153fa04/deploy-status)](https://app.netlify.com/sites/farrelf/deploys)
![GitHub](https://img.shields.io/github/license/FarrelF/FarrelF-Blog?label=Lisensi&style=flat-square)

*Repository* GitHub ini merupakan Kode Sumber dari Blog saya. Blog ini saya buat menggunakan Pelican, yang berbasis Python.

## Cara Kerja
Kode Sumber ini hanya berguna untuk menghasilkan berkas HTML statis saja, dan ini tidak bisa di eksekusi secara langsung, seperti hal nya Blog yang di buat dengan WordPress. (Karena sesuai dengan peruntukan nya, yakni: *Static Site Generator*)

Untuk menghasilkan konten yang kemudian di sebar melalui Internet, saya men-*deploy* kode sumber ini ke Netlify, lalu mereka lah yang menghasilkan berkas HTML statis di dalam nya, yang kemudian di sebar ke Internet.

## Cara Memperoleh nya
Untuk memperoleh nya, Anda bisa Unduh Kode Sumber nya dengan meng-klik pada *Button* 'Clone & Download', lalu kamu klik 'Download ZIP' untuk mengunduh nya sebagai ZIP.

Namun, jika Anda lebih suka meng-*clone* atau meng-kloning nya dengan Git, Anda bisa eksekusi perintah berikut untuk meng-klon nya:

```bash
$ git clone https://github.com/FarrelF/FarrelF-Blog.git
```

Setelah Anda meng-klon nya, terutama dengan perintah di atas, kode sumber akan secara otomatis tersimpan di dalam Folder yang bernama `FarrelF-Blog`.

## Cara Install
Untuk meng-installnya, buatlah sebuah 'Lingkungan Virtual' (atau bahasa Inggris nya adalah: *Virtual Environment*) dengan `virtualenv`, lalu aktifkan "Lingkungan" tersebut.

Saya sarankan Anda gunakan Python 3.6, Python 3.7 atau yang lebih baru sebelum/saat membuat sebuah Lingkungan Virtual.

Setelah di aktifkan, Install semua ketergantungan yang ada di dalam berkas `requirements.txt` dengan `pip`.

Lalu, kamu bisa coba untuk menghasilkan sebuah berkas HTML Statis ini dengan Pelican, yang kemudian bisa kamu akses dengan Web Browser kamu.

Di dalam GNU/Linux atau macOS (Atau, Sistem Operasi berbasis Unix-like/Unix lain nya), kamu dapat eksekusi perintah berikut agar Pelican dapat menghasilkan Berkas HTML Statis dan juga mengaktifkan fitur Web Server pada Python:

**Catatan**: Tapi sebelum itu, pastikan kalau kamu sudah berada di dalam Folder Kode Sumber nya, yah :slightly_smiling_face:

```bash
$ pelican --autoreload --listen
```
Atau, bisa melalui perintah berikut:
```bash
$ make devserver
```
Sedangkan di Windows, ada tiga (yang sebenarnya 'empat') langkah yang harus kamu turuti, yaitu:
1. Hasilkan Berkas HTML terlebih dahulu dengan Pelican, menggunakan Perintah berikut:
```powershell
> pelican --autoreload
```
2. Kemudian, kamu buka lagi CMD/PowerShell di Jendela yang baru atau buka Tab Baru jika kamu menggunakan [Windows Terminal](https://github.com/microsoft/terminal), lalu aktifkan "Lingkungan Virtual" nya.

3. Setelah itu, Aktifkan fitur Web Server pada Python dengan perintah berikut:
```powershell
> pelican --listen
```

Setelah semua nya selesai dan dinyatakan berhasil, bisa kamu coba buka Alamat URL `http://localhost:8000` di dalam Web Browser kamu, dan kamu akan melihat hasilnya :slightly_smiling_face:

Untuk cara penggunaan Pelican yang lebih lengkap, silahkan kamu kunjungi Halaman [Dokumentasi nya](https://docs.getpelican.org).

## Cara Kontribusi
Kontribusi bisa di lakukan dengan banyak cara, seperti memberikan Kritik dan Saran, Memberikan Komentar/Pertanyaan yang bermanfaat, Donasi, sampai turut membantu untuk memodifikasi/merubah Kode Sumber atau Artikel yang ada di Blog ini.

Jika "Kontribusi" yang Anda maksud adalah ingin memodifikasi Kode Sumber atau ingin merubah Artikel nya, itu sangat di perbolehkan.

Cara nya mudah, buatlah sebuah *fork* dari Repo ini dan pastikan selalu fokus pada Repo *fork* yang telah Anda buat, lalu klon kan Repo *fork* yang telah Anda buat tadi (Lihat: Cara Memperoleh nya), setelah itu tinggal Anda Install saja (Lihat: Cara Install).

Nah, setelah Anda meng-install nya, Anda bisa merubah Kode Sumber/Berkas yang ada, dan Anda bisa merubah dan memasukkan Kode Sumber yang telah Anda rubah tadi kedalam Repo sesuka Anda, tapi selama itu masih di dalam Repo *fork* yang Anda buat, yah.

Kalau Anda serius untuk merubah Kode Sumber yang ada di dalam Repo ini, setelah Anda merubah kode sumber yang berada di dalam Repo *fork* Anda, buatlah sebuah *Pull Request* di dalam GitHub nya, dan deskripsi kan (kalo bisa) dengan jelas apa saja yang telah Anda lakukan terhadap Kode Sumber nya.

Setelah itu, nanti akan saya pertimbangkan apa saja yang Anda ubah dan apa akibatnya bagi Blog ini nantinya, serta menerima hasil ubahan kamu atau tidaknya.

Namun, ada satu hal lagi yang ingin saya kasih tahu sebelum Anda merubah Kode Sumbernya, yaitu Tema 'Flex' yang saya gunakan itu berada di dalam folder [`themes/Flex`](https://github.com/FarrelF/FarrelF-Blog/tree/master/themes/Flex) dan folder tersebut merupakan 'Subtree' dari Repo [`Modified-Repo`](https://github.com/FarrelF/Modified-Flex) yang saya turunkan dari Tema [Asli nya](https://github.com/alexandrevicenzi/Flex).

Jadi, jika Anda ingin merubah Kode Sumber Tema nya, silahkan ubah itu melalui Repo [`Modified-Flex`](https://github.com/FarrelF/Modified-Flex) dan Anda bisa mengubah nya dari situ.

Sedangkan, jika Anda langsung mengubah kode sumber tema nya langsung melalui Repo ini (dan *fork* nya), silahkan tanggung sendiri resiko nya dan kalo Anda mengirimkan *Pull Request* dengan perubahan seperti ini, maka saya akan pertimbangkan untuk menolak nya secara mentah-mentah atau meng-hapus perubahan tersebut. Jadi, jangan kaget, yah :blush:

Nah, itulah cara kontribusi nya, jika Anda mempunyai pertanyaan atau masalah yang berhubungan dengan Kode Sumber atau konten yang ada di dalam Blog ini, silahkan tanyakan itu melalui Bagian "Issue" atau Berkomentar di dalam Blog, yah :slightly_smiling_face:

## Lisensi
Kode Sumber ini saya Lisensikan dengan GNU Affero General Public License v3 (GNU AGPLv3) yang merupakan Lisensi *Copyleft* dan bisa Anda lihat/baca di dalam berkas [COPYING](https://github.com/FarrelF/FarrelF-Blog/blob/master/COPYING).

Sedangkan konten yang ada di dalam blog ini, beserta terjemahan nya (kecuali jika di nyatakan [sebaliknya](https://farrel.franqois.id/catatan-hukum)) di lisensi kan dengan [Creative Commons Attribution-ShareAlike Internasional 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (Atau, disingkat: CC BY-SA 4.0).

Untuk lebih lengkap nya, silahkan kunjungi Laman [Lisensi](https://farrel.franqois.id/lisensi) di dalam Blog Saya :slightly_smiling_face:
