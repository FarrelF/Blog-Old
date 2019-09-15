---
Title: Cara saya membuat Blog dengan Pelican, Netlify dan Cloudflare
Category: Tutorial, Blogging
Tag: Pelican, Netlify, Cloudflare
Slug: cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare
Authors: Farrel Franqois
Summary: Saya memposting tentang cara saya membuat blog ini melalui Pelican, yang tentu saja dengan bantuan Netlify sebagai Hosting nya dan juga Cloudflare sebagai DNS nya. Cara membuat nya ini cukup mudah, kok, penasaran? Bisa kamu baca artikel ini lebih lanjut :slightly_smilling_face:
---

<style>
article.single p {
    text-align: justify;
}

article.single p a {
    vertical-align: middle;
    text-align: center;
}

article.single img {
    display: block;
    margin: 0 auto;
}
</style>

## **Daftar Isi**
[TOC]

## **I. Pembuka**
Halo, semua! Seperti yang Anda tahu, bahwa blog saya ini merupakan HTML Statis, yang tidak di proses secara dinamis, melainkan ini hanyalah sebuah HTML statis yang di hasilkan dari *Static Site Generator* seperti [Pelican](https://blog.getpelican.com). 

Kamu bisa baca Artikel yang berjudul "[Halo Dunia! (Lagi)]({filename}/artikel/2019-08-27-halo-dunia.md)" mengenai Blog yang saya gunakan, beserta hosting nya dan kenapa saya menggunakan nya, dll.

Selain menggunakan Netlify sebagai Hosting nya, blog ini juga menggunakan Cloudflare sebagai DNS nya. Tentu saja, semua ini gratis, gak ada biaya yang di keluarkan, kecuali domain.

Setelah Anda tahu alasan saya kenapa fokus menggunakan/memanfaatkan *Static Site Generator* untuk blogging daripada menggunakan WordPress, apakah Anda termotivasi untuk menggunakan nya? Kalo iya, saya akan beritahu cara nya melalui Tutorial ini.


## **II. Persyaratan**
Tapi, sebelum Anda melakukan nya, ada syarat-syarat tertentu yang harus Anda turuti/lakukan sebelum Anda membuat sebuah Blog dengan memanfaatkan *Static Site Generator* (bisa di singkat *SSG*) seperti Pelican, yaitu:

**Untuk Membuat Blog dan konfigurasi dasar**:

Di bawah ini merupakan Persyaratan bagi yang ingin membuat blog berbasis Pelican, dan juga melakukan konfigurasi dasar nya (Seperti: Menggantikan Tema, membuat robots.txt, mengaktifkan Komentar Disqus, dll), berikut adalah Persyaratan nya:

1. Tahu cara mengelola DNS (Seperti menambahkan Subdomain dengan menambahkan CNAME Record, dll).

2. Punya Domain (kalo perlu, karena pada tutorial ini saya akan menggunakan 'Custom Domain'/'Custom Subdomain') dan pastikan Nameserver nya kamu arahkan ke Cloudflare.

3. Mempunyai Akun dari Layanan Git yang di dukung penuh oleh Netlify, seperti [GitHub](https://github.com) dan [GitLab](https://gitlab.com).

4. Mau/gak mau, kamu harus belajar Markdown (Gampang, kok :blush:) atau reStructuredText (rst) untuk menulis Artikel.

5. Pastikan Komputer/Laptop kamu sudah terinstall [Python 3](https://www.python.org), Pip (biasanya 'Pip' sudah terinstall secara default setelah meng-install Python) dan juga [Git](https://git-scm.org)

6. Dan, pastikan juga kamu mempunyai Editor Teks/Kode Favorit kamu, kali ini saya gunakan [VSCodium](https://www.vscodium.com).


**Untuk Konfigurasi Menengah atau Tingkat Lanjut (Opsional)**:

Di bawah ini merupakan Persyaratan Tambahan bagi yang ingin meng-konfigurasi Blog nya, seperti meng-install Plugin, menambahkan Response Header saat publikasi, mengatur Markdown (Contoh: Menambahkan Fitur Emoji, Menambahkan Daftar Isi, dll), sampai memodifikasi/menambahkan fitur pada tema. Syarat nya sebagai berikut:

1. Mempelajari Dasar dari Bahasa Pemrograman Python 3 (Seperti Penggunaan: Variabel, 'List', 'Dictionary', 'Tuple', Tipe Data Primitif (seperti: String, Integer, dan Boolean), Pengkondisian dengan if/elif/else, dan 'Import') atau di atas nya, karena Pelican ini berbasis Python.

2. Kalo perlu, pelajari juga cara memasukkan Sintaks Python ke dalam View pada *Web Framework* Python seperti Django atau Flask, untuk memodifikasi tema.

Dah, gitu aja syarat nya, lagian konfigurasi lebih lanjut gak saya bahas terlalu jauh, saya paling banyak cuma membahas dasar nya disini, selebihnya Anda yang atur.

## **III. Memenuhi Persyaratan**
### **1. Install Virtualenv dan kenapa menggunakan nya**
Kita disini akan meng-install 'Virtualenv', aplikasi ini berfungsi untuk membuat sebuah *Lingkungan Virtual* pada Python untuk Proyek Python.

*Lingkungan Virtual* yang saya maksud disini adalah sebuah Lingkungan modul-modul atau Program Python yang terisolasi.

'Terisolasi' disini maksudnya adalah tertutup dan tidak bisa di akses dari luar.

Program Python yang berada di dalam 'Virtualenv' (*Lingkungan Virtual*) akan memiliki modul-modul nya sendiri dan Program dari luar itu tidak bisa mengakses nya sama sekali. Jadi, yang di isolasi disini adalah Modul-modul nya, bukan Proyek nya.

Kenapa kita harus menggunakan *Lingkungan Virtual*? Sebenarnya bisa saja tanpa perlu menggunakan nya, hanya saja, masalahnya adalah:

1. Karena Pelican di Install di dalam Lingkungan Sistem Operasi (Lingkungan Global), maka modul Pelican akan 'bebarengan' dengan modul-modul yang terinstall lain nya, karena di dalam Lingkungan yang sama.

2. Karena bebarengan, maka kita akan kesulitan untuk menentukan paket apa saja yang perlu di Install untuk membuat Blog SSG ini, karena tercampur dengan modul-modul yang sebenarnya tidak perlu kita Install. <br>**Contoh:** Kita install `Django` untuk belajar *Web Framework* dengan Python, `youtube-dl` untuk meng-unduh Video dari YouTube dan `Pelican` untuk keperluan *Static Blogging* yang mana ketiga nya ini di Install di dalam Lingkungan OS (tanpa Virtualenv), dan setelah kita selesai membuat blog, maka sebelum menyebarkan nya ke Internet, kita harus menentukan paket mana saja yang harus di Install untuk membuat sebuah Blog SSG. **Karena Django, 'youtube-dl' dan Pelican ter-install di dalam Lingkungan OS, maka selain Pelican, Django dan 'youtube-dl' juga termasuk paket yang akan terinstall**. <br>Nah, kan lucu, untuk menyebarkan sebuah Blog SSG saja, masa kita harus meng-install Django dan 'youtube-dl' juga di dalam nya?

3. Membuat Proses Deploy pada Netlify berlangsung lama, kenapa? Karena saat dalam Proses Deploy, ia akan meng-install modul-modul yang sebenarnya tidak perlu di Install.

4. Dan, karena bebarengan itu, maka kemungkinan konflik antar modul itu akan sering terjadi, terutama jika Anda sudah meng-install banyak sekali modul di dalam Lingkungan Sistem Operasi.

5. Percayalah, dengan meng-install semua nya ke dalam Lingkungan Sistem Operasi, selain membuat konflik, tidak rapih dan membuat Proyek Anda menjadi kacau, Anda juga membuat Proyek Anda ini di penuhi dengan *bloatware* karena ter-install modul-modul yang seharusnya tidak perlu di-install.

Nah, untuk mengatasi masalah-masalah tersebut, lahirlah 'Virtualenv'. Untuk alasan lain nya, bisa kamu kunjungi Artikel dari PetaniKode [Mengenai 'Virtualenv'](https://www.petanikode.com/python-virtualenv/).

#### **Untuk GNU/Linux, macOS dan Sistem Operasi \*nix lainnya:**
Di dalam Sistem Operasi GNU/Linux, macOS dan Sistem Operasi berbasis Unix/Unix-like lain nya, Anda bisa meng-install 'Virtualenv' dengan cukup mudah dengan memanfaatkan Pip, untuk itu, silahkan Anda eksekusi salah satu dari perintah berikut untuk meng-installnya:

**Catatan:** Pastikan Anda menggunakan Python 3 untuk meng-install nya dengan Pip, bukan versi 2 (Python 2).

```bash
## Metode 1: Menggunakan Pip3 secara langsung ##
$ sudo -H pip3 install virtualenv

## Metode 2: Menggunakan Python 3 untuk mengeksekusi Pip ## 
$ sudo -H python3 -m pip install virtualenv

## Metode 3: Menggunakan Python 3.7 (atau, dengan versi yang lebih spesifik) untuk mengeksekusi Pip ##
$ sudo -H python3.7 -m pip install virtualenv
```

#### **Untuk Windows:**
Sedangkan untuk Windows, jika Anda sudah ter-install Python 3 di dalam nya, maka untuk meng-install 'Virtualenv' dengan Pip, bisa Anda eksekusikan perintah berikut di dalam CMD, PowerShell atau Bash:

**Catatan:** Pastikan Anda membuka CMD, PowerShell atau Bash sebagai Administrator sebelum meng-install 'Virtualenv' dengan Pip, kalau tidak, maka modul tidak akan ter-install dengan baik. Dan, pastikan juga Python yang di gunakan nya adalah Python 3.

```powershell
## Metode 1: Menggunakan Pip secara langsung ## 
> pip install virtualenv

## Metode 2: Menggunakan Python 3 untuk mengeksekusi Pip ##
> python -m pip install virtualenv
```

### **2. Membuat Virtualenv dan Install Pelican**
Setelah meng-install 'Virtualenv', sebaik nya Anda buat sebuah Folder Proyek nya terlebih dahulu dan navigasikan ke dalam Folder tersebut setelah nya, dengan perintah berikut:

```bash
$ mkdir Demo-Blog; cd "$_"
```

Anda bisa gantikan `Demo-Blog` disini dengan Nama Blog yang Anda inginkan, disini saya menamainya dengan `Demo-Blog`.

Lalu, buatlah sebuah 'Virtualenv' di dalam folder tersebut dengan perintah berikut:

```bash
$ virtualenv pelican-envs
```

Anda bisa gantikan `pelican-envs` disini dengan Nama 'Virtualenv' yang Anda inginkan, disini saya menamainya dengan `pelican-envs` agar mudah di ingat.

Atau, jika Anda ingin membuat nya di dalam lokasi yang berbeda, Anda bisa eksekusi perintah berikut:

```bash
$ virtualenv /path/to/new/pelican-envs
```

Ganti `/path/to/new/pelican-envs` dengan lokasi yang Anda inginkan. Tapi, saya sarankan untuk meletakkan nya di dalam Folder Proyek nya saja, biar mudah dalam mengelola nya. Dan, di tutorial ini, saya akan meletakkan nya di dalam Folder Proyek nya.

Setelah di buat (di dalam Proyek Blog nya), kira-kira Struktur Direktori nya akan seperti ini:
```text
Demo-Blog
└── pelican-envs
    ├── bin
    ├── include
    └── lib
```

Sedangkan di Windows akan menjadi seperti ini:
```text
Demo-Blog
└── pelican-envs
    ├── Include
    ├── LICENSE.txt
    ├── Lib
    ├── Scripts
    └── tcl
```

Setelah kita membuatnya tadi, aktifkan Virtualenv yang barusan kita buat tadi. Di dalam GNU/Linux, macOS atau Sistem Operasi berbasis Unix/\*nix lain nya, bisa kamu aktifkan Virtualenv nya dengan perintah berikut:

```bash
$ source pelican-envs/bin/activate
```

Atau:

```bash
$ source /path/to/pelican-envs/bin/activate
```

Ganti `/path/to/pelican-envs` menjadi Lokasi Virtualenv yang Anda buat tadi, dan itu bagi Anda yang membuatnya di dalam lokasi yang berbeda.

Jika Anda menggunakan Windows, dan karena Windows bisa memiliki *Shell* yang berbeda-beda (Selain CMD, ada juga PowerShell, dan juga Bash), jadi perintah pengaktifannya akan berbeda-beda di setiap *Shell*.

Untuk Pengguna CMD (Command Prompt), bisa Anda eksekusikan perintah berikut ini untuk mengaktifkan Virtualenv melalui CMD:

```console
> pelican-envs\Scripts\activate
```

Untuk Pengguna PowerShell (PowerShell 5 atau PowerShell Core), perintah yang di eksekusi sama dengan yang ada di CMD, hanya saja Anda perlu menambahkan tanda titik "." (tanpa kutip) di awal perintah nya. Sehingga, perintah nya akan menjadi seperti di bawah ini:

```powershell
> . pelican-envs\Scripts\activate
```

Sedangkan untuk pengguna Bash di Windows (Contoh: Git Bash, Windows Subsystem Linux, dll), sama seperti CMD, hanya saja Anda harus menambahkan perintah `source` di paling awalnya. Sehingga, perintah nya akan menjadi seperti berikut:

```bash
$ source pelican-envs/Scripts/activate
```

Setelah Anda mengaktifkan nya, kemudian Install Pelican beserta ketergantungan nya, dengan perintah berikut: (tanpa memerlukan `sudo` ataupun membuka nya sebagai Admin)

```bash
$ pip install pelican Markdown
```

Karena pada tutorial ini akan membahas cara menulis artikel dengan menggunakan Markdown, jadi Markdown harus di Install, kalaupun Anda tidak mau, ya tidak masalah.

### **3. Install Git**
Karena kita akan membuat blog dan menyebarkan nya melalui internet, kita sangat perlu untuk meng-install Git di dalam Komputer kita.

Untuk meng-install nya, Anda perlu meng-unduh Git nya terlebih dahulu, bisa kunjungi situs web resmi nya untuk meng-unduh Git, yakni: [https://git-scm.com](https://git-scm.com). Lalu, klik pada *Button* "Download bla bla bla". Atau, Anda juga bisa mengunjungi [Halaman Unduhan](https://git-scm.com/downloads) Resmi nya untuk meng-unduh Git.

Pada GNU/Linux atau Sistem Operasi berbasis Unix/Unix-like lain nya (kecuali macOS, meski bisa di Install), biasanya mereka akan memberikan petunjuk cara instalasi Git nya untuk masing-masing Distribusi atau Sistem Operasi nya. Kalau begitu, Anda tinggal ikuti saja petunjuk nya.

Sedangkan untuk Windows, Anda bisa ikuti petunjuk nya berikut.

#### **Cara Install Git di Windows**
Cara Install Git di Windows sangatlah berbeda daripada Install Git di GNU/Linux, Installer nya menggunakan GUI, sehingga dapat mempermudah kamu selama meng-install Git.

Hanya saja, jika kamu salah langkah, maka yang terjadi adalah Git akan mengalami "kesalahan" (*error*) saat di gunakan, entah itu tidak bisa meng-kloning *Repository* sampai mengurus nya.

Maka dari itu, jika Anda adalah pengguna Windows, maka Anda bisa ikuti cara instalasi nya berikut:

1. Unduh [Git untuk Windows](https://git-scm.com/download/win/).

2. Setelah di Unduh, buka berkas tersebut. Jika muncul UAC (*User Account Control*), klik pada *Button* 'OK'.

3. Setelah itu, Install Git dengan Langkah-langkah berikut:

##### **1. Perjanjian Lisensi**
Nanti akan muncul Perjanjian Lisensi (*License Agreement*) setelah membuka berkas tersebut, klik pada *Button* 'Next >' untuk melanjutkan Instalasi. (Catatan: Jika Anda klik *Button* tersebut dan meng-install nya, ini artinya Anda telah menyetujui Perjanjian tersebut)

##### **2. Pilih Komponen mana yang ingin di Install**
Pada langkah ini, silahkan Anda atur Komponen mana yang ingin Anda install dan di aktifkan oleh Anda, seperti: Asosiasi Berkas, Integrasi Windows Explorer, Pintasan di Desktop, dll.
   
Jika Anda ingin menggunakan TrueType di dalam semua Konsole Windows, centang "Use a TrueType font in all console Windows", seperti cuplikan berikut:
   
[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_1.png)](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_1.png)

Setelah Anda selesai memilih nya, klik pada *Button* 'Next >' untuk melanjutkan ke Langkah ke-3.

##### **3. Pilih Editor mana yang akan di gunakan**
Pada langkah ini, Anda bisa pilih editor yang akan di gunakan oleh Git nanti nya

Pada tutorial ini, saya akan gunakan 'GNU nano' sebagai editor bawaan untuk Git, berikut cuplikan nya:

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_2.png)](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_2.png)

Karena secara bawaan Git memilih 'nano' sebagai editor nya, maka untuk langkah ini, bisa langsung Anda klik *Button* 'Next >' untuk melanjutkan ke Langkah ke-4.

##### **4. Pilih Cara untuk Eksekusi Git**
Setelah itu, pilih opsi untuk cara eksekusi Git, saya sarankan untuk pilih opsi **Git from the command line and also from 3rd-party software** (atau, membiarkan nya karena sudah terpilih) agar Git bisa di akses atau di eksekusi dari manapun, termasuk dari CMD (Command Prompt). 
   
[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_3.png)](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_3.png)

Setelah Anda memilih opsinya, klik pada *Button* 'Next >' untuk melanjutkan.

##### **5. Pilih Perangkat Lunak untuk Eksekusi SSH untuk Git**
Setelah itu, pilih eksekusi SSH untuk Git, ini akan berguna nanti ketika Anda mengelola *Repository* Git dengan SSH. Agar lebih mudah, pilih "OpenSSH" dengan memilih opsi **Use OpenSSH**, seperti pada cuplikan berikut: 

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_4.png)](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_4.png)

Setelah Anda memilih nya, klik pada *Button* 'Next >' untuk melanjutkan ke Langkah ke-6.

##### **6. Memilih Pustaka untuk HTTPS pada Git (_Choose HTTPS transport backend_)**
Pada langkah **Choose HTTPS transport backend**, Anda akan memilih *Library*/Pustaka mana yang akan di gunakan untuk 'transportasi' HTTPS pada Git nanti nya. 

Saya sarankan untuk menggunakan Pustaka Bawaan dari Windows saja, yakni ['Windows Secure Channel'](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380123(v=vs.85).aspx) (atau bisa di sebut 'winSSL' atau 'Schannel'), agar Git dapat mengenali CA (Certification Authority) dan Sertifikat SSL lain nya secara langsung di dalam Windows. 

Maka dari itu, pilihlah opsi **Use the native Windows Secure Channel library**, daripada/bukan **Use OpenSSL** (Kecuali jika Anda meng-install OpenSSL di dalam Windows), seperti pada cuplikan layar berikut ini:

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_5.png)](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_5.png)

