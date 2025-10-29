## <p style='color:#6cd82f '>TMUX</p>

1. ### ℹ️ Tmux Nma

   - 📝 Tmux terminal multplexer bolib bir vaqtni ozida bir nechta sessiyalardan bir oyna orqali foydalanish imkoniyatini beradigan dastur
   - tmux sessiyalari serverlarda saqlanadi, local terminal yoki compda emas va bu degani ishni istalgan joyda toxtab keyin yana osha joyidan davom etirib ketsa boladi
   - 💡 serverlarda ishlayotganda tmuxdan foydalanish best practice hisoblanadi

   - 💡 tmux afzaligi qilinyatogan ish yopilsaham osha yerda va osha holatda saqlanib qolishi eng afzal tomoni hisoblanadi

2. ### 📋 Tmux Sessiyalari

   - Sessiyalar assoiy ishi ishlanayotgan vaziyatni saqlash
   - attached - biriktirilgan osha ekranga

3. ### 💻 TMUX COMMANDS

```bash
   # create session
   $ tmux

   # create session ism bilan
   $ tmux new -t sessioname
   # sessiayalr royxati
   $ tmux ls

   # sessiyani biriktirib beradi sessiyani qayta tiklash
   # osha oynani ochadi
   $ tmux a # attached
   # attached with session name
   $ tmux a -t session name

   # current sessiyani ochirib yuboradi
   $ tmux kill-ses
   # ism boyicha ochiradi
   $ tmux kill-ses -t session name

   # tmux ichida ishlidi
   $ ctrl + b [Flags]

   $ ctrl + b d # deteched session yopish
   $ ctrl + b w # oyna session royxati
   $ ctrl + b c # oyna yaratish
   $ ctrl + b & # oyna yopish
   $ ctrl + b % # split pane vertical
   $ ctrl + b '"' # split pane gorizantal
   $ ctrl + b ; # switch pane toggle 
   $ ctrl + b x # close pane
   $ ctrl + b -> # switch pane direction
   $ ctrl + b <-  # switch pane direction
   $ ctrl + b "[" # scroll 
```
