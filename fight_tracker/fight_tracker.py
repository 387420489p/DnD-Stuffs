#TODO exception handling !!!!!!!!!!!
#figth közben kidobott :'((((
#TODO npc darabszám szorzás
from random import randint


initiative = []
fighters = []

def get_character(name, hp, ac, ini, pc):
    fighters.append({"Name": name,
                    "HP": int(hp),
                    "AC": ac,
                    "Initiative": ini,
                     "PC": pc,
                    })

def get_started():
    global fighters
    while True:
        pc = input("PC or NPC? Type FIGHT to start the fight!")
        while pc.lower() not in ["pc", "npc", "fight"]:
            pc = input("PC or NPC? Type FIGHT to start the fight!")
        if pc.lower() == "fight":
            build_initiative()
        elif pc.lower() == 'pc':
            pc = True
        else:
            pc = False
        nev = input("Name: ").lower()
        if nev in ["baldwin", "bob", "bog", "luna", "doni", "urist", "beni"]:
            pc_character(nev)
            break
        while True:
            try:
                hp = int(input("HP: "))
                break
            except ValueError:
                print("HP must be a number!")
        while True:
            try:
                ac = int(input("AC: "))
                break
            except ValueError:
                print("AC must be a number!")
        if pc == False:
            ini = randint(1, 20)
        else:
            ini = int(input("Initiative: "))
        get_character(nev, hp, ac, ini, pc)


def build_initiative():
    global fighters, initiative
    for fighter in fighters:
        initiative.append([fighter["Initiative"], fighter["Name"], fighter["HP"], fighter["PC"], fighter["AC"]])
    initiative.sort(reverse=True)
    for char in initiative:
        char.pop(0)
    fight()

def get_new_ini():
    global initiative
    initiative = []
    for fighter in fighters:
        if fighter["HP"] > 0:
            initiative.append([fighter["Initiative"], fighter["Name"], fighter["HP"], fighter["PC"], fighter["AC"]])
        else:
            if fighter["PC"] == True:
                initiative.append([fighter["Initiative"], fighter["Name"], fighter["HP"], fighter["PC"], fighter["AC"]])
    initiative.sort(reverse=True)
    for char in initiative:
        char.pop(0)
    fight()

def fight():
    global initiative, fighters
    print("\nInitiative: ")
    for i in initiative:
        if i[2] == True and i[1] <= 0:
            print(f"{i[0].capitalize()}, PLAYER DOWN!")
        else:
            print(f"{i[0].capitalize()}: HP: {i[1]}, AC: {i[3]}")
    print("\n")
    print("==========================================================")

    name = input("Who got dmg? ").lower()
    #validation of name. dead npc-s still accepted, but it's a feature not a bug :) 
    names = []
    for fighter in fighters:
        names.append(fighter["Name"])
    while name not in names:
        print("There's no one with that name!")
        name = input("Who got dmg? ").lower()
    while True:
        try:
            dmg = int(input("How much dmg? (Type negative for heal) "))
            break
        except ValueError:
            print("Only numbers are accepted!")
    if dmg == 387420489:
        egg()
    print(r"""        /""")
    print(f"*//////[<>==================- {name.capitalize()} - {dmg}")
    print(r"""        \ """)
    for fighter in fighters:
        if fighter["Name"] == name:
            fighter["HP"] = fighter["HP"] - dmg
            if fighter["HP"] <= 0:
                fighter["HP"] = 0
                print(f"            (✖╭╮✖) {name.upper()} DIED! (✖╭╮✖)")
    get_new_ini()

def pc_character(name):
    if name == "baldwin":
        ac = 19
        hp = 79
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "bob":
        ac = 20
        hp = 77
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "luna":
        ac = 13
        hp = 54
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "bog":
        ac = 17
        hp = 47
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "doni":
        ac = 15
        hp = 80
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "urist":
        ac = 14
        hp = 71
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)
    elif name == "beni":
        ac = 10
        hp = 49
        ini = int(input("Initiative: "))
        pc = True
        get_character(name, hp, ac, ini, pc)

    get_started()
def egg():
    print(r"""              .---. .---.     Nice job, you found me!
             :     : o   :       Have a cookie!
         _..-:   o :     :-.._     - 387420489
     .-''  '  `---' `---' "   ``-.      /
   .'   "   '  "  .    "  . '  "  `.  
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
       `. "    '"--...--"'  . ' .'  .'  o   `.
      .'`-._'    " .     " _.-'`. :       o  :
     '      ```--.....--'''    ' `:_ o       :
 .'    "     '         "     "   ; `.;";";";'
;         '       "       '     . ; .' ; ; ;
;     '         '       '   "    .'      .-'
'  "     "   '      "           "    _.-'""")

get_started()