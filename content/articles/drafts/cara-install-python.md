---
Title: Cara Install Python (di Windows dan GNU/Linux)
Category: Tutorial
Tags: Cara Install, Python, Python 3, Windows, GNU/Linux
Slug: cara-install-python
Author: Farrel Franqois
Cover: https://cdn.statically.io/gl/FarrelF/blog-images/35ac221f/cara-install-python/python-logo.png?fit=447,151&quality=80
Summary: Apakah Anda ingin meng-install Python, tapi gak tahu caranya? Kali ini, saya akan memposting bagaimana caranya meng-install Python di dalam Windows dan juga GNU/Linux, terutama untuk Python 3 yang merupakan versi terbaru nya. Penasaran? Silahkan baca artikel ini, kalau tidak, ya tidak apa-apa :slightly_smiling_face:
Description: Apakah Anda ingin tahu bagaimana cara install Python (terutama Python 3)? Baik itu di Windows atau GNU/Linux? Jika iya, Anda bisa langsung kunjungi dan baca Artikel ini.
---

## Daftar Isi
[TOC]

## Pembuka
Python merupakan bahasa pemrograman yang sangat populer karena kemudahan nya, namum bisa untuk segala keperluan. Saking mudah nya, bahkan Anak SD pun sudah bisa belajar Python sebagai Bahasa Pemrograman nya.

Namun, di Indonesia ini, banyak orang yang belum mengenal bahasa Pemrograman yang satu ini, terutama di lingkungan akademik (Terutama yang berhubungan dengan "Informatika") yang masih menggunakan bahasa Pemrograman lain nya (Seperti Java, PASCAL atau lain nya) sebagai Standar untuk pembelajaran, meski baru-baru ini kampus saya telah beralih ke Python sebagai Bahasa Pemrograman Standar untuk Angkatan baru nya, mungkin kampus lain nya juga bisa ikutan?

Begitupun juga Lingkungan Sekolah yang tidak di ajarkan Bahasa Pemrograman sama sekali oleh Kurikulum Pendidikan.

Sebagai imbasnya, bagi yang ingin mempelajari Bahasa Pemrograman Python, banyak yang tidak tahu harus di mulai dari mana dan bagaimana cara meng-install nya, terutama di Windows yang banyak sekali langkah instalasi nya, yang di rasa kebingungan.

## I. Cara Install Python
### **Install Python di dalam GNU/Linux**
Biasanya, di dalam beberapa Distribusi GNU/Linux, terutama Distribusi Ubuntu dan Turunan nya, sudah ter-install Python 2 dan Python 3 secara Bawaan.

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
$ sudo apt update; sudo apt install python python-dev python-pip python-doc python3 python3-dev python3-pip python3-venv python3-doc python3-tk
```

Atau:

    # apt update; apt install python python-dev python-pip python-doc python3 python3-dev python3-pip python3-venv python3-doc python3-tk

Atau, jika Anda merupakan pengguna Distribusi selain Debian, Ubuntu dan Turunan nya, bisa Anda install Python 2 dan 3 dengan salah satu perintah berikut:

```bash
## Untuk Pengguna Fedora dan Turunan nya ##
$ sudo dnf install python2 python3

## Untuk Pengguna Arch Linux dan Turunan nya ##
$ sudo pacman -S python python2

## Untuk Pengguna OpenSUSE dan Turunan nya ##
$ sudo zypper in python python3

## Untuk Pengguna Gentoo dan Turunan nya ##
$ sudo emerge --ask dev-lang/python:3.8  # Untuk meng-install Python 3.8 di dalam Gentoo
```

**Catatan:** Perintah Instalasi di atas memang lebih pendek dan lebih singkat daripada perintah Instalasi Python untuk Debian, Ubuntu dan Turunan nya. Namun, itu bukan berarti sekali install langsung bisa jadi untuk keperluan normal (Seperti penggunaan Venv, Pip, dll), bisa jadi ada paket lain yang kurang/belum terinstall. Jika ada, maka Anda bisa berkomentar untuk tambahan nya atau saran lain nya.

**Catatan (Khusus untuk pengguna Arch):** Paket [`:::text python`](https://www.archlinux.org/packages/?q=python) yang tertera di situ adalah Python 3, bukanlah Python 2, ini tidak seperti Distribusi GNU/Linux kebanyakan lain nya.

### **Install Python versi terbaru di Ubuntu dan Turunan nya**
Di dalam Distribusi Ubuntu dan Turunan nya (seperti Mint, dan lain nya), biasanya di sediakan Python versi 3 di dalam _Repository_ nya. Namun, besaran versi yang di gunakan itu bisa berbeda untuk setiap versi dari Distribusi itu sendiri.

Dan, sebagai akibatnya, terkadang versi Python yang di gunakan itu lambat dapat pembaruan, atau malah tidak dapat pembaruan sama sekali. 

Jadi, Agar Anda bisa meng-install Python 3 versi terbaru nya, saya sarankan Anda harus menambahkan _Repository PPA_ dari 'Deadsnakes' terlebih dahulu, dengan perintah berikut: (Walau sebenarnya ini Opsional jika Anda menggunakan Ubuntu 18.04 dan di atas nya)

```bash
$ sudo -- sh -c 'add-apt-repository ppa:deadsnakes/ppa; apt update'
```

Setelah itu, silahkan Anda install Python 3 versi terbaru tersebut dan tentu kan terlebih dahulu versi mana yang ingin di-install.

Misal, jika Anda ingin meng-install Python versi 3.7, maka Anda harus meng-install nya dengan perintah berikut:

```bash
$ sudo apt install python3.7 python3.7-dev python3.7-venv python3.7-doc
```

Atau, jika Anda ingin meng-install Python versi 3.8, maka Anda harus meng-install nya dengan perintah berikut:

```bash
$ sudo apt install python3.8 python3.8-dev python3.8-venv python3.8-doc
```

Dan, begitupula dengan seterus nya. 
