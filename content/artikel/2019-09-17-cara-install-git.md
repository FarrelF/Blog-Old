Title: Cara Install Git di Windows, GNU/Linux dan macOS (tanpa basa-basi!)
Category: Tutorial
Tag: Git
Slug: cara-install-git
Authors: Farrel Franqois
Cover: https://cdn.statically.io/gl/FarrelF/blog-images/cb559d22/cara-install-git/Git-Logo-2Color.png?fit=500,209
Status: published
Summary: Artikel ini akan membahas tentang Cara Install Git, baik itu di dalam GNU/Linux dan Windows, tentu saja, tanpa basa-basi terlebih dahulu (alias, langsung saya bahas bagaimana cara meng-install nya). Kalau Anda ingin meng-install Git di dalam Komputer Anda, silahkan Anda simak lebih lanjut artikel ini, kalau tidak ya tidak apa-apa :slightly_smiling_face:

<style>
article.single p img.centered {
    display: block;
    margin: 0 auto;
}
</style>

## Daftar Isi
[TOC]

## I. Cara Install Git
Untuk meng-install nya, Anda hanya perlu meng-unduh Git nya terlebih dahulu, bisa Anda kunjungi situs web resmi nya untuk meng-unduh Git, yakni: [https://git-scm.com](https://git-scm.com). Lalu, klik pada *Button* "Download Git" bla bla bla. Atau, Anda juga bisa mengunjungi [Halaman Unduhan](https://git-scm.com/downloads) Resmi nya untuk meng-unduh Git.

### **Cara Install Git di GNU/Linux, macOS dan Sistem Operasi berbasis \*nix lain nya**
Pada GNU/Linux atau Sistem Operasi berbasis Unix/Unix-like lain nya (kecuali macOS, yang tidak di beritahukan cara Install nya disana), biasanya mereka akan memberikan petunjuk cara instalasi Git nya untuk masing-masing Distribusi atau Sistem Operasi nya. Kalau begitu, Anda tinggal ikuti saja [petunjuk nya](https://git-scm.com/download/linux).

Atau, kalo Anda tidak ingin mengunjungi nya, Anda bisa ikuti Petunjuk nya di bawah ini:

```bash
## Untuk pengguna Distribusi Ubuntu dan Turunan nya ##
$ sudo -- sh -c 'add-apt-repository ppa:git-core/ppa; apt update; apt install git'

## Untuk pengguna Distribusi Debian dan Turunan nya ##
$ sudo apt install git

## Untuk pengguna Distribusi Arch Linux, Manjaro dan Turunan nya ##
$ sudo pacman -S git

## Untuk pengguna Distribusi Fedora ##
$ sudo yum install git # Untuk Fedora 21 dan di bawah nya
$ sudo dnf install git # Untuk Fedora 22 dan di atas nya

## Untuk pengguna Distribusi OpenSUSE dan Turunan nya ##
$ sudo zypper install git

## Untuk pengguna Distribusi Gentoo ##
$ sudo emerge --ask --verbose dev-vcs/git

## Untuk pengguna NixOS atau yang menggunakan Nix Package Manager ##
$ sudo nix-env -i git

## Untuk pengguna Alpine ##
$ apk add git

## Untuk pengguna FreeBSD ##
pkg install git # Harap Eksekusi perintah ini dalam keadaan 'root'
```

Untuk pengguna macOS, bisa Anda Unduh dan Install Git nya dari [sini](https://git-scm.com/download/mac). 

Sedangkan untuk Windows, Anda bisa ikuti petunjuk nya berikut.

### **Cara Install Git di Windows**
Cara Install Git di Windows sangatlah berbeda daripada Install Git di GNU/Linux, Installer nya menggunakan GUI, sehingga dapat mempermudah kamu selama meng-install Git.

Hanya saja, jika kamu salah langkah, maka yang terjadi adalah Git akan mengalami "kesalahan" (*error*) saat di gunakan, entah itu tidak bisa meng-kloning *Repository* sampai mengurus nya.

Maka dari itu, jika Anda adalah pengguna Windows, maka Anda bisa ikuti cara instalasi nya berikut:

1. Unduh [Git untuk Windows](https://git-scm.com/download/win/).

2. Setelah di Unduh, buka berkas tersebut. Jika muncul UAC (*User Account Control*), klik pada *Button* 'OK'.

3. Setelah itu, Install Git dengan Langkah-langkah berikut:

#### **1. Perjanjian Lisensi**
Nanti akan muncul Perjanjian Lisensi (*License Agreement*) setelah membuka berkas tersebut, klik pada *Button* 'Next >' untuk melanjutkan Instalasi. 

**Catatan:** Jika Anda klik *Button* tersebut dan lanjut meng-install nya, ini artinya Anda telah menyetujui Perjanjian tersebut.

#### **2. Pilih Komponen mana yang ingin di Install (_Select Components_)**
Pada langkah ini, silahkan Anda atur Komponen mana yang ingin Anda install dan di aktifkan oleh Anda, seperti: Asosiasi Berkas, Integrasi Windows Explorer, Pintasan di Desktop, dll.
   
Jika Anda ingin menggunakan TrueType di dalam semua Konsole Windows, centang "Use a TrueType font in all console Windows", seperti cuplikan berikut:
   
[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_1.png){class="centered"}](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_1.png)

Setelah Anda selesai memilah-milih nya, klik pada *Button* 'Next >' untuk melanjutkan ke Langkah ke-3.

#### **3. Pilih Editor mana yang akan di gunakan (_Choosing the default editor used by Git_)**
Pada langkah ini, Anda bisa pilih editor yang akan di gunakan oleh Git nanti nya

Pada tutorial ini, saya akan gunakan 'GNU nano' sebagai editor bawaan untuk Git, berikut cuplikan nya:

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_2.png){class="centered"}](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_2.png)

Kalo Anda ingin menggunakan Editor Favorit, sedangkan editor nya tidak tersedia disitu, nanti Anda bisa konfigurasi lagi

Karena secara bawaan Git memilih 'nano' sebagai editor nya, maka untuk langkah ini, bisa langsung Anda klik *Button* 'Next >' untuk melanjutkan ke Langkah ke-4.

#### **4. Pilih Cara untuk Eksekusi Git (_Adjusting your PATH environment_)**
Setelah itu, pilih opsi untuk cara eksekusi Git, saya sarankan untuk pilih opsi **Git from the command line and also from 3rd-party software** (atau, membiarkan nya karena sudah terpilih) agar Git bisa di akses atau di eksekusi dari manapun, termasuk dari CMD (Command Prompt). 
   
[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_3.png){class="centered"}](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_3.png)

