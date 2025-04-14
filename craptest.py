#Ram eater 500k

import os

aislop = 0
crap = 0
content = 0
shiter = 0

while True:
    print('Count is currently at ' + str(shiter) + "reels.")
    if shiter == 100:
        print("Feed is currently " + str(aislop), "% AI slop, " + str(crap), "% low effort content, and " + str(content) + "% real content.")
        os.system('pause')
    print("Test is swayed by your algorithm. Results are to be sent raw.")
    inputme = input("Is is 1. Slop, 2. Crap, or 3. Content: ")
    if inputme == 1:
        aislop += 1
        shiter += 1
        os.system("cls")
    elif inputme == 3:
        content += 1
        shiter += 1
        os.system("cls")
    elif inputme == 2:
        crap += 1
        shiter += 1
        os.system("cls")
    else:
        os.system("cls")