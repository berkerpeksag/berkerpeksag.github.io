# Pyİst, Julython ve Pyresto

2012-08-08 18:44:21 | 2012-08-08 19:00:07

---

Yaklaşık 3 hafta önce Pyİst olarak Bahçeşehir Üniversitesi'nde Julython hackathon'ı düzenledik. Etkinliği son anda organize ettiğimden doğal olarak pek verimli geçmese de umarım katılan herkes(son saydığımızda 18 kişiydik) için farklı bir tecrübe olmuştur.

Julython, Temmuz ayı içinde daha önce başlayıp bitiremediğiniz ya da uzun zamandır başlamak isteyip de başlayamadığınız hobi projelerinizi 1 ay boyunca geliştirmeniz için teşvik eden bir proje.

Pyİst ekibi olarak Temmuz ayı boyunca birçok proje üzerinde çalıştık ancak ben bu yazıda hackathon'a yoğunlaşacağım.

## Pyresto

Pyresto, GitHub Badge'i geliştirirken ortaya çıkan ihtiyacı gidermek için geliştirilen bir proje. Hatta bir nevi GitHub Badge "spin-off"'u da diyebiliriz.

Julython öncesi projenin eksikleri şunlardı:

* Authentication desteği
* Farklı servislerin implementasyonu
* Birim testler

Authentication desteğini Samet Atdağ ve Bekir Doğan güzel bir pair programming örneğiyle tamamladılar. Hatta bu sayısı yazdığım an itibariyle 0.2 sürümü ile PyPI'daki yerini aldı.

Alper Kanat, her ne kadar anti-REST karşıtı BYK karşı çıksa da Twitter, Gökmen Görgen Bitbucket ben de Bugzilla implementasyonlarına başladım.

Benim Pyresto koduna BYK kadar hakim olmamam projeye girişi zorlaştırsa da gördüğü ilgi epey olumluydu.

## Darkside

Darkside'ı geliştirmeye başlama amacım Requests'in kodlarını incelerken çerezlerle alakalı bölümün gereğinden fazla karmaşık olmasıydı. Ayrıca, Python 3 ile birlikte biraz daha adam edilse de standard kütüphanede cookie ve cookielib modüllerini tek bir paket altında ve temiz bir API ile birleştirmekti. Henüz tasarım aşamasında olduğundan da yapılacak işler Pyresto'ya göre çok daha fazlaydı.

Serdar Dalgıç ile kod tabanının düzenlenmesi, 

## Sözlük

<!-- meta: archive(0) active(0) -->
