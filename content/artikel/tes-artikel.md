Title: Tes Artikel
Date: 2019-08-25 17:49
Modified: 2019-08-26 12:57
Category: Lainnya
Tags: Tes
Slug: tes-artikel
Authors: Farrel Franqois
Summary: Ini adalah artikel uji coba pertama

Ini adalah isi dari Artikel ini, dan ini adalah huruf **tebal**, sedangkan *ini* adalah huruf miring.

Sedangkan di bawah ini merupakan barisan kode:

    #!python
    nilai_1 = int(input("Masukkan Nilai Pertama: "))
    nilai_2 = int(input("Masukkan Nilai Kedua: "))
    nilai_3 = int(input("Masukkan Nilai Ketiga: "))
    nilai_4 = int(input("Masukkan Nilai Keempat: "))
    nilai_akhir = (nilai_1 + nilai_2 + nilai_3 + nilai_4) / 4

    if nilai_akhir >= 85:
        peringkat = "A"
        cetak = "Selamat, kamu lulus dengan nilai yang sangat baik!"
    elif nilai_akhir >= 75:
        peringkat = "B"
        cetak = "Selamat, kamu lulus dengan nilai yang baik!"
    elif nilai_akhir >= 60:
        peringkat = "C"
        cetak = "Kamu lulus dengan nilai yang cukup, perbaiki nilai mu nanti!"
    elif nilai_akhir >= 40:
        peringkat = "D"
        cetak = "Sayang sekali, kamu tidak lulus ujian dengan nilai yang buruk, perbaiki lagi!"
    elif nilai_akhir >= 0:
        peringkat = "E"
        cetak = "Sayang sekali, kamu tidak lulus ujian dengan nilai yang sangat buruk, perbaiki lagi!"

    print(f'Peringkat: {peringkat}')
    print(f'Nilai Akhir: {nilai_akhir}')
    print(cetak)

# Ini adalah Header 1
## Ini adalah Header 2
### Ini adalah Header 3
#### Ini adalah Header 4
##### Ini adalah Header 5
###### Ini adalah Header 6
