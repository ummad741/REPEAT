## <p style='color:#e31d1d'>WORKING WITH LINUX </p>

1. ### ℹ️ NEGA LINUX

   - 💡 eng asosiy sabab 96% serverlar Linuxda ishlaydi

   - 📝 bepul va ochiq tizim
   - 📝 tez, juda onson va yengil tizim
   - 📝 operatsion tizimi organish uchun ochiq resurslari kop
   - 📝 shell commandala bilan boshqarish imkoniyati kengroq
   - 📝 Nega linux os nega windows os emas chunki windows osda ishlayotgan paytda hato sabablarini toliq korsata bera olmaydi ekran ortida qolib ketadi, linuxsda esa errorlarni qayerdan va nma sababdan yuz berayotganini toliq korsatib berish qobilyati yaxshi rivojlangan
   - 💡 Linux 1991 - yil Linus Tordwals tomonidan yaratilgan 1994 - yil rasman ishga tushgan
   - 💡 Windows 1985 yil yaratilgan microsoft tomonidan

2. ### 📋 TERMINAL,SHELL,BASH,COMMANDLINE
   - 📝 Terminal - shell buyruqlarini(command) yozish imkoniyatini beradigan qora oyna
   - 📝 Shell - foydlanuvchi(User) tomonidan operatsion tizimga(Operation System) kelgan buyruqlarni(command) qabul qilib, uning natijasini qaytaruvchi dastur,shell oziga tegishli buyruq(command) qabul qilib va unga javob qaytaradi agar notanish buyruq(command) berilsa u (Unknown) error beradi
   - 📝 Bash - linux shell dasturlaridan biri yani standart(default) shell hisoblanadi linuxda
   - 📝 Command Line - Textual commands orqali yozuvchi harqanday interface
3. ### 📋Commands
   - 📝 Command - command _ Flag _ argument: echo -n hello world

```bash
    # echo buyruqni (string) sifatida qaytaradi
    $ echo hello world

    # man - Manual bu command instructsiyasi
    $ man command

    # pwd - print working directory qayerdaman
    $ pwd

    # ls ishlanvotgan joyda qanday filelar
    # log qilish
    $ ls [OPTION] [FILE] | ls -a Desktop # list sessions

    # RELATIVE AND ABSOLUTE PATH
    $ cd Desktop # Relative
    $ cd home/user/Desktop # Absolute

    # touch file yaratish yoki file vaqtini yangilash
    $ touch docs.txt |

    # cd change directory
    $ cd [FILE] | cd Desktop

    # mkdir make directory papka yaratadi
    $ mkdir [ARGUMENT] | mkdir newfolder

    # cp file copy contenti bilan
    $ cp [OPTION] ... [SOURCE] [DEST]

    # rm ochirib yuboradi hard delete
    $ rm [OPTION] [FILE]

    # mv Move folderdan folderga ob otish
    $ mv [OPTION] ... [SOURCE] [DEST]
    $ mv [OPTION] ... [SOURCE] [DIRECTORY]

    $ [FILE] .. #ORTGA | # ../ YUQORIGA . OSHA FILENE OZI
    $ find # file path show
    $ tree # file structura show

    # Paketlarni ornatish, ochirish va boshqarish uchun
    # ishlatiladi
    # ubuntu repostory yani .deb filelardan olib keladi
    apt # advanced package tool
```

4. ### 📋 Linux Users Sudo va Root

- 💡 Linuxda 3 xil turdagi user bor
  1. System User - root misol bola oladi u tizimda har qanday ishi bajaraoladi
  2. Regular User
  3. Service User - regular va normal userlarda cheklovlar yani uni imkoniyatlari cheklangan boladi
- 📝 Sudo switch user do yani sudo commandi bilan odiy user bir vaqt root user bolib ishlidi sudo ishlatotgan user sudoer bolishi yani root imkoniyatlariga ega bolishi kere

- Permission va Chmod

