---
Title: Cara saya membuat Blog dengan Pelican, Netlify dan Cloudflare
Category: Tutorial, Blogging
Tag: Pelican, Netlify, Cloudflare
Slug: cara-membuat-blog-dengan-pelican-netlify-dan-cloudflare
Authors: Farrel Franqois
Summary: Saya memposting tentang cara saya membuat blog ini melalui Pelican, yang tentu saja dengan bantuan Netlify sebagai Hosting nya dan juga Cloudflare sebagai DNS nya. Cara membuat nya ini cukup mudah, kok, penasaran? Bisa kamu baca artikel ini lebih lanjut :slightly_smilling_face:
---

<style>
article.single img {
    display: block;
    margin: 0 auto;
}
</style>

## **Daftar Isi**
[TOC]

## **I. Pembuka**
Halo, semua! Seperti yang Anda tahu, bahwa blog saya ini merupakan HTML Statis, yang tidak di proses secara dinamis, melainkan ini hanyalah sebuah HTML statis yang di hasilkan dari *Static Site Generator* seperti [Pelican](https://blog.getpelican.com). 

Kamu bisa baca Artikel yang berjudul "[Halo Dunia! (Lagi)]({filename}/articles/2019-08-27-halo-dunia.md)" mengenai Blog yang saya gunakan, beserta hosting nya dan kenapa saya menggunakan nya, dll.

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


### **2. Install Git**
Karena kita akan membuat blog dan menyebarkan nya melalui internet, kita sangat perlu untuk meng-install Git di dalam Komputer kita.

Jika Anda ingin meng-install Git di dalam Komputer Anda, silahkan Anda kunjungi [Artikel tersebut]({filename}/articles/2019-09-17-cara-install-git.md) untuk mengetahui cara Install nya di dalam masing-masing Sistem Operasi.

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
