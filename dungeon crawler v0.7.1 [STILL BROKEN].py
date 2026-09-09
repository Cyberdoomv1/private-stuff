#imports----------------------------------------
from random import randint, choice
from time import sleep

#lists------------------------------------------
male = ["he","him","his","they","his"]
female = ["she","her","hers","they","her"]
unknown = ["it","them","its","they","their"]
roomlist = ["trap","encounter","encounter","chest","chest","chest","chest","empty","empty","empty"]
directions = ["north","south","east","west"]
#variable definitions---------------------------


#classes-------------------------------------------------------------------------------------------
class Entity:
    def __init__(self, name, gender, health, maxhealth, exp, gold, atk, wpn, xcor, ycor):
        self.name = name
        self.gender = gender
        self.health = health
        self.maxhealth = maxhealth
        self.exp = exp
        self.gold = gold
        self.atk = atk
        self.wpn = wpn
        self.xcor = xcor
        self.ycor = ycor
    
    def greeting(self):
        print("hello my name is",self.name)
        
    def attack(self,target,gender,wpn):
        print("***********************")
        print(self.name,self.wpn.wpnswing[randint(1,len(wpn.wpnswing))],target.name)
        print("dealing",self.atk,"damage")
        target.health = target.health - self.atk
        if target.health < (target.maxhealth * 0.25):
            print(gender[0],"is barely standing")
        elif target.health < (target.maxhealth * 0.5):
            print(gender[0],"is looking weak")
        elif target.health < (target.maxhealth * 0.75):
            print(gender[0],"is a little tired")
        if target.health > 0:
            print(target.name+"'s health is now",target.health)
        else:
            target.health = 0
            print("the",target.name,"is defeated")
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
    def __init__(self,roomtype,enemy):
        self.roomtype = roomtype
        self.enemy = enemy

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
celestialbreath = Weapon("breath",9999999999999999999999999999999999999999999999999999999999999999,["sprays fire","blows fire"])


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
player = Entity("steven the brave",male,100,100,0,0,shortsword.wpnatk,shortsword.wpnname,0,4)
# validating = True
# while validating:
#     nchoice = input("what is the heros name: ").title()
#     answer = str(input("you have chosen \""+nchoice+"\" is this correct? y/n: ")).lower()
#     if answer in("y","ye","yes"):
#         print("name set to",nchoice)
#         player.name = nchoice
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
#         print(player.name+"'s gender is now male")
#         player.gender = male
#         validating = False
#     elif gender in("f","female","girl"):
#         print(player.name+"'s gender is now female")
#         player.gender = female
#         validating = False
#     elif gender in("n","non","nonbinary","non-binary","non binary","none","no"):
#         print(player.name+"'s gender is now unknowable")
#         player.gender = unknown
#         validating = False
#     else:
#         print("invalid input try again")

#subroutines-----------------------------------------------------------------------------

def encounterstart(male,female,unknown,directions):
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
        print("""
⢨⠿⣽⢯⣟⡿⣽⣻⢟⡿⣽⣻⡟⣿⣽⣻⣟⣿⣻⣟⣿⣿⣿⡿⣿⣟⣿⣻⣟⣟⡻⢏⡛⠻⢿⣏⡙⢶⡈⠣⡀⢢⠀⠀⠀⠀⠀⠀⣿⢿⡽⣻⣽⣻⣽⣻⢯⣟⡿⣽⣻⢯⣟⣿⣻⢯⣟⣿⣻⢟⣿⣻⡟⣿⣽⣻⢯⣟⣯⠿⣽⢯⢿⡽⢯⡿⡽⢯⣿⣹⢯⢿⣹⢯⡿⡽⣯⣟⢿⣽⣻⢯⣟⡿⣻⣽⣻⣟⡿⣻⢯⣟⡿⣽⣻⢯⣟⡿⣽⣻
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
⣿⣿⣻⣟⡿⣿⣿⣶⣦⣦⡶⣖⡶⣮⢿⡽⣞⡷⣯⢿⡽⣞⡿⣶⢯⣟⡷⣯⢷⡯⣟⡷⣯⣟⡾⣽⢻⡜⢤⡓⣎⠒⡌⠥⢃⠠⠀⠀⠀⣻⣯⢿⣵⡻⣗⣿⣚⣯⠷⣯⣻⠾⣝⣳⣭⣟⣾⢳⣯⣳⢯⣞⡷⢯⣟⡾⣽⣻⣞⣯⣟⡷⣯⢿⣝⡿⣞⣽⣳⢾⡽⣽⢯⡿⣽⢯⣟⣾⣳⣟⡾⣽⣻⣞⡷⣯⢿⡽⣯⢿⡽⣯⣟⣷⣻⢾⣻⣽⣻⣽
""")
        print("you flee in terror")
        montype = "unspeakable horror"
        monhealth = 99999999999999999999999999999999999999999999999999999999999999999999999999
        monmaxhealth = monhealth
        monexp = 9999999999999999999999999999999999999999999999999999999999999
        wpn = celestialbreath
        wpnatk = wpn.wpnatk
        gend = unknown
        
    
        
    monster = Entity(montype,gend,monhealth,monmaxhealth,monexp,mongold,wpnatk,wpn,0,0)
    if monster.name not in("unspeakable horror"):
        fight(directions,monster,gend,wpn)
    else:
        print(monster.stats)
        escape()