Setelah Anda memilih opsinya, klik pada *Button* 'Next >' untuk melanjutkan.

#### **5. Pilih Perangkat Lunak untuk Eksekusi SSH untuk Git (_Choosing the SSH executable_)**
Setelah itu, pilih eksekusi SSH untuk Git, ini akan berguna nanti ketika Anda mengelola *Repository* Git dengan SSH. Agar lebih mudah, pilih "OpenSSH" dengan memilih opsi **Use OpenSSH**, seperti pada cuplikan berikut: 

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_4.png){class="centered"}](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_4.png)

Setelah Anda memilih nya, klik pada *Button* 'Next >' untuk melanjutkan ke Langkah ke-6.

#### **6. Menentukan Pustaka untuk HTTPS pada Git (_Choose HTTPS transport backend_)**
Pada langkah **Choose HTTPS transport backend**, Anda akan menentukan *Library*/Pustaka mana yang akan di gunakan untuk 'transportasi' HTTPS pada Git nanti nya. 

Saya sarankan untuk menggunakan Pustaka Bawaan dari Windows saja, yakni ['Windows Secure Channel'](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380123(v=vs.85).aspx) (atau bisa di sebut 'winSSL' atau 'Schannel'), agar Git dapat mengenali CA (Certification Authority) dan Sertifikat SSL lain nya secara langsung di dalam Windows. 

Maka dari itu, pilihlah opsi **Use the native Windows Secure Channel library**, bukan **Use OpenSSL** (Kecuali jika Anda meng-install OpenSSL dan mempunyai berkas `ca-bundle.crt` di dalam Windows), seperti pada cuplikan layar berikut ini:

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_5.png){class="centered"}](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_5.png)

Setelah Anda memilih nya, klik pada *Button* 'Next >' untuk melanjutkan ke Langkah ke-7.

#### **7. Menentukan "Baris Baru" untuk Git (_Configuring the line ending conversions_)**
Selanjutnya, pada langkah **Configuring line endings conversions**, Anda akan menentukan bagaimana Git akan memperlakukan "Line Ending" (Baris Baru) nantinya.

Karakter *Line Ending* itu sendiri berbeda-beda, tergantung Sistem Operasi mana yang kamu gunakan, contoh: Pada Windows dan kebanyakan Sistem Operasi yang bukan berbasis Unix lain nya, karakter *Line Ending* yang berlaku adalah `:::text \r\n`, sedangkan GNU/Linux, macOS atau Sistem Operasi berbasis Unix/Unix-like lain nya menggunakan `:::text \n` saja.

Ada beberapa istilah mengenai *Line Ending* ini, salah satu nya adalah: LF, CR dan CRLF. LF merupakan singkatan dari *Line Feed* atau `:::text \n`, sedangkan CR merupakan singkatan dari *Carriage Return* atau `:::text \r`. Dan, CRLF merupakan gabungan dari CR dan LF, atau `:::text \r\n` yang di berlakukan oleh Sistem Operasi Windows dan macOS hingga saat ini.

