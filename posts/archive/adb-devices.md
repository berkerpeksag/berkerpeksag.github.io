# adb devices

2010-06-05 00:00:35 | 2010-06-05 00:00:35

---

Google Nexus One'ımı kurcalama serüvenim devam ediyor. Yardımlarından ötürü Murat Koç'a teşekkür etmeden geçmek olmaz :) Kurcalarken yaşadığım sorunları ve çözümlerini küçük notlar halinde yazacağım. Ubuntu GNU/Linux üzerinde Android SDK'ini kurduktan sonra, `adb devices` komutunu çalıştırdığımda aşağıdaki hatayı aldım.

    berkerpeksag@berkerpeksag:~/android/android-sdk-linux_86/tools$ adb devices
    List of devices attached ???????????? no permissions

Sebebini yetki problemi olduğunu düşündüm ama yine de küçük bir araştırma yaptım. Aşağıdaki şekilde root yetkisiyle denediğimde sorunsuzca cihazımı görüntüleyebildim:

    berkerpeksag@berkerpeksag:~/android/android-sdk-linux_86/tools$ adb kill-server
    berkerpeksag@berkerpeksag:~/android/android-sdk-linux_86/tools$ sudo ./adb start-server
    * daemon not running. starting it now *
    * daemon started successfully *
    berkerpeksag@berkerpeksag:~/android/android-sdk-linux_86/tools$ adb devices
    List of devices attached HT*********** device

<!-- meta: archive(1) active(1) -->
