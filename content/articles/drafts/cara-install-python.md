Title: Cara Install Python (di Windows dan GNU/Linux)
Category: Tutorial
Tags: Cara Install, Python, Python 3, Windows, GNU/Linux
Slug: cara-install-python

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