Untuk mempelajari lebih lanjut mengenai apa itu *Line Ending*, cari sendiri lewat Google, yah :slightly_smiling_face:

Jadi, karena Anda saat ini meng-install Git untuk Windows, maka pilihan yang terbaik untuk Sistem Operasi Windows adalah Opsi Pertama, yaitu **Checkout Windows-style, commit Unix-style line endings**.

Seperti cuplikan layar berikut:

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_6.png){class="centered"}](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_6.png)

Setelah Anda memilih nya, klik pada *Button* 'Next >'.

#### **8. Memilih Terminal Emulator untuk Git Bash (_Configuring the terminal emulator to use with Git Bash_)**
Pada langkah ini, Anda akan memilih Terminal Emulator bawaan untuk Git Bash nya, apakah menggunakan Konsol Windows atau MinTTY. 

Mohon maaf, saat ini saya tidak mempunyai cuplikan layar sebagai contoh nya. Namun, pada tutorial ini, saya memilih menggunakan MinTTY dan saya sarankan untuk menggunakan nya daripada menggunakan Konsol Windows, dengan memilih opsi **Use MinTTY (the default terminal of MSYS2)**. 
   
[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_7.png){class="centered"}](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_7.png)

Lalu, klik *Button* 'Next >'.
   
#### **9. Konfigurasi Opsi Tambahan (_Configuring extra options_)**
Pada langkah ini, nanti akan ada tiga opsi, Anda bisa aktifkan semua opsi tersebut dengan mencentang nya.

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_8.png){class="centered"}](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_8.png)

Lalu, klik *Button* 'Next >'.

#### **10. Konfigurasi Opsi Eksperimental (_Configuring experimental options_)**
Pada langkah ini, nanti akan ada satu opsi yang bisa Anda aktifkan, namun karena sifat nya Eksperimental, maka saya sarankan agar tidak mengaktifkan nya, kecuali jika Anda ingin mencoba nya. 

[![Langkah-langkah Instalasi Git](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_9.png){class="centered"}](https://cdn.statically.io/gl/FarrelF/blog-images/0e1e98da/cara-install-git/Install_Git_9.png)

Pada Git versi 2.23, akan ada opsi seperti cuplikan di atas, namun hal ini mungkin tidak berlaku untuk versi kedepan nya.

Klik pada *Button* 'Next >' untuk melanjutkan. Atau, jika ada *Button* 'Install', klik pada *Button* tersebut untuk meng-install Git.

#### **11. Proses Instalasi sampai Selesai**
Instalasi Git sedang dalam Proses, harap bersabar hingga selesai dalam beberapa menit kedepan.

Jika Git telah berhasil ter-install, klik pada *Button* 'Finish'. Sebelum itu, Anda juga bisa hapus centang **Launch Git Bash** jika Anda tidak ingin menjalankan 'Git Bash' setelah selesai Install.

## II. Akhir kata
Sudah? Iya, sudah, cuma itu saja yang perlu Anda lakukan. Ini merupakan Artikel yang membahas tentang 'Cara Install Git', bukan 'Apa itu Git dan Cara Install nya', jadi saya tidak perlu basa-basi disini.

Yang perlu kamu lakukan setelah Install Git adalah, sebaiknya kamu pelajari mengenai penggunaan Git, banyak di Internet caranya, atau mungkin kamu akan lihat kedepan nya nanti jika Anda membuat/mengembangkan sebuah Perangkat Lunak.

Jika kamu mempunyai pertanyaan, kritik dan saran, komentar atau masukkan lain nya, silahkan kamu berkomentar melalui kolom komentar yang tersedia.

Terima kasih atas perhatian nya :blush:

## III. Penggunaan Gambar dan Atribusi
Berkas-berkas Gambar (seperti Cuplikan layar dan Gambar lain nya) yang di gunakan di dalam artikel ini, disediakan di dalam folder `cara-install-git` yang berada di dalam Repository GitLab [`blog-images`](https://gitlab.com/FarrelF/blog-images) milik saya. 

Jika Anda ingin menjelajahi nya, silahkan kunjungi Alamat URL berikut:

```text
https://gitlab.com/FarrelF/blog-images/tree/master/cara-install-git
```

Gambar yang terletak di paling atas dan di bawah judul artikel itu merupakan Logo Git, yang telah di buat oleh [Jason Long](https://twitter.com/jasonlong). 

Logo Git di lisensi kan dengan [Creative Commons Attribution 3.0 Unported (CC BY 3.0)](https://creativecommons.org/licenses/by/3.0/) oleh pembuatnya, begitupun juga dengan varian logo Git [lain nya](https://git-scm.com/downloads/logos).

Jika Anda ingin meng-unduh lebih banyak, silahkan Anda kunjungi [halaman web resmi nya](https://git-scm.com/downloads/logos).
