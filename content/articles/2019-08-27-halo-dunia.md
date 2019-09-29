---
Title: Halo Dunia! (Lagi)
Category: Lainnya
Slug: halo-dunia
Status: published
Authors: Farrel Franqois
Summary: Ini adalah Artikel bukan uji-coba yang paling pertama di dalam blog ini. Jadi, kalo mau baca silahkan, kalo gak yah silahkan. Tapi, di dalam artikel ini saya menjelaskan fokus saya kedepan nya untuk blog ini dan juga blog lama saya, jadi saya sarankan untuk di baca, kalo gak ya gak apa-apa, hehe :grinning:
---

<style>
    article.single p {
        text-align: justify;
    }
</style>

## Daftar Isi
[TOC]

## Pembuka
Halo Dunia! (Lagi. "Eh, emang pernah, yah?"), ini adalah artikel pertama yang bukan merupakan artikel uji coba.

Sudah lama sekali saya tidak pernah menulis artikel di dalam blog saya. Tapi, mulai sekarang ini, saya akan lebih fokus dalam penggunaan *Static Site Generator* bila di bandingkan dengan menggunakan WordPress untuk mengelola Blog saya ini.

Seperti yang Anda tahu, bahwa Blog ini merupakan sebuah berkas HTML Statis, yang di hasilkan melalui [Pelican](https://blog.getpelican.org) yang bertindak sebagai *Static Site Generator*.

Jadi, blog ini di tenagai oleh 'Pelican'. Ehh, tapi bukan oleh [Burung 'Pelican'](https://www.google.com/search?q=burung+pelikan&tbm=isch), yah, hehe :grinning:

## Hosting yang saya gunakan
Untuk hosting nya, saya gunakan [Netlify](https://www.netlify.com/) sebagai pengganti dari Web Hosting, agar saya bisa menghemat biaya yang cukup banyak, karena tidak perlu lagi bayar perbulan nya (Saya harap ini bertahan sampai seterusnya). Palingan, saya cuma perlu bayar domain saya saja.

Selain menghemat biaya, dengan memanfaatkan *Static Site Generator* ini, saya hanya perlu menggunakan Editor Teks/Kode untuk menulis Artikel, yang sebelumnya pada WordPress saya harus membuka Web Browser terlebih dahulu.

Belum lagi Web Browser nya yang terus-menerus membuat Kinerja Sumber Daya dalam Komputer saya membengkak saat menulis artikel, apalagi kalo kalimat nya banyak.

Dan, itupun dalam menulis (terutama untuk menyimpan Artikel sebagai konsep/draf), saya harus dalam keadaan Online sedangkan Koneksi Internet di saya tidak selalu memadai disini. Serta, saya juga harus menuruti banyak sekali langkah, yang sekira nya itu cukup 'merepotkan' saya.

Serta, hal ini dapat meminimalisir kesalahan 503 Internal Server Error atau Gangguan Server lain nya saat menulis Artikel/Laman, karena untuk menulis dan menyimpan nya gak harus menggunakan koneksi Internet.

Jadi, itulah kenapa saya lebih memilih untuk menggunakan *Static Site Generator* seperti Pelican ini bila di bandingkan dengan WordPress.

## Kenapa memilih Netlify daripada Layanan Sejenis seperti Zeit?
Karena di Netlify saya di berikan kemudahan untuk men-_deploy_ Blog dan Konten nya dari Kode Sumber. 

Di tambah, ada beberapa referensi untuk men-_deploy_ Pelican dengan Netlify di Google daripada menggunakan Layanan Sejenis lain nya seperti [Zeit](https://zeit.co) dan (mungkin) [Commons Host](https://commons.host).

Saya kira itu saja alasan nya, atau mungkin saya kurang mempelajari Layanan Sejenis lain nya.

Oh, iya, saya bisa membangun sebuah blog berbasis Pelican dan men-_deploy_ nya menggunakan Netlify, itu berkat referensi dari [sini](https://www.edwinksl.com/blog/set-up-website-with-pelican-google-domains-and-netlify.html).

## Bagaimana dengan CDN nya?
Untuk CDN nya, seperti biasa, saya selalu gunakan CDN dari [Statically](https://statically.io), baik untuk memuat berkas Gambar, Emoji, JS dan CSS di dalam Blog saya ini.

Kenapa pake CDN ini? Agar bisa menghemat *Bandwidth* yang cukup besar, mengingat disini ada Font yang sebesar lebih dari 2 MB. Meskipun di Netlify memiliki CDN (Artinya, ketika Anda mengakses blog ini, maka sebenarnya Anda mengakses blog ini dari Server Netlify terdekat), namun *Bandwidth* yang di sediakan cukup terbatas, yakni sebesar 100 GB/bulan.

Gede sih batasan nya untuk blog seperti ini, cuma ya kalo bisa di hemat, kenapa tidak? Nah, karena CDN Statically ini gratis dan juga *Bandwidth* nya 'tidak terbatas', maka saya manfaatkan CDN ini untuk memuat berkas yang ada di dalam Repo GitHub saya, terutama berkas statik yang berada di dalam Repo Tema yang sudah saya [Modifikasi](https://github.com/FarrelF/Modified-Flex).

Dengan ini, (harusnya) *Bandwidth* Netlify tidak terpakai sama sekali/tidak terakumulasi, karena saya menggantungkan Asset Blog ini kepada Statically yang mana menghantarkan sebuah berkas dari dalam Repo GitHub, dan itupun dimuat secara eksternal (diluar blog ini). Jadi, lalu lintas bisa sedikit di perhemat :slightly_smiling_face:

Saya mempunyai Akun [BunnyCDN](https://bunnycdn.com), cuma saya gak implementasikan disini, mengingat mungkin kedepan nya saya akan terus menggunakan CDN Statically daripada BunnyCDN, karena saya lebih nyaman disitu, meski gak ada fitur Custom Domain dan kurang lengkap (karena Statically merupakan Layanan *Public CDN*) :slightly_smiling_face:

## Apa Fokus kedepan nya?
Karena saya lebih suka penggunaan *Static Site Generator* bila dibandingkan dengan menggunakan WordPress untuk keperluan Blogging, seperti yang saya bilang tadi.

Jadi, bisa kamu tebak dong jawaban nya seperti apa? Yap! Saya akan lebih fokus untuk menulis disini, daripada di [blog lama](https://farrelf.wpinter.com) saya yang berbasis WordPress. Jadi, blog lama saya berhentikan, alias udah gak saya urus lagi.

Sudah saya bahas alasan nya di bagian "[Hosting yang saya gunakan](#hosting-yang-saya-gunakan)", jadi saya kira alasan nya sudah jelas :slightly_smiling_face:

Tapi, sebelum saya menulis artikel lagi, mungkin saya akan fokus untuk merombak blog sedikit terlebih dahulu, mengingat ini jauh sekali dari kata 'lengkap', seperti ada Laman yang kosong, Mesin Pencarian juga tidak ada, begitu pula dengan Analitik nya, dan fitur-fitur lain nya.

## Lalu, bagaimana dengan Blog lama nya? Apakah ada niatan untuk menyalinkan artikel lama kesini?
Memang saya memiliki beberapa artikel di dalam blog yang lama. Tapi, sayangnya, saya tidak berniat untuk menyalinkan semua artikel yang berada di blog lama saya ke dalam blog ini.

Alias, saya tidak pernah berniat untuk bermigrasi, karena migrasi dari *Platform* lama itu membuang pikiran, tenaga dan waktu saya. Jadi, saya tidak berpikir untuk melakukan nya, lebih baik seperti ini saja.

Karena semua itu, akhirnya blog ini saya mulai dari awal lagi, ini bukan berarti blog yang lama nya saya hapus, yah, kamu masih bisa mengakses nya [disini](https://farrelf.wpinter.com).

Oh, ya, untuk sekarang ini, blog saya ini saya "Bebaskan", baik konten nya ataupun Kode Sumber nya. Tentu saja "Bebaskan" yang saya maksud itu adalah memberikan Anda "kebebasan".

Nah, "kebebasan" yang saya maksud/beri disini adalah "kebebasan" untuk menggunakan nya, mempelajari, memodifikasi, menyalinkan dan mendistribusikan ulang terutama kepada Keluarga, Tetangga, Teman atau Rekan, untuk keperluan apapun termasuk keperluan komersial sekalipun, sesuai dengan [filosofi Perangkat Lunak Bebas](https://www.gnu.org/philosophy/free-sw.html.en).

Dengan syarat, pastikan kamu memberikan "kebebasan" yang sama dengan "kebebasan" yang ada di blog ini pada turunan yang Anda buat. Untuk lebih lengkapnya, silahkan baca Laman [Lisensi]({filename}/halaman/lisensi.md). Kamu juga bisa memperoleh kode sumber nya, caranya bisa kamu kunjungi laman [Kode Sumber]({filename}/halaman/kode-sumber.md)

## Rangkuman/Kesimpulan
Jika Anda merasa bahwa artikel ini kepanjangan atau sulit untuk di baca, maka saya akan merangkum isi artikel ini menjadi sebuah kesimpulan, dalam format yang mudah dibaca oleh Anda. Berikut rangkuman nya:

1. Blog ini, artikel serta laman nya merupakan Berkas HTML Statis yang di hasilkan menggunakan *Static Site Generator* (atau di singkat "SSG") seperti [Pelican](https://blog.getpelican.com). Iya, jadi saya menggunakan/memanfaatkan SSG untuk menulis dan mengubah artikel/laman di dalam blog ini. Alasan nya:

    - Saya merasa jauh lebih nyaman dalam menulis artikel dengan memanfaatkan Editor Teks/Kode di bandingkan dengan lewat Web Browser dengan Editor WYSIWYG (*What You See Is What You Get*) nya.

    - Untuk menulis atau/dan mengubah Artikel/Laman, gak harus terkoneksi dengan Internet (Dalam keadaan Offline). Kecuali, jika menerbitkan Artikel di dalam Blog dan men-_deploy_ nya, itu memerlukan koneksi Internet, hanya saja lebih 'ramah' untuk pengguna Internet seperti saya (Karena penggunaan Git).

    - Langkah-langkah menulis artikel/laman menjadi lebih 'sederhana' dibandingkan dengan menulisnya melalui WordPress, yang cenderung lebih 'merepotkan'. Contohnya: Saya buka Web Browser -> Masuk ke dalam Admin WordPress (`wp-admin`) -> Login dengan menggunakan Akun yang saya punya -> Masuk ke Dasbor -> Klik pada "Pos", dan langkah-langkah lain nya untuk menulis sebuah artikel/laman saja.

    - Saat saya menulis artikel/laman dengan WordPress, Komputer/Laptop saya terkadang seringkali mengalami 'pembengkakan' kinerja, terutama pada bagian penggunaan Sumber Daya (seperti: CPU, RAM, dll.) seiring lamanya atau banyaknya kalimat di dalam artikel/laman yang saya tulis di dalam Editor.

    - Meminimalisir kesalahan 503 (*Internal Server Error*, baik karena Salah konfigurasi sampai Server Hosting) dan juga segala Gangguan dari Server Hosting saat menulis artikel. Karena saya menulisnya di dalam Editor, gak harus Online juga, hehe :grinning:

2. Blog ini juga menggunakan Netlify sebagai Hosting nya. Alasan kenapa saya menggunakan nya sebagai berikut:

    - Karena Gratis, sehingga tidak perlu bayar hosting/server per bulan/tahun nya (Kecuali Domain). Sehingga ini akan sangat menghemat biaya untuk orang seperti saya :slightly_smiling_face:

    - Secara Default, Netlify menggunakan CDN (Atau, lebih tepatnya 'ADN' yang merupakan kepanjangan dari 'Application Delivery Network'), sehingga dapat meminimalisir lambatnya akses ketika pertama kali di buka. Gratis pula.

    - Gagal Update Blog karena perbedaan Koneksi Jaringan Internet antara Server Hosting dan Server lain nya dapat di minimalisir.

    - Terintegrasi dengan GitHub, GitLab dan Bitbucket.

    - Selain itu semua, alasan saya memilih Netlify sebagai Hosting di bandingkan dengan layanan sejenis, seperti [Zeit](https://zeit.co) itu karena kemudahan nya dalam men-_deploy_ Blog Statis dari [Kode Sumber](https://github.com/FarrelF/FarrelF-Blog).

3. Meskipun Netlify menggunakan CDN pada Jaringan nya, Blog ini juga masih menggunakan Layanan CDN Umum seperti [Statically](https://statically.io) untuk memuat berkas statis lain nya. Alasan nya:

    - Karena Gratis dan memiliki *Bandwidth* yang 'tidak terbatas'. Sehingga, ini dapat menghemat *Bandwidth* Netlify yang di batasi hingga 100 GB/Bulan untuk paket Gratis nya.

    - Memiliki Infrastruktur Multi-CDN, yang artinya Statically memiliki 4 CDN di dalam nya. Seperti: BunnyCDN, Cloudflare, CDN77 dan Fastly.

    - Gambar-gambar sudah langsung di optimasi ketika dimuatkan. Sehingga, ini memudahkan saya untuk mengoptimasi gambar tanpa harus terlalu menggantungkan nya kepada pihak ke-3 lain nya.

    - Lamanya Penyimpanan Tembolok (Cache) dan Integritas berkas di dalam Tembolok itu ditentukan berdasarkan *Branch*, *Tag* atau *Commit* yang ada pada *Repository* Git. Sehingga, ketika saya ingin menggantikan gambar di dalam artikel, saya cukup unggah gambarnya kedalam *Repository* Git, lalu saya ganti *Commit* nya saja, tidak perlu sampai menggunakan fitur *Purge Cache*, bahkan menggantikan nama berkas.

4. Dengan semua alasan ini, maka untuk kedepan nya, saya akan fokus untuk Blogging dengan memanfaatkan SSG dibandingkan dengan menggunakan WordPress. Jadi, imbasnya, blog lama udah gak saya urus lagi, meski Blog lama [masih ada](https://farrelf.wpinter.com) dan gak akan saya hapus.

5. Tapi, saya tidak berniat untuk memigrasikan dari Blog lama ke blog baru ini, karena membuang waktu, pikiran dan juga tenaga. Sehingga, saya ingin memulai nya dari awal lagi.

6. Saya juga memberikan Anda kebebasan untuk menggunakan, mempelajari, menyalinkan, mendistribusi kan ulang, dan juga memodifikasi nya dengan keperluan apapun, termasuk komersial sekalipun, baik untuk konten nya, dan juga [kode sumber nya](https://github.com/FarrelF/FarrelF-Blog). Tapi, jangan lupa untuk sertakan kredit dan atribusi nya serta memberikan 'hak' yang sama dengan yang ada di blog ini. Untuk lebih lanjut, silahkan lihat/baca laman [Lisensi]({filename}/halaman/lisensi.md).

## Penutup
Jadi, sudah dulu yah, saya juga mau fokus merombak blog ini terlebih dahulu, dibandingkan dengan menulis artikel. Seperti yang Anda tahu, blog ini sangat 'jauh' sekali dari kata "lengkap", seperti ada halaman yang dalam masih di buat/di draf, dan lain sebagai nya.

Terima kasih atas perhatian nya :blush: