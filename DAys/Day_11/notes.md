DAY 11 - FILE HANDLING

1. open()
File open/create karne ke liye.

2. Modes

"r" -> Read
"w" -> Write (purana data delete)
"a" -> Append (purane data ke end me add)

3. with open()

with open("file.txt","r") as file:
    data = file.read()

Automatic file close ho jati hai.

4. file.read()
Poora data read karta hai.

5. file.write()
File me data likhta hai.

Important:
Always prefer "with open()" instead of open()+close().