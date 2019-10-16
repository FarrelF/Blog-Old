Title: Cara Install LAMP Stack (Apache2, MariaDB, PHP 7) + phpMyAdmin di Ubuntu dan Turunan nya
Category: Tutorial
Tag: Cara Install, LAMP Stack, Apache2, MariaDB, PHP 7
Slug: cara-install-lamp-stack
Authors: Farrel Franqois
Status: draft
Description: Apakah Anda ingin mencari Cara Install LAMP Stack dengan benar untuk keperluan Pengembangan di dalam Sistem Ubuntu Anda? Jika iya, maka Anda bisa kunjungi dan baca artikel ini, dan saya langsung membahas nya.
Summary: Artikel ini akan membahas tentang bagaimana caranya meng-install _LAMP Stack_ di dalam Sistem Operasi GNU/Linux, khususnya untuk pengguna Distribusi Ubuntu dan Turunan nya (seperti Linux Mint) dengan "benar". Penasaran? Silahkan baca artikel ini, kalau tidak, ya tidak apa-apa :slightly_smiling_face: 

## Daftar Isi

[TOC]

## Pembuka
Banyak sekali pengguna GNU/Linux yang ingin menguji Aplikasi Web yang telah di buatnya, seperti seseorang yang ingin menguji Aplikasi Web yang di buat nya dengan bahasa pemrograman PHP dengan meng-install Webserver seperti Apache2 serta Bahasa Pemrograman Web seperti PHP juga turut di Install, agar Aplikasi Web tersebut bisa di uji.

Namun, masih ada yang bingung tentang bagaimana cara meng-install Aplikasi yang di perlukan tersebut. 

Dan, sayangnya, banyak sekali praktik yang salah mengenai ini, contoh nya, masih ada pengguna yang meng-install nya dengan XAMPP, yang akan mengakibatkan Apache2, PHP dan MariaDB/MySQL tidak terinstall sama sekali ke dalam Sistem Operasi.

Atau, bahkan yang lebih parahnya adalah ada yang menggunakan 'chmod 777' pada “Document Root” nya (seperti `:::text /var/www/html/`) yang akan menimbulkan celah keamanan yang fatal, salah kepemilikan _Document Root_ yang mengakibatkan tidak bisa membuat/mengedit atau menghapus file/folder di dalam _Document Root_, menginstall phpMyAdmin melalui Repo, dsb. 

Lalu, bagaimana caranya agar kita bisa meng-install _Web Stack_ ke dalam sistem operasi dengan "benar"? Anda bisa baca tutorial nya di dalam artikel ini, tapi sebelumnya Anda harus membaca Sanggahan Tambahan nya terlebih dahulu agar Anda bisa paham.

## Sanggahan
Cara ini bukanlah cara cepat untuk meng-install _LAMP Stack_ ke dalam Sistem Anda, ini adalah cara yang ‘fleksibel’ untuk meng-install _LAMP Stack_. Jadi, tutorial ini tidaklah cocok bagi Anda yang ingin serba instan. Jadi, Artikel ini akan membahasnya dengan “Panjang x Lebar”, dan saya harap Anda kuat baca dan pemahamnya, hehe :grinning:

Dengan “Panjang x Lebar” nya pembahasan ini, saya harapkan bahwa Anda bisa mempelajari apa yang kamu lakukan nanti nya, baik itu sebelum melakukan nya sampai sesudah melakukan nya.
Artikel ini tidak pernah saya tujukan untuk pengguna Server (meski bisa), melainkan untuk Web Developer/Programmer yang ingin menggunakan/meng-install _LAMP Stack_.

Karena di tujukan untuk Web Developer/Programmer, maka bahasan tentang Keamanan dan Optimasi disini harusnya akan sangat berbeda jika di bandingkan dengan pengguna Server. Jadi, bagi Web Developer/Programmer, Anggap saja pembahasan keamanan dan optimasi disini sebagai bonus, dan di harapkan agar Anda bisa mengatur keamanan dan optimasi nya sendiri untuk kedepan nya.

Artikel ini memang membahas tentang “cara install yang benar”, bukan berarti Artikel ini sepenuhnya benar. “Benar” disini maksudnya adalah melakukan sesuatu dengan praktek yang lebih baik atau/dan "lebih benar" daripada yang Anda praktekkan sebelumnya, bukan bermaksud pada “sepenuhnya benar”. 

Jadi, mohon perhatian dan pengertian nya dari pembaca sekalian :slightly_smiling_face:

Ngomong-ngomong, pernyataan ini adalah pernyataan tambahan dari yang [sebenarnya]({filename}/pages/ketentuan-hukum-dan-sanggahan.md).

Terima kasih atas perhatian dan pengertian nya :blush:

## I. Sebelum Install
Sebelum Anda meng-install _LAMP Stack_, sebaiknya Anda Perbarui (_Update_) terlebih dahulu Repo Anda dan semua Perangkat Lunak yang terpasang terlebih dahulu, dengan menggunakan perintah berikut:

```bash
$ sudo apt update
$ sudo apt full-upgrade
```

Bisa kamu gunakan Aplikasi yang berbasis GUI kalau kamu lebih suka GUI. Sedangkan, kalau kamu menggunakan Mint, maka kamu bisa gunakan “Update Manager”.

## II. Install Apache2
### Cara Install
Instalasi nya memang sangat mudah, buka _Terminal Emulator_ pada sistem Ubuntu (dan Turunan nya) Anda, lalu eksekusi perintah berikut ini untuk meng-install 'Apache2':

```bash
$ sudo apt install -y apache2 apache2-utils
```

### Setelah Instalasi


## III. Install MariaDB
### Menambahkan Repo (Opsional)

## IV. Install PHP7
## V. Install phpMyAdmin
