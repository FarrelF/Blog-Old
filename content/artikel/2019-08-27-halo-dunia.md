Title: Halo Dunia! (Lagi)
Category: Lainnya
Slug: halo-dunia
Status: published
Authors: Farrel Franqois
Summary: Ini adalah Artikel bukan uji-coba yang paling pertama di dalam blog ini. Jadi, yah, kalo mau baca silahkan, kalo gak ya silahkan. Tapi, di dalam artikel ini saya menjelaskan fokus saya kedepan nya untuk blog ini dan juga blog lama saya, jadi saya sarankan untuk di baca, kalo gak ya gak apa-apa, hehe :grinning:

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

Belum lagi Web Browser nya yang terus-menerus membuat Sumber Daya dalam Komputer saya membengkak saat menulis artikel, apalagi kalo kalimat nya banyak.

Dan, itupun dalam menulis (terutama untuk menyimpan Artikel sebagai konsep/draf), saya harus dalam keadaan Online sedangkan Koneksi Internet di saya tidak selalu memadai disini. Serta, saya juga harus menuruti banyak sekali langkah, yang sekira nya itu cukup 'merepotkan' saya.

Jadi, itulah kenapa saya lebih memilih untuk menggunakan *Static Site Generator* seperti Pelican ini bila di bandingkan dengan WordPress.

## Bagaimana dengan CDN nya?
Untuk CDN nya, seperti biasa, saya selalu gunakan CDN dari [Statically](https://statically.io), baik untuk memuat berkas Gambar, Emoji, JS dan CSS di dalam Blog saya ini.

Kenapa pake CDN ini? Agar bisa menghemat *Bandwidth* yang cukup besar, mengingat disini ada Font yang sebesar 2 MB. Meskipun di Netlify memiliki CDN (Artinya, ketika Anda mengakses blog ini, maka sebenarnya Anda mengakses blog ini dari Server Netlify terdekat), namun *Bandwidth* yang di sediakan cukup terbatas, yakni sebesar 100 GB/bulan.

Gede sih batasan nya untuk blog seperti ini, cuma ya kalo bisa di hemat, kenapa tidak? Nah, karena CDN Statically ini gratis dan juga *Bandwidth* nya 'tidak terbatas', maka saya manfaatkan CDN ini untuk memuat berkas yang ada di dalam Repo GitHub saya, terutama berkas statik yang berada di dalam Repo Tema yang sudah saya [Modifikasi](https://github.com/FarrelF/Modified-Flex).

Dengan ini, (harusnya) *Bandwidth* Netlify tidak terpakai sama sekali/tidak terakumulasi, karena saya menggantungkan Asset Blog ini kepada Statically yang mana menghantarkan sebuah berkas dari dalam Repo GitHub, dan itupun dimuat secara eksternal (diluar blog ini). Jadi, lalu lintas bisa sedikit di perhemat :slightly_smiling_face:

Saya mempunyai Akun BunnyCDN, cuma saya gak implementasikan disini, mengingat mungkin kedepan nya saya akan terus menggunakan CDN Statically daripada BunnyCDN, karena disitu fiturnya lebih lengkap, meski gak ada Custom Domain :slightly_smiling_face:

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

Dengan syarat, pastikan kamu memberikan "kebebasan" yang sama dengan "kebebasan" yang ada di blog ini pada turunan yang Anda buat. Untuk lebih lengkapnya, silahkan baca Laman [Lisensi](https://farrel.franqois.id/lisensi). Kamu juga bisa memperoleh kode sumber nya, caranya bisa kamu kunjungi laman [Kode Sumber](https://farrel.franqois.id/kode-sumber)

## Penutup
Jadi, sudah dulu yah, saya juga mau fokus merombak blog ini terlebih dahulu, dibandingkan dengan menulis artikel. Seperti yang Anda tahu, blog ini sangat 'jauh' sekali dari kata "lengkap", seperti ada halaman yang dalam masih di buat/di draf, dan lain sebagai nya.

Terima kasih atas perhatian nya :blush: