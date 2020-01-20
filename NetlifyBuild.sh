#!/bin/sh

## Mengembalikan Tembolok ##
restore_home_cache ".cache" "pip cache"
restore_cwd_cache '.venv' 'python virtualenv'

## Meng-install Pengelola Paket Poetry dengan Pip ##
pip3 install -q poetry

## Konfigurasi Poetry ##
poetry config virtualenvs.in-project true

## Meng-install paket-paket dan ketergantungan dengan Poetry ##
poetry install --no-dev
# Catatan: Saya menambahkan parameter '--no-dev'. \
# Karena dalam produksi, kita tidak perlu menambahkan modul \
# yang memang hanya di perlukan untuk Pengembangan, seperti PyLint.

## Membangun dan Menerbitkan Blog ##
poetry run make publish
