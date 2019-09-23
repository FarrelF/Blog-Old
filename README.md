# Farrel Franqois Blog
[![Netlify Status](https://api.netlify.com/api/v1/badges/edc59a5f-e63a-426c-ae65-cffe9153fa04/deploy-status)](https://app.netlify.com/sites/farrelf/deploys)
![GitHub](https://img.shields.io/github/license/FarrelF/FarrelF-Blog?label=Lisensi&style=flat-square)

*Repository* GitHub ini merupakan Kode Sumber dari Blog saya. Blog ini saya buat menggunakan Pelican, yang berbasis Python.

## Cara Kerja
Kode Sumber ini hanya berguna untuk menghasilkan berkas HTML statis saja, dan ini tidak bisa di eksekusi secara langsung, seperti hal nya Blog yang di buat dengan WordPress. (Karena sesuai dengan peruntukan nya, yakni: *Static Site Generator*)

Untuk menghasilkan konten yang kemudian di sebar melalui Internet, saya men-*deploy* kode sumber ini ke Netlify, lalu mereka lah yang menghasilkan berkas HTML statis di dalam nya, yang kemudian di sebar ke Internet.

## Cara Memperoleh nya
Untuk memperoleh nya, Anda bisa Unduh Kode Sumber nya dengan meng-klik pada *Button* 'Clone & Download', lalu kamu klik 'Download ZIP' untuk mengunduh nya sebagai ZIP.

Namun, jika Anda lebih suka meng-*clone* atau meng-kloning nya dengan Git, Anda bisa eksekusi perintah berikut untuk meng-kloning nya:

```bash
$ git clone https://github.com/FarrelF/FarrelF-Blog.git
```

Setelah Anda meng-kloning nya, terutama dengan perintah di atas, kode sumber akan secara otomatis tersimpan di dalam Folder yang bernama `FarrelF-Blog`.

## Cara Install
Cara installnya mudah, Anda tinggal ikuti langkah-langkah berikut dengan Bash Shell:

**Catatan**: Di dalam Sistem Operasi GNU/Linux, macOS dan Sistem Operasi berbasis Unix/Unix-like lain nya, kamu bisa gunakan Terminal Bawaan, sedangkan di Windows kamu bisa gunakan "Git Bash".

```bash
$ python3 -m pip install virtualenv
$ virtualenv pelican-env
$ source pelican-env/bin/activate # Gunakan perintah 'source pelican-env/Scripts/activate' (tanpa kutip) jika Anda sedang menggunakan Windows
$ pip install -r requirements.txt # Tambahkan parameter '--upgrade' (tanpa kutip) jika Anda ingin langsung memperbarui nya
```

Setelah kamu meng-installnya, kamu bisa coba untuk menghasilkan sebuah berkas HTML Statis ini dengan Pelican, yang kemudian bisa kamu akses dengan Web Browser kamu.

Di dalam GNU/Linux atau macOS (Atau, Sistem Operasi berbasis Unix-like/Unix lain nya), kamu dapat eksekusi perintah berikut agar Pelican dapat menghasilkan Berkas HTML Statis dan juga mengaktifkan fitur Web Server pada Python:

**Catatan**: Tapi sebelum itu, pastikan kalau kamu sudah berada di dalam Folder Kode Sumber nya, yah :slightly_smiling_face:

```bash
$ pelican --autoreload --listen
```

Atau, bisa melalui perintah berikut: (Selamat terinstall [GNU Make](https://www.gnu.org/software/make/) di dalam Sistem)

```bash
$ make devserver
```

Sedangkan di Windows, ada tiga (yang sebenarnya 'empat') langkah yang harus kamu turuti, yaitu:

1. Hasilkan Berkas HTML terlebih dahulu dengan Pelican, gunakan Perintah berikut:
```powershell
> pelican --autoreload
```
2. Kemudian, kamu buka lagi CMD/PowerShell/Bash di Jendela yang baru atau buka Tab Baru jika kamu menggunakan [Windows Terminal](https://github.com/microsoft/terminal), lalu aktifkan "Lingkungan Virtual" nya.

3. Setelah itu, Aktifkan fitur Web Server pada Python dengan perintah berikut:
```powershell
> pelican --listen
```

Setelah semua nya selesai dan dinyatakan berhasil, bisa kamu coba buka Alamat URL `http://localhost:8000` di dalam Web Browser kamu, dan kamu akan melihat hasilnya :slightly_smiling_face:

Untuk cara penggunaan Pelican yang lebih lengkap, silahkan kamu kunjungi Halaman [Dokumentasi nya](https://docs.getpelican.org).

## Cara Kontribusi
Jika Anda ingin Berkontribusi terhadap Blog ini, Anda bisa baca/lihat [Panduan Kontribusi](https://github.com/FarrelF/FarrelF-Blog/blob/master/CONTRIBUTING.md) untuk mengetahui cara nya, karena banyak sekali yang saya bahas disitu.

## Lisensi
Kode Sumber ini saya Lisensikan dengan GNU Affero General Public License v3 (GNU AGPLv3) yang merupakan Lisensi *Copyleft* dan bisa Anda lihat/baca di dalam berkas [COPYING](https://github.com/FarrelF/FarrelF-Blog/blob/master/COPYING).

Sedangkan konten yang ada di dalam blog ini, beserta terjemahan nya (kecuali jika di nyatakan [sebaliknya](https://farrel.franqois.id/ketentuan-hukum-dan-sanggahan)) di lisensi kan dengan [Creative Commons Attribution-ShareAlike Internasional 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (Atau, disingkat: CC BY-SA 4.0).

Untuk lebih lengkap nya, silahkan kunjungi Laman [Lisensi](https://farrel.franqois.id/lisensi) di dalam Blog Saya :slightly_smiling_face:
