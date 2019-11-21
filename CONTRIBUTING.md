# Cara Berkontribusi
Kontribusi bisa di lakukan dengan banyak cara, seperti memberikan Kritik dan Saran, Memberikan Komentar/Pertanyaan yang bermanfaat, Donasi, sampai turut membantu untuk memodifikasi/merubah Kode Sumber atau Artikel yang ada di Blog ini.

Anda bisa ber-kontribusi terhadap Blog ini menggunakan (salah satu/lebih) cara berikut ini:

## Cara 1: Mengubah Kode Sumber

Jika Anda ingin berkontribusi dengan membantu konfigurasi Blog ini atau ikut serta dalam mengubah Kode Sumber nya. Cara nya cukup mudah, Anda tinggal ikuti langkah di bawah ini:

1. Buatlah sebuah _fork_ dari Repo ini.

2. Klon Repo GitHub dari Repo yang Anda buat _fork_ nya tadi.

3. Penuhi terlebih dahulu semua [Persyaratan nya](https://github.com/FarrelF/FarrelF-Blog#persyaratan) (terutama yang wajib), termasuk Install Git, Python 3.7 atau di atasnya dan Poetry di dalam Sistem Operasi Anda, lalu Install semua keperluan nya. Setelah memenuhi persyaratan, untuk meng-install dan membangun blog ini, Anda bisa baca/lihat caranya [disini](https://github.com/FarrelF/FarrelF-Blog#cara-install)

4. Navigasikan _Shell_ yang Anda gunakan ke dalam Folder Kode Sumber yang Anda klon tadi dengan perintah `cd`. 

5. Lalu, buatlah sebuah _Branch_ baru dari Repo yang Anda _fork_ tadi, Anda bisa turunkan _Branch_ tersebut dari `origin/drafts` jika Anda ingin memperbaiki Artikel/Laman atau `origin/master` jika Anda ingin memperbaiki/mengusir kutu (_bug_) atau memperbaiki/menyelesaikan masalah secepat nya.

6. Setelah Anda membuat _Branch_ baru, silahkan alihkan ke _Branch_ tersebut. Lalu, ubah Kode Sumber nya dari situ, bisa melalui Editor Teks/Kode Favorit kamu.

7. (Opsional, tapi disarankan) Sebelum melakukan _Commit_, pastikan Anda sudah menambahkan Kunci GPG di dalam GitHub dan pastikan juga untuk mengaktifkan _Commit Signing_ di dalam Git. Silahkan lihat/baca [Panduan nya](https://help.github.com/en/articles/managing-commit-signature-verification) untuk mengetahui cara menambahkan dan menggunakan Kunci GPG pada GitHub atau layanan Git lain nya. Untuk lebih lanjut, silahkan lihat sub-bagian nya [di bawah](#opsional-tapi-disarankan-membuat-dan-menggunakan-kunci-gpg-untuk-menandatangani-setiap-commit-commit-signing).

8. Lakukan _Staging_, buatlah sebuah _Commit_ dan pesannya, lalu lakukan _Push_.

9. Setelah Anda selesai, buatlah sebuah _Pull Request_ jika Anda benar-benar ingin mengubah Kode Sumber ini. Dan, pastikan Anda membuatnya dari _Branch_ yang Anda buat tadi di dalam Repo _fork_ Anda ke tujuan `FarrelF-Blog:drafts` atau `FarrelF-Blog:master` jika _Branch_ yang Anda buat itu di turunkan dari `origin/master`, jangan ke yang lain nya.

### (Opsional, tapi disarankan) Membuat dan Menggunakan Kunci GPG untuk 'menandatangani' setiap _Commit_ (_Commit Signing_)
Melanjutkan No. 7. Sebelum melakukan _Commit_, pastikan Anda sudah menambahkan Kunci GPG di dalam GitHub dan pastikan juga untuk mengaktifkan _Commit Signing_ di dalam Git. Silahkan lihat/baca [Panduan nya](https://help.github.com/en/articles/managing-commit-signature-verification) untuk mengetahui cara menambahkan dan menggunakan Kunci GPG pada GitHub atau layanan Git lain nya. 

Jika Anda berhasil, biasanya sebelum _Commit_, Anda akan di minta untuk memasukkan _Passphrase_ pada Kunci GPG nya, dan jika benar-benar berhasil, maka akan muncul 'Verified' pada setiap _Commit_ nya. Contoh nya: Coba Anda lihat log dari [_Commit_](https://github.com/FarrelF/FarrelF-Blog/commits/drafts) yang telah saya lakukan, Anda akan melihat kalau di sebelah nya ada tulisan 'Verified'.

Setelah mengaktifkan nya di dalam Git, pastikan Anda juga sudah mengaktifkan fitur _Git Commit Signing_ tersebut di dalam Editor Teks/Kode Favorit Anda, karena terkadang opsi tersebut tidak di aktifkan secara bawaan (default), contoh: [Visual Studio Code/VSCodium](https://stealthpuppy.com/signing-git-commits-for-sweet-verified-badges/) 


**Catatan**

~~Tema 'Flex' yang saya gunakan itu berada di dalam folder [`themes/Flex`](https://github.com/FarrelF/FarrelF-Blog/tree/master/themes/Flex) dan folder tersebut merupakan 'Subtree' dari Repo [`Modified-Repo`](https://github.com/FarrelF/Modified-Flex) yang saya turunkan dari Tema [Asli nya](https://github.com/alexandrevicenzi/Flex).~~

~~Jadi, jika Anda ingin merubah Kode Sumber Tema nya, silahkan ubah itu melalui Repo [`Modified-Flex`](https://github.com/FarrelF/Modified-Flex) dan Anda bisa mengubah nya dari situ.~~

~~Sedangkan, jika Anda langsung mengubah kode sumber tema nya langsung melalui Repo ini (dan *fork* nya), silahkan tanggung sendiri resiko nya dan kalo Anda mengirimkan *Pull Request* dengan perubahan seperti ini, maka saya akan pertimbangkan untuk menolak nya secara mentah-mentah atau meng-hapus perubahan tersebut. Jadi, jangan kaget, yah :blush:~~

**PEMBARUAN 03 Oktober 2019:** Untuk sekarang ini, saya tidak akan menggunakan *Git Subtree* lagi untuk menyimpan Tema yang saya gunakan, melainkan saya meng-kloning nya dari *Repository* GitHub saat saya men-*deploy* nya dengan Netlify. Hal ini agar saya tidak perlu lagi repot-repot melakukan `git subtree pull` lagi setiap pembaruan pada Tema.

Tapi, tetap saja, jika Anda ingin memodifikasi tema nya, silahkan Anda ubah itu melalui Repo [`Modified-Flex`](https://github.com/FarrelF/Modified-Flex) dan Anda bisa memodifikasi nya dari situ.

## Cara 2: Melakukan Donasi
Anda bisa menyisihkan sedikit uang Anda untuk mendonasikan nya sebagai kontribusi Anda untuk Blog ini. 

Untuk sementara ini, saya hanya menyediakan LinkAja dan GoPay saja, sedangkan metode lain nya seperti OVO, PayPal, Patreon dan juga Liberapay akan segera hadir jika memungkinkan dan ATM tidak akan saya hadirkan disini, karena saya tidak menggunakan ATM.

Jika Anda ingin mendonasikan nya, Anda bisa ikuti cara berikut:

### LinkAja (Sebelum nya bernama "TCASH")
Jika Anda ingin menggunakan LinkAja (yang sebelumnya adalah "TCASH") untuk berdonasi, Anda tinggal Pindai *QR Code* berikut di bawah ini:

<p align="center">
    <a href="https://cdn.statically.io/gh/FarrelF/FarrelF-Blog/283d3aa/content/extras/qrcode_linkaja.jpg" rel="dns-prefetch">
        <img style="display: block; margin: 0 auto;" src="https://cdn.statically.io/gh/FarrelF/FarrelF-Blog/283d3aa/content/extras/qrcode_linkaja.jpg" alt="QR Code LinkAja" width="320" height="320" />
    </a>
</p>

Setelah Anda memindai nya, pastikan kamu mentransfer nya ke akun/rekening tujuan dengan Atas Nama: **OK MOHAMAD EDBERT FARREL FRANQOIS**.

### GoPay (GOJEK)
Jika Anda ingin menggunakan GoPay untuk berdonasi, Anda tinggal Pindai *QR Code* berikut di bawah ini:

<p align="center">
    <a href="https://cdn.statically.io/gh/FarrelF/FarrelF-Blog/283d3aa/content/extras/qrcode_gopay.jpg" rel="dns-prefetch">
        <img style="display: block; margin: 0 auto;" src="https://cdn.statically.io/gh/FarrelF/FarrelF-Blog/283d3aa/content/extras/qrcode_gopay.jpg?fit=320,320" alt="QR Code GoPay" width="313" height="320" />
    </a>
</p>

Setelah Anda memindai nya, pastikan kamu mentransfer nya ke akun/rekening tujuan dengan Atas Nama: **Farrel Franqois**.

### OVO, Paypal, Patreon, dan Liberapay

Untuk sementara ini, ke empat metode pembayaran tersebut belum di sediakan. 

Ke-empat metode pembayaran tersebut akan segera hadir jika situasi dan kondisi nya yang memungkinkan :slightly_smiling_face:

## Cara 3: Lain nya
Untuk cara lain nya, Anda bisa bertanya, memberikan kritik dan saran, serta berkomentar di dalam blog ini.

- Jika Anda ingin menanyakan atau memberikan kritik dan saran yang berkaitan dengan Kode Sumber ini dan konten Artikel nya, silahkan untuk membuat tiket ["Issue"](https://github.com/FarrelF/FarrelF-Blog/issues) di dalam Repo ini.

- Jika Anda ingin berkomentar atau kritik dan saran mengenai Artikel di dalam [Blog ini], silahkan berkomentar melalui kolom komentar yang tersedia di akhir Artikel Blog.

- Jika Anda ada pertanyaan lainnya, silahkan hubungi saya.

Nah, itulah cara kontribusi nya, jika Anda mempunyai pertanyaan mengenai Berkas ini, silahkan tanyakan itu melalui ["Issue"](https://github.com/FarrelF/FarrelF-Blog/issues) di dalam Repo ini.

Terima kasih :blush:
