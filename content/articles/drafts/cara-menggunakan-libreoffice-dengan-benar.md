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

<style>
main article blockquote, main article h3 {
    font-size: 1.17em;
}
</style>

## Daftar Isi
[TOC]

## Pembuka
LibreOffice merupakan sebuah Perangkat Lunak Paket Perkantoran yang merupakan Perangkat Lunak Bebas/FLOSS (Free/Libre Open Source Software) dan juga bisa di peroleh secara gratis. Biasanya Perangkat Lunak ini bisa menjadi alternatif, bahkan menggantikan Microsoft Office itu sendiri. Perangkat Lunak ini di kembangkan oleh sebuah organisasi nirlaba, yakni: [The Document Foundation (TDF)](https://www.documentfoundation.org/) dan sejumlah kontributor lain nya.

Perangkat Lunak ini cukup populer, terutama di kalangan pengguna GNU/Linux. Salah satu alasannya adalah karena Distribusi GNU/Linux yang mereka gunakan itu biasanya sudah ter-install LibreOffice secara bawaan (_default_). Ubuntu, Varian (Seperti: Xubuntu, Lubuntu, Kubuntu, Ubuntu MATE, dll) dan Turunan nya (seperti Mint, Pop_OS!, dll) merupakan salah satu contoh nya.

Namun sayangnya, banyak sekali dari mereka yang mengeluhkan yang seharusnya tidak perlu di keluhkan, apa saja masalah nya? Mungkin, bisa Anda lanjut simak artikel ini.

## Sanggahan
Tapi sebelum itu, ada yang ingin saya sampaikan, bahwa Artikel ini akan membahas hal-hal yang sangatlah mendasar untuk menggunakan LibreOffice. 

Jadi, artikel ini tidak akan membahas penggunaan LibreOffice lebih lanjut. Dan, maksud "Benar" disini berarti benar secara penggunaan, bukan pada keseluruhan isi artikel ini. 

Perlu saya ingatkan juga, bahwa kemungkinan Artikel ini akan menyinggung salah satu Produk dari Microsoft dan format nya, saya tidak bermaksud dan tidak ada perasaan untuk membenci terhadap Microsoft dan segala produk-produk nya, serta saya juga bukanlah seorang yang meng-Anti kan nya. 

Tapi, yang saya bahas ini merupakan penjelasan dan kenyataan nya saja, yang berdasarkan dari pengalaman seseorang/saya, dan referensi-referensi yang telah saya ambil dari beberapa situs web, baik dari luar Situs Web Microsoft, bahkan dari Situs Microsoft itu sendiri.

Pernyataan di atas merupakan pernyataan tambahan dari yang [sebenarnya]({filename}/pages/ketentuan-hukum-dan-sanggahan.md).

## I. Masalah Kompatibilitas saat di buka dengan Microsoft Office (begitupun juga sebaliknya)
Ini adalah masalah paling klasik yang paling sering di bicarakan oleh kebanyakan pengguna GNU/Linux di Indonesia, berdasarkan dari banyaknya komunitas GNU/Linux di dunia maya (terutama di Indonesia). 

Hal ini terjadi ketika pengguna menyelesaikan pembuatan Dokumen (entah itu sekedar Dokumen biasa, Lembar Kerja (_Spreadsheet_), Presentasi, dll), setelah itu ia simpan dokumen nya menggunakan Format OOXML (Office Open XML Format), ini artinya mereka menyimpan nya dengan ekstensi DOCX atau DOC, XLSX atau XLS, PPTX atau PPT, dan Ekstensi dengan format OOXML lain nya.

Ketika mereka ingin membuka Dokumen nya dengan Microsoft Office, tentunya dengan ekspektasi bahwa dokumen tersebut harusnya bisa di 'render' dengan baik, yang artinya, dokumen tersebut harusnya tampil dengan tampilan yang 'seharusnya'. Namun ternyata, dokumen yang di tampilkan malah berantakan, dan tentu saja itu jauh (bahkan 'sangat jauh') dari ekspektasi si pengguna tersebut.

Masalah di atas merupakan salah satu contoh dari Masalah Kompatibilitas saat dokumen di buka dengan Microsoft Office, dan ini bisa terjadi sebaliknya (Dokumen di buat dengan Microsoft Office, dan di buka dengan LibreOffice). Masih ada sebenarnya yang mirip dengan ini, cuma lebih baik saya bahas satu ini saja.

> ### Kenapa hal itu bisa terjadi?

Alasan nya sederhana, karena LibreOffice sendiri memfokuskan penggunaan format ODF (OpenDocument Format) daripada OOXML (Office Open XML) sebagai format Dokumen bawaan dan format asli (_native_) nya.

Jadi, masalah seperti ini sebenarnya tidak perlu di keluhkan, bahkan sama sekali.

> ### Kenapa mereka memfokuskan format ODF sebagai format bawaan nya? Dan, kenapa mereka tidak memfokuskan format OOXML saja? Bukan nya OOXML ini termasuk "Open Format"?

Karena Format OOXML itu [bersifat tidak konsisten](https://joinup.ec.europa.eu/collection/open-source-observatory-osor/document/complex-singularity-versus-openness), hal ini terjadi karena spesifikasi dari OOXML itu sendiri dan juga Implementasi nya di Microsoft Office [itu berbeda](https://brattahlid.wordpress.com/2012/05/08/is-docx-really-an-open-standard/). 

Perlu Anda ketahui, bahwa di dalam Format OOXML itu memiliki 3 versi (atau sub-standar), diantara nya adalah: 

- Versi ECMA-376 (atau di sebut "Versi ECMA")
- ISO/IEC 29500 Transitional (atau di sebut "Versi Transitional")
- ISO/IEC 29500 Strict (atau di sebut "Versi Strict")

Nah, yang jadi masalah nya adalah, Spesifikasi untuk Sub-Standar 'Transitional' dan 'Strict' itu tertutup dan tidak di publikasikan, serta berdasarkan dari Laman [Wikipedia nya](wikipedia_en>Office_Open_XML), bahwa Microsoft Office hanya mendukung baca/tulis untuk dokumen yang di buat dengan Versi 'Transitional' saja, dan dokumen yang di buat dengan Versi 'Strict' hanya bisa di baca pada Microsoft Office 2010, serta bisa baca/tulis pada Microsoft Office 2013 dan 2016, itupun sebagai ['tambahan'](https://technet.microsoft.com/en-us/library/cc179191%28v=office.15%29.aspx).

Selain itu, dokumen dengan versi ECMA hanya bisa di baca saja. 

Jadi, ini artinya, ketika Anda menyimpan dokumen dari Microsoft Office (terutama dengan ekstensi yang berformat OOXML), maka Anda menyimpan dokumen nya bukan sebagai "Office Open XML" yang selama ini "di iklankan" sebagai "Format Terbuka".

Sedangkan, kebanyakan Perangkat Lunak Perkantoran lain nya hanya mampu meng-implementasi Versi ECMA dari Format OOXML nya saja (itupun belum tentu sepenuhnya), yang artinya, jika Anda menyimpan nya sebagai ekstensi dengan format OOXML di Perangkat Lunak Perkantoran selain Microsoft Office, maka yang Anda simpan itu adalah versi ECMA dari OOXML nya.

Selain itu, format ini memiliki beberapa masalah ketika di implementasikan oleh Perangkat Lunak Perkantoran selain Microsoft Office.

Sehingga, ini akan membuat Pengembang Perangkat Lunak Bebas/FLOSS seperti LibreOffice, bahkan Perangkat Lunak lain nya seperti WPS Office, Softmaker FreeOffice, dan lain nya akan mengalami kesulitan untuk memenuhi standar dari Format OOXML itu sendiri. 

Masalah-masalah nya seperti:

- Memerlukan penautan/penghubungan ke teknologi atau fitur yang di kendalikan atau/dan hanya bisa di gunakan secara eksklusif oleh Vendor/Perangkat Lunak tertentu (Seperti: SmartArt, PivotTable, dll).

- Jumlah Halaman dari Dokumen Spesifikasi nya sendiri nya mencapai [&pm;6000 halaman](https://www.ecma-international.org/publications/standards/Ecma-376.htm), yang bahkan itu melebihi POSIX/SUSv3 yang cuma sampai [&pm;3700 halaman saja](wikipedia_en>Single_UNIX_Specification). Dan, itupun untuk versi ECMA nya, belum 'Transitional' dan 'Strict' nya. Sehingga, hal itu akan menyulitkan Pengembang Perangkat Lunak lain nya untuk meng-implementasikan format tersebut.

- Format OOXML itu sendiri telah terbebani oleh [Paten](http://noooxml.wikidot.com/patents) [Perangkat Lunak](http://en.swpat.org/wiki/OOXML), sehingga hal itu akan membuat Pengembang Perangkat Lunak perkantoran lain nya menjadi tidak mungkin untuk menyempurnakan dukungan/implementasi format OOXML nya.

- Dan, masalah lain nya.

Masalah-masalah di atas bukan hanya mempengaruhi pengembang Perangkat Lunak saja, tapi itu akan mempengaruhi pengguna nya secara keseluruhan, terutama jika pengguna tersebut membuka atau membuat dokumen ber-format OOXML dengan Perangkat Lunak Perkantoran selain Microsoft Office.

Sehingga, Perangkat Lunak Perkantoran yang paling bisa meng-implementasikan nya dan yang paling mengikuti/memenuhi standar dalam Format OOXML adalah Microsoft Office itu sendiri.

Selain alasan di atas, Alasan mereka hanya fokus (bahkan [mempromosikan](https://wiki.documentfoundation.org/LibreOffice_OOXML#Does_The_Document_Foundation_support_OOXML_.3F)) format ODF adalah karena mereka percaya bahwa tidak ada standar/format dokumen lain yang menawarkan tingkat netralitas terhadap vendor dengan tepat. Dan, mereka juga percaya bahwa format tersebut akan bermanfaat untuk semua orang kedepan nya.

Ini artinya, mereka percaya bahwa ODF merupakan format yang paling 'netral' saat ini, bila di bandingkan dengan format OOXML.

Jika OOXML di nyatakan sebagai "Open Format", apakah artinya OOXML ini termasuk Standar Terbuka (_Open Standard_) atau bebas? Seperti nya belum tentu juga.

Jadi, apakah itu merupakan suatu hal yang wajar jika tampilan atau bahkan dokumen nya menjadi kacau saat dokumen OOXML di buat atau/dan di buka dengan Perangkat Lunak selain Microsoft Office? Wajar, bahkan normal jika itu terjadi, kecuali jika Anda cuma tahu Microsoft Office atau/dan Ekstensi berformat OOXML nya saja. 

Bagaimana kalau dokumen nya tidak menjadi kacau, atau tampilan nya sangat baik, bahkan "sempurna"? Itu artinya, "Anda beruntung!" :slightly_smiling_face:

Mau Referensi lain nya? Silahkan klik salah satu tautan berikut:

- Salah satu artikel yang di tulis oleh Kang Ade Malsasa Akbar (dalam Bahasa Inggris): ["Support Open Document Format | Dreambox"](https://linuxdreambox.wordpress.com/2016/01/10/support-open-document-format/)

- [MS-OOXML - Overview | Free Software Foundation Europe (FSFE)](https://fsfe.org/activities/os/msooxml.html)

- [What's in a label? ODF vs. OOXML and Open Standards | Open Source Initiative](https://opensource.org/node/266)

- [We Can Put an End to Word Attachments - GNU Project](https://www.gnu.org/philosophy/no-word-attachments.html)

- [Reject proprietary formats! Pledge to use OpenDocument! — Free Software Foundation](https://www.fsf.org/campaigns/opendocument/reject)

- [Why you should not use Microsoft Office! | TLFR.io](https://www.tfir.io/never-use-microsofts-ooxml-pseudo-standard-format/)

> ### Lalu, apa solusi nya?

Solusinya mudah, tinggalkan dan jangan pernah gunakan format OOXML di dalam LibreOffice untuk membuat dokumen Anda. 

Lalu, bagaimana caranya? Caranya adalah, ketika Anda sudah selesai membuat Dokumen nya, simpanlah dokumen tersebut sebagai Ekstensi yang berformat ODF, seperti .ODT (untuk LibreOffice Writer), .ODS untuk (LibreOffice Calc), dan .ODP (untuk LibreOffice Impress), daripada ekstensi yang berformat OOXML seperti .DOC, .DOCX, .XLS, .XLSX, .PPT, .PPTX dan ekstensi dengan format OOXML lain nya.

Terakhir, jangan pernah mengharapkan kalau LibreOffice bisa membuka dokumen dengan format OOXML sebaik Microsoft Office.

> ### Bagaimana jika saya berada di Rental Komputer/Warung Internet suatu saat nanti?

LibreOffice mendukung Sistem Operasi Windows, jadi ia bisa di install di Sistem Operasi Windows. Jika tidak mungkin bisa di install (Entah itu karena terkendala izin Administrator sampai tidak ada waktu atau terlalu repot), LibreOffice juga telah menyediakan versi Portabel nya agar LibreOffice bisa di jalankan secara langsung di dalam USB tanpa izin terlebih dahulu ke Administrator. 

Ini akan sangat membantu Anda yang sedang menggunakan Komputer yang mana Anda tidak dapat menggunakan Izin Administrator atau bagi Anda yang tidak ingin repot-repot atau membuang-buang waktu serta tenaga untuk meng-install LibreOffice di Komputer lain, seperti di Warnet, Rental Komputer, Komputer Lab Sekolah/Kampus, Komputer Kantor, dll nya.

> ### Bagaimana jika saya membuka berkas OOXML di LibreOffice?

Sudah saya bilang sebelumnya, bahwa lebih baik Anda tidak terlalu berharap untuk bisa membuka berkas yang berformat OOXML di LibreOffice sebaik Microsoft Office. Namun, Anda bisa saja membuka nya, hanya saja hasilnya nanti tidak sebaik Microsoft Office, karena fitur-fitur yang ada/digunakan pada dokumen tersebut belum tentu dapat di 'render' dengan baik oleh LibreOffice, karena masalah format OOXML itu sendiri.

Meskipun artikel ini menyinggung Microsoft Office dan Format OOXML nya, bukan berarti saya melarang Anda untuk menggunakan kedua nya. 

Anda bisa menggunakan Microsoft Office untuk membuka berkas berformat OOXML, atau jika Anda tidak mempunyai Microsoft Office nya (Entah itu sengaja gak di install atau gak bisa di Install karena sebab lain), Anda bisa menggunakan Perangkat Lunak Perkantoran lain nya selain Microsoft Office, seperti WPS Office, Softmaker FreeOffice, dll.

Atau, jika hal tersebut tidak memungkinkan, maka sebaiknya Anda minta saja kepada pengirimnya untuk mengirimkan ulang berkas sebagai Format PDF jika Anda hanya ingin membacanya saja, atau dengan Format Teks Polos/ODF (Sesuai kebutuhan) jika Anda ingin mengubah nya juga. Jadi, sesuaikan dengan kebutuhan.

> ### Bagaimana jika saya mengirimkan berkas kepada orang lain, entah itu teman, dosen, HRD, dll nya suatu saat nanti?

Tergantung, Apakah mereka hanya ingin membaca dokumenmu saja atau ingin mengubah nya juga atau cuma sekedar menyoroti teks saja? Biasanya (apalagi dosen atau HRD), mereka akan butuh dokumen kamu hanya untuk di baca saja, karena mereka pada dasar nya tidak terlalu perlu untuk mengubah dokumen kamu. (Contoh kasus: Jika kamu mengirimkan CV kepada HRD, Tugas Kuliah ke Dosen, dll).

Kalau mereka hanya ingin membacanya saja, kirimkan saja berkas nya dengan Format PDF.

Tapi, kalau mereka ingin mengubah dokumen mu, maka kalau bisa, kirimkan berkas tersebut kepada mereka dan sarankan kepada mereka baik-baik untuk meng-install LibreOffice jika kamu merasa dekat dengan mereka.

Atau, kalau mereka menginginkan format selain PDF hanya karena ia tidak bisa membuka nya dengan baik, jika kamu dekat dengan mereka, coba kamu bantu untuk memperbaiki nya atau gunakan Web Browser untuk membuka PDF.

Sedangkan, jika kebutuhan nya hanya menyoroti teks di dalam dokumen nya, kamu hanya perlu mengirimkan berkas PDF saja, biasanya Aplikasi Peninjau PDF bisa melakukan nya jika hanya menyoroti teks saja.

## II. Tampilan nya jelek dan merasa susah untuk di gunakan
Tidak bisa di pungkiri lagi, bahwa secara bawaan, LibreOffice memiliki penampilan yang agak 'jelek' dan penggunaan nya yang memang rumit. Sehingga, orang-orang merasa 'pusing' untuk menggunakan Perangkat Lunak satu ini.

Salah satu penyebabnya adalah bahwa kebanyakan orang telah terbiasa dengan Penampilan "Ribbon" yang ada di Microsoft Office sejak versi 2007, begitupun juga versi di atasnya.

Mungkin saja, tampilan itu memang terasa familiar bagi Anda yang sudah pernah menggunakan Microsoft Office 2003 sebelumnya. Tapi, yang menjadi masalah nya adalah bahwa kebanyakan orang yang sudah familiar dengan penampilan "Ribbon" dan mengingatnya, kalaupun sebelumnya ada yang sudah pernah menggunakan Microsoft Office 2003, bukan berarti mereka familiar akan tampilan nya serta tidak semua orang menggunakan nya.

Namun, sejak LibreOffice versi 6.2 dirilis, Anda dapat menikmati penampilan "Ribbon" di LibreOffice dengan mengubah Setelan tampilan nya. Dulu, sebelum versi 6.2, memang sempat ada fitur seperti ini, hanya saja itu masih beta/eksperimental dan masih memerlukan Berkas JAR Eksternal (dari luar).

Sekarang, Anda sudah bisa menikmati nya tanpa harus memuat Berkas JAR Eksternal lagi.

> Lalu, bagaimana caranya?

