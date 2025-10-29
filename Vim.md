# VIM

- 💡 faylar operatsion tizimning eng muhum qismi,ular doimiy hotirada diskda ssd saqlanadi

- cat concatinate

```bash
    $cat [OPTION] [file.txt] # file oqidi

    $tac file.txt # reverse oqish
    # - 💡 ">" faylni tozalab, qaytadan yozadi
    $echo something > file.txt # add to file

    $echo something >> file.txt # append to file

    $echo  tee working | tee file.txt # output va file

    #
    $cat file.txt | less # yengi oyna yaratib show qiladi
    #
    $cat file.txt | head -n 5 # boshidan 5 qator Pipe
    $cat file.txt | tail -n 5 # ohiridan 5 qator Pipe
    $head -n3 file.txt # boshidan 3 qator
    $tail -n3 file.txt # ohiridan 3 qator
    $tail -f # log qilib turadi ohiridan
```
