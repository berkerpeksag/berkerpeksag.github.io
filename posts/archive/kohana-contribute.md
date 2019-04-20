# Kohana'ya katkıda bulunmak için geliştirme ortamının hazırlanması

2010-06-13 22:20:18 | 2010-06-13 22:20:18

---

Kohana, geliştirilmesine CodeIgniter forku olarak başlanıp 3.x versiyonuyla beraber en baştan yazılan popüler bir PHP frameworküdür. Bu yazıda, Kohana projesine katkıka bulunmak için bir geliştime ortamının hazırlanmasını anlatacağım. Yazıyı, temel seviyede Git ve GNU/Linux bilginizin olduğunu varsayarak hazırladım.

Kohana, Github üzerinden geliştiriliyor. Bundan sonra sık sık kullanacağımız issue list ise Kohana'nın kendi web sitesinde görülebilir. İlk iş olarak Kohana için bir klasör oluşturup, Git'i aktive edelim:

    mkdir kohana/
    git init

`kohana/` klasörünü yazdığımız kodları uygulama üzerinde denemek/geliştirmek gibi amaçlar için kullanacağız. Şimdi asıl geliştirme yapacağımız çekirdek kodları eklemeye geldi. Devam etmeden önce, GitHub hesabınızdan [kohana/core](https://github.com/kohana/core) projesini fork etmelisiniz. GitHub üzerinde forkunuzu oluşturduktan sonra, bu depoyu klonlayacağız:

    git clone git@github.com:berkerpeksag/core.git system

Burada, göreceğiniz üzere sizin forkunuzunu klonladık. Şimdi, ana depodaki güncellemeleri çekip, bizim güncellemelerimizle birleştirmek, kısacası depoyu güncel tutmak için hayati öneme sahip remote ayarlarını yapacağız:

    git remote add upstream git://github.com/kohana/core.git
    git fetch upstream

Eğer her şey yolunda gittiyse, aşağıdaki gibi bir çıktıyla karşılaşmalısınız:

    berkerpeksag@berkerpeksag:/var/www/kohana/system$ git fetch upstream
    From git://github.com/kohana/core
    * [new branch]      inline_route_regex -> upstream/inline_route_regex
    * [new branch]      master     -> upstream/master
    * [new branch]      testing     -> upstream/testing
    * [new branch]      text_binary -> upstream/text_binary
    * [new branch]      text_number -> upstream/text_number
    * [new branch]      unstable   -> upstream/unstable

Gördüğünüz gibi tüm branchler oluşturuldu. Şimdi değişiklikleri commit edebiliriz:

    git add .git commit -m "Çekirdek kodları eklendi."

Asıl işi yaptıktan sonra varsayılan Kohana klasör yapısını oluşturacağız. Çoğu Kohana projesinin klasör yapısı aşağıdaki gibidir:

    application/
    application/cache
    application/config
    application/views
    application/logs
    application/classes
    application/classes/model
    application/classes/controller

Sırasıyla klasörlerimizi oluşturalım:

    mkdir -p application/classes/{controller,model}
    mkdir -p application/{config,views}

`cache/` ve `logs/` klasörlerine yazma izni verelim:

    mkdir -m 0777 -p application/{cache,logs}

Yine herhangi bir hata almazsanız klasör yapısı aşağıdaki gibi olacaktır. Test etmek için:

    berkerpeksag@berkerpeksag:/var/www/kohana$ find application/
    application/
    application/cache
    application/config
    application/views
    application/logs
    application/classes
    application/classes/model
    application/classes/controller

`cache/` ve `logs/` klasörleri aksi belirtilmediği sürece çalışma zamanında çeşitli dosyalar oluşturacaklardır. Geliştirme süresince bu dosyalara Git'in ihtiyacı olmayacağı için bunları gözmezlik gelmesini söylemeliyiz:

    touch .gitignore
    sudo gedit .gitignore

İçerik olarak aşağıdaki şekilde doldurup kaydedip, kapatalım:

    application/cache/*
    application/logs/*

Şimdi proje için gerekli diğer dosyaları indirelim:

    wget --no-check-vertificate https://github.com/kohana/kohana/raw/master/index.php
    wget --no-check-certificate https://github.com/kohana/kohana/raw/master/application/bootstrap.php -O application/bootstrap.php
    wget --no-check-certificate https://github.com/kohana/kohana/raw/master/application/classes/controller/welcome.php -O application/classes/controller/welcome.php
    wget --no-check-certificate https://github.com/kohana/kohana/raw/master/example.htaccess -O .htaccess

Evet, işimiz bitti ve değişiklikleri Git'e bildirip commit edebiliriz:

    git add .git commit -m "Klasör yapısı oluşturuldu."

Artık, `application/bootstrap` dosyasından gerekli ayarları yapıp, projeye katkıda bulunmaya başlayabilirsiniz. Geliştirme süresince, kendi kodunuzu ana proje ile sürekli eş tutmanız gerekecek. Bunun için [`sync.sh`](https://gist.github.com/436936) betiğini kullanabilirsiniz.

Kullanmak için:

    sudo chmod +x sync.sh

komutunu uygulamanız yeterli.

<!-- meta: archive(1) active(1) -->
