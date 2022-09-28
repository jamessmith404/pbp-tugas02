# Tugas 4 Pemrograman Berbasis Platform: Pengimplementasian Form dan Autentikasi Menggunakan Django

### Kegunaan `{% csrf_token %}` pada elemen `<form>` dan apa yang terjadi bila tidak ada potongan kode tersebut.
Kode `{% csrf_token %}` pada elemen `<form>` adalah mekanisme pertahanan yang dibuat oleh _framework_ Django dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah serangan yang memaksa end-user untuk menjalankan/mengeksekusi tindakan yang tidak diinginkan pada aplikasi web. Bila tidak ada potongan kode tersebut pada `<form>`, ketika aplikasi web mendapat serangan CSRF, terlebih pada akun administratif, maka hal tersebut akan membahayakan aplikasi web secara keseluruhan. Hal-hal seperti pencurian data, eksploitasi akun, hingga perusakan sistem bisa terjadi.

### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Elemen `<form>`, layaknya GUI pada Java, dapat dibuat secara manual tanpa menggunakan generator. Secara gambaran besar, `<form>` dapat dibuat dengan menginisalisasinya terlebih dahulu, kemudian mengisi bagian _body_ dengan elemen-elemen yang dibutuhkan.
```html
<form>
    <!-- body -->
</form>
```
Terdapat banyak atribut yang dapat ditambahkan kepada bagian _body_ pada `<form>`. Namun, atribut yang paling sering digunakan adalah `<input>`. `<input>` ini juga dapat ditampilkan dengan beragam bentuk, tergantung dari `type`-nya. Contohnya antara lain,

`<input type="text">`    : Input untuk baris tunggal<br>
`<input type="radio">`   : Input berupa _radio button_<br>
`<input type="checkbox">` : Input berupa kotak yang bisa dicentang<br>
`<input type="submit"> ` : Input berupa tombol submisi form<br>
`<input type="button">` : Input berupa tombol yang dapat diklik

### Proses alur data dari submisi yang dilakukan oleh pengguna
Ketika user menekan tombol _submit_, server akan menerima data form dengan _values_ dari web browser kita. Data tersebut perlu divalidasi terlebih dahulu. Bila datanya tidak valid, server harus menampilkan formnya kembali dengan data yang telah di-_input_ user pada fields yang bersesuaian beserta pesan error-nya.

Setelah data yang di-_input_ valid dan tombol _submit_ kembali ditekan, server akan menerima _request_ dan server dapat menjalankan tindakan yang tepat sesuai dengan yang di-_request_ oleh user (seperti menyimpan data, mencari data pencarian, mengunggah file, dan lainnya), kemudian mengembalikan pesan berhasil dan mengarahkan browser ke laman yang bersesuaian dengan _routing_.

Untuk kasus tambah/modifikasi data, data yang sudah diinput akan masuk ke dalam models, kemudian dari models akan diolah dan disimpan di _database_. Untuk kasus pencarian data, data yang dibutuhkan akan diambil dari models ke views, kemudian dari views diproses untuk ditampilkan di template.  

### Implementasi Checklist Tugas 4
Pertama-tama, saya menjalankan _virtual environment_ di Command Prompt. Setelah itu membuat aplikasi baru bernama `todolist` dengan me-run perintah
```
python manage.py startapp todolist
```
Hal ini bertujuan untuk membuat `django-app` baru dengan folder bernama `todolist` pada _local_. Setelah itu, tambahkan _path_ `todolist` pada _settings.py_ di variabel INSTALLED_APPS pada folder `project-django`.

Setelah itu, saya melakukan routing di _urls.py_ untuk pengaksesan _page_ http://localhost:8000/todolist. Lalu, buat class baru bernama `Todolist` dengan atribut-atribut seperti yang diminta soal sesuai dengan kebutuhannya di `models.py`. Setelah itu, saya jalankan
```
python manage.py makemigrations
python manage.py migrate
```
Kode di atas bertujuan untuk mempersiapkan dan melaksanakan skema model dalam _database_. Setelah itu, saya lanjutkan dengan mengimplementasikan form registrasi, login, dan logout.

Untuk form registrasi, saya membuat file `register.html` di folder `templates`. Setelah itu, saya menuliskan judul di blok `meta` serta membuat _division_ class bernama `login`. Isi dari `login` adalah _header_ registrasi, kemudian dilanjutkan dengan menuliskan blok `form` bertipe POST yang berisi `csrf_token` (sebagai _safety measure_) serta `table` yang isinya form yang di-_generate_.

Untuk login, saya membuat file `login.html` di folder `templates`. Setelah itu, saya menuliskan judul di blok `meta` serta membuat _division_ class bernama `login`. Isi dari `login` adalah _header_ login, kemudian dilanjutkan dengan menuliskan blok `form` bertipe POST yang berisi `csrf_token` (sebagai _safety measure_) serta `table` yang isinya adalah `<input>` yang bertipe text untuk menulis username, password untuk menulis password, dan btn login_btn sebagai tombol login.

