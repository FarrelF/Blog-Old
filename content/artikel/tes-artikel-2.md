Title: Tes Artikel 2
Date: 2019-08-25 17:49
Category: Lainnya
Tags: Tes
Slug: tes-artikel-2
Authors: Farrel Franqois
Summary: Ini adalah artikel uji coba ke-2

Ini adalah isi dari Artikel ini, dan ini adalah huruf **tebal**, sedangkan *ini* adalah huruf miring.

Sedangkan di bawah ini merupakan barisan kode:

    #!python
    nilai_1 = int(input("Masukkan Nilai Pertama: "))
    nilai_2 = int(input("Masukkan Nilai Kedua: "))
    nilai_3 = int(input("Masukkan Nilai Ketiga: "))
    nilai_4 = int(input("Masukkan Nilai Keempat: "))
    nilai_rata2 (nilai_1 + nilai_2 + nilai_3 + nilai_4) / 4

    if nilai_rata2 >= 85 && nilai_rata2 <= 100:
        peringkat = "A"
        cetak = "Selamat, kamu lulus dengan nilai yang sangat baik!"
    elif nilai_rata2 >= 75 && nilai_rata2 <= 84:
        peringkat = "B"
        cetak = "Selamat, kamu lulus dengan nilai yang baik!"
    elif nilai_rata2 >= 60 && nilai_rata2 <= 74:
        peringkat = "C"
        cetak = "Kamu lulus dengan nilai yang cukup, perbaiki nilai mu nanti!"
    elif nilai_rata2 >= 40 && nilai_rata2 <= 59:
        peringkat = "D"
        cetak = "Sayang sekali, kamu tidak lulus ujian dengan nilai yang buruk, perbaiki lagi!"
    elif nilai_rata2 >= 0 && nilai_rata2 <= 39:
        peringkat = "E"
        cetak = "Sayang sekali, kamu tidak lulus ujian dengan nilai yang sangat buruk, perbaiki lagi!"

    print(f'Peringkat: {peringkat}')
    print(f'Nilai Rata-rata: {nilai_rata2}')
    print(cetak)

# Ini adalah Header 1
## Ini adalah Header 2
### Ini adalah Header 3
#### Ini adalah Header 4
##### Ini adalah Header 5
###### Ini adalah Header 6
