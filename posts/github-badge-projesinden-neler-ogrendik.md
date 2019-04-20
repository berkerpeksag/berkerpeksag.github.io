# GitHub Badge projesinden neler öğrendik

2012-05-06 12:52:30 | 2012-06-19 16:15:20

---

[GitHub Badge](http://githubbadge.appspot.com/) başlangıçta kullanıcıların
[GitHub ](https://github.com/) [profilleri](https://github.com/berkerpeksag) ile
ilgili birkaç istatistiki bilginin gösterileceği ve geliştiricilerin özgeçmişlerine
veya bloglarına koyabilecekleri basit bir bilgi alanından ibaretti. Aslında hala
öyle ancak "birkaç istatistiki bilgi" kısmını biraz genişlettik.

İlk sürümü yayınlandıktan sonra,

- [Google App Engine](http://appengine.google.com/)'in
  [ücret politikasının değişmesi](http://googleappengine.blogspot.com/2011/08/50-credit-for-new-billing-signups-and.html)
- Kullanıcı sayısının hızla artması
- Yeni eklenen özelliklerle uygulamanın kullandığı kaynağın artması

gibi nedenlerle mevcut yapı App Engine'in ücretsiz kullanım limitlerini zorlamaya
başladı.

### Ölçeklenebilirlik

#### Memcache

İlk yaptığımız şey üretilen HTML sayfasının belirsiz süreyle [Memcache](http://en.wikipedia.org/wiki/Memcache)
üzerinde önbelleğe alınmasıydı ki bu oldukça etkili bir çözüm oldu. Her ne kadar
sunduğumuz bilgiler her zaman en güncel bilgiler olmasa da iletilen bir şikayet olmadı.
Kaldı ki çoğu durumda GitHub'ın agresif önbellekleme stratejisinden dolayı GitHub
arayüzünden daha güncel veriler sunmamız rastlanmayan bir durum değil(eğer bir
projeyi veya kullanıcı takip etmediyseniz ya da bir gönderi yapmadıysanız profilinize
ait bilgiler GitHub Badge'e göre daha eski olabilir). Ancak gönderi yoğunluğunu
gösteren [sparkline](http://en.wikipedia.org/wiki/Sparkline) özelliği yayına girdiğinde
her öğenin yaşam süresini 24 saatle kısıtlamamız gerektiğine karar verdik.

Bu durumun üzerine "bizi destekleyin" ve "Google Analytics'i kapat" gibi HTML çıktısını
değiştiren özelliklerin eklenmesiyle sadece üretilen HTML sayfasının önbelleğe alınması
yetmemeye başladı. Bu durumu çözmek için hesaplanan kullanıcı bilgilerinin bulunduğu
sözlük nesnesini de JSON biçiminde önbellekte
[saklamaya ](https://github.com/berkerpeksag/github-badge/commit/8ac138464207a192687729e8e9af7db6448ac31f)
[başladık](https://github.com/berkerpeksag/github-badge/commit/3e6526459901f56734b72d54984c7621166f4c6a).

Google App Engine, Memcache kullanımını ücretlendirmediği için alabildiğimiz tüm bilgileri
Memcache ile önbelleğe aldık ya da önbelleğe aldığımız veri miktarını arttırmaya çalıştık.
Bu durum, artan günlük ziyaretçi sayımıza ve kullanıcılarımıza rağmen hala ücretsiz kullanım
sınırları içerisinde kalabilmemizin iki temel sebebinden bir tanesi.

#### Ön yüz

Ön yüzde neredeyse ilk sürümden beri HTML ve CSS sıkıştırma kullanıyoruz, Google App Engine
de gzip kısmını kendisi hallediyor. Buna ek olarak
[tüm sayfanın yarım günlüğüne tarayıcı önbelleğine alınması](https://github.com/berkerpeksag/github-badge/commit/08983f8d60e53a1798e07b2d772252eb1b65919a)
ve kişilerin GitHub'da görünen resimlerinin de sunucu tarafında yeniden boyutlandırılıp
[sayfaya gömülmesi](https://github.com/berkerpeksag/github-badge/issues/48) gibi optimizasyonlar
ile bant genişliğimizi oldukça etkin kullanmayı başardık.

### API kullanımı ve Pyresto

GitHub Badge'in ilk sürümünde, GitHub API'ı ilgili işleri yapmak, takipçi sayısı gibi
bilgileri hesaplamak için [bir nesne ve buna bağlı birkaç yöntem](https://github.com/berkerpeksag/github-badge/blob/v1/app.py#L23)
yeterliydi. Gönderi grafiği, kişinin kendisi dışındaki toplam proje takipçi sayısı gibi veri
işleme gerektiren, daha ayrıntılı bilgileri göstermek istediğimizdeyse bu basit sınıfın
işimizi görmeyeceğini anlayıp farklı çözümler aramaya karar verdik. Yaptığımız küçük araştırmada
GitHub için halihazırda yazılmış olan Python istemcilerinin ya eski ya da istediğimiz gibi
olmadığını gördük ve "[hepsine hükmedecek tek bir yüzük olmalı](http://en.wikipedia.org/wiki/One_Ring)"
diyerek "adam gibi yazılmış" [REST](http://en.wikipedia.org/wiki/REST) tabanlı her türlü
uygulama arayüzü ile çalışacak bir [ORM](http://en.wikipedia.org/wiki/Object-relational_mapping)
projesi yazmaya karar verdik. İlk kurbanımız elbette ki GitHub olacaktı.

Bu noktada GitHub'ın sunduğu uygulama geliştirme arayüzünün [üçüncü sürümünün](http://developer.github.com/v3/)
gerçekten mükemmele çok yakın olduğunu, mükemmel olmayan kısımlarında da GitHub ekibinin
yaptığımız hata bildirimleri ve özellik isteklerine olumlu ve hızlı yanıt verdiğini belirtmekte
fayda var ki bu da geliştirme sürecinde işimizi oldukça kolaylaştırdı. Pyresto'nun asıl yaptığı
şey veri ile uğraşmak isteyen programcıyı arkaplanda dönen karmaşık işlemlere bulaştırmamak,
basitçe onun önünden çekilmek ve veriyle rahatça uğraşmasına izin vermek, bunu yaparken de
farklı platformların geliştirme arayüzü tanımlamalarını olabildiğince basite indirgemek.
Örneğin şu an kullanmakta olduğumuz GitHub modülü sadece
[70 satırlık bir dosya](https://github.com/BYK/pyresto/blob/e51003d47ab747650d627f134861c151b6af0e30/pyresto/apis/GitHub.py)dan
ibaret. Bu kod elbette tam değil ve her şeyi kapsamıyor ancak yaptığımız ve sıradan olmaktan
uzak GitHub uygulaması için fazlasıyla yeterli. İşin güzel yanı bu 70 satırın çoğu aslında
veri modelini tanımlıyor, yani gerçek kod değil.

Sözün özü GitHub Badge projesinin kalbinde aslında Pyresto yatıyor ve bir sonraki hedefimiz
bu kütüphaneyi hem belgelemesi hem de testleri ile herkesin rahatça kullanabileceği bir hale
getirip yaygınlaşmasını sağlamak. Şu anki hali de [PyPI üzerinden indirilebilir durumda](http://pypi.python.org/pypi/pyresto/).

### Arayüz

Eklenen yeni özelliklerle beraber, bu özelliklerin son kullanıcıya nasıl sunulacağı da önemli
bir soru haline geldi. Bu nedenle arayüz toplamda üç kez değişti. Bu süreç, ürünün özelliklerini
kısıtlı bir alanda, kullanıcının kafasını karıştırmadan, mümkün olan en sade ve güzel tasarımla,
olabilecek en fazla bilgiyi sunmaya çalışmak gibi hedefler nedeniyle epey öğretici ancak bize
göre sunum konusunda hala olması gerekenden uzakta olan bir tasarım deneyimi oldu. Yani bu
konuda [tavsiyelere açığız](https://github.com/berkerpeksag/github-badge/issues/new).

### Açık kaynak topluluğu ile iletişim

GitHub Badge öncesinde başta [Mozilla](http://www.mozilla.org/contribute) ve [Python](http://www.python.org/)
olmak üzere açık kaynak projelere katkıda bulunuyorduk ancak [jGrow](https://github.com/berkerpeksag/jGrow)
haricinde sıfırdan yazdığımız ve topluluktan geribildirim aldığımız bir proje geliştirmemiştik.
GitHub Badge ilk katkılarını yayına girdikten birkaç saat sonra aldı. Test sürecinde farketmediğimiz
hataları da yine bu sayede düzelttik.

Bir açık kaynak projeye katkıda bulunmanın tek yolu kod yazmak değil. Başlangıçta çok basit olarak
düşündüğümüz proje, [Emre Sevinç](https://github.com/emres)'in [katkılarıyla](https://github.com/berkerpeksag/github-badge/issues/8)
çok daha fazla bilgi sunar hale geldi. Her ne kadar yeni sürümlerde eklediğimiz JSONP ve CORS
tabanlı API'lar için beklediğimiz geri bildirimi alamamış olsak da sağlıklı bir açık kaynak proje
nasıl olur ve nasıl gelişir konularında bir miktar tecrübe kazandık.

> Bu yazı projenin diğer geliştiricisi olan [Burak Yiğit Kaya](http://twitter.com/madBYK) ile
> birlikte hazırlanmış olup, kendisinin [blogunda](http://blog.byk.im/) da [yayınlanmıştır](http://blog.byk.im/2012/05/github-badge-projesinden-neler-ogrendik.html).

<!-- meta: archive(0) active(1) -->
