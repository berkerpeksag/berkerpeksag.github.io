# uEmacs/PK'i denedim

2013-07-28 20:43:52.749708 | 2013-12-27 17:27:54.541554

---

Emacs'i bir süredir daemon olarak çalıştırıyorum ama Ubuntu üzerinde genelde çöküp duruyor. Henüz oturup araştırmaya vakit bulamadım(yani üşendim). Genellikle o an yaptığımla işle alakasız bir dosyayla uğraşmam gerektiğinde hızlıca Vim ile hallediyordum.

Bugün [/r/emacs/](http://www.reddit.com/r/emacs/)'te [Famous Emacs users](http://www.reddit.com/tb/1ix4ro) yazısını gördükten sonra aklıma UEmacs/PK geldi ve denemeye karar verdim.

Eğer benim gibi kod yazmanız gerekirken alakasız bir dolu şey yapmaya bayılıyorsanız denemek için:

    :::bash
    $ git clone http://git.kernel.org/pub/scm/editors/uemacs/uemacs.git/
    $ make
    $ sudo make install

`C-x C-f`, `C-g` gibi bazı temel Emacs kısayolları sorunsuzca çalışıyor. Okuduğum belgelere göre GNU Emacs'e göre epey farklılıklar da varmış.

Özelleştirmeyle biraz daha uğraştıktan sonra benzer "düzenle ve çık" işleri için Vim yerine uEmacs'i kullanmayı deneyeceğim.

<!-- meta: archive(0) active(0) -->
