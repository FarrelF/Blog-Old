Title: Tentang youtube-dl - Pengunduh Video YouTube Alternatif!
Date: 2019-08-30 05:08
Category: Tutorial, Perangkat Lunak
Tag: youtube-dl
Slug: tentang-youtube-dl
Authors: Farrel Franqois
Summary: 

## Daftar Isi
[TOC]

## I. Pembuka
Halo, semua. Seperti yang Anda ketahui, menonton video dari Internet (atau biasa di sebut “Video Streaming”) juga merupakan salah satu keseharian bagi pengguna Internet yang hampir tidak terhindarkan, contoh terdekatnya adalah menonton video di salah satu Layanan Video Streaming yang ada di Internet, yakni [YouTube](https://www.youtube.com).

YouTube adalah salah satu layanan Video Streaming yang paling sering di gunakan setiap hari nya oleh pengguna Internet di seluruh Indonesia.

Namun, masalah nya adalah tidak semua orang mempunyai kuota Internet atau memiliki akses yang cepat, baik untuk menonton pertama kali ataupun ingin menonton video nya lagi.

Untuk mengatasi masalah tersebut, biasanya pengguna Internet mengunduh Video nya secara langsung. (Bisa di mana saja, lagian gak harus menggunakan koneksi Internet dari dia nya juga, kan? Hehe :grinning:)

Banyak sekali metode pengunduhan Video YouTube yang bisa Anda coba, salah satunya memanfaatkan Situs Web seperti [Savefrom](https://savefrom.net), atau YouTube Wrapper seperti [Invidious](https://invidio.us). Selain itu, Anda juga bisa memanfaatkan Download Manager Eksternal seperti: [XDM (Xtreme Download Manager)](http://xdman.sourceforge.net), [IDM (Internet Download Manager)](https://www.internetdownloadmanager.com), dll.

Namun, masalahnya adalah Situs Web seperti 'Savefrom' dan lain nya terkadang tidak menyediakan Video beresolusi Full HD (1080p) atau di atas nya, dan YouTube Wrapper seperti 'Invidious' menyedia kan nya, hanya saja memisahkan Video dan Audio nya, sehingga hal itu akan sangat merepotkan.

Masalah tersebut memang bisa diselesaikan dengan menggunakan Download Manager Eksternal seperti XDMan dan IDM. Tapi, itu kurang ‘asyik’ lah kalau menurut saya, hehe :grinning:

Hampir semua metode mengunduh video YouTube yang ada (terutama di atas), itu belum termasuk dengan subtitle nya dan tidak di tambahkan metadata nya. Ini akan sangat merepotkan, terutama bagi kamu yang ingin mendownload video dengan bahasa selain Bahasa Indonesia.

Karena hal itu, sebagai solusi nya, Anda bisa mengunduh nya dengan memanfaatkan `youtube-dl`. Tentu saja, sebagai Alternatif, bukan pengganti dari yang ada.

Ribet? Tentu itu kembali lagi ke diri masing-masing, justru menurut saya lewat GUI itu lebih ribet lagi. Kurang terbiasa? Mungkin, istilah inilah yang paling tepat saat ini, karena memang pada dasarnya Anda kurang terbiasa dengan youtube-dl ini. Dulu saya juga gitu, hehe :grinning:

Lalu, apa itu youtube-dl? Bagaimana cara meng-installnya sekaligus menggunakan nya? Bisa kamu lanjut baca artikel ini :slightly_smiling_face:

## II. Sekilas Tentang 'youtube-dl'

### Apa itu 'youtube-dl'?
[`youtube-dl`](https://yt-dl.org/) merupakan sebuah Program berbasis CLI (Command-Line Interface) untuk mengunduh video dari YouTube dan banyak [Situs Web lain nya](https://ytdl-org.github.io/youtube-dl/supportedsites.html). Dibuat dalam Bahasa [Python](https://www.python.org) (Python Intepreter), dan Program ini tidak bergantung pada satu Platform tertentu saja.

Karena itu, harusnya program ini bekerja dengan baik di hampir semua Platform yang ada, seperti di dalam Sistem Operasi berbasis UNIX (seperti: macOS, Keluarga/Varian BSD, dll), UNIX-like (seperti: GNU/Linux, dll), dan Windows.

Program tersebut di rilis sebagai Public Domain dan di bawah Lisensi “Unlicense”. Jadi, Anda bisa bebas menggunakan, menyalin, memodifikasi dan mendistribusikan ulang Program tersebut berserta dengan Kode Sumber nya, untuk keperluan apapun, termasuk keperluan komersial sekalipun. 

Tentu saja, tanpa jaminan dan tanggung jawab dari pembuat nya.

### Mengapa youtube-dl? Apa Kelebihan dan Kekurangan nya?
#### (+) Kelebihan

**1. (+) Berfitur paling lengkap**

Tidak dapat di pungkiri, bahwa youtube-dl ini merupakan Program Pengunduh Video dari Internet dengan fitur yang paling lengkap bila di bandingkan dengan Pengunduh sejenis lain nya.

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

Apalagi kalo si pengguna mengeksekusi Program CLI yang menampilkan banyak sekali log/’verbose’, seperti youtube-dl ini, yang nantinya akan menimbulkan perasaan kalo kamu adalah orang ‘satu-satunya’ atau bahkan di anggap “Hacker” oleh orang terdekat kamu (Padahal, belum tentu, hehe :grinning:)


**4. (+) Dapat Di Program (Programmable)**

Seperti yang Anda tahu, bahwa youtube-dl ini merupakan Program yang berbasis CLI, sehingga dapat di program dengan mudah oleh Program/Aplikasi lain nya, baik itu berbasis CLI, bahkan GUI. 

Baik itu sekedar meng-eksekusi nya, bahkan bisa meng-embed nya. Karena di buat dengan Bahasa Python yang bisa di tujukan kemana saja, maka Anda dapat dengan mudah meng-embed nya ke dalam Program/Aplikasi yang ingin Anda buat dan dapat di panggil oleh hampir semua bahasa Pemrograman.


**5. (+) Merupakan Perangkat Lunak Bebas dan bisa di peroleh secara Gratis**

Sudah saya jelaskan di awal, bahwa Program ini merupakan Perangkat Lunak Bebas (Free Software), “Bebas” sebagaimana “bebas dari pengekangan”/”penjara”. 

Jadi, Anda bisa bebas menggunakan, menyalin, memodifikasi dan mendistribusikan ulang Program tersebut berserta dengan Kode Sumber nya, untuk keperluan apapun, termasuk keperluan komersial sekalipun. Tentu saja, tanpa jaminan dan tanggung jawab dari pembuat nya.

Apalagi, Program tersebut di rilis sebagai Public Domain dan menggunakan Lisensi “[Unlicense](https://github.com/ytdl-org/youtube-dl/blob/master/LICENSE)”.  Sehingga Anda bebas untuk melakukan apapun terhadap Program nya.
Walaupun begitu, Anda juga dapat memperoleh Program ini secara gratis, dan tidak perlu membayarnya terlebih dahulu.


#### (-) Kekurangan

**6. (-) Ribet**

Karena Program ini berbasis CLI, ada sebagian orang yang menganggap ini Ribet, sehingga tidak mau mempelajari hal apa yang ada di dalam nya atau sekedar menggunakan nya.

Daripada istilah Ribet, mungkin yang sedikit benar adalah kurang terbiasa, karena pada dasarnya, Anda kurang terbiasa untuk menggunakan nya, sehingga di anggap Ribet.
Tapi, Ribet atau tidak nya, itu kembali kepada diri Anda masing-masing, lagian tergantung siapa yang menilai Ribet atau tidak nya. Kalo menurut saya, justru lebih ribet kalo mengunduhnya dengan Program GUI.


**7. (-) Perlu meng-install ‘Program Tambahan’ dengan ukuran cukup besar**

Kata siapa keperluan youtube-dl ini cuma sebatas Python (atau Visual C++ 2010 untuk Windows) saja? Bisa saja cuma bermodal hanya itu, namun hal ini tidak membuat youtube-dl dapat di gunakan secara maksimal, alias minim fitur.

Agar youtube-dl dapat di gunakan secara maksimal, Anda harus meng-install Program/Aplikasi ‘Tambahan” lain nya yang sayangnya itu berukuran besar, sekitar 35-60+ MBan.
Jadi, kalo kamu pengen bisa mengunduh video dari YouTube dengan resolusi 1080p atau di atas nya, maka Anda harus meng-install Program tersebut agar youtube-dl dapat menggabungkan antara format Video dan Audio setelah di unduh nanti.

Program tersebut bisa berupa: FFmpeg atau Avconv (Libav). Namun, untuk pembahasan ini saya akan lebih membahas cara instalasi FFmpeg daripada Avconv, selain populer, FFmpeg juga dapat di Install dengan mudah. (Atau, mungkin saya nya yang kudet?)