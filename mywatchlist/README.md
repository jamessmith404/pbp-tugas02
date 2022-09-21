# Tugas 3 Pemrograman Berbasis Platform

## Perbedaan HTML, JSON, dan XML

1. JSON<br>
   _JavaScript Object Notation_ atau JSON adalah format yang ringan untuk menyimpan dan mengirim data (_data delivery_). JSON bersifat _self-describing_ serta mudah dimengerti karena format yang digunakan adalah sebuah _key-value pair_ seperti _dictionary_ di Python. JSON juga dapat menggunakan konsep _nested_ dalam menyajikan datanya. File JSON akan disimpan dengan ekstensi `.json`. 

2. XML<br>
   _Extensible Markup Language_ atau XML merupakan _markup language_ yang memiliki fungsi utama seperti JSON, yaitu untuk menyimpan dan mengirim data (_data delivery_). Namun, hal yang membedakan antara XML dengan JSON adalah formatnya yang cukup serupa dengan HTML, di mana XML menggunakan _tags_. File XML akan disimpan dengan ekstensi `.xml`.

3. HTML<br>
   _Hypertext Markup Language_ atau yang biasa dikenal dengan HTML adalah bahasa _markup_ yang digunakan untuk membuat dan menampilkan halaman pada website. HTML terdiri dari beberapa elemen yang merupakan kombinasi teks dan simbol dan nantinya akan disimpan dalam sebuah file berekstensi `.html` Dalam membuat halaman web, kita menggunakan format _tags_.

JSON lebih _favorable_ dibanding XML karena bentuk _formatted_ dari JSON lebih rapi dan mudah dilihat dibandingkan dengan XML karena JSON menggunakan _dictionary_, dibandingkan XML yang menggunakan _tags_ yang bila dibuat bersarang akan sulit untuk dibaca

### Pentingnya _Data-Delivery_ dalam Platform
_Data Delivery_ sangatlah vital pada platform karena mekanisme tersebut berfungsi agar terjadi sirkulasi data dari _database_ (backend) ke _template_ (frontend) serta sebaliknya. Bila tidak ada _data delivery_, data dari _database_ tidak dapat ditampilkan ke _user_ sehingga aplikasi menjadi tidak berguna. 


### Implementasi Checklist Tugas 3
Pertama-tama, saya membuat aplikasi baru bernama `mywatchlist` dengan me-run perintah
```
python manage.py startapp mywatchlist
```
Hal ini bertujuan untuk membuat `django-app` baru dengan folder bernama `mywatchlist` pada _local_. Setelah itu, tambahkan _path_ `mywatchlist` pada _settings.py_ di variabel INSTALLED_APPS serta _urls.py_ path-path untuk penyajian data HTML, XML, dan JSON. Lalu, buat class baru bernama MyWatchList dengan atribut-atribut seperti yang diminta soal sesuai dengan kebutuhannya. Setelah itu, kita jalankan
```
python manage.py makemigrations
python manage.py migrate
```
Kode di atas bertujuan untuk mempersiapkan dan melaksanakan skema model dalam _database_. Setelah itu, kita membuat folder bernama `fixture` di dalam aplikasi `mywatchlist` dan membuat file bernama `initial_watchlist_data.json` yang berisi 10 data dari class `MyWatchList` yang telah dibuat sebelumnya. Lalu, saya menjalankan perintah `python manage.py loaddata initial_wishlist_data.json` untuk memasukkan data tersebut ke dalam _database_ lokal.

Setelah itu, saya lanjutkan dengan menyajikan data dalam HTML, XML, dan JSON dengan membuat 3 fungsi yang me-handle masing-masing format di `views.py` di folder `mywatchlist`. Untuk HTML, saya me-_retrieve_ semua data pada _database_, dalam kasus ini adalah `initial_watchlist_data.json`, serta dimasukkan ke dalam _dictionary_ `context`. Hal ini dilanjutkan dengan menggunakan fungsi `render()` yang di-import sebelumnya. Di bagian bonus, saya menambahkan variable `watched` dan `not_watched` untuk menentukan apakah user banyak atau sedikit menonton kemudian saya masukkan pada `context` dengan key `is_watchlist`. Data pada `context` akan ditampilkan di `mywatchlist.html` untuk format HTML.

Pada XML dan JSON, seperti pada HTML, saya me-_retrieve_ semua data pada _database_. Namun, yang berbeda adalah fungsi untuk kedua format ini mengembalikan `HttpResponse` yang isinya adalah data yang di-serialize sesuai dengan tipe kontennya.

Dalam _routing_ HTML, JSON, dan XML, saya sudah menambahkannya sebelumnya dengan menambahkannya dari `views.py` yang ada di `mywatchlist` sebelumnya (penjelasan pada paragraf 2). 

Dalam melakukan _deployment_, saya hanya me-push ke remote dari Tugas 2 PBP sebelumnya yang sudah di-deploy sehingga projek kali ini langsung ter-deploy ulang.

### Pemeriksaan _Routes_ dengan Postman

1. `~/mywatchlist/html`<br><br>

   ![postman_HTML_Tugas3](https://user-images.githubusercontent.com/107617626/191416556-2e4557ae-e318-47a1-a64b-9dda8ed3e941.png)

2. `~/mywatchlist/json`<br><br>
   ![postman_JSON_Tugas3](https://user-images.githubusercontent.com/107617626/191416575-4625d37d-5c8a-4798-8fda-29703b919ee5.png)

3. `~/mywatchlist/xml`<br><br>
   ![postman_XML_Tugas3](https://user-images.githubusercontent.com/107617626/191416585-af70e67a-394e-45a1-be8f-fc19afefa335.png)
