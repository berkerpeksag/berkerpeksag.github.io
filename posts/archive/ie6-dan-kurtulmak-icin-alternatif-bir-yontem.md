# Internet Explorer 6'dan kurtulmak için alternatif bir yöntem

2009-07-14 11:52:41 | 2009-07-14 11:52:41

---

Fatih Hayrioğlu'nun FriendFeed'deki [Internet Explorer 6 konulu girdisinde](http://friendfeed.com/fatihhayri/531eb2bb/nternet-explorer-6-ile-u-ra-rken-arabesk), sadece IE6 kullanıcıları için tarayıcıyı kilitleyecek bir kod yazmayı [önermiştim](http://friendfeed.com/fatihhayri/531eb2bb/nternet-explorer-6-ile-u-ra-rken-arabesk#c-33df807337684ebd97f24da99966c94c).

Bugün, uykusuzluğumu da gidermek amacıyla küçük bir çalışma yaptım. Aşağıdaki kod ile, sayfayı IE6 ile ziyaret ederseniz tarayıcı göçecektir :)

    var IE6 = false /*@cc_on || @_jscript_version &lt;= 5.7 @*/;
    if (IE6) for (x in document.write) document.write(x); // [1]

[1] [Wikipedia](http://en.wikipedia.org/wiki/Internet_explorer_6#Criticism)

<!-- meta: archive(1) active(1) -->