Setelah Anda memilih nya, klik pada *Button* 'Next >' untuk melanjutkan ke Langkah ke-7.

##### **7. Memilih "Line Ending" untuk Git**
Selanjutnya, pada langkah **Configuring line endings conversions**, biarkan saja bawaan atau bisa Anda pilih Opsi **Checkout Windows-style, commit Unix-style line endings**, lalu klik 'Next >'.
   
[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_6.png)](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_6.png)


##### **8. Memilih Terminal Emulator untuk Git Bash**
Pada langkah ini, Anda akan memilih Terminal Emulator bawaan untuk Git Bash nya, apakah menggunakan Konsol Windows atau MinTTY. Pada tutorial ini, saya memilih menggunakan MinTTY, dengan memilih opsi **Use MinTTY (the default terminal of MSYS2)**. Lalu, klik *Button* 'Next >'.
   
[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_7.png)](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_7.png)
   
##### **9. Konfigurasi Opsi Tambahan**
Pada langkah **Configuring extra options**, disitu nanti akan ada tiga opsi, Anda bisa aktifkan semua opsi tersebut dengan mencentang nya. Lalu, klik *Button* 'Next >'.

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_8.png)](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_8.png)

##### **10. Konfigurasi Opsi Eksperimental**
Pada langkah **Configuring experimental options**, disitu nanti akan ada satu opsi yang bisa Anda aktifkan, namun karena sifat nya Eksperimental, maka saya sarankan agar tidak mengaktifkan nya, kecuali jika Anda ingin mencoba nya. Klik pada *Button* 'Next >' untuk melanjutkan. Atau, jika ada *Button* 'Install', klik pada *Button* tersebut untuk meng-install Git.

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_9.png)](https://cdn.statically.io/gl/FarrelF/blog-images/83716833/cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare/Install_Git_9.png)

##### **11. Proses Instalasi sampai Selesai**
Instalasi Git sedang dalam Proses, harap bersabar hingga selesai dalam beberapa menit kedepan.

Jika Git telah berhasil ter-install, klik pada *Button* 'Finish'. Sebelum itu, Anda juga bisa hapus centang **Launch Git Bash** jika Anda tidak ingin menjalankan 'Git Bash' setelah selesai Install.

## **IV. Membuat Blog SSG dengan Pelican**
### **1. Membuat 'Pelican Sites'**
### **2. Konfigurasi Pelican Dasar**
### **3. Menulis Artikel**
### **4. Meng-install Tema Pelican**
### **5. Menggantikan Tema**
### **6. Membuat Berkas Statik 'robots.txt', 'favicon.ico' dan 'CNAME' sebelum deploy**


## **V. Menggunakan Netlify sebagai Hosting**
### **1. Membuat berkas yang di perlukan**
#### **Membuat Berkas 'netlify.toml'**
#### **Membuat Berkas 'requirements.txt' dan 'runtime.txt'**
### **2. Menambahkan 'Sites' dan Men-_deploy_ Blog ke Netlify**