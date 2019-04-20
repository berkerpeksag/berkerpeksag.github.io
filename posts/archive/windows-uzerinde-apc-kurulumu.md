# Windows işletim sistemi üzerine APC kurulumu

2009-01-12 02:35:20 | 2012-03-18 00:01:00

---

APC, PHP tarafından PECL eklentisi olarak geliştirilen bir cache sistemidir. Kurulumunun ve kullanımının kolay olması nedeniyle memcached yerine tercih edilebilir.

APC eklentisini Windows işletim sistemi üzerinde kulanmak için birkaç seçenek mevcut.

- PEAR ile kurulum
- Kaynak pakediyle derleme
- PECL eklentisi(dll) olarak kurulum

Ben üçüncü ve en hızlı çözümü seçtim.

**Kurulum**

- Kurulu PHP sürümünüze uygun `php_apc.dll` dosyasını indirin. *5.2.x* sürümü için uygun DLL'i [buradan indirebilirsiniz](http://kromann.info/php5_2-Release_TS/php_apc.dll).
- İndirdiğiniz `php_apc.dll` dosyasını PHPyi kurduğunuz dizindeki `/ext` klasörü içine kopyalayın. Örneğin: `d:\php\ext\php.ini` dosyasını açıp şu satırı ekleyin: `extension = php_apc.dll`.

Kurulumu test etmek için boş bir sayfa oluşturup aşağıdaki kodu yazın:

    <?php phpinfo();

Herhangi bir hata almadıysanız APC kurulumunu başarıyla tamamladınız demektir. Bundan sonraki yazılarımda APCnin nasıl kullanılabileceğini anlatacağım.

<!-- meta: archive(1) active(1) -->
