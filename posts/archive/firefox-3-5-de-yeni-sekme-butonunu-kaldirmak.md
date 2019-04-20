# Firefox 3.5'te yeni sekme butonunu kaldırmak

2009-08-17 02:09:47 | 2009-08-17 02:09:47

---

Hep unuttuğum için buraya not düşüyorum. Firefox 3.5 ile gelen yeni sekme butonuna alışamayanlardansanız, çözüm basit:

`C:\Documents and Settings\Berker Peksağ\Application Data\Mozilla\Firefox\Profiles\8y2epd80.default\chrome` yolunu takip edip, `userChrome-example.css` dosyasının kopyalayın ve adını `userChrome.css` değiştirip şu kodu ekleyin:

    .tabs-newtab-button { display: none !important; }

Tarayıcınızı yeniden başlattığınızda, buton gözükmeyecektir.

<!-- meta: archive(1) active(1) -->
