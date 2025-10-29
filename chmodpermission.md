# <p style='color:#55a8fa'>CHMOD AND PERMISSION </p>

1. ## PERMISSION

- PERMISSION - Linux tizimidagi eng assosiy havsizlik modeli hisoblanadi.
- fayl yoki dirga berilgan maxsus ruxsat
  ```bash
    $ ls -l
    total 2
    -rw-rw-r--  1 ummad741 ummad741  151 Apr 19
    2024 token.txt
  ```
- fayl 10 ta symboldan iborat va permissionlari 3 tadan o'qiladi
- 💡 fayl turi - or d
- permission rw-r--r-- 1-uchtalik user 2-guruh 3-others tizim ichidagi hamma
- user: ummad741
- guruh group: ummad741
- r - read
- w - write
- x - execute faylni dastur qilib ishlatsa boladi

2. ## CHMOD - CHANGE MOD

- chmod - fayl permissionlarini ozgartiradi

```bash
    # userda read qilishni olib tashla
    $ chmod u-r # u-(user) - -(remove) r-(read)

    # group other all ga write execute qilishni qo'sh
    $ chmod g+w # g-(group) + - (add) w-(write)
    $ chmod o+x # o-(others) + - (add) x-(execute)
    $ chmod a+x # a -(all) + - (add) x-(execute)

    $chmod 644 myfile.txt  # Safe default for files
    $chmod 755 myscript.sh # Script: executable by all
    $chmod 700 secret.txt # Private file
    $chmod 777 temp_dir/ # Public writable dir careful
```

- u - (user)
- g - (group)
- o - (other)
- a - (all)
- "-" - (remove)
- "+" - (add)

3. ## CHMOD ABSOLUTE WITH NUMBERS
  
4. ## PIPE
- && - and hamma command ishlashi kerak
- || - or birortasi ishlashi  kerak
- ; - ketma ket command bajarish imkonini beradi
- | - PIPE birinchi codeni outputini keyingi beriladigan commandga input qilib beradi
- wc word counter -l qator 
- history - ishlatilgan commmandlar royxati 
- grep - commandlarni filter qilish uchun ishlatiladi

```bash
  $sudo apt update && sudo apt upgarade # and 
  $sudo uft update || sudo apt remove # or 
  $echo birinchi cmd : echo ikkinchi cmd # ketma ket 
  $ ls -l | wc -l # PIPE bir outputi ikkiga input
  $ wc 1qator 2soni 12character # word counter
  $ history # command history
  $ grep rm || grep "rm -rf" # finder  
```