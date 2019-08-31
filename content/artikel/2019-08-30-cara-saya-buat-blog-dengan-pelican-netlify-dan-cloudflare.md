Title: Cara saya membuat Blog dengan Pelican, Netlify dan Cloudflare
Date: 2019-08-30 05:08
Category: Tutorial, Blogging
Tag: Pelican, Netlify, Cloudflare
Slug: cara-membuat-blog-dengan-pelican-netlify-cloudflare
Authors: Farrel Franqois
Summary: Saya memposting tentang cara saya membuat blog ini melalui Pelican, yang tentu saja dengan bantuan Netlify sebagai Hosting nya dan juga Cloudflare sebagai DNS nya. Cara membuat nya ini cukup mudah, kok, penasaran? Bisa kamu baca artikel ini lebih lanjut :slightly_smilling_face:

## Daftar Isi
[TOC]

## I. Pembuka
Halo, semua! Seperti yang Anda tahu, bahwa blog saya ini merupakan HTML Statis, yang tidak di proses secara dinamis, melainkan ini hanyalah sebuah HTML statis yang di hasilkan dari *Static Site Generator* seperti [Pelican](https://blog.getpelican.com). 

Kamu bisa baca Artikel yang berjudul "[Halo Dunia! (Lagi)](https://farrel.franqois.id/halo-dunia)" mengenai Blog yang saya gunakan, beserta hosting nya dan kenapa saya menggunakan nya, dll.

Selain menggunakan Netlify sebagai Hosting nya, blog ini juga menggunakan Cloudflare sebagai DNS nya. Tentu saja, semua ini gratis, gak ada biaya yang di keluarkan, kecuali domain.

Setelah Anda tahu alasan saya kenapa fokus menggunakan/memanfaatkan *Static Site Generator* untuk blogging daripada menggunakan WordPress, apakah Anda termotivasi untuk menggunakan nya? Kalo iya, saya akan beritahu cara nya melalui Tutorial ini.


## II. Persyaratan
Tapi, sebelum Anda melakukan nya, ada syarat-syarat tertentu yang harus Anda turuti sebelum Anda membuat sebuah Blog dengan memanfaatkan *Static Site Generator* seperti Pelican, yaitu:

**Untuk Membuat Blog dan konfigurasi dasar**:
1. Tahu cara mengelola DNS (Seperti menambahkan Subdomain dengan menambahkan CNAME Record, dll).
2. Punya Domain (kalo perlu, karena pada tutorial ini saya akan menggunakan 'Custom Domain'/'Custom Subdomain') dan pastikan Nameserver nya kamu arahkan ke Cloudflare.
3. Mempunyai Akun dari Layanan Git yang di dukung penuh oleh Netlify, seperti [GitHub](https://github.com) dan [GitLab](https://gitlab.com).
4. Mau/gak mau, kamu harus belajar Markdown (Gampang, kok :blush:) atau reStructuredText (rst) untuk menulis Artikel.
5. Pastikan Komputer/Laptop kamu sudah terinstall [Python 3](https://www.python.org), Pip (biasanya 'Pip' sudah terinstall secara default setelah meng-install Python) dan juga [Git](https://git-scm.org)
6. Dan, pastikan juga kamu mempunyai Editor Teks/Kode Favorit kamu, kali ini saya gunakan [VSCodium](https://www.vscodium.com).


**Untuk Konfigurasi Menengah atau Tingkat Lanjut** (Opsional)
1. Mempelajari Dasar dari Bahasa Pemrograman Python 3 (Seperti Penggunaan: 'List', 'Dictionary', 'Tuple', Tipe Data Primitif (seperti: String, Integer, dan Boolean), Pengkondisian dengan if/elif/else, dan 'Import') atau di atas nya, karena Pelican ini berbasis Python.
2. 