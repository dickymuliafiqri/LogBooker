# LogBooker

## Tutorial Singkat

1. Edit isi file `data.example.json` dan rubah namanya menjadi `data.json`
2. Buat folder `static`
3. Taruh file laporan ke dalam folder tersebut, contoh: `1.png`, `ttd.png`, dll
4. Install requirements python dengan perintah `pip install -r requirements.txt`
5. Jalankan script dengan perintah `python main.py`
6. Jika semuanya benar, maka web akan bisa diakses di alamat `http://localhost:8080`

## Endpoint

- `/` -> Halaman utama, simpan halaman ini ke bentuk pdf untuk dijadikan laporan mingguan
- `/text` -> Menghasilkan laporan dalam format text, bigunakan untuk mengisi laporan harian
