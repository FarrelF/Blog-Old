Title: Tentang youtube-dl - Pengunduh Video YouTube Alternatif!
Category: Tutorial, Perangkat Lunak
Tag: youtube-dl
Slug: tentang-youtube-dl
Authors: Farrel Franqois
Summary: 

## **Daftar Isi**
[TOC]

## **I. Pembuka**
Halo, semua. Seperti yang Anda ketahui, menonton video dari Internet (atau biasa di sebut “Video Streaming”) juga merupakan salah satu keseharian bagi pengguna Internet yang hampir tidak terhindarkan, contoh terdekatnya adalah menonton video di salah satu Layanan Video Streaming yang ada di Internet, yakni [YouTube](https://www.youtube.com).

YouTube adalah salah satu layanan Video Streaming yang paling sering di gunakan setiap hari nya oleh pengguna Internet di seluruh Indonesia.

Namun, masalah nya adalah tidak semua orang mempunyai kuota Internet atau memiliki akses yang cepat, baik untuk menonton pertama kali ataupun ingin menonton video nya lagi.

Untuk mengatasi masalah tersebut, biasanya pengguna Internet mengunduh Video nya secara langsung. (Bisa di mana saja, lagian gak harus menggunakan koneksi Internet dari dia nya juga, kan? Hehe :grinning:)

Banyak sekali metode pengunduhan Video YouTube yang bisa Anda coba, salah satunya memanfaatkan Situs Web seperti [Savefrom](https://savefrom.net), atau YouTube Wrapper seperti [Invidious](https://invidio.us). Selain itu, Anda juga bisa memanfaatkan Download Manager Eksternal seperti: [XDM (Xtreme Download Manager)](http://xdman.sourceforge.net), [IDM (Internet Download Manager)](https://www.internetdownloadmanager.com), dll.

Namun, masalahnya adalah Situs Web seperti 'Savefrom' dan lain nya terkadang tidak menyediakan Video beresolusi Full HD (1080p) atau di atas nya, dan YouTube Wrapper seperti 'Invidious' menyedia kan nya, hanya saja memisahkan Video dan Audio nya, sehingga hal itu akan sangat merepotkan.

Masalah tersebut memang bisa diselesaikan dengan menggunakan Download Manager Eksternal seperti XDMan dan IDM. Tapi, itu kurang ‘asyik’ lah kalau menurut saya, hehe :grinning:

Hampir semua metode mengunduh video YouTube yang ada (terutama di atas), itu belum termasuk dengan subtitle nya dan tidak di tambahkan metadata nya. Ini akan sangat merepotkan, terutama bagi kamu yang ingin mendownload video dengan bahasa selain Bahasa Indonesia.

Karena hal itu, sebagai solusi nya, Anda bisa mengunduh nya dengan memanfaatkan `youtube-dl`. Tentu saja, sebagai Alternatif, bukan pengganti dari yang ada.

Ribet? Tentu itu kembali lagi ke diri masing-masing, justru menurut saya lewat GUI itu lebih ribet lagi. Kurang terbiasa? Mungkin, istilah inilah yang paling tepat saat ini, karena memang pada dasarnya Anda kurang terbiasa dengan `youtube-dl` ini. Dulu saya juga gitu, hehe :grinning:

Lalu, apa itu `youtube-dl`? Bagaimana cara meng-installnya sekaligus menggunakan nya? Bisa kamu lanjut baca artikel ini :slightly_smiling_face:

## **II. Sekilas Tentang `youtube-dl`**

### **Apa itu `youtube-dl`?**
[`youtube-dl`](https://yt-dl.org/) merupakan sebuah Program berbasis CLI (Command-Line Interface) untuk mengunduh video dari YouTube dan banyak [Situs Web lain nya](https://ytdl-org.github.io/youtube-dl/supportedsites.html). Dibuat dalam Bahasa [Python](https://www.python.org) (Python Intepreter), dan Program ini tidak bergantung pada satu Platform tertentu saja.

Karena itu, harusnya program ini bekerja dengan baik di hampir semua Platform yang ada, seperti di dalam Sistem Operasi berbasis UNIX (seperti: macOS, Keluarga/Varian BSD, dll), UNIX-like (seperti: GNU/Linux, dll), dan Windows.

Program tersebut di rilis sebagai Public Domain dan di bawah Lisensi “Unlicense”. Jadi, Anda bisa bebas menggunakan, menyalin, memodifikasi dan mendistribusikan ulang Program tersebut berserta dengan Kode Sumber nya, untuk keperluan apapun, termasuk keperluan komersial sekalipun. 

Tentu saja, tanpa jaminan dan tanggung jawab dari pembuat nya.

### **Mengapa `youtube-dl`? Apa Kelebihan dan Kekurangan nya?**
#### **(+) Kelebihan**

**1. (+) Berfitur paling lengkap**

Tidak dapat di pungkiri, bahwa `youtube-dl` ini merupakan Program Pengunduh Video dari Internet dengan fitur yang paling lengkap bila di bandingkan dengan Pengunduh sejenis lain nya.

Fitur nya apa saja? Fitur nya sebagai berikut:

- Bisa mengunduh Video atau Audio nya saja. Bahkan, bisa mengunduh kedua nya (Video+Audio) dan kemudian di gabungkan.
- Bisa juga mengunduh Video dan Audio dengan berbagai Format berbeda, selama Format tersebut tersedia.
- Anda bisa mengunduh Subtitle nya juga (kalo ada). Kalo gak ada Subtitle, Anda juga bisa mengunduh Subtitle Otomatis nya (hanya dari YouTube).
- Selain mengunduh Subtitle, Anda juga bisa memasukkan Subtitle-subtitle tersebut ke dalam Video setelah selesai mengunduh Video nya, secara otomatis. Jadi, video tersebut akan memiliki “Soft Subtitle” di dalamnya. (Kalo ada)
- Menambahkan Metadata ke dalam Video setelah di unduh.
- Selain menambahkan Metadata dan Subtitle, Anda juga bisa meng-konversikan Video/Audio yang telah Anda unduh ke dalam format yang berbeda.
- Mendukung Pengunduh Eksternal (seperti: Wget, aria2, dll) agar bisa mengunduh Video/Audio dengan Perantara di dalam youtube-dl 
- Dan, banyak fitur-fitur lain nya.


**2. (+) Ringan**

Sudah jelas sekali kalo Program ini sangatlah ringan, karena berbasis CLI, sehingga tidak perlu proses Grafis seperti ketika kamu membuka Program dengan berbasis GUI.
Kecuali, kalo kamu memproses Video dan Audio dengan Program CLI, seperti FFmpeg.


**3. (+) Biar keliatan beda/keren**

Kalo ini, mungkin lebih ke alasan “sosial” daripada fitur dari program itu sendiri. Ya, tidak dapat di pungkiri, bahwa kebanyakan Program yang berbasis CLI dapat meningkatkan rasa kepuasan tersendiri, karena menjadi berbeda dari yang lain. 

Apalagi kalo si pengguna mengeksekusi Program CLI yang menampilkan banyak sekali log/’verbose’, seperti `youtube-dl` ini, yang nantinya akan menimbulkan perasaan kalo kamu adalah orang ‘satu-satunya’ atau bahkan di anggap “Hacker” oleh orang terdekat kamu (Padahal, belum tentu, hehe :grinning:)


**4. (+) Dapat Di Program (Programmable)**

Seperti yang Anda tahu, bahwa youtube-dl ini merupakan Program yang berbasis CLI, sehingga dapat di program dengan mudah oleh Program/Aplikasi lain nya, baik itu berbasis CLI, bahkan GUI. 

Baik itu sekedar meng-eksekusi nya, bahkan bisa meng-embed nya. Karena di buat dengan Bahasa Python yang bisa di tujukan kemana saja, maka Anda dapat dengan mudah meng-embed nya ke dalam Program/Aplikasi yang ingin Anda buat dan dapat di panggil oleh hampir semua bahasa Pemrograman.


**5. (+) Merupakan Perangkat Lunak Bebas dan bisa di peroleh secara Gratis**

Sudah saya jelaskan di awal, bahwa Program ini merupakan Perangkat Lunak Bebas (Free Software), “Bebas” sebagaimana “bebas dari pengekangan”/”penjara”. 

Jadi, Anda bisa bebas menggunakan, menyalin, memodifikasi dan mendistribusikan ulang Program tersebut berserta dengan Kode Sumber nya, untuk keperluan apapun, termasuk keperluan komersial sekalipun. Tentu saja, tanpa jaminan dan tanggung jawab dari pembuat nya.

Apalagi, Program tersebut di rilis sebagai Public Domain dan menggunakan Lisensi ["Unlicense"](https://github.com/ytdl-org/youtube-dl/blob/master/LICENSE).  Sehingga Anda bebas untuk melakukan apapun terhadap Program nya.
Walaupun begitu, Anda juga dapat memperoleh Program ini secara gratis, dan tidak perlu membayarnya terlebih dahulu.


#### **(-) Kekurangan**

**1. (-) Ribet**

Karena Program ini berbasis CLI, ada sebagian orang yang menganggap ini Ribet, sehingga tidak mau mempelajari hal apa yang ada di dalam nya atau sekedar menggunakan nya.

Daripada istilah Ribet, mungkin yang sedikit benar adalah kurang terbiasa, karena pada dasarnya, Anda kurang terbiasa untuk menggunakan nya, sehingga di anggap Ribet.
Tapi, Ribet atau tidak nya, itu kembali kepada diri Anda masing-masing, lagian tergantung siapa yang menilai Ribet atau tidak nya. Kalo menurut saya, justru lebih ribet kalo mengunduhnya dengan Program GUI.


**2. (-) Perlu meng-install ‘Program Tambahan’ dengan ukuran cukup besar**

Kata siapa keperluan `youtube-dl` ini cuma sebatas Python (atau Visual C++ 2010 untuk Windows) saja? Bisa saja cuma bermodal hanya itu, namun hal ini tidak membuat `youtube-dl` dapat di gunakan secara maksimal, alias minim fitur.

Agar `youtube-dl` dapat di gunakan secara maksimal, Anda harus meng-install Program/Aplikasi ‘Tambahan” lain nya yang sayangnya itu berukuran besar, sekitar 35-60+ MBan.
Jadi, kalo kamu pengen bisa mengunduh video dari YouTube dengan resolusi 1080p atau di atas nya, maka Anda harus meng-install Program tersebut agar `youtube-dl` dapat menggabungkan antara format Video dan Audio setelah di unduh nanti.

Program tersebut bisa berupa: FFmpeg atau Avconv (Libav). Namun, untuk pembahasan ini saya akan lebih membahas cara instalasi FFmpeg daripada Avconv, selain populer, FFmpeg juga dapat di Install dengan mudah. (Atau, mungkin saya nya yang kudet?)

## **III. Cara Install dan Update nya**
### **Untuk GNU/Linux atau macOS (atau, Sistem Operasi berbasis *nix lain nya)**
Sebelum meng-install program ini di dalam Sistem Operasi berbasis UNIX dan UNIX-like Anda, setidak nya Anda harus meng-install Python terlebih dahulu. Versi Python yang yang dapat Anda gunakan yaitu 2.6, 2.7 atau 3.2+ (Kalo mau di Install dua-dua nya, seperti Python 2.7 dan Python 3.2+ juga tidak masalah).

Kali ini, karena saya hanya menggunakan GNU/Linux, maka saya hanya bahas ini untuk pengguna GNU/Linux, dan saya lebih mengutamakan nya untuk distribusi Debian dan Turunan nya.

#### **1. Install Python di dalam GNU/Linux**
Biasanya, di dalam beberapa Distribusi GNU/Linux, terutama Distribusi Ubuntu dan Turunan nya, sudah ter-install Python 2 dan Python 3 secara Default.

Jadi, Anda tidak perlu meng-install nya lagi, kalo gak percaya, silahkan eksekusi (salah satu/kedua) perintah berikut: (Lewati ini kalo bener-bener yakin sudah ter-install)

```bash
$ python3   # Untuk meng-eksekusi Python 3
$ python    # Untuk meng-eksekusi Python 2
```

Jika perintah nya menghasilkan Output seperti di bawah ini (contohnya saya eksekusi Python 3):

```bash
$ python3
Python 3.6.8 (default, Jan 14 2019, 11:02:34)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()   # Untuk keluar dari Python Shell
```

Maka berarti Python 3 atau 2 sudah terinstall di dalam Sistem Anda. Contoh di atas menggunakan Python 3, untuk Python 2 akan sama Output nya jika sudah ter-install, cuma beda versi aja.

Kalo ternyata belum di Install, maka install Python 2 dan Python 3 di dalam Sistem Anda, untuk pengguna Distribusi Debian, Ubuntu dan Turunan nya, bisa gunakan perintah berikut:

```bash
$ sudo apt update; sudo apt install python python3
```

Atau:

    # apt update; apt install python python3

Atau, jika Anda merupakan pengguna Distribusi selain Debian, Ubuntu dan Turunan nya, bisa Anda install Python 2 dan 3 dengan salah satu perintah berikut:

```bash
## Untuk Pengguna Fedora dan Turunan nya ##
$ sudo dnf install python2 python3

## Untuk Pengguna Arch Linux dan Turunan nya ##
$ sudo pacman -S python python2

## Untuk Pengguna OpenSUSE dan Turunan nya ##
$ sudo zypper in python python3

## Untuk Pengguna Gentoo dan Turunan nya ##
$ sudo emerge --ask dev-lang/python:3.7  # Untuk meng-install Python 3.7 di dalam Gentoo
```

#### **2. Install 'Program Tambahan' di dalam GNU/Linux (Opsional)**
##### **Install FFmpeg**
Setelah selesai Install Python, silahkan eksekusikan Python dengan cara di atas tadi. Sudah sampai disini saja? Tentu saja belum, dan `youtube-dl` bukan cuma bergantung pada Python saja, ada beberapa Aplikasi yang di perlukan, seperti FFmpeg.

Nah, Agar `youtube-dl` dapat menggunakan fitur nya secara maksimal, Anda sangat wajib untuk meng-install FFmpeg ke dalam Sistem Operasi Anda.

Ada banyak sekali Tutorial mengenai Cara instalasi yang beredar di Internet, kamu bisa Googling sendiri untuk meng-install nya. (Terutama jika Anda menggunakan Sistem Operasi berbasis Unix/Unix-like selain GNU/Linux)

Tapi, kebanyakan tutorial cara meng-install FFmpeg pada Sistem Operasi GNU/Linux itu menyarankan agar sebaiknya di install melalui Package Manager, yang padahal sebenarnya itu terasa ‘kurang’.

Kenapa di bilang seperti itu? Karena FFmpeg sendiri telah menyediakan Static Binary nya, yang dapat di jalankan di dalam Sistem Operasi GNU/Linux (apapun Distribusi nya), langsung dapat versi terbaru serta bisa di percaya (karena di sediakan FFmpeg sendiri/Pihak Hulu).

Sedangkan, kalo melalui Package Manager terkadang kita tidak dapat versi terbaru dan juga kurang di percaya (terutama kalo menggunakan Repo dari Luar) karena di sediakan oleh pihak ke-3, dsb.

Selain itu, meng-install nya dengan Package Manager itu akan cenderung berbeda-beda setiap Distribusi, sehingga hal itu akan menimbulkan ‘keribetan’ terutama bagi yang suka gonta-ganti Distribusi, karena cara instalasi nya yang berbeda-beda nantinya.

Nah, karena itu, saya akan memberikan Tutorial cara meng-install FFmpeg ini untuk Sistem Operasi GNU/Linux, yang tentu nya bida di jalankan/di gunakan oleh semua Distribusi.

Tanpa basa-basi lagi, berikut adalah cara instalasi nya:

1. Unduh terlebih dahulu Static Binary FFmpeg dari Halaman Situs Web nya [‘John Van Sickle’](https://johnvansickle.com/ffmpeg/) yang di Rekomendasikan oleh [Situs Web Resmi](https://ffmpeg.org/download.html) nya (https://johnvansickle.com/ffmpeg/). 

2. **CATATAN**: Sebelum mengunduh nya, Anda harus siapkan kuota yang cukup untuk meng-unduhnya, karena besarnya mencapai 35+ MB.

3. Setelah itu, pilih Arsitektur Sistem yang Anda gunakan. Kalo Anda lebih suka menggunakan Terminal untuk mengunduhnya, Anda bisa manfaatkan aria2 atau Wget untuk hal ini, berikut perintah nya (dan langkah-langkahnya):

```bash
## 1. Menentukan Jenis Rilisan FFmpeg ##
$ FFMPEG_RELEASE_TYPE="release"; export FFMPEG_RELEASE_TYPE

## Catatan: Di atas merupakan Jenis Rilisan dari FFmpeg yang ingin Anda Unduh, ganti dengan 'git' jika ingin menggunakan Versi "Nightly"/"Git" nya, atau biarkan tetap 'release' agar mendapatkan versi "Stabil" nya. (Default: "release") ##

## 2. Menentukan Variabel RELEASE_PATH untuk URL Unduhan nanti ##
$ if [ "$FFMPEG_RELEASE_TYPE" = "release" ]; then FFMPEG_RELEASE_PATH="releases"; elif [ "$FFMPEG_RELEASE_TYPE" = "git" ]; then FFMPEG_RELEASE_PATH="builds"; fi; export FFMPEG_RELEASE_PATH

## 3. Menentukan Arsitektur Sistem ##
$ SYSTEM_ARCH = "amd64"; export SYSTEM_ARCH

## Catatan: Anda bisa menentukan Arsitektur Sistem untuk FFmpeg yang ingin Anda Unduh. Bisa Anda isi dengan Arsitektur Sistem Operasi yang Anda gunakan. Nilai yang tersedia dan yang bisa Anda gunakan: 'amd64' (x86-64, 64-bit), 'i686' (x86, 32-bit), 'arm64', 'armhf', dan 'armel'. (Default: "amd64")  ##

## 4. Menentukan Nama File yang akan di Unduh ##
$ FFMPEG_FILENAME="ffmpeg-$FFMPEG_RELEASE_TYPE-$SYSTEM_ARCH-static.tar.xz"; export FFMPEG_FILENAME

## 5.a: Di bawah ini untuk mengunduh FFmpeg dengan aria2 ##
$ aria2c -x16 "https://johnvansickle.com/ffmpeg/$FFMPEG_RELEASE_PATH/$FFMPEG_FILENAME"

## 5.b: Atau, mengunduh nya dengan GNU Wget ##
$ wget "https://johnvansickle.com/ffmpeg/$FFMPEG_RELEASE_PATH/$FFMPEG_FILENAME"
```

4. Setelah Anda mengunduhnya, buatlah sebuah folder yang bernama `ffmpeg.d` di dalam direktori `/usr/local/bin`, dan ekstrak berkas yang telah Anda Unduh tersebut kedalam folder yang barusan Anda buat, dengan perintah berikut:

```bash
$ sudo mkdir /usr/local/bin/ffmpeg.d
$ sudo tar -xvJf "$FFMPEG_FILENAME" --strip-components=1 -C /usr/local/bin/ffmpeg.d; sudo chown -R root:root /usr/local/bin/ffmpeg.d; cd "$_" || return
```

5. Terakhir, buatlah *Symlink* dari berkas FFmpeg yang berada di dalam `/usr/local/bin` dan `/usr/bin` yang menargetkan FFmpeg yang berada di dalam direktori yang Anda ‘jelajahi’ sekarang, yakni `/usr/local/bin/ffmpeg.d` dengan cara berikut:
```bash
$ sudo ln -sf "$PWD"/ffmpeg /usr/local/bin/ffmpeg
$ sudo ln -sf "$PWD"/ffprobe /usr/local/bin/ffprobe
```

6. Selesai, deh!

Nah, dengan ini, FFmpeg telah ter-install dengan sangat baik didalam Sistem Operasi GNU/Linux Anda, apapun Distribusi nya. 

##### **Install Aria2c sebagai Pengunduh Eksternal**

#### **3. Install `youtube-dl`**

Untuk Meng-install youtube-dl itu sendiri sebenarnya sangat mudah, ada beberapa metode yang bisa Anda coba, yakni sebagai berikut:

##### **Metode 1 : Install dengan cara langsung (Paling mudah dan disarankan)**
##### **Metode 2 : Install dengan Pip (dan cara update nya)**
##### **Metode 3 : Install dengan Homebrew**

#### **4. Setelah Install `youtube-dl` (Opsional)**
##### **Cek Versi yang di gunakan**
##### **Menguji `youtube-dl`**


#### **5. Imbauan untuk yang bukan pengguna Windows**
Jika Anda adalah bukan pengguna Windows atau tidak ingin meng-install `youtube-dl` di dalam Sistem Operasi Windows, untuk menghemat waktu, sebaik nya Anda lewati saja pembahasan berikutnya, dan langsung masuk ke pembahasan “[**IV. Cara Menggunakan nya**](#iv-cara-menggunakan-nya)” (tanpa kutip).

Karena pembahasan berikut nya adalah meng-install `youtube-dl` beserta ketergantungan nya di dalam sistem operasi Windows, yang mungkin membuang waktu Anda jika tidak menggunakan nya atau tidak ingin meng-installnya.


### **Untuk Windows**


## **IV. Cara Menggunakan nya**
## **V.**
