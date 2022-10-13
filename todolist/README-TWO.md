# Tugas 6 Pemrograman Berbasis Platform: Javascript dan Ajax

### Perbedaan antara _asynchronous_ dan _synchronous programming_
_Asynchronous programming_ bersifat multi-thread, hal ini berarti operasi atau program dapat dijalankan secara bersamaan. Hal ini disebabkan karena program dijalankan tanpa harus menunggu proses antrian _request_ dari client ke server dan dari server ke client. _Synchronous programming_ bersifat single-thread dan sequential, hal ini berarti operasi atau program dijalankan satu persatu. Hal ini disebabkan oleh sistem melakukan _blocking_ kepada operasi atau program selanjutnya.

### Paradigma _Event-Driven Programming_ dan contoh penerapan dalam tugas
Dalam pemrograman, _Event-Driven Programming_ merupakan paradigma di mana alur dari program ditentukan jalannya oleh _event_ atau sebuah perilaku yang dilakukan oleh _user_ seperti klik, sensor, dan pesan.<br>
Contoh penerapan dari konsep paradigma ini dalam tugas 6 adalah pada method `click()` pada tombol _add-task-ajax-btn_ yang nanti akan dijalankan _anonymous function_-nya

### Penerapan _asynchronous programming_ pada AJAX
AJAX menerapkan _asynchronous programming_ pada browser dengan mengeksekusi program dalam _framework_ Javascript. Ketika HTML dimuat, data dibaca melalui web server. Dengan AJAX, data dapat diperbarui tanpa harus me-_reload_ halaman web. Hal ini terjadi karena proses transfer data terjadi di web server pada _background_. Oleh karena itu, AJAX dapat bekerja dalam mengubah halaman web tanpa web perlu di-_reload_.

### Implementasi checklist tugas 6
1. Membuat views baru khusus untuk proses AJAX di `views.py` seperti fungsi `show_todolist_json` dan empat fungsi lain untuk menambah, menghapus, dan mengubah status dari task yang dimiliki oleh _user_. <br>
2. Mengatur _routing_ pada `urls.py` untuk fungsi-fungsi baru yang sudah dibuat di `views.py` secara bersesuaian.<br>
3. Membuat file `todolist-ajax.html` agar template pada tugas 4 dan 5 tidak diganti (karena belum demo tugas 4-5). <br>
4. Menambahkan link script Bootstrap JS dan jQuery di `todolist-ajax.html` agar dapat menggunakan modals dan AJAX yang telah disediakan oleh Bootstrap.<br>
5. Melakukan GET ke endpoint JSON untuk me-retrieve data, memproses setiap permintaan dan membuat tampilan HTML _card_ untuk setiap _task_ yang ada, kemudian menambahkannya kepada sebuah container untuk menampung _card-card_ yang ada. Pada tiap-tiap _card_ juga dibuat _widget_ tambahan seperti button, teks berisi status dari tugas, serta tanggal pembuatan task. Semua ini dilakukan di internal Javascript. <br>
6. Mengimplementasikan modal dari Bootstrap dengan tipe _Static backdrop_ dengan membuatnya di navbar serta menambahkan form pembuatan task baru di dalamnya. Kaitkan button `Add Task` dengan AJAX POST agar dapat menambahkan _card_ baru secara _asynchronous_. Juga terapkan reset form setiap penambahan task baru agar _text field_-nya kosong.<br>
7. Kaitkan button `Hapus Task` pada masing-masing card dengan AJAX DELETE agar dapat menghapus card task secara _asynchronous_ ketika diklik. <br>
8. Mengubah return render dari fungsi `show-todolist` di `views.py` dengan nama template `todolist-ajax.html` (hanya untuk tugas 6).<br>