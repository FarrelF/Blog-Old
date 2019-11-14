---
Title: Cara menggunakan LibreOffice dengan "Benar"
Category: Tutorial, Opini
Author: Farrel Franqois
Tags: Cara menggunakan, LibreOffice, Windows, GNU/Linux
Slug: cara-menggunakan-libreoffice
Cover: https://cdn.statically.io/gl/FarrelF/blog-images/35ac221f/cara-menggunakan-libreoffice/LibreOffice-External-Logo.png?fit=437,130&quality=80
Cover_Width: 437
Cover_Height: 130
description: Apakah Anda merasa kesulitan saat menggunakan LibreOffice? Terutama untuk masalah kompatibilitas yang seringkali Anda jumpai? Mau tau cara menggunakan LibreOffice dengan "Benar"? Silahkan baca Artikel ini.
Summary: Banyak sekali pengguna LibreOffice yang merasa kesulitan dalam menggunakan nya, seperti dokumen nya yang berantakan saat di buka dengan Microsoft Office, masalah kompatibilitas dan masalah lain nya. Artikel ini akan membahas hal-hal dasar yang harus di lakukan ketika Anda menggunakan LibreOffice dengan "Benar", dan saya bahas pada bagian yang paling "dasar" nya saja, yang mana ini tidak banyak di ketahui oleh banyak orang. Penasaran? Silahkan baca artikel ini, kalau tidak, yah tidak apa-apa :slightly_smiling_face:
---

## Daftar Isi
[TOC]

