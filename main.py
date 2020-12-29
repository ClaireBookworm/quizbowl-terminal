import json
import sys
from time import sleep
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

file = "./" + input("Please input file name, no extensions: ") + ".json"
star = open('./starred.html', 'a')
bio = open('./bio.html','a')
phys = open('./phys.html','a')
chem = open('./chem.html','a')
math = open('./math.html', 'a')
cs = open('./cs.html', 'a')
other = open('./other.html','a')

for reader in [star, bio, phys, chem, math, cs, other]:
    reader.write("""<head>
        <style>
            body {
                font-family: "Graphik"; 
                margin: 5em;
                font-size: 16px;
            }
        </style>
    </head>""")


def quiz(filename):
    f = open(filename,)
    data = json.load(f)


    for datum in data['tossups']:
        print(color.BOLD + datum['category']['name'] + " | " + datum['subcategory']['name'] + color.END + '\n')
        print(datum['text'])
        # for char in datum['text']:
        #     sleep(0.03)
        #     sys.stdout.write(char)
        #     sys.stdout.flush()
        input("\nPress enter to see answer...")
        print(color.CYAN + datum['answer'] + color.END + ".\nThis was difficulty: " + datum['tournament']['difficulty'] + "!\n")
        s = input("Star? ").lower()
        if s == "s":
            note = input(color.YELLOW + "🧠 Note: " + color.END);
            question = "<h2 style='color: #273444'>✨ " + str(datum['id']) + "</h2>\n<p>" + datum['text']+"</p>\n<p style='color:#009aab'>"+datum['answer']+ "</p>\n<p style='font-family: Graphik; color:#ff5a5f; font-weight: 700'>📜 Note: " + note + "</p>\n\n"
            star.write(question)
            star.flush()

            cat = datum['subcategory']['name']
            if (cat == "Science Biology"):
                print ("Biology!!")
                bio.write(question)
                bio.flush()
            elif (cat == "Science Physics"):
                phys.write(question)
                phys.flush()
            elif (cat ==  "Science Chemistry"):
                chem.write(question)
                chem.flush()
            elif (cat == "Science Math"):
                math.write(question)
                math.flush()
            elif (cat == "Science Computer Science"):
                cs.write(question)
                cs.flush()
            else:
                other.write(question)
                other.flush()
            

            print ("Starred! ⭐️")
            star.write("<div style='background:#e0e6ed; width: 85% !important; border-radius: 5px'><br /></div>")
        cont = input("\nNext question?")
        if (cont == 'n') or (cont == 'N'):
            f.close()
            star.close()
            return 
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc')

quiz(file)

star = open("./starred.html", 'r')
print("Starred: \n" + star.read())
star.close()

#   "data": {
#     "num_tossups_found": 7661,
#     "num_tossups_shown": 750,
