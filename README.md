# Farrel Franqois Blog
[![CircleCI](https://circleci.com/gh/FarrelF/FarrelF-Blog/tree/master.svg?style=svg)](https://circleci.com/gh/FarrelF/FarrelF-Blog/tree/master)
[![Netlify Status](https://api.netlify.com/api/v1/badges/edc59a5f-e63a-426c-ae65-cffe9153fa04/deploy-status)](https://app.netlify.com/sites/farrelf/deploys)
![GitHub](https://img.shields.io/github/license/FarrelF/FarrelF-Blog?label=Lisensi&style=flat-square)

*Repository* GitHub ini merupakan Kode Sumber dari Blog saya. Blog ini saya buat menggunakan Pelican, yang berbasis Python.

## Cara Kerja
Kode Sumber ini hanya berguna untuk menghasilkan berkas HTML statis saja, dan ini tidak bisa di eksekusi secara langsung, seperti hal nya Blog yang di buat dengan WordPress. (Karena sesuai dengan peruntukan nya, yakni: *Static Site Generator*)

Untuk menghasilkan konten yang kemudian di sebar melalui Internet, saya men-*deploy* kode sumber ini ke Netlify, lalu mereka lah yang menghasilkan berkas HTML statis di dalam nya, yang kemudian di sebar ke Internet.

## Persyaratan
Sebelum memulai, adakala nya untuk memenuhi Persyaratan nya terlebih dahulu, yakni ter-installnya:

### Persyaratan Wajib
- Git: https://git-scm.com/downloads
- Python 3.7 atau di atasnya: https://www.python.org/downloads/ (Jelas, wajib!)
- Poetry: https://poetry.eustace.io/docs/

### Persyaratan Opsional
- NodeJS: https://nodejs.org/en/download/ (Opsional, tapi disarankan)
- Yarn Package Manager: https://yarnpkg.com/lang/en/docs/install/ (Opsional, tapi disarankan setelah sudah ter-install NodeJS)
- GNU Make: https://www.gnu.org/software/make/ (Opsional, tapi di sarankan, meski ada alternatif nya, yakni 'Invoke' yang merupakan salah satu modul Python)

Di dalam Sistem Operasi Anda.

## Cara Memperoleh nya
Untuk memperoleh nya, Anda bisa Unduh Kode Sumber nya dengan meng-klik pada *Button* 'Clone & Download', lalu kamu klik 'Download ZIP' untuk mengunduh nya sebagai ZIP.

Namun, jika Anda lebih suka meng-*clone* atau meng-kloning nya dengan Git, Anda bisa eksekusi perintah berikut untuk meng-kloning nya:

```bash
$ git clone https://github.com/FarrelF/FarrelF-Blog.git
```

Setelah Anda meng-kloning nya, terutama dengan perintah di atas, kode sumber akan secara otomatis tersimpan di dalam Folder yang bernama `FarrelF-Blog`.

## Cara Install
Cara installnya mudah, Anda tinggal navigasikan ke dalam Folder Kode Sumber dengan perintah `cd`, lalu ikuti langkah-langkah berikut dengan Bash Shell:

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

Sebagai tambahan, jika Anda berniat ingin menggunakan Kode Sumber ini untuk tujuan Produksi, Anda bisa meng-install semua paket/pustaka beserta ketergantungan nya dengan menambahkan parameter `--no-dev`, contohnya seperti perintah berikut:

```bash
$ poetry install --no-dev
```

### Mengenai Berkas `build.sh`
**Catatan:** Karena sekarang blog ini di bangun dengan bantuan CircleCI dan Netlify hanya men-*deploy* HTML nya saja, maka kemungkinan berkas `build.sh` tidak akan saya gunakan. Untuk melihat konfigurasi nya, silahkan lihat berkas [`.circleci/config.yml`](https://github.com/FarrelF/FarrelF-Blog/blob/master/.circleci/config.yml).

Sebenarnya, berkas tersebut saya buat agar Netlify bisa meng-install semua keperluan nya dengan baik, termasuk Poetry yang merupakan Pengelola Paket dan Ketergantungan untuk Python, yang sampai saat ini [tidak di dukung secara langsung](https://github.com/netlify/build-image/issues/221) oleh Netlify.

Walaupun sebenarnya Anda bisa meng-install nya secara langsung menggunakan berkas tersebut, tapi sebaik nya Anda jangan meng-install nya dari situ, karena berkas tersebut memiliki perintah dan cara Install yang berbeda daripada yang ada disini. 

Perbedaan nya dengan Cara Install di atas adalah:
- Poetry akan di Install menggunakan perintah `pip` bukan `pip3`. Biasanya, `pip` di suatu Sistem Operasi, terutama berbasis Unix/Unix-like, itu merujuk kepada Pip untuk Python 2, bukan Python 3. Jadi, jika Anda meng-eksekusi nya, ini artinya Anda meng-install Poetry untuk Python 2, bukan Python 3, kecuali jika Anda berada di dalam Virtualenv atau Pyenv yang menggunakan Python 3, berjalan di dalam Lingkungan "Sandbox" atau di dalam Windows yang hanya terinstall Python 3 saja.

- Di dalam `build.sh`, Poetry sudah di konfigurasi agar tidak membuatkan Virtualenv setelah meng-install semua paket/pustaka lain nya dengan Poetry. Hal ini akan sangat beresiko jika Anda ingin menggunakan/memodifikasi Kode Sumber ini di dalam Komputer Anda, seperti konflik antar paket/pustaka lain nya.

- Poetry tidak akan meng-install semua paket/pustaka yang ada, melainkan hanya meng-install paket/pustaka untuk keperluan produksi saja. Jadi, Anda tidak akan bisa menikmati semua paket/pustaka untuk keperluan pengembangan, karena tidak ter-install, contoh nya: PyLint. Kecuali, jika Anda bisa meng-install nya.

- Akan menggunakan `make publish` untuk membangun Blog ini, yang mana seharus itu di gunakan untuk Produksi.

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

**Catatan**: Hal ini bisa di lakukan jika di dalam Sistem Operasi Anda sudah terinstall Node.js, dan Yarn Package Manager, serta sudah melakukan instalasi ketergantungan/pustaka JavaScript lain nya (seperti Gulp.js) dengan Yarn, caranya ada [di atas](#cara-install).

```bash
$ yarn invoke-devserver
```

Atau, jika kamu terinstall [GNU Make](https://www.gnu.org/software/make/), maka kamu bisa ikuti perintah berikut:

```bash
$ yarn make-devserver
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
Jika Anda ingin Berkontribusi terhadap Blog ini, Anda bisa baca/lihat [Panduan Kontribusi](https://github.com/FarrelF/FarrelF-Blog/blob/master/CONTRIBUTING.md) untuk mengetahui cara nya, karena banyak sekali yang saya bahas disitu.

## Lisensi
Kode Sumber ini, saya Lisensikan dengan GNU Affero General Public License v3 (GNU AGPLv3) atau di atas nya yang merupakan Lisensi *Copyleft* dan bisa Anda lihat/baca di dalam berkas [COPYING](https://github.com/FarrelF/FarrelF-Blog/blob/master/COPYING).

Sedangkan konten yang ada di dalam blog ini, beserta terjemahan nya (kecuali jika di nyatakan [sebaliknya](https://farrel.franqois.id/ketentuan-hukum-dan-sanggahan)) di lisensi kan dengan [Creative Commons Attribution-ShareAlike Internasional 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (Atau, disingkat: CC BY-SA 4.0).

Untuk lebih lengkap nya, silahkan kunjungi Laman [Lisensi](https://farrel.franqois.id/lisensi) di dalam Blog Saya :slightly_smiling_face:
