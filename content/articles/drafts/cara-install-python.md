Title: Cara Install Python (di Windows dan GNU/Linux)
Category: Tutorial
Tags: Cara Install, Python, Python 3, Windows, GNU/Linux
Slug: cara-install-python
Author: Farrel Franqois
Cover: https://cdn.statically.io/gl/FarrelF/blog-images/35ac221f/cara-install-python/python-logo.png?fit=447,151&quality=80
Cover_Width: 447
Cover_Height: 151
Summary: Apakah Anda ingin meng-install Python, tapi gak tahu caranya? Kali ini, saya akan memposting bagaimana caranya meng-install Python di dalam Windows dan juga GNU/Linux, terutama untuk Python 3 yang merupakan versi terbaru nya. Penasaran? Silahkan baca artikel ini, kalau tidak, ya tidak apa-apa :slightly_smiling_face:
Description: Apakah Anda ingin tahu bagaimana cara install Python (terutama Python 3)? Baik itu di Windows atau GNU/Linux? Jika iya, maka Anda bisa langsung kunjungi dan baca Artikel ini.

## Daftar Isi
[TOC]

## Pembuka
Python merupakan bahasa pemrograman yang sangat populer karena kemudahan nya, namum bisa untuk segala keperluan. Saking mudah nya, bahkan Anak SD pun sudah bisa belajar Python sebagai Bahasa Pemrograman nya.

Namun, di Indonesia ini, banyak orang yang belum mengenal bahasa Pemrograman yang satu ini, terutama di lingkungan akademik (Terutama yang berhubungan dengan "Informatika") yang masih menggunakan bahasa Pemrograman lain nya (Seperti Java, PASCAL atau lain nya) sebagai Standar untuk pembelajaran, meski baru-baru ini kampus saya telah beralih ke Python sebagai Bahasa Pemrograman Standar untuk Angkatan baru nya, mungkin kampus lain nya juga bisa ikutan?

Begitupun juga Lingkungan Sekolah yang tidak di ajarkan Bahasa Pemrograman sama sekali oleh Kurikulum Pendidikan.

Sebagai imbasnya, bagi yang ingin mempelajari Bahasa Pemrograman Python, banyak yang tidak tahu harus di mulai dari mana dan bagaimana cara meng-install nya, terutama di Windows yang banyak sekali langkah instalasi nya, yang di rasa kebingungan.

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
