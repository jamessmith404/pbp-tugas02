## Link Repository
https://james-pbp-tugas2.herokuapp.com/

## Bagan *Request Client* ke Web Aplikasi berbasis Django

![BaganMVT_Tugas2](https://user-images.githubusercontent.com/107617626/189880988-11b9aec3-7bad-4ca6-ad96-60eb44072b54.png)


### Penjelasan Bagan di Atas
Ketika *user* membuka peramban, ia mengetik URL di laman pencarian. Ketika user menekan ENTER, peramban akan melakukan HTTP request kepada server yang menyimpan semua data website tersebut. Server merespons dengan me-run aplikasi Django, melalui *manage.py*. Saat dijalankan, aplikasi akan membaca URL route dari URL yang sudah diinput oleh user. Dalam tugas kali ini misalnya, jika user mengetikkan https://james-pbp-tugas2.herokuapp.com/katalog, maka URL Route menjadi "/katalog".

Django akan mengakses *urls.py* serta mencari *pattern* yang cocok dengan *urlpatterns*. Jika ditemukan, *urls.py* akan memanggil *function* sesuai dengan URL yang dimaksud. Tetapi jika tidak ditemukan *pattern*-nya, maka Django memanggil *error handler* untuk memanggil halaman error dengan kode 404 (not found).

*views.py* dapat dikatakan sebagai "*controller*" dari Django. Program tersebut akan menerima *web request*, berkomunikasi dengan *database* melalui *models.py* untuk mengambil/menulis/menghapus data, mengatur bagaimana data ditampilkan pada *template*, serta memilih *template* sesuai dengan permintaan sebelumnya.

Susunan data yang ada disimpan pada program *models.py* sehingga model mengatur pengelolaan data serta *query* ke *database*.

Halaman yang nantinya muncul ke layar *user* adalah hasil respons *webserver* atas HTTP request yang dilakukan sebelumnya, dalam bentuk file *.html*. File-file ini disimpan dalam *templates*.

## Mengapa Menggunakan *Virtual Environment*?
Penggunaan *Virtual Environment* sebenarnya tidak diwajibkan. Kita akan tetap dapat membuat aplikasi tanpanya. Namun, hal tersebut direkomendasikan karena *Virtual Environment* membantu untuk mengatur *dependencies* yang dibutuhkan dalam masing-masing *project* agar tetap terpisah satu sama lain dengan membuat sistem yang terisolasi untuk masing-masing *project*. Hal ini berguna agar *developer* dapat me-*maintain* *project* tersebut lebih mudah untuk skala yang besar dan yang memakan waktu yang cukup lama. Tanpa *Virtual Environment*, *environment* global kita akan berantakan sehingga kita sulit untuk menjalankan *project* yang berbeda-beda dalam waktu yang berdekatan.

## Cara Pengimplementasian Program Tugas 2
Pertama-tama, dengan memanfaatkan *template* yang ada saya menambahkan fungsi yang ada pada *views.py*, yaitu *show_katalog*. Lalu, dilanjutkan dengan mengambil dari *database* semua data yang ada di entitas CatalogItem. Saya melanjutkan dengan membuat dan melengkapkan dictionary *show_katalog* dengan key-value pair nama pribadi serta NPM saya. Kemudian, dictionary tersebut akan di-*forward* ke file html.

Kedua, saya melengkapkan isi *urls.py*, yaitu *urlpatterns* yang berisi list yang menyimpan semua *routing* URL ke katalog app, sesuai dengan fungsi yang ada. 

Ketiga, saya mengiterasi *list_katalog* untuk memetakan semua data yang diteruskan dari fungsi *show_katalog* pada views. Hal ini dilakukan di file *katalog.html*. Data diakses dengan syntax "{{\<KEY>}}.

Terakhir, saya membuat aplikasi baru pada Heroku. Setelah itu saya menambahkan *secrets* "HEROKU_API_KEY" dan "HEROKU_API_NAME" pada repository Tugas 2 ini. Setelah itu, melakukan *redeploy* di file dpl.yml. Aplikasi berhasil dibuat dan tinggal dijalankan