def fight(directions,monster,gender,wpn):
    fighting = True
    while fighting:
        player.stats()
        monster.stats()
        validating = True
        while validating:
            if monster.name[0].lower() not in("o"):
                print("a",monster.name,"stands before you")
            else:
                print("an",monster.name,"stands before you")
            print("what will you do?")
            action = input("flee or attack: ").lower()
            if action in("r","run","flee","escape","1"):
                if monster.name == "Goblin":
                    escchance = randint(1,20)
                    if escchance > 5:
                        escape(directions,monster)
                        fighting = False
                    else:
                        print("the tiny but still intimidating Goblin brandishing its",monster.wpn.name,"blocked your way")
                        monster.attack(player,gender,wpn)
                elif monster.name == "Orc":
                    escchance = randint(1,20)
                    if escchance > 10:
                        escape(directions,monster)
                        fighting = False
                    else:
                        print("the strong Ork brandishing its",monster.wpn.wpnname,"blocked your way")
                        monster.attack(player,gender,wpn)
                        validating = False
                elif monster.name == "Ghoul":
                    escchance = randint(1,20)
                    if escchance > 17:
                        escape(directions,monster)
                        fighting = False
                    else:
                        print("the fearsome Ghoul brandishing its claws blocked your way")
                        monster.attack(player,gender,wpn)
                        validating = False
                elif monster.name == "Golem":
                    escchance = randint(1,20)
                    if escchance > 12:
                        escape(directions,monster)
                        fighting = False
                    else:
                        print("the hulking Golem brandishing its clublike fists blocked your way")
                        monster.attack(player,gender,wpn)
                        validating = False
                elif monster.name == "Dragon":
                    escchance = randint(1,20)
                    if escchance > 15:
                        escape(directions,monster)
                        fighting = False
                    else:
                        print("the fearsome dragon snorting flame blocked your way")
                        monster.attack(player,gender,wpn)
                        validating = False
                        
            elif action in("fight","attack","atk","strike","2"):
                player.attack(monster,gender,wpn)
                
        if monster.health == 0:
            if monster.name in("goblin","orc"):
                loot()

def escape(directions,monster):
    if player.xcor == 0 :
        directions.remove("west")
    elif player.xcor == 4:
        directions.remove("east")
    if player.ycor == 0:
        directions.remove("south")
    elif player.ycor == 4:
        directions.remove("north")
    validating2 = True
    while validating2:
        print("which way?")
        esc = input(str(directions)+": ").lower()
        if esc in("n","north","up","1") and "north" in directions:
            print("you dodge past the",monster.name,"and escape to the north chamber")
            player.ycor = player.ycor + 1
            validating2 = False
        elif esc in("e","east","right","2") and "east" in directions:
            print("you dodge past the",monster.name,"and escape to the east chamber")
            player.xcor = player.xcor + 1
            validating2 = False
        elif esc in("s","south","down","3") and "south" in directions:
            print("you dodge past the",monster.name,"and escape to the south chamber")
            player.ycor = player.ycor - 1
            validating2 = False
        elif esc in("w","west","left","4") and "west" in directions:
            print("you dodge past the",monster.name,"and escape to the west chamber")
            player.xcor = player.xcor - 1
            validating2 = False
        else:
            print("can't do that")
            validating2 = True

def loot():
    lootchance = randint(1,20)
    if lootchance > 14:
        print("the",monster.name,"dropped",monster.gender[2],monster.wpn)
        print(moster.name+"'s weapon")
        print("name:",monster.wpn)
        print("damage:",monster.atk)
        print("your weapon")
        print("name:",player.wpn)
        print("damage:",player.atk)
        validating = True
        while validating:
            choice = input("would you like to take",monster.gender[2],monster.wpn+"? y/n: ").lower()
            if choice in("y","yes","1"):
                print("you dropped your",player.wpn,"and you picked up the",monster.wpn,"from its corpse")
                player.wpn = monster.wpn
                validating = False
            elif choice in("n","no","2","nien"):
                print("you kicked the",monster.name+"'s",monster.wpn,"away")
            else:
                print("huh?")









#main-----------------------------------------
print("A large oaken door stands before",player.name," the entrance to a dungeon that has claimed many a brave adventurer")
print("the choice before "+player.gender[1]+" is one many have asked themselves: do you go in? ")
choice = input(":").lower()
validating = True
while validating:
    if choice in("y","yes","ye","i do"):
        player.xcor = 0
        player.ycor = 0
        encounterstart(male,female,unknown,directions)
        valdating = False
    elif choice in("n","no","i dont"):
        print("Despite all the money",player.name,"spent on",player.gender[2],"gear and cool sword",player.gender[0],"decides",player.gender[2],"life is worth more than fame riches and glory")
        print("and so",player.gender[0],"walked off back to",player.gender[4],"town never to do anything brave ever again.")
        sleep(3)
        print("""______ _       _____   __  _____ _   _  _____   _____   ___  ___  ___ _____  ____________ _________________ ___________ _   __   __
| ___ \ |     / _ \ \ / / |_   _| | | ||  ___| |  __ \ / _ \ |  \/  ||  ___| | ___ \ ___ \  _  | ___ \ ___ \  ___| ___ \ |  \ \ / /
| |_/ / |    / /_\ \ V /    | | | |_| || |__   | |  \// /_\ \| .  . || |__   | |_/ / |_/ / | | | |_/ / |_/ / |__ | |_/ / |   \ V / 
|  __/| |    |  _  |\ /     | | |  _  ||  __|  | | __ |  _  || |\/| ||  __|  |  __/|    /| | | |  __/|  __/|  __||    /| |    \ /  
| |   | |____| | | || |     | | | | | || |___  | |_\ \| | | || |  | || |___  | |   | |\ \\ \_/ / |   | |   | |___| |\ \| |____| |  
\_|   \_____/\_| |_/\_/     \_/ \_| |_/\____/   \____/\_| |_/\_|  |_/\____/  \_|   \_| \_|\___/\_|   \_|   \____/\_| \_\_____/\_/  
                                                                                                                                   
                                                                                                                                   """)
        validating = False
    else:
        print("I didnt catch that")
        choice = input("do you go in? ")
        