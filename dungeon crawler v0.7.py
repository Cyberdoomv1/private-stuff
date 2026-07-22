#imports----------------------------------------
from random import randint, choice

#lists------------------------------------------
male = ["he","him","his"]
female = ["she","her","hers"]
unknown = ["it","it","its"]
roomlist = ["trap","encounter","encounter","treasure","treasure","heal","heal","empty","empty","empty"]

#classes-------------------------------------------------------------------------------------------
class Entity:
    def __init__(self, name, gender, health, maxhealth, exp, gold, atk, wpn):
        self.name = name
        self.gender = gender
        self.health = health
        self.maxhealth = maxhealth
        self.exp = exp
        self.gold = gold
        self.atk = atk
        self.wpn = wpn
    
    def greeting(self):
        print("hello my name is",self.name)
        
    def attack(self,target):
        print("***********************")
        print(self.name,self.wpn.wpnswing,target.name)
        print("dealing",self.atk,"damage")
        target.health = target.health - self.atk
        print(target.name+"'s health is now",target.health)
        print("***********************")
        
    def heal(self):
        foodval = randint(5,30)
        if self.health + foodval > self.maxhealth:
            wchoice = randint(1,2)
            if wchoice == 1:
                print(self.name,"finds some food and eats it healing",self.maxhealth - self.health)
                self.health = self.health + foodval
            else:
                print(self.name,"finds a potion and drinks it healing",self.maxhealth - self.health)
            self.health = self.maxhealth
        else:
            wchoice = randint(1,2)
            if wchoice == 1:
                print(self.name,"finds some food and eats it healing",foodval,"HP")
                self.health = self.health + foodval
            else:
                print(self.name,"finds a potion and drinks it healing",foodval,"HP")
                self.health = self.health + foodval
    
    def stats(self):
        print("-------------------")
        print("name:",self.name)
        print("health:",self.health)
        print("max health:",self.maxhealth)
        print("exp:",self.exp)
        print("atk:",self.atk)
        print("-------------------")
            
class Weapon:
    def __init__(self,wpnname,wpnatk,wpnswing):
        self.wpnname = wpnname
        self.wpnatk = wpnatk
        self.wpnswing = wpnswing

class Room:
    def __init__(self,roomtype,discovered):
        self.roomtype = roomtype
        self.discovered = discovered

#objects-------------------------------------------------------------------------------------------------------------------------
shortsword = Weapon("shortsword",20,["slices at","slashes","cleaves into","strikes","jabs","pokes","cuts"])
longsword = Weapon("longsword",30,["slices at","slashes","cleaves into","strikes","jabs","pokes","cuts"])
sword = Weapon("sword",25,["slices at","slashes","cleaves into","strikes","jabs","pokes","cuts"])
dagger = Weapon("dagger",15,["stabs at","slashes","cuts","slashes"])
stick = Weapon("stick",5,["thwacks","bonks","whacks","whips","jabs"])
metalbar = Weapon("metal bar",10,["thwacks","bonks","whacks","jabs"])
mace = Weapon("mace",20,["thwacks","bonks","whacks","jabs"])
club = Weapon("club",15,["thwacks","bonks","whacks","jabs"])
flail = Weapon("flail",12,["whips","flails","bonks"])
fists = Weapon("fists",3,["punches","jabs at","swings at","hooks","thumps","whacks"])
golemfists = Weapon("fists",25,["punches","swipes at","crushes","flings"])
claws = Weapon("claws",20,["slashes","slices","claws at","bites"])
knuckleduster = Weapon("knuckle duster",7,["punches","jabs at","swings at","hooks","thumps","whacks"])
dragonsbreath = Weapon("breath",40,["sprays fire","blows fire"])
fishesbreath = Weapon("breath",9999999999999999999999999999999999999999999999999999999999999999,["sprays fire","blows fire"])


d = []
for i in range(5):
    r = []
    for x in range(5):
       r.append(Room(choice(roomlist),False))
    d.append(r)
   
# count = 0
# for x in d:
#     print(count)
#     for i in x:
#         print(i.roomtype)
#     count += 1


