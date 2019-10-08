#!/bin/sh

## Mengembalikan Tembolok ##
restore_home_cache ".cache" "pip cache"

## Meng-install Pengelola Paket Poetry dengan Pip ##
pip install poetry

## Konfigurasi Poetry ##
poetry config settings.virtualenvs.create false
# Catatan: Karena di Netlify memiliki lingkungan Isolasi nya sendiri saat men-deploy, \
# maka seharusnya kita tidak perlu lagi membuatkan Virtualenv saat meng-install paket-paket nya dengan Poetry. \
# Hal ini supaya kita tidak memperlambat proses Deploy pada Netlify.

## Meng-install paket-paket dan ketergantungan dengan Poetry ##
poetry install --no-dev
# Catatan: Saya menambahkan parameter '--no-dev'. \
# Karena dalam produksi, kita tidak perlu menambahkan paket/pustaka \
# yang memang hanya di perlukan untuk Pengembangan, seperti PyLint.

## Membangun dan Menerbitkan Blog ##
make publish