## Pembuka
LibreOffice merupakan sebuah Perangkat Lunak Paket Perkantoran yang merupakan Perangkat Lunak Bebas/FLOSS (Free/Libre Open Source Software) dan juga bisa di peroleh secara gratis. Biasanya Perangkat Lunak ini bisa menjadi alternatif, bahkan menggantikan Microsoft Office itu sendiri. Perangkat Lunak ini di kembangkan oleh sebuah organisasi nirlaba, yakni: [The Document Foundation (TDF)](https://www.documentfoundation.org/) dan sejumlah kontributor lain nya.

Perangkat Lunak ini cukup populer, terutama di kalangan pengguna GNU/Linux. Salah satu alasannya adalah karena Distribusi GNU/Linux yang mereka gunakan itu biasanya sudah ter-install LibreOffice secara bawaan (_default_). Ubuntu, Varian (Seperti: Xubuntu, Lubuntu, Kubuntu, Ubuntu MATE, dll) dan Turunan nya (seperti Mint, Pop_OS!, dll) merupakan salah satu contoh nya.

Namun sayangnya, banyak sekali dari mereka yang mengeluhkan yang seharusnya tidak perlu di keluhkan, apa saja masalah nya? Mungkin, bisa Anda lanjut simak artikel ini.

Oh, iya, sebelum itu, ada yang ingin saya sampaikan, bahwa Artikel ini akan membahas hal-hal yang sangatlah mendasar untuk menggunakan LibreOffice. 

Jadi, artikel ini tidak akan membahas penggunaan LibreOffice lebih lanjut. Dan, maksud "Benar" disini berarti benar secara penggunaan, bukan pada keseluruhan isi artikel ini. Silahkan kamu baca Laman ['Ketentuan Hukum dan Sanggahan']({filename}/pages/ketentuan-hukum-dan-sanggahan.md) untuk lebih lanjut.

## I. Masalah Kompatibilitas saat di buka dengan Microsoft Office (begitupun juga sebaliknya)
Ini adalah masalah paling klasik yang paling sering di bicarakan oleh salah satu/kebanyakan anggota dari banyaknya komunitas GNU/Linux di dunia maya (terutama di Indonesia). 

Hal ini terjadi ketika pengguna menyelesaikan pembuatan Dokumen (entah itu sekedar Dokumen biasa, Lembar Kerja (_Spreadsheet_), Presentasi, dll), setelah itu ia simpan dokumen nya menggunakan Format OOXML (Office Open XML Format), ini artinya mereka menyimpan nya dengan ekstensi DOCX atau DOC, XLSX atau XLS, PPTX atau PPT, dan Ekstensi dengan format OOXML lain nya.

Ketika mereka ingin membuka Dokumen nya dengan Microsoft Office, tentunya dengan ekspektasi bahwa dokumen tersebut harusnya bisa di 'render' dengan baik, yang artinya, dokumen tersebut harusnya tampil dengan tampilan yang 'seharusnya'. Namun ternyata, dokumen yang di tampilkan malah berantakan, dan tentu saja itu jauh (bahkan 'sangat jauh') dari ekspektasi si pengguna tersebut.

Masalah di atas merupakan salah satu contoh dari Masalah Kompatibilitas saat dokumen di buka dengan Microsoft Office, dan ini bisa terjadi sebaliknya (Dokumen di buat dengan Microsoft Office, dan di buka dengan LibreOffice). Masih ada sebenarnya yang mirip dengan ini, cuma lebih baik saya bahas satu ini saja.

> Kenapa hal itu bisa terjadi?

Alasan nya sederhana, karena LibreOffice sendiri memfokuskan penggunaan format ODF (OpenDocument Format) daripada OOXML (Office Open XML) sebagai format Dokumen bawaan dan format asli (_native_) nya.

> Kenapa mereka memfokuskan format ODF sebagai format bawaan nya? Dan, kenapa mereka tidak memfokuskan format OOXML saja? Bukan nya OOXML ini termasuk "Open Format"?

Karena Format OOXML itu selalu berubah dan bersifat tidak konsisten seiring berjalan nya waktu dan perubahan versi, serta spesifikasi dari OOXML itu sendiri dan juga Implementasi OOXML di Microsoft Office itu berbeda, sehingga akan menimbulkan inkompatibilitas pada Format itu sendiri dan akan membuat Pengembang Perangkat Lunak Bebas/FLOSS seperti LibreOffice, bahkan Perangkat Lunak lain nya seperti WPS, FreeOffice, dan lain nya akan mengalami kesulitan untuk memenuhi standar dari Format OOXML itu sendiri. 

Ketidakkonsistenan ini menyebabkan masalah bagi pengembang Perangkat Lunak Perkantoran lain nya (terutama Perangkat Lunak Bebas), termasuk:

- Metadata yang hilang.
- Kesalahan saat menampilkan Grafis dan Objek tertanam lain nya di hasil akhir.
- Format ini memerlukan penautan yang tertanam ke teknologi atau fitur yang di kendalikan atau/dan hanya bisa di gunakan secara eksklusif oleh Vendor tertentu/Perangkat Lunak tertentu (Seperti: SmartArt, PivotTable, dll).
- Dan, masalah lain nya.

Masalah ini bukan hanya mempengaruhi pengembang Perangkat Lunak saja, tapi itu akan mempengaruhi pengguna nya secara keseluruhan, terutama jika pengguna tersebut membuka dokumen di Perangkat Lunak (bahkan termasuk Microsoft Office) versi Lama.

Sehingga, Perangkat Lunak yang bisa meng-implementasikan nya dengan paling baik dan yang paling mengikuti/memenuhi standar dalam Format OOXML adalah Microsoft Office itu sendiri, itupun jika menggunakan versi terbaru nya, tanpa kecuali.

Selain alasan di atas, Alasan mereka hanya fokus (bahkan mempromosikan) format ODF adalah karena mereka percaya bahwa tidak ada standar/format dokumen lain yang menawarkan tingkat netralitas terhadap vendor dengan tepat. Dan, mereka juga percaya bahwa format tersebut akan bermanfaat untuk semua orang kedepan nya.

Jadi, jika OOXML di nyatakan sebagai "Open Format", apakah artinya OOXML ini termasuk Standar Terbuka (_Open Standard_) atau bebas? Seperti nya belum tentu juga :slightly_smiling_face:

> Lalu, apa solusi nya?

Solusinya mudah, tinggalkan dan jangan gunakan format OOXML di dalam LibreOffice. Bagaimana caranya? Caranya adalah, ketika Anda sudah selesai membuat Dokumen nya, simpanlah dokumen tersebut sebagai Ekstensi yang berformat ODF, seperti .ODT (untuk LibreOffice Writer), .ODS untuk (LibreOffice Calc), dan .ODP (untuk LibreOffice Impress), daripada ekstensi dengan format OOXML seperti .DOC, .DOCX, .XLS, .XLSX, .PPT, .PPTX dan ekstensi dengan format OOXML lain nya.