Untuk landing page utama, todolist, saya membuat file `todolist.html` di folder `templates`. Kemudian, saya membuat sebuah `table` yang berisi task-task yang sudah ada dan dimiliki oleh suatu user tertentu serta setiap atributnya. Saya juga membuat tombol `Buat Task Baru` dan `Logout` agar user bisa menambah task baru atau keluar dari akun yang sedang digunakan.Untuk bagian bonus, saya membuat tombol `Selesai` dan `Belum Selesai` untuk mengubah atribut `is_finished`, serta `Hapus Task` untuk menghapus task tertentu berdasarkan urutan task-nya.

Untuk laman pembuatan task baru, saya membuat file `create-task.html` di folder `templates`. Setelah itu, saya menuliskan judul di blok `meta` serta membuat _division_ class bernama `login`. Isi dari `login` adalah _header_ tambah task, kemudian dilanjutkan dengan menuliskan blok `form` bertipe POST yang berisi `csrf_token` (sebagai _safety measure_) serta `table` yang isinya adalah `<input>` yang bertipe text untuk menuliskan nama task, btn login_btn sebagai tombol untuk menambah task, serta `textarea` untuk field menulis deskripsi tugas

Di `views.py`, saya membuat beberapa fungsi yang akan me-handle request dari user dan me-import beberapa library yang dibutuhkan, seperti yang sudah dijelaskan di Lab03. Fungsi yang saya buat ada 8, antara lain:

1. show_todolist(), fungsi ini dibuat untuk menampilkan daftar todolist yang sudah dibuat oleh user tertentu. Dibuat dengan me-retrieve data yang ada di models dengan filter username dari akun yang sedang login, kemudian saya masukkan ke dalam `context` beserta dengan nama user. Data pada `context` akan ditampilkan di `todolist.html`
2. create_task(), fungsi ini dibuat untuk user dapat menambah task. Dibuat dengan mengecek apakah tipe request user adalah POST. Jika iya, akan membuat objek Task baru berdasarkan judul dan deskripsi yang diinput beserta waktu kapan sang user membuatnya. Jika tidak, me-refresh laman.
3. delete_task(), fungsi ini dibuat untuk user dapat menghapus task yang sudah ada. Dibuat dengan me-retrieve objek Task yang ingin dihapus berdasarkan index kemudian dihapus. Lalu, akan me-refresh laman
4. done_task(), fungsi ini dibuat untuk user dapat menandai task yang sudah diselesaikan. Dibuat dengan me-retrieve objek Task yang ingin ditandai selesai berdasarkan index kemudian mengubah atribut `is_finished` nya menjadi True. Lalu, akan me-refresh laman
5. undone_task(), fungsi ini dibuat untuk user dapat menandai task yang sudah diselesaikan menjadi belum. Dibuat mirip seperti done_task(), tetapi yang membedakan hanyalah mengubah atribut `is_finished` nya menjadi False.
6. logout_user(), fungsi ini dibuat agar user yang sudah login dapat logout. Dibuat dengan me-logout user, kemudian mengarahkan ke laman login serta menghapus _cookie_ user.
7. register(), dibuat agar pengguna dapat membuat akun baru dengan _username_ dan _password_ tertentu. Dibuat dengan mengecek apakah tipe request user adalah POST. Jika iya, akan membuat user baru dari class UserCreationForm dan di-assign ke variable `form`, jika tidak ada error pada `form`, maka akan memunculkan prompt berhasil dan mengarahkan ke laman login. Jika tidak, me-refresh laman.
8. login_user(), dibuat agar pengguna dapat login menggunakan akun mereka dan menggunakan fitur dari web app Todolist. Dibuat dengan mengecek apakah tipe request user adalah POST. Jika iya, akan me-otentikasi username dan password berdasarkan _database_. Jika benar, akan membuat respons untuk diarahkan ke laman todolist dan _cookie_ untuk me-record activity. Jika tidak, akan menunjukkan prompt kesalahan serta me-refresh laman.

Fungsi pada poin 1-6 dilengkapi _decorator_ @login_required agar pengaksesan fitur tersebut hanya bisa dilakukan ketika user sedang dalam kondisi login.

Untuk pembuatan akun dan _dummy_ data, saya memanfaatkan laman register untuk membuat akun, login, kemudian create-task untuk menambah _dummy_ data.

Dalam _routing_, saya menambahkan fungsi-fungsi dari `views.py` yang ada di `todolist` sebelumnya ke `urlpatterns` yang ada di `urls.py` dengan nama _route_ yang bersesuaian dengan fungsi.

Dalam melakukan _deployment_, saya hanya me-push ke remote dari Tugas 2 PBP sebelumnya yang sudah di-deploy sehingga projek kali ini langsung ter-redeploy oleh Github ke Heroku.