# Internet Explorer'daki setAttribute sorunu

2009-11-18 11:18:35 | 2009-11-18 11:18:35

---

Bugün, Internet Explorer'ın başa bela sorunlarından biriyle daha karşılaştım. Eğer, aşağıdaki gibi bir kodunuz varsa Internet Explorer'da çalışmayacaktır.

    var div = document.createElement(div);
    div.setAttribute('style', 'border: 1px solid #ff0000');
    div.innerHTML = 'Iron Maiden'\s gonna get all of you!';

`QuirksMode` sağolsun, Internet Explorer 8. sürümüne kadar `setAttribute` style niteliğini set etmiyormuş. Çözüm için kodumuzda küçük bir değişiklik yapmak yeterli:

    var div = document.createElement(div);
    div.style.cssText = 'border: 1px solid #ff0000;';
    div.innerHTML = 'Iron Maiden'\s gonna get all of you!';

<!-- meta: archive(1) active(1) -->
