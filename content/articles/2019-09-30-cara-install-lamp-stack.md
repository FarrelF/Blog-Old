Title: Cara Install LAMP Stack (Apache2, MariaDB, PHP 7) + phpMyAdmin di Ubuntu dan Turunan nya
Category: Tutorial
Tag: Cara Install, LAMP Stack, Apache2, MariaDB, PHP 7
Slug: cara-install-lamp-stack
Authors: Farrel Franqois
Status: draft
Description: Apakah Anda ingin mencari Cara Install LAMP Stack dengan benar untuk keperluan Pengembangan di dalam Sistem Ubuntu Anda? Jika iya, maka Anda bisa kunjungi dan baca artikel ini, dan saya langsung ke pembahasan nya.

<!-- PELICAN_BEGIN_SUMMARY -->

Banyak sekali pengguna GNU/Linux yang ingin menguji Aplikasi Web yang telah di buatnya, seperti seseorang yang ingin menguji Aplikasi Web yang di buat nya dengan bahasa pemrograman PHP dengan meng-install Webserver seperti Apache2 serta Bahasa Pemrograman Web seperti PHP juga turut di Install, agar Aplikasi Web tersebut bisa di uji.

Namun, masih ada yang bingung tentang bagaimana cara meng-install Aplikasi yang di perlukan tersebut. 

Dan, sayangnya, banyak sekali praktik yang salah mengenai ini, seperti menggunakan chmod 777 pada “Document Root” (seperti `:::text /var/www/html/`) yang akan menimbulkan celah keamanan yang fatal, salah kepemilikan Document Root yang mengakibatkan tidak bisa membuat/mengedit atau menghapus file/folder di dalam Document Root, menginstall phpMyAdmin melalui Repo, dsb.

Atau, masih ada yang meng-install nya dengan XAMPP, yang akan mengakibatkan Apache2, PHP dan MariaDB/MySQL tidak terinstall sama sekali ke dalam Sistem.

Lalu, bagaimana caranya agar kita bisa meng-install Web Stack ke dalam sistem dengan "benar"? Silakan Anda baca artikel ini, untuk dapat memahami nya lebih lanjut 

<!-- PELICAN_END_SUMMARY -->

## Daftar Isi

[TOC]

## I. Sebelum Install
Sebelum Anda meng-install LAMP Stack, sebaiknya Anda Update terlebih dahulu Repo Anda dan semua Perangkat Lunak yang terpasang terlebih dahulu, dengan menggunakan perintah berikut:

```bash
$ sudo apt update
$ sudo apt full-upgrade
```

Bisa kamu gunakan Aplikasi yang berbasis GUI kalo kamu lebih suka GUI. Kalo kamu menggunakan Mint, maka kamu bisa gunakan “Update Manager”.

## II. Install Apache2
### Cara Install
Cara instalasi nya memang sangat mudah, buka terminal pada sistem Ubuntu (dan Turunan nya) Anda, lalu eksekusi perintah berikut ini untuk meng-install Apache2:

```bash
$ sudo apt install -y apache2 apache2-utils
```

## III. Install MariaDB
## IV. Install PHP7
## V. Install phpMyAdmin