#player setup--------------------------------------------------------------------------------------
player1 = Entity("steven the brave",male,100,100,0,0,shortsword.wpnatk,shortsword.wpnname)
# validating = True
# while validating:
#     nchoice = input("what is the heros name: ").title()
#     answer = str(input("you have chosen \""+nchoice+"\" is this correct? y/n: ")).lower()
#     if answer in("y","ye","yes"):
#         print("name set to",nchoice)
#         player1.name = nchoice
#         validating = False
#     elif answer in("n","no","nien"):
#         print("trying again")
#     else:
#         print("invalid input try again")
# 
# validating = True
# while validating:
#     gender = input("what is the heros gender(m/f/n): ").lower()
#     if gender in("m","male","man"):
#         print(player1.name+"'s gender is now male")
#         player1.gender = male
#         validating = False
#     elif gender in("f","female","girl"):
#         print(player1.name+"'s gender is now female")
#         player1.gender = female
#         validating = False
#     elif gender in("n","non","nonbinary","non-binary","non binary","none","no"):
#         print(player1.name+"'s gender is now unknowable")
#         player1.gender = unknown
#         validating = False
#     else:
#         print("invalid input try again")

#subroutines-----------------------------------------------------------------------------
def encounter(male,female,unknown):
    montype = randint(1,101)
    if montype < 26:
        montype = "Goblin"
        monhealth = randint(15,30)
        monmaxhealth = monhealth
        monexp = randint(5,15)
        mongold = randint(0,30)
        wpn = choice([shortsword,dagger,stick,metalbar,mace])
        wpnatk = wpn.wpnatk
        gend = randint(1,5)
        if gend == 1:
            gend = male
        elif gend == 2:
            gend = female
        else:
            gend = unknown
    elif montype < 51:
        montype = "Orc"
        monhealth = randint(30,50)
        monmaxhealth = monhealth
        monexp = randint(20,30)
        mongold = randint(0,10)
        wpn = choice([shortsword,sword,longsword,dagger,mace,club,flail])
        wpnatk = wpn.wpnatk
        gend = randint(1,5)
        if gend == 1:
            gend = male
        elif gend == 2:
            gend = female
        else:
            gend = unknown
    elif montype < 81:
        montype = "Ghoul"
        monhealth = randint(40,60)
        monmaxhealth = monhealth
        monexp = randint(75,85)
        mongold = randint(0,20)
        wpn = claws
        wpnatk = wpn.wpnatk
        gend = randint(1,5)
        if gend == 1:
            gend = male
        elif gend == 2:
            gend = female
        else:
            gend = unknown
    elif montype < 96:
        montype = "Golem"
        monhealth = randint(60,80)
        monmaxhealth = monhealth
        monexp = randint(90,110)
        mongold = 0
        wpn = golemfists
        wpnatk = wpn.wpnatk
        gend = unknown
    elif montype < 101:
        montype = "Dragon"
        monhealth = randint(80,120)
        monmaxhealth = monhealth
        monexp = randint(150,250)
        mongold = randint(80,110)
        wpn = dragonsbreath
        wpnatk = wpn.wpnatk
        gend = unknown
    else:
        print("""⢨⠿⣽⢯⣟⡿⣽⣻⢟⡿⣽⣻⡟⣿⣽⣻⣟⣿⣻⣟⣿⣿⣿⡿⣿⣟⣿⣻⣟⣟⡻⢏⡛⠻⢿⣏⡙⢶⡈⠣⡀⢢⠀⠀⠀⠀⠀⠀⣿⢿⡽⣻⣽⣻⣽⣻⢯⣟⡿⣽⣻⢯⣟⣿⣻⢯⣟⣿⣻⢟⣿⣻⡟⣿⣽⣻⢯⣟⣯⠿⣽⢯⢿⡽⢯⡿⡽⢯⣿⣹⢯⢿⣹⢯⡿⡽⣯⣟⢿⣽⣻⢯⣟⡿⣻⣽⣻⣟⡿⣻⢯⣟⡿⣽⣻⢯⣟⡿⣽⣻
⢨⠿⣽⠾⣽⣞⡷⣯⢿⣽⣳⢯⣟⡷⣯⢷⣞⠷⣯⢟⡯⣿⣻⣿⣿⢿⡷⣯⢞⣼⣱⡉⡙⠶⣄⡈⠳⡄⠙⡄⠡⠀⢀⠀⠀⠠⢪⣥⣿⣯⣟⣳⡽⣾⣱⢯⣟⡾⣽⣳⢯⣟⣾⣳⢯⣟⣾⣳⢯⣟⣾⣳⣟⡷⣽⡞⣟⣮⢯⢿⡽⣞⣻⣞⢯⣷⢻⡟⣶⢯⣻⣭⡟⣾⡽⣻⡵⣞⡿⢮⣟⡽⣾⣽⣳⢯⡷⣯⢿⣽⡻⣾⢽⣳⢯⣟⡾⣽⣳⢯
⠀⡿⣝⣻⢧⡿⣽⣞⣟⡾⣽⣻⢾⡽⣯⣟⣾⣻⣼⣣⡽⣆⢧⢣⠏⢧⠛⡴⢫⢔⣀⠋⠓⢦⠀⠹⡄⠘⠀⠀⠀⠀⠀⠀⠀⣴⠿⠛⠉⡉⢉⡙⡷⠯⣯⣟⡾⣽⣳⢯⣟⡾⢧⣟⣟⡾⣳⢯⣟⣾⣳⠿⣼⣛⣧⢿⡽⣞⡯⣟⡾⣝⡷⣞⣻⡼⣏⣟⣧⡟⣧⢷⣛⣧⡟⣷⣻⣭⡟⣟⡾⣽⣳⢾⡽⣯⢷⣯⢟⣶⣻⡽⢯⣻⣛⡾⣽⣳⢯⣟
⠀⠘⣯⢯⣟⡽⣾⣹⢾⣽⣳⢯⡿⣽⣳⢿⡳⣟⢷⡻⠿⡝⣏⠮⡙⢎⡙⠦⢡⢎⡈⠙⠆⠀⠑⠀⠀⠀⠀⠀⢀⡀⠰⣈⠕⢁⡠⢐⣡⣶⣿⡹⣖⠲⠄⠽⣿⣧⠿⣽⣺⣽⢻⡾⣭⢿⣽⢻⣞⣧⡟⣿⡳⣟⣾⢫⡷⢯⡽⣾⣹⡽⣞⣽⣣⢿⣹⣞⣮⣽⣛⡾⣽⣺⢽⡳⣧⢷⣻⡽⣽⡳⣯⢟⡾⣽⣳⢯⣟⣞⣧⣟⣯⢷⣯⣟⡷⣯⣟⣾
⠀⠀⠘⣻⠾⣽⣳⢯⣟⡾⣭⣟⠾⣵⢫⠞⡵⣩⠖⡱⢍⡜⠤⢃⠍⠂⠌⡐⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⢂⠼⠃⣀⢔⣉⡰⣚⣿⡵⡾⠃⢀⡴⠡⠀⠈⢿⢿⣳⡽⣞⣯⠷⣯⣻⢞⣟⣮⢷⣻⣳⢟⡽⣞⣯⢟⣯⡽⡶⣏⣷⣛⡶⣏⣯⠷⣞⡵⡾⣭⢷⣻⡼⢯⣽⡳⣯⣳⢟⡾⣝⣳⢯⣟⣳⢯⣟⡾⣽⢾⣹⣞⡿⣞⣭⣟⣷⣻⢾
⠀⠀⠀⢨⣛⢷⢯⣟⡾⣽⣳⢏⡿⣘⠧⡛⡔⠣⢎⡑⢊⠰⢁⠊⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠜⠁⣴⠏⣴⣯⣟⣵⣿⣷⢧⠱⡍⣒⡆⠀⠀⠀⠂⠈⠛⣿⢾⣱⣟⣳⢯⣻⡞⣽⣞⣳⣭⠿⣽⡞⣽⡞⣧⣟⣳⠿⣜⡷⣫⡽⣞⣻⣭⢟⣳⢯⡷⣫⣞⠿⣶⣻⡵⣯⣻⡽⣝⣯⣟⡾⣽⣛⡾⣽⣏⣿⣳⢯⡿⣽⢾⡽⣾⣽⣻
⠀⣀⢠⢦⡝⣿⣟⡾⣽⣳⡝⣎⠶⣑⢎⡱⡘⠍⠆⡙⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠒⠈⣀⠴⣋⠏⢸⢿⣴⣻⣿⣾⣳⡿⠃⠘⠁⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠿⣭⢿⣱⣟⣳⡞⣷⣫⣟⡧⣟⣧⣟⣳⠾⣭⢿⣹⡞⣷⣫⡽⣞⣮⢟⡽⣾⣹⡗⣯⣟⣳⢷⣫⢷⣳⢿⣹⣞⡾⣽⣳⢯⣟⣷⣻⢾⡽⣯⢿⡽⣯⣟⡷⣯⣟
⣜⢦⣻⢾⣽⡳⢯⡟⡷⢿⣼⠮⠕⠊⠀⠁⠈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⠁⠀⠀⡰⠁⡴⠠⠂⡎⢻⣿⣿⡿⠃⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣻⠽⣞⣳⣞⣧⢟⣳⢷⣹⠾⣝⣶⣫⣽⢻⡽⣺⢧⡟⣧⡟⣵⣻⡼⣏⡿⣖⢿⣼⣳⢯⣻⠾⣽⣫⡽⣞⡷⣯⣟⡷⣯⣟⣾⣳⢯⡿⣽⢯⡿⣽⣳⢯⣟⣷⣻
⣯⢿⣽⣿⣷⣻⡟⣼⢣⡃⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⡠⠃⠀⠀⠀⠀⢰⡤⢏⢃⠌⡌⢹⠠⠓⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢯⡿⣭⠷⣾⣹⠾⣽⠾⣭⢿⣹⢶⡻⣼⢏⡷⢯⣳⢟⣵⡻⢧⣷⢫⡽⣞⣭⣟⡶⢯⣛⣷⣻⠷⣏⡿⣽⢯⡷⣾⣽⣳⣟⡾⣽⢯⡿⣽⢯⣟⡷⣯⢿⣞⣷⣻
⣿⡿⣽⣻⣷⣯⣟⣽⢣⡝⠬⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⡱⠁⠀⠀⠀⠀⠀⠃⡇⠋⠔⡨⠒⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣳⡟⣧⣟⣻⣭⢿⣹⠾⣭⢷⣛⣧⢿⣹⢯⣳⢟⣮⣽⢻⡼⣏⣿⣹⣞⠾⣽⢯⣟⢾⣭⢿⣽⣻⣭⢿⣽⣳⣞⡷⣯⢿⡽⣯⢿⣽⣻⢾⡽⣯⣟⣾⣳⢿
⣿⣿⢿⣟⣷⡿⣞⣮⢳⡬⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠉⠡⠊⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣻⡵⣞⡷⡽⣾⡹⣟⡽⢾⣹⢮⣛⣮⢯⣗⣻⣞⡼⣯⣳⢟⣶⡻⣼⣻⡽⢾⣭⣟⢾⣻⣼⣳⢯⣟⣾⣳⢯⡿⣽⢯⡿⣽⣻⢾⡽⣯⣟⣷⣻⢾⣽⣻
⣿⣻⡿⣯⣿⣻⣽⢮⡳⣜⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⡴⠶⣝⡤⣤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣻⣝⡾⣽⢳⣻⣝⡾⣏⡷⣏⡿⣼⢳⢯⣞⠾⣽⠶⣏⡿⢶⣛⣷⣳⡻⣟⡼⣞⣯⢷⣳⢯⣟⣾⣳⢯⡿⣽⢯⡿⣽⣳⢯⡿⣽⣳⣟⡾⣽⣻⢾⣽
⣿⣳⣟⣯⠷⣯⣟⢯⡳⣍⠦⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣖⡆⢔⡶⣽⡞⣤⡗⠈⣲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⣻⡼⣏⡿⣵⣞⣳⢯⣳⢯⣳⢯⢯⡷⣫⣟⢧⡿⣽⣹⢯⣛⡶⣯⡽⢯⣽⢻⡼⣏⣷⣻⢞⣧⣟⣯⢿⡽⣯⣟⡷⣯⢿⣽⣳⣟⡾⣽⢷⣻⣟⣾
⣿⣳⢾⣜⢻⡖⢯⢳⡙⣆⠣⠜⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⠼⣳⣡⠜⠒⠚⠷⠮⡄⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣻⣭⢷⣳⠾⣭⢷⣫⢯⣗⣯⣻⣼⢳⢯⣛⣾⢳⣏⡿⣭⢷⢯⣽⣛⡾⢯⣽⢻⣼⡳⣟⡾⣽⣞⣯⣟⡷⣯⢿⣽⣻⣞⡷⣯⢿⡽⣯⢷⣻⢾
⣿⡽⣏⢮⣓⡎⡇⢧⡙⢦⡛⡜⣜⣶⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠈⣰⡿⡿⠆⡀⠀⠀⢱⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣟⡾⣭⢿⣹⠾⣭⢷⣞⢮⢷⡞⣯⣻⣝⠾⣏⡾⣽⠽⣞⣯⢶⢯⣛⡿⣼⡻⣶⣻⡽⣽⢾⡽⣾⣽⣻⣽⣻⣞⡷⣯⢿⡽⣯⢿⣽⣻⣽⣻
⣿⡽⣞⣧⢻⡜⡹⢎⡝⢦⡹⣹⢮⣿⢧⡑⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠁⠀⠠⠋⣸⣷⣆⢹⠀⣆⡼⠃⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠙⠻⡾⣭⢷⣻⠽⣞⣞⢯⡷⣻⣵⣳⡞⣿⣹⡽⣞⢿⣹⡞⣯⣻⣭⢷⢯⡷⣏⣷⣻⡽⣾⣽⣳⢷⣻⣞⡷⣯⢿⡽⣯⢿⣽⣻⣞⡷⣯⢿
⣿⣽⡻⣜⠧⣙⢧⠫⡜⢣⠒⡁⠻⣽⠢⡑⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠏⠆⠀⠀⠰⣿⣿⣿⡘⢠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡅⡀⠀⡄⢶⣜⣿⢞⣭⢿⣹⢮⣟⣼⣳⢧⡷⣛⣧⢿⣱⢯⡟⣧⣟⣳⠷⣽⣞⣻⣼⢻⡶⣯⢷⣻⢾⡽⣯⢷⣯⢿⡽⣯⢿⣽⣻⣞⡷⣯⢿⣽⣻
⣟⠶⣉⠆⣁⠂⢂⠑⠨⢁⠂⠀⠁⠢⠑⡠⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠝⡸⠀⠀⠀⢅⠻⡿⢏⣁⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠤⠀⣿⠅⡞⣰⣶⡄⢻⣻⢮⢯⣳⡟⣼⢧⣟⡾⣝⣻⡼⣏⣯⢟⣾⣳⣭⡟⣯⢷⣞⣳⢯⣟⡷⣯⢿⡽⣯⢿⣽⣻⣞⣯⢿⣽⣻⣞⡷⣯⢿⣽⣻⢾⣽
⣿⢯⡷⣞⣵⣎⣦⡜⣤⢂⡐⡄⢂⠄⡡⠀⠄⠁⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠂⡇⠃⠀⠀⠈⠃⠝⠁⢜⣾⠥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⢿⣿⣿⡇⣸⡷⢯⣻⡵⣻⠽⣞⣾⣹⡽⢧⣿⣹⣞⣻⢶⣛⣶⣻⢽⡾⣭⠿⣽⠾⣽⢯⡿⣽⢯⣟⣾⣳⣟⡾⣯⡷⣟⣾⣻⡽⣟⣾⡽⣟⣾
⡿⣯⢿⡽⣾⡹⢾⡹⣏⢯⡳⣝⢮⡚⢤⠃⠌⡀⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡍⢰⢁⠀⠀⠈⠐⠠⠀⠀⠸⡥⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⡀⠐⠀⣻⡆⢙⣿⠟⢁⡿⡽⣏⡷⣽⢫⣿⣹⠶⣯⣽⣛⡶⢯⡾⣝⣯⢿⡼⣏⣷⣻⣽⣻⣽⣻⡽⣯⢿⣽⣻⣞⣷⣻⣞⣿⣳⣟⣯⣷⣻⣽⢯⡷⣟⣯⢿
⣿⡽⣯⣟⣶⣛⢯⡳⡝⣎⡳⣍⠶⣙⠦⡉⢆⠠⠁⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠠⠀⠀⢀⠊⠀⠀⣠⣶⣿⣿⣿⣦⣥⣒⠠⡀⠈⠢⡁⠘⢽⡀⡉⣰⣿⢻⡽⣝⣳⢯⣟⡶⢯⣟⣳⠾⣭⣟⢯⣷⢻⣞⣯⣽⢻⡾⣵⣳⣟⣾⣳⢿⣽⣻⣞⣷⣻⣞⣷⣻⣞⣷⣻⣞⣷⣻⢾⣻⣽⢿⣽⣻
⣿⣽⣳⢯⣶⡹⣎⠷⣝⢮⠳⢎⡹⢄⠣⢌⡐⢂⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢺⠀⠀⠁⠀⠀⠀⠀⠀⠀⠠⠀⠐⢀⠆⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⢂⠀⠱⠀⠀⡉⢉⣿⣭⢿⣹⡽⣫⣞⣧⡟⣿⡼⣫⣟⠷⣞⣻⣼⣻⢞⣧⣟⣯⣟⣳⣟⣾⣳⢯⣟⣾⣳⣟⣾⣳⣟⣾⣳⣟⡾⣷⣻⢾⣽⣻⣽⢾⣻⣞⣿
⣿⢾⣽⡳⣎⢷⣩⠛⣌⠦⣙⢦⠒⢎⠑⠂⢀⠂⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⡞⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡟⠃⠀⠆⠀⡇⠀⠀⣾⣟⢾⣫⢷⣛⡷⣽⣎⡿⣵⣻⣳⡽⣻⡽⣣⢷⢯⣟⡾⢧⣟⣾⣳⣟⡾⣽⣻⣞⣷⣻⣞⣷⣻⢾⣳⣟⣾⣻⢷⣻⣯⢷⡿⣽⣻⣽⣾⣻
⣿⣻⠾⣵⢫⢶⣡⠟⣬⠓⡍⢢⠉⣄⠊⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢰⠀⠀⠡⠂⠀⠀⠀⠀⠀⠀⠀⠠⣳⠄⣇⠀⠀⠀⠀⠈⠓⠚⠹⠛⠿⣿⣿⠀⠀⠀⠀⠀⡇⠀⣲⡿⣞⣯⡽⣏⣟⡾⣳⠾⣝⣧⢷⣻⣼⡳⣟⡽⣯⣻⢞⣽⣻⣞⡷⣻⢾⣽⣳⣟⣾⣳⣟⣾⣳⢯⣟⡿⣞⡷⣯⣿⣳⣯⡿⣽⣟⣷⣻⣾⣽
⣿⡽⣻⢜⡫⢚⠴⡉⢆⡱⡘⠦⡙⠠⢁⡀⢤⡰⢀⠈⠀⢀⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠐⠒⡄⠀⠁⡄⠀⠀⠀⠀⠀⠀⠓⠉⢹⠞⠑⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣠⣿⡽⢯⣶⢻⡽⣺⡽⣽⢻⡽⣞⣻⢶⣳⠿⣭⢷⣏⣷⣻⣞⣷⣫⢿⣽⣻⣞⣷⣻⣞⣷⣻⢾⡽⣯⢿⡽⣯⣟⡷⣯⣷⣻⣽⣟⣾⢯⣷⣟⣾
⡟⡼⡑⢎⠴⡉⠖⡉⢆⠱⡈⠔⣤⢳⣬⢿⣍⢇⡀⣀⣴⣿⢾⣽⣖⡀⠀⠀⢀⡀⠤⠐⢉⣴⣔⣼⠏⠒⢄⠈⠙⠄⠀⠀⠀⠀⠐⢦⡀⠀⠀⡀⠀⠈⠀⠊⠉⣁⣒⠒⠀⠀⢀⣀⢀⡠⢞⡴⣟⢧⢻⡙⣎⢷⡹⢇⠿⣜⢧⡻⣜⢧⢯⣝⡻⣭⢷⣻⣼⣳⢯⡶⣯⣟⣾⣳⣟⣾⣳⣟⡾⣽⢯⡿⣽⢯⣟⡷⣯⢿⣳⣯⣟⣾⣽⡾⣟⣷⣯⢿
⣞⡴⣉⣎⣲⣉⢦⣱⣊⢶⣙⡾⣼⣻⣾⣿⣾⣾⡶⣟⣯⢯⢷⡺⣽⡭⠖⠊⡁⠀⣠⣶⡿⠃⠋⡾⠄⡀⠀⠑⠌⡐⠳⢤⡀⠂⠀⠀⠈⠑⠒⠠⠤⢤⠔⠊⠉⠉⡚⠁⠀⠠⠔⢀⣴⡖⠯⠞⡉⠦⠷⢚⡉⢦⡙⠮⡙⠎⠣⢓⣍⡚⡶⢎⠷⣭⢳⣏⡾⣝⡯⣟⣳⣟⣾⣳⣟⣾⣳⢯⡿⣽⢯⡿⣽⣻⣞⡿⣽⣻⣽⢾⣽⣾⣳⢿⣻⣾⡽⣿
⣿⣿⣿⣿⣿⣿⣯⣷⣽⣫⣿⣽⣿⣿⣿⣟⡯⢷⣻⣝⣮⣟⠾⠋⡁⣤⠖⣫⣥⣾⡿⠏⠀⠀⠀⠁⠀⠚⠄⠀⠀⠀⠀⠀⠢⠉⡑⠢⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠐⢀⣠⠴⠊⠁⠀⡈⠙⠂⠉⣀⠉⠉⠉⠀⠀⠠⠀⠐⠈⠃⢈⠱⢡⣋⠞⣴⢫⢞⡱⢏⡞⣱⢯⣞⣷⣻⣞⡷⣯⢿⡽⣯⢿⣽⣳⣯⢿⡽⣯⣟⣾⢯⣷⢯⣟⡿⣽⣾⣻⣽
⣿⡿⣿⢿⣿⡿⣿⢿⡿⣿⢿⣟⡿⣳⢯⡾⡽⣏⠷⢚⣩⡔⣰⡾⢋⣴⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠘⡄⠀⠀⠀⠈⠀⠐⠠⠠⠔⠂⠇⡀⢀⠀⢐⣄⣶⣯⣶⡿⣿⣟⣿⡻⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣉⡂⠁⢋⡔⢣⢎⠵⢋⡜⡱⢾⣻⣞⡷⣯⢿⡽⣯⢿⣽⣻⣞⡷⣯⡿⣽⢷⣯⣟⡿⣞⣿⣽⣻⣽⡾⣯⢿
⣿⡽⣯⣟⡾⣽⢯⡿⣽⢯⣟⡾⣹⢝⡧⠟⢋⣡⣶⠟⠋⠙⠉⠰⠟⣉⠠⠤⠤⠀⠀⠠⠄⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⢒⣩⣿⢿⢯⡷⢯⡽⣶⣻⣼⢻⡵⣯⢿⡶⣄⡀⠉⠢⠤⣀⡀⠀⠀⠀⠀⠀⠈⠙⠦⣌⠁⢊⠔⠂⠰⣉⣿⣟⡾⣽⢯⡿⣽⢯⣟⣾⣳⢯⣟⡷⣟⣯⡿⣾⣽⣻⣽⢷⣯⣟⡷⣿⣻⢿
⣿⣽⣳⢯⡿⣽⢫⡟⡵⢋⣐⠬⢉⣩⣴⣾⣿⡯⠁⠈⠀⠄⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⡿⢯⣻⣛⡾⣯⢟⡷⣽⣺⢯⣟⡽⡾⣝⣿⣻⣵⣢⢤⣀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠂⠀⠀⠁⣰⣿⢯⡿⣽⢯⡿⣽⣻⣞⣷⣻⢯⡿⣽⢯⣷⣟⡷⣯⣷⣻⣟⣾⣽⣻⢷⣻⢿
⣟⠾⣭⠳⡝⢦⡏⠶⢓⣊⣥⣶⣿⣿⡿⠛⠉⠠⠔⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣮⣷⢶⣦⣴⣀⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣠⣴⡾⣟⣯⢟⣯⢷⢯⣻⡵⣯⣟⣳⣭⢷⣯⢻⡽⢯⣶⣛⡾⡽⣯⣟⡷⣿⢿⡿⣴⣖⣢⣤⣄⣀⠀⠀⠀⠀⣴⣿⢯⡿⣽⢯⡿⣽⣳⣟⣾⣳⢯⣿⡽⣯⢿⡾⣽⣻⢷⣯⢷⣻⣞⡷⣟⣯⢿⣻
⣎⠳⣌⡳⠞⣡⣴⢾⠿⡿⠿⢟⠋⡉⢁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣛⣾⣛⡾⣳⢯⢿⣹⢓⠈⢠⡙⢦⢖⡾⣷⣟⣯⢷⣻⡽⣞⣻⡞⣯⣻⢧⣟⡷⣽⣳⢯⣟⣞⣯⣽⣻⢶⢯⣛⣷⣳⢯⡾⣽⠾⣝⣟⡾⣽⢯⣟⣿⣻⢿⡿⣿⢿⡽⣯⢿⡽⣯⣟⣷⣻⣞⡷⣯⢿⡾⣽⢯⡿⣽⢷⣻⣟⡾⣿⡽⣯⣟⣯⣿⣻⣽
⠤⠡⢠⠁⣾⣋⠠⠉⠘⠡⠉⠊⠡⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⠿⣽⢶⣻⠶⣏⡷⣯⢯⣯⢳⡃⠌⠠⠁⠈⢎⢻⡷⣯⣞⢯⣗⣯⣽⢳⣻⣳⢯⣻⣞⣽⣳⢯⣟⡾⣽⡞⣧⣟⣯⣟⡽⣶⢯⡷⣻⣭⢿⡽⡾⣝⣷⣻⢞⣳⢯⡿⣽⢯⣻⡽⣯⢿⣽⣳⣟⣾⣳⢯⡿⣽⢯⡿⣽⣻⣽⢯⣟⡷⣯⣟⡷⣿⡽⣾⣻⢾⣽⣻
⠂⠓⠤⠦⢤⠤⠭⠤⣅⠠⣄⠡⠄⠄⠤⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⢀⣴⡿⣿⡽⣻⡽⡾⣝⣿⣹⡽⣞⣳⢯⡳⢌⠢⠁⠀⠀⠀⠘⣿⣳⣞⣟⡾⣞⣞⡯⢷⣫⣟⣳⣞⣧⡟⣯⢾⣽⡳⣟⡷⣯⣞⢾⡽⣞⣳⣟⣳⡽⡾⣽⡽⣛⡶⣯⢿⡽⣯⢿⣹⢯⣷⣻⣽⣻⣞⣷⣻⢾⡽⣯⢿⡽⣯⣟⣷⣻⣞⣯⢿⡽⣷⣻⣽⢷⣻⢷⣻⣯⡷⣿
⣤⣈⢀⠀⡀⠈⠀⠁⡀⠁⢀⠀⠂⠀⠀⠀⠀⠀⢀⡠⠐⡀⠔⣁⣴⡿⣯⣟⣳⣽⣳⠿⣽⣻⣼⣳⢯⣻⣭⠷⡍⢆⠡⠌⡀⠀⠀⠈⠼⣷⢯⣞⢷⣻⢮⣟⢯⡷⣽⣳⡞⣧⢿⡽⣯⢶⣻⣽⣳⢟⡼⣯⣻⣝⡷⣞⣳⢿⣹⣗⣻⡽⢯⡽⣾⡽⣏⡿⣽⣻⣞⢷⡯⣷⣻⢾⡽⣯⢿⡽⣯⣟⣷⣻⣞⡷⣯⣟⣯⣟⣷⣻⣞⡿⣽⣻⢷⣯⢿⣽
⠀⠉⠊⠓⠡⠋⠜⠒⠰⠉⠂⠘⠀⠁⣀⡠⠔⠒⡁⠔⢈⣴⣪⣷⢿⣽⣳⢯⡷⣯⣽⡻⣷⣛⡶⣯⢿⡵⣞⡻⡘⢄⠪⠔⡀⠄⠀⠀⢸⢻⣟⡾⣏⣷⡻⣞⣻⣼⡳⢷⣻⣭⣟⡾⣽⣫⢷⣳⢯⣻⣽⢳⣯⠾⣽⣝⣯⣞⣷⣫⢷⣻⢯⣟⣳⢿⣹⡟⣷⣛⡾⣯⣟⡷⣯⢿⡽⣯⢿⣽⣳⣟⣾⣳⢯⣟⣷⣻⢾⡽⣞⡷⣯⢿⡽⣯⣟⣾⢯⣿
⣿⣶⣵⣢⣔⡤⠠⢄⠠⢀⠐⠠⠐⠀⠀⢀⣀⣤⣴⡾⣟⣯⢷⣯⣟⡾⣭⣟⣳⣟⡾⣽⣳⢯⣟⡽⡾⣝⣣⠱⢌⢎⡑⠢⠐⠂⠀⠀⠀⢻⣟⡾⣽⡞⣽⡽⣧⢷⣻⢯⣳⢷⡾⣽⣳⢯⡟⣧⣟⣳⣞⡿⣼⣻⢧⣟⡾⣽⢶⢯⡿⣭⣟⡾⣽⢯⣷⣻⢷⣯⣟⡷⣯⢿⡽⣯⢿⣽⣻⣞⣷⣻⢾⣽⣻⣞⡷⣯⢿⡽⣯⢿⡽⣯⣟⣷⢯⣟⡿⣾
⣿⣿⣻⣟⡿⣿⣿⣶⣦⣦⡶⣖⡶⣮⢿⡽⣞⡷⣯⢿⡽⣞⡿⣶⢯⣟⡷⣯⢷⡯⣟⡷⣯⣟⡾⣽⢻⡜⢤⡓⣎⠒⡌⠥⢃⠠⠀⠀⠀⣻⣯⢿⣵⡻⣗⣿⣚⣯⠷⣯⣻⠾⣝⣳⣭⣟⣾⢳⣯⣳⢯⣞⡷⢯⣟⡾⣽⣻⣞⣯⣟⡷⣯⢿⣝⡿⣞⣽⣳⢾⡽⣽⢯⡿⣽⢯⣟⣾⣳⣟⡾⣽⣻⣞⡷⣯⢿⡽⣯⢿⡽⣯⣟⣷⣻⢾⣻⣽⣻⣽""")
        print("you flee in terror")
        montype = "Cosmic horror"
        monhealth = 99999999999999999999999999999999999999999999999999999999999999999999999999
        monmaxhealth = monhealth
        monexp = 9999999999999999999999999999999999999999999999999999999999999
        wpn = fishesbreath
        wpnatk = wpn.wpnatk
        gend = unknown
    
        
    monster = Entity(montype,gend,monhealth,monmaxhealth,monexp,mongold,wpnatk,wpn)
    monster.stats()

#main-----------------------------------------
encounter(male,female,unknown)