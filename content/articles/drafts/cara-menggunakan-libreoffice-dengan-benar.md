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

Karena Format OOXML itu bersifat [tidak konsisten](https://joinup.ec.europa.eu/collection/open-source-observatory-osor/document/complex-singularity-versus-openness), hal ini terjadi karena spesifikasi dari OOXML itu sendiri dan juga Implementasi nya di Microsoft Office [itu berbeda](https://brattahlid.wordpress.com/2012/05/08/is-docx-really-an-open-standard/). 

Perlu Anda ketahui, bahwa di dalam Format OOXML itu memiliki 3 versi (atau sub-standar), diantara nya adalah: 

- ECMA-376 (atau di sebut versi/sub-standar "ECMA")
- ISO/IEC 29500 Transitional (atau di sebut versi/sub-standar "Transitional")
- ISO/IEC 29500 Strict (atau di sebut versi/sub-standar "Strict")

Nah, yang jadi masalah nya adalah, Spesifikasi untuk Sub-Standar 'Transitional' dan 'Strict' itu tertutup dan tidak di publikasikan, serta berdasarkan dari Laman [Wikipedia nya](wikipedia_en>Office_Open_XML), bahwa Microsoft Office hanya mendukung baca/tulis untuk dokumen yang di buat dengan Versi 'Transitional' saja, dan dokumen yang di buat dengan Versi 'Strict' hanya bisa di baca pada Microsoft Office 2010, serta bisa baca/tulis pada Microsoft Office 2013 dan 2016, itupun sebagai ['tambahan'](https://technet.microsoft.com/en-us/library/cc179191%28v=office.15%29.aspx).

Selain itu, dokumen dengan versi ECMA hanya bisa di baca saja di Microsoft Office 2010, entah apa yang terjadi di atas nya. 

Jadi, ini artinya, ketika Anda menyimpan dokumen dari Microsoft Office (terutama dengan ekstensi yang berformat OOXML), maka Anda menyimpan dokumen nya bukan sebagai "Office Open XML" yang selama ini "di iklankan" sebagai "Format Terbuka".

Sedangkan, kebanyakan Perangkat Lunak Perkantoran lain nya hanya mampu meng-implementasi Versi ECMA dari Format OOXML nya saja (itupun belum tentu sepenuhnya), yang artinya, jika Anda menyimpan nya sebagai ekstensi dengan format OOXML di Perangkat Lunak Perkantoran selain Microsoft Office, maka yang Anda simpan itu adalah versi ECMA dari OOXML nya.

Selain itu, format ini memiliki beberapa masalah ketika di implementasikan oleh Perangkat Lunak Perkantoran selain Microsoft Office.

Sehingga, ini akan membuat Pengembang Perangkat Lunak Bebas/FLOSS seperti LibreOffice, bahkan Perangkat Lunak lain nya seperti WPS Office, Softmaker FreeOffice, dan lain nya akan mengalami kesulitan untuk memenuhi standar dari Format OOXML itu sendiri. 

Masalah-masalah nya seperti:

- Memerlukan penautan/penghubungan ke teknologi atau fitur yang di kendalikan atau/dan hanya bisa di gunakan secara eksklusif oleh Vendor/Perangkat Lunak tertentu (Seperti: SmartArt, PivotTable, dll).

- Jumlah Halaman dari Dokumen Spesifikasi nya sendiri nya mencapai [&pm;6000 halaman](https://www.ecma-international.org/publications/standards/Ecma-376.htm), yang bahkan itu melebihi POSIX/SUSv3 yang cuma sampai [&pm;3700 halaman saja](https://en.wikipedia.org/wiki/Single_UNIX_Specification). Dan, itupun untuk versi ECMA nya, belum 'Transitional' dan 'Strict' nya. Sehingga, hal itu akan menyulitkan Pengembang Perangkat Lunak lain nya untuk meng-implementasikan format tersebut.

- Format OOXML itu sendiri telah terbebani oleh [Paten](http://noooxml.wikidot.com/patents) [Perangkat Lunak](http://en.swpat.org/wiki/OOXML), sehingga hal itu akan membuat Pengembang Perangkat Lunak perkantoran lain nya menjadi tidak mungkin untuk menyempurnakan dukungan/implementasi format OOXML nya.

- Dan, masalah lain nya.

Masalah-masalah di atas bukan hanya mempengaruhi pengembang Perangkat Lunak saja, tapi itu akan mempengaruhi pengguna nya secara keseluruhan, terutama jika pengguna tersebut membuka atau membuat dokumen ber-format OOXML dengan Perangkat Lunak Perkantoran selain Microsoft Office.

Sehingga, Perangkat Lunak Perkantoran yang paling bisa meng-implementasikan nya dan yang paling mengikuti/memenuhi standar dalam Format OOXML adalah Microsoft Office itu sendiri.

Selain alasan di atas, Alasan mereka hanya fokus (bahkan [mempromosikan](https://wiki.documentfoundation.org/LibreOffice_OOXML#Does_The_Document_Foundation_support_OOXML_.3F)) format ODF adalah karena mereka percaya bahwa tidak ada standar/format dokumen lain yang menawarkan tingkat netralitas terhadap vendor dengan tepat. Dan, mereka juga percaya bahwa format tersebut akan bermanfaat untuk semua orang kedepan nya.

Ini artinya, mereka percaya bahwa ODF merupakan format yang paling 'netral' saat ini, bila di bandingkan dengan format OOXML.

Lagian, di Indonesia, Format ODF ini sudah memasuki ketentuan Standar Nasional Indonesia (SNI) pada tahun 2010 dengan Nomor [`:::text SNI ISO/IEC 26300:2011`](http://sispk.bsn.go.id/SNI/DetailSNI/8541) melalui surat keputusan dengan Nomor [`:::text 41/KEP/BSN/4/2011`](http://akses-sispk.bsn.go.id/Upload/Dokumen/SK_SNI/7476_SK%20SNI%2041-04-2011.PDF) dari Kepala BSN (Badan Standardisasi Nasional) pada waktu itu. Sampai sekarang, Standar ini masih berlaku di Indonesia.

Bahkan, format ini telah di akui oleh Pemerintah kita melalui [Kemenkominfo (Kementerian Komunikasi dan Informatika)](https://jdih.kominfo.go.id/produk_hukum/unduh/id/75/t/peraturan+menteri+komunikasi+dan+informatika++nomor+7+tahun+2013+tanggal+5+maret+2013) (Atau, Anda bisa unduh [versi DOCX](https://web.kominfo.go.id/sites/default/files/RPM%20Pedoman%20Penerapan%20Interoperabilitas%20Dokumen%20Perkantoran%20Bagi%20Penyelenggara%20Sistem%20Elektronik%20Untuk%20Pelayanan%20Publik.docx) nya) dan [Kemenkumham (Kementerian Hukum dan Hak Asasi Manusia)](http://ditjenpp.kemenkumham.go.id/arsip/bn/2013/bn474-2013lamp.pdf) pada Tahun 2013 yang lalu.

Selain itu, menurut [artikelnya](https://kominfo.go.id/index.php/content/detail/3434/open+source+di+kominfo+/0/program_prioritas), pihak Kemenkominfo telah menggunakan Perangkat-Perangkat Lunak tersebut di dalam lingkungan nya untuk menunjang keperluan mereka, termasuk LibreOffice dan Format ODF nya. (Ngomong-ngomong, Artikel itu di terbitkan sejak tahun 2014 yang lalu. Entah apa yang terjadi sekarang, apakah mereka masih menggunakan nya? Siapa tahu masih juga, kan?)

Jadi, jika OOXML di nyatakan sebagai "Open Format", apakah artinya OOXML ini termasuk Standar Terbuka (_Open Standard_) atau bebas? Seperti nya belum tentu juga.

Apakah itu merupakan suatu hal yang wajar jika tampilan atau bahkan dokumen nya menjadi kacau saat dokumen OOXML di buat atau/dan di buka dengan Perangkat Lunak selain Microsoft Office? Wajar, bahkan normal jika itu terjadi, kecuali jika Anda cuma tahu Microsoft Office atau/dan Ekstensi berformat OOXML nya saja. 

Dan, apakah masalah seperti ini perlu di keluhkan? Kalau menurut saya, tidak perlu, bahkan sama sekali.

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

Lalu, bagaimana caranya? Caranya adalah, ketika Anda sudah selesai membuat Dokumen nya, simpanlah dokumen tersebut sebagai Ekstensi yang berformat ODF (OpenDocument Format), seperti .ODT (untuk LibreOffice Writer), .ODS untuk (LibreOffice Calc), dan .ODP (untuk LibreOffice Impress), daripada ekstensi yang berformat OOXML seperti .DOC, .DOCX, .XLS, .XLSX, .PPT, .PPTX dan ekstensi dengan format OOXML lain nya.

Terakhir, jangan pernah mengharapkan kalau LibreOffice bisa membuka dokumen dengan format OOXML sebaik Microsoft Office.

> ### Bagaimana jika saya berada di Rental Komputer/Warung Internet yang rata-rata menggunakan Windows suatu saat nanti?

LibreOffice mendukung Sistem Operasi Windows, jadi ia bisa di install di Sistem Operasi Windows. Jika tidak mungkin bisa di install (Entah itu karena terkendala izin Administrator sampai tidak ada waktu atau terlalu repot), LibreOffice juga telah menyediakan versi Portabel nya agar LibreOffice bisa di jalankan secara langsung di dalam USB tanpa izin terlebih dahulu ke Administrator. 

Ini akan sangat membantu Anda yang sedang menggunakan Komputer yang mana Anda tidak dapat menggunakan Izin Administrator atau bagi Anda yang tidak ingin repot-repot atau membuang-buang waktu serta tenaga untuk meng-install LibreOffice di Komputer lain, seperti di Warnet, Rental Komputer, Komputer Lab Sekolah/Kampus, Komputer Kantor, dll nya.

> ### Bagaimana jika saya membuka berkas OOXML di LibreOffice?

Sudah saya bilang sebelumnya, bahwa lebih baik Anda tidak terlalu berharap untuk bisa membuka berkas yang berformat OOXML di LibreOffice sebaik Microsoft Office. Namun, Anda bisa saja membuka nya, hanya saja hasilnya nanti tidak sebaik Microsoft Office, karena fitur-fitur yang ada/digunakan pada dokumen tersebut belum tentu dapat di 'render' dengan baik oleh LibreOffice, karena masalah format OOXML itu sendiri.

Meskipun artikel ini menyinggung Microsoft Office dan Format OOXML nya, bukan berarti saya melarang Anda untuk menggunakan kedua nya. 

Anda bisa menggunakan Microsoft Office untuk membuka berkas berformat OOXML, atau jika Anda tidak mempunyai Microsoft Office nya (Entah itu sengaja gak di install atau gak bisa di Install karena sebab lain), Anda bisa menggunakan Perangkat Lunak Perkantoran lain nya selain Microsoft Office, seperti WPS Office, Softmaker FreeOffice, dll.

Atau, jika hal tersebut tidak memungkinkan, maka sebaiknya Anda minta saja kepada pengirimnya untuk mengirimkan ulang berkas sebagai Format PDF jika Anda hanya ingin membacanya saja, atau dengan Format Teks Polos/ODF (Sesuai kebutuhan) jika Anda ingin mengubah nya juga. Jadi, sesuaikan dengan kebutuhan.

> ### Bagaimana jika saya mengirimkan berkas kepada orang lain, entah itu teman, dosen, HRD, dll nya suatu saat nanti?

Tergantung, apakah mereka hanya ingin membaca dokumenmu saja atau ingin mengubah nya juga atau cuma sekedar mengulas/meninjau ulang (_review_) dokumen mu saja? Biasanya (apalagi dosen atau HRD), mereka akan butuh dokumen kamu hanya untuk di baca saja, karena pada dasar nya, mereka tidak terlalu perlu untuk mengubah dokumen kamu. (Contoh kasus: Jika kamu mengirimkan CV atau _Resume_ kepada HRD untuk melamar pekerjaan, Tugas Kuliah ke Dosen, dll).

Kalau mereka hanya ingin membacanya saja, ekspor berkas tersebut ketika Anda sudah selesai mengetik/membuat dokumen nya dan kirimkan saja hasil nya sebagai Format PDF.

Tapi, kalau mereka ingin mengubah dokumen mu, maka kalau bisa, kirimkan berkas tersebut kepada mereka dan sarankan kepada mereka dengan baik-baik untuk meng-install LibreOffice jika kamu merasa dekat dengan mereka.

Atau, kalau mereka menginginkan format selain PDF hanya karena ia tidak bisa membuka nya dengan baik, jika kamu dekat dengan mereka, coba kamu bantu untuk memperbaiki nya atau sarankan kepada mereka untuk menggunakan Peramban Web (_Web Browser_) untuk membuka PDF.

Sedangkan, jika kebutuhan nya hanya mengulas/meninjau ulang dokumen nya saja (entah itu dengan menyoroti teks nya, memberikan komentar, dll), kamu hanya perlu mengirimkan berkas PDF saja, biasanya Aplikasi Peninjau PDF (Kecuali Peramban Web) bisa melakukan nya jika hanya menyoroti teks atau mengulas dokumen saja.

## II. Tampilan nya membuat LibreOffice sulit untuk di gunakan
Tidak bisa di pungkiri lagi, bahwa secara bawaan, LibreOffice memiliki penampilan yang agak kurang familiar dan penggunaan nya yang memang rumit. Sehingga, orang-orang merasa 'pusing' dan sulit untuk menggunakan Perangkat Lunak satu ini.

Salah satu penyebabnya adalah bahwa kebanyakan orang telah terbiasa dengan Penampilan "Ribbon" yang ada di Microsoft Office sejak versi 2007, begitupun juga versi di atasnya, sampai sekarang.

Mungkin saja, tampilan itu memang terasa familiar bagi Anda yang sudah pernah menggunakan Microsoft Office 2003 sebelumnya. Tapi, yang menjadi masalah nya adalah bahwa kebanyakan orang sudah duluan familiar dengan penampilan "Ribbon" dan mengingatnya, kalaupun sebelumnya ada yang sudah pernah menggunakan Microsoft Office 2003, bukan berarti mereka familiar akan tampilan nya serta tidak semua orang menggunakan nya.

Namun, sejak LibreOffice versi 6.2 dirilis, Anda dapat menikmati penampilan "Ribbon" di LibreOffice dengan mengubah Setelan tampilan nya. Dulu, sebelum versi 6.2, memang sempat ada fitur seperti ini, hanya saja itu masih beta/eksperimental dan masih memerlukan Berkas JAR Eksternal (dari luar).

Sekarang, Anda sudah bisa menikmati nya tanpa harus memuat Berkas JAR Eksternal lagi.

> ### Lalu, bagaimana caranya?

Caranya mudah, yaitu:

1. Pastikan Aplikasi LibreOffice sudah di buka (Untuk varian nya bisa apa saja, LO Writer, Spreadsheet, Impress atau lain nya)

2. Klik pada Menu "View" -> Lalu, klik "Tabbed" untuk mengaktifkan fitur "Ribbon"

Mudah, bukan?
