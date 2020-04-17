# Farrel Franqois Blog
[![GitHub Actions](https://github.com/FarrelF/Blog/workflows/Build%20and%20Deploy/badge.svg)](https://github.com/FarrelF/Blog/actions?query=workflow%3A%22Build+and+Deploy%22)
[![Netlify Status](https://api.netlify.com/api/v1/badges/edc59a5f-e63a-426c-ae65-cffe9153fa04/deploy-status)](https://app.netlify.com/sites/farrelf/deploys)
[![Lisensi](https://img.shields.io/github/license/FarrelF/Blog?label=Lisensi&style=flat-square)](LICENSE)

_Repository_ GitHub ini merupakan Kode Sumber dari Blog saya. Blog ini saya buat menggunakan Pelican, yang berbasis Python.

## Cara Kerja
Kode Sumber ini hanya berguna sebagai konfigurasi dan menyimpan konten nya saja. Konfigurasi ini akan di gunakan ketika kita membuat Web/Blog Statis yang mana itu akan di hasilkan sebagai Berkas HTML, dan ini tidak bisa di eksekusi secara langsung, seperti hal nya Blog yang di buat dengan WordPress. (Karena sesuai dengan peruntukan nya, yakni: _Static Site Generator_)

Untuk menghasilkan konten yang kemudian di sebar melalui Internet, Layanan Platform Pengembangan CI/CD (_Continuous Integration and Delivery_) seperti [GitHub Actions](https://github.com/features/actions) akan membangun sebuah Web/Blog Statis yang tentu nya akan memanfaatkan Kode Sumber ini sebagai konfigurasi dan konten nya. Setelah membangun sebuah web/blog statis, mereka (GitHub Actions) akan menyebarkan hasil keluaran (_output_) nya ke Netlify melalui `netlify-cli`. 

Untuk proses pembangunan nya atau ingin melihat log nya, Anda bisa lihat log nya [disini](https://github.com/FarrelF/Blog/actions). (Selama kamu login ke GitHub menggunakan Akun kamu, kalau tidak, maka kamu tidak bisa mengakses nya)

Jadi, Peran Netlify disini tidak membangun sebuah Web/Blog melalui kode sumber, melainkan cuma meng-_hosting_-kan hasil (_output_) nya saja, yakni berkas HTML yang di hasilkan oleh GitHub Actions tadi. 

## Persyaratan
Sebelum memulai, adakala nya untuk memenuhi Persyaratan nya terlebih dahulu, yakni ter-installnya:

### Persyaratan Wajib
- Git: https://git-scm.com/downloads (Untuk mengetahui Cara Install nya, silahkan baca artikel [ini](https://farrel.franqois.id/cara-install-git))
- Python 3.6 atau di atasnya: https://www.python.org/downloads/ (Jelas, wajib!)
- Poetry: https://python-poetry.org/docs/

### Persyaratan Opsional
- NodeJS: https://nodejs.org/en/download/ (Opsional, tapi disarankan)*
- Yarn Package Manager: https://yarnpkg.com/lang/en/docs/install/ (Opsional, tapi disarankan setelah sudah ter-install NodeJS)*
- GNU Make: https://www.gnu.org/software/make/ (Opsional, tapi di sarankan, meski ada alternatif nya, yakni 'Invoke' yang merupakan salah satu modul Python bisa langsung terinstall secara bawaan oleh Poetry)

Di dalam Sistem Operasi Anda.

**\*Catatan**: NodeJS bisa di Install melalui [NVM (Node Version Manager)](https://github.com/nvm-sh/nvm) untuk pengguna Sistem Operasi berbasis \*nix atau [`nvm-windows`](https://github.com/coreybutler/nvm-windows) untuk pengguna Windows. Sedangkan, "Yarn Package Manager" bisa di Install melalui [YVM (Yarn Version Manager)](https://yvm.js.org/docs/overview) setelah kamu meng-install NodeJS nya.

## Cara Memperoleh nya
Untuk memperoleh nya, Anda bisa Unduh Kode Sumber nya dengan meng-klik pada *Button* 'Clone & Download', lalu kamu klik 'Download ZIP' untuk mengunduh nya sebagai ZIP.

Namun, jika Anda lebih suka meng-*clone* atau meng-kloning nya dengan Git, Anda bisa eksekusi perintah berikut untuk meng-kloning nya:

```bash
$ git clone https://github.com/FarrelF/Blog.git FarrelF-Blog
```

Setelah Anda meng-kloning nya, terutama dengan perintah di atas, kode sumber akan secara otomatis tersimpan di dalam Folder yang bernama `FarrelF-Blog`.

## Cara Install
Cara installnya mudah, Anda tinggal navigasikan ke dalam Folder Kode Sumber dengan perintah `cd`, lalu ikuti langkah-langkah berikut dengan Terminal:

**Catatan**: Di dalam Sistem Operasi GNU/Linux, macOS dan Sistem Operasi berbasis Unix/Unix-like lain nya, kamu bisa gunakan Terminal Bawaan, sedangkan di Windows kamu bisa gunakan "Git Bash".

```bash
$ poetry install && poetry shell
$ invoke devtheme # Untuk membangun Tema nya, atau 'invoke static' kalo mau langsung membangun Web/Blog nya dan Tema nya juga
$ yarn install # Opsional
```

Atau, jika di dalam Sistem Operasi kamu terinstall [GNU Make](https://www.gnu.org/software/make/), maka kamu bisa ikuti cara nya berikut:

```bash
$ poetry install && poetry shell
$ make devtheme # Untuk membangun Tema nya, atau 'make static-files' kalo mau langsung membangun Web/Blog nya dan Tema nya juga
$ yarn install # Opsional
```

Lokasi Venv nya nanti berada di dalam folder `.venv`, yang tentu saja itu berada di dalam Folder Proyek nya.

Sebagai tambahan, jika Anda berniat ingin menggunakan Kode Sumber ini untuk tujuan Produksi, Anda bisa meng-install semua modul Python beserta ketergantungan nya dengan menambahkan parameter `--no-dev`, contohnya seperti perintah berikut:

```bash
$ poetry install --no-dev
```

### Mengenai Berkas `NetlifyBuild.sh`
**Catatan:** Karena sekarang blog ini di bangun dengan bantuan GitHub Actions dan Netlify hanya men-_hosting_-kan berkas HTML nya saja, maka kemungkinan berkas [`NetlifyBuild.sh`](NetlifyBuild.sh) tidak akan saya gunakan. Untuk melihat konfigurasi nya, silahkan lihat berkas konfigurasi nya di dalam folder [`.github/workflows`](.github/workflows).

Sebenarnya, berkas tersebut saya buat agar Netlify bisa meng-install semua keperluan nya dengan baik, termasuk Poetry yang merupakan Pengelola Paket dan Ketergantungan untuk Python, yang sampai saat ini [tidak di dukung secara langsung](https://github.com/netlify/build-image/issues/221) oleh Netlify.

Walaupun sebenarnya Anda bisa meng-install nya secara langsung menggunakan berkas tersebut, tapi sebaik nya Anda jangan meng-install nya dari situ, karena berkas tersebut memiliki perintah dan cara Install yang berbeda daripada yang ada disini. 

Perbedaan nya dengan Cara Install di atas adalah:
- Sudah jelas dari Nama Berkas nya, kalau berkas ini memang di tujukan untuk Netlify, bukan untuk lain nya.

- Poetry tidak akan meng-install semua modul yang ada, melainkan hanya meng-install modul untuk keperluan produksi saja. Jadi, Anda tidak akan bisa menikmati semua modul untuk keperluan pengembangan, karena tidak ter-install, contoh nya: PyLint. Kecuali, jika Anda bisa meng-install nya.

- Akan menggunakan `poetry run make publish` untuk membangun Blog ini, yang mana seharus itu di gunakan untuk Produksi.

Selain itu, berkas tersebut akan di eksekusi oleh Netlify saat men-*deploy*, yang memiliki Sistem dan cara kerja yang berbeda daripada Sistem pada Komputer Anda, serta saat men-*deploy*, Sistem mereka berjalan di dalam "Kontainer" yang di buat dengan "Docker".

Sehingga, bisa di katakan, bahwa mereka berjalan di dalam Lingkungan Sistem yang ter-"isolasi" atau di dalam Lingkungan *Sandbox*.

## Setelah Meng-installnya
Setelah kamu meng-installnya, kamu bisa coba untuk menghasilkan sebuah berkas HTML Statis ini dengan Pelican, yang kemudian bisa kamu akses dengan Web Browser kamu.

Di dalam GNU/Linux atau macOS (Atau, Sistem Operasi berbasis Unix-like/Unix lain nya), kamu dapat eksekusi perintah berikut agar Pelican dapat menghasilkan Berkas HTML Statis dan juga mengaktifkan fitur Web Server pada Python:

**Catatan**: Tapi sebelum itu, pastikan kalau kamu sudah berada di dalam Folder Kode Sumber nya, yah :slightly_smiling_face:

```bash
$ pelican --autoreload --listen
```

Atau, bisa melalui perintah berikut: (Selama terinstall [GNU Make](https://www.gnu.org/software/make/) di dalam Sistem)

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

Atau, jika Anda tidak ingin repot-repot melakukan hal di atas pada Windows, serta ingin menikmati fitur 'Live Reload' yakni bisa Memuat Ulang Blog secara otomatis setelah perubahan, Anda bisa gunakan perintah berikut:

**Catatan**: Hal ini bisa di lakukan jika di dalam Sistem Operasi Anda sudah terinstall Node.js, dan Yarn Package Manager, serta sudah melakukan instalasi modul JavaScript lain nya (seperti Gulp.js) dengan Yarn, caranya ada [di atas](#cara-install).

```bash
$ yarn invoke:devserver
```

Atau, jika kamu terinstall [GNU Make](https://www.gnu.org/software/make/), maka kamu bisa ikuti perintah berikut:

```bash
$ yarn make:devserver
```

Perintah di atas juga bisa dilakukan oleh hampir semua Sistem Operasi (termasuk GNU/Linux dan macOS) selama bisa terinstall dan menggunakan Python Invoke atau GNU Make, NodeJS dan Yarn Package Manager.

Dan, perintah di atas juga akan menjalankan Gulp.js yang ter-install melalui `yarn install`, hanya saja Gulp.js ini hanya berlaku untuk Kode Sumber ini dan melalui perintah di atas saja.

Kalau Anda ingin Gulp.js bisa di eksekusi di mana saja, selain di dalam Folder Kode Sumber ini saja, Anda bisa install paket `gulp-cli` ini di dalam Sistem Operasi Anda dengan perintah berikut:

```bash
$ yarn global add gulp-cli
```

Setelah semua nya selesai dan dinyatakan berhasil, bisa kamu coba buka Alamat URL `http://localhost:9001` di dalam Web Browser kamu, dan kamu akan melihat hasilnya :slightly_smiling_face:

Untuk cara penggunaan Pelican yang lebih lengkap, silahkan kamu kunjungi Halaman [Dokumentasi nya](https://docs.getpelican.org).

## Cara Kontribusi
Jika Anda ingin Berkontribusi terhadap Blog ini, Anda bisa baca/lihat [Panduan Kontribusi](CONTRIBUTING.md) untuk mengetahui cara nya, karena banyak sekali yang saya bahas disitu.

## Lisensi
Kode Sumber ini, (Kecuali yang berada di dalam folder [`content`](content)) saya Lisensikan dengan GNU Affero General Public License v3 (GNU AGPLv3) atau di atas nya yang merupakan Lisensi *Copyleft* dan bisa Anda lihat/baca di dalam berkas [LICENSE](LICENSE).

### Pengecualian Lisensi
Meski seluruh Kode Sumber ini berlisensi GNU Affero General Public License v3 (GNU AGPLv3) atau di atas nya/lebih baru, bukan berarti ini tanpa pengecualian.

Pengecualian nya adalah bahwa Konten yang ada di dalam blog ini (berupa Artikel, Laman, dan Berkas Gambar yang telah saya buat sendiri, yang terletak di dalam folder [`content`](content)) (tapi tidak [semua berkas di dalam nya](https://farrel.franqois.id/ketentuan-hukum-dan-sanggahan), terutama untuk berkas-berkas yang berada di dalam [`content/extras`](content/extras)), beserta terjemahan nya di lisensi kan dengan [Creative Commons Attribution-ShareAlike Internasional 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (Atau, disingkat: CC BY-SA 4.0).

Untuk lebih lengkap nya, silahkan kunjungi Laman [Lisensi](https://farrel.franqois.id/lisensi) di dalam Blog Saya :slightly_smiling_face:
