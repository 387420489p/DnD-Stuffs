#TODO földre kerülés PC-knek DONE
#TODO exception handling
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
        if pc.lower() == "fight":
            build_initiative()
        elif pc.lower() == 'pc':
            pc = True
        else:
            pc = False
        nev = input("Name: ")
        hp = int(input("HP: "))
        ac = int(input("AC: "))
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
    print("=============================" * len(fighters))
    print("\nInitiative: ", end=" ")
    for i in initiative:
        if i[2] == True and i[1] <= 0:
            print(f"Name: {i[0]}, PLAYER DOWN!||", end=" ")
        else:
            print(f"Name: {i[0]}, HP: {i[1]}, AC: {i[3]} ||", end=" ")
    print("\n")
    print("=============================" * len(fighters))

    name = input("Who got dmg? ")
    dmg = int(input("How much dmg? (Type negative for heal) "))
    for fighter in fighters:
        if fighter["Name"] == name:
            fighter["HP"] = fighter["HP"] - dmg
            if fighter["HP"] < 0:
                fighter["HP"] = 0
    print(r"""        /""")
    print(f"*//////[<>==================- {name} - {dmg}")
    print(r"""        \ """)
    get_new_ini()


get_started()