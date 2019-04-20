# Ubuntu update manager sorunu

2010-10-10 18:09:08 | 2010-10-10 18:09:08

---

Bir süredir Ubuntu'mda update manager'ı çalıştırırken aşağıdaki gibi bir hata alıyordum:

    berkerpeksag@berkerpeksag:/var/www$ update-manager
    Traceback (most recent call last):
    File /usr/bin/update-manager, line 32, in
    from UpdateManager.UpdateManager import UpdateManager
    File /usr/lib/python2.6/dist-packages/UpdateManager/UpdateManager.py, line 30, in 
    import gconfImportError: No module named gconf

Bugün tembellik yapıp ertelediğim sorunu çözmek için biraz araştırma yaptım. Bulunamayan `python-gconf` modülünü reconfigure ederek problemimi çözdüm:

    sudo dpkg-reconfigure python-gconf

<!-- meta: archive(1) active(1) -->
