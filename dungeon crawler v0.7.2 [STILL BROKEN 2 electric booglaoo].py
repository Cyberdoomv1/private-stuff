#imports----------------------------------------
from random import randint, choice
from time import sleep

#lists------------------------------------------
male = ["he","him","his","they","his"]
female = ["she","her","hers","they","her"]
unknown = ["it","them","its","they","their"]
roomlist = ["trap","encounter","encounter","chest","chest","chest","chest","empty","empty","blocked"]
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
    def __init__(self,roomtype,enemy,discovered):
        self.roomtype = roomtype
        self.enemy = enemy
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
celestialbreath = Weapon("breath",9999999999999999999999999999999999999999999999999999999999999999,["sprays fire","blows fire"])


   
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

#creates the monsters for enounter rooms
def encountersetup():
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
#         print("""
# ⢨⠿⣽⢯⣟⡿⣽⣻⢟⡿⣽⣻⡟⣿⣽⣻⣟⣿⣻⣟⣿⣿⣿⡿⣿⣟⣿⣻⣟⣟⡻⢏⡛⠻⢿⣏⡙⢶⡈⠣⡀⢢⠀⠀⠀⠀⠀⠀⣿⢿⡽⣻⣽⣻⣽⣻⢯⣟⡿⣽⣻⢯⣟⣿⣻⢯⣟⣿⣻⢟⣿⣻⡟⣿⣽⣻⢯⣟⣯⠿⣽⢯⢿⡽⢯⡿⡽⢯⣿⣹⢯⢿⣹⢯⡿⡽⣯⣟⢿⣽⣻⢯⣟⡿⣻⣽⣻⣟⡿⣻⢯⣟⡿⣽⣻⢯⣟⡿⣽⣻
# ⢨⠿⣽⠾⣽⣞⡷⣯⢿⣽⣳⢯⣟⡷⣯⢷⣞⠷⣯⢟⡯⣿⣻⣿⣿⢿⡷⣯⢞⣼⣱⡉⡙⠶⣄⡈⠳⡄⠙⡄⠡⠀⢀⠀⠀⠠⢪⣥⣿⣯⣟⣳⡽⣾⣱⢯⣟⡾⣽⣳⢯⣟⣾⣳⢯⣟⣾⣳⢯⣟⣾⣳⣟⡷⣽⡞⣟⣮⢯⢿⡽⣞⣻⣞⢯⣷⢻⡟⣶⢯⣻⣭⡟⣾⡽⣻⡵⣞⡿⢮⣟⡽⣾⣽⣳⢯⡷⣯⢿⣽⡻⣾⢽⣳⢯⣟⡾⣽⣳⢯
# ⠀⡿⣝⣻⢧⡿⣽⣞⣟⡾⣽⣻⢾⡽⣯⣟⣾⣻⣼⣣⡽⣆⢧⢣⠏⢧⠛⡴⢫⢔⣀⠋⠓⢦⠀⠹⡄⠘⠀⠀⠀⠀⠀⠀⠀⣴⠿⠛⠉⡉⢉⡙⡷⠯⣯⣟⡾⣽⣳⢯⣟⡾⢧⣟⣟⡾⣳⢯⣟⣾⣳⠿⣼⣛⣧⢿⡽⣞⡯⣟⡾⣝⡷⣞⣻⡼⣏⣟⣧⡟⣧⢷⣛⣧⡟⣷⣻⣭⡟⣟⡾⣽⣳⢾⡽⣯⢷⣯⢟⣶⣻⡽⢯⣻⣛⡾⣽⣳⢯⣟
# ⠀⠘⣯⢯⣟⡽⣾⣹⢾⣽⣳⢯⡿⣽⣳⢿⡳⣟⢷⡻⠿⡝⣏⠮⡙⢎⡙⠦⢡⢎⡈⠙⠆⠀⠑⠀⠀⠀⠀⠀⢀⡀⠰⣈⠕⢁⡠⢐⣡⣶⣿⡹⣖⠲⠄⠽⣿⣧⠿⣽⣺⣽⢻⡾⣭⢿⣽⢻⣞⣧⡟⣿⡳⣟⣾⢫⡷⢯⡽⣾⣹⡽⣞⣽⣣⢿⣹⣞⣮⣽⣛⡾⣽⣺⢽⡳⣧⢷⣻⡽⣽⡳⣯⢟⡾⣽⣳⢯⣟⣞⣧⣟⣯⢷⣯⣟⡷⣯⣟⣾
# ⠀⠀⠘⣻⠾⣽⣳⢯⣟⡾⣭⣟⠾⣵⢫⠞⡵⣩⠖⡱⢍⡜⠤⢃⠍⠂⠌⡐⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠈⢂⠼⠃⣀⢔⣉⡰⣚⣿⡵⡾⠃⢀⡴⠡⠀⠈⢿⢿⣳⡽⣞⣯⠷⣯⣻⢞⣟⣮⢷⣻⣳⢟⡽⣞⣯⢟⣯⡽⡶⣏⣷⣛⡶⣏⣯⠷⣞⡵⡾⣭⢷⣻⡼⢯⣽⡳⣯⣳⢟⡾⣝⣳⢯⣟⣳⢯⣟⡾⣽⢾⣹⣞⡿⣞⣭⣟⣷⣻⢾
# ⠀⠀⠀⢨⣛⢷⢯⣟⡾⣽⣳⢏⡿⣘⠧⡛⡔⠣⢎⡑⢊⠰⢁⠊⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠜⠁⣴⠏⣴⣯⣟⣵⣿⣷⢧⠱⡍⣒⡆⠀⠀⠀⠂⠈⠛⣿⢾⣱⣟⣳⢯⣻⡞⣽⣞⣳⣭⠿⣽⡞⣽⡞⣧⣟⣳⠿⣜⡷⣫⡽⣞⣻⣭⢟⣳⢯⡷⣫⣞⠿⣶⣻⡵⣯⣻⡽⣝⣯⣟⡾⣽⣛⡾⣽⣏⣿⣳⢯⡿⣽⢾⡽⣾⣽⣻
# ⠀⣀⢠⢦⡝⣿⣟⡾⣽⣳⡝⣎⠶⣑⢎⡱⡘⠍⠆⡙⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠒⠈⣀⠴⣋⠏⢸⢿⣴⣻⣿⣾⣳⡿⠃⠘⠁⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠿⣭⢿⣱⣟⣳⡞⣷⣫⣟⡧⣟⣧⣟⣳⠾⣭⢿⣹⡞⣷⣫⡽⣞⣮⢟⡽⣾⣹⡗⣯⣟⣳⢷⣫⢷⣳⢿⣹⣞⡾⣽⣳⢯⣟⣷⣻⢾⡽⣯⢿⡽⣯⣟⡷⣯⣟
# ⣜⢦⣻⢾⣽⡳⢯⡟⡷⢿⣼⠮⠕⠊⠀⠁⠈⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⠁⠀⠀⡰⠁⡴⠠⠂⡎⢻⣿⣿⡿⠃⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣻⠽⣞⣳⣞⣧⢟⣳⢷⣹⠾⣝⣶⣫⣽⢻⡽⣺⢧⡟⣧⡟⣵⣻⡼⣏⡿⣖⢿⣼⣳⢯⣻⠾⣽⣫⡽⣞⡷⣯⣟⡷⣯⣟⣾⣳⢯⡿⣽⢯⡿⣽⣳⢯⣟⣷⣻
# ⣯⢿⣽⣿⣷⣻⡟⣼⢣⡃⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⡠⠃⠀⠀⠀⠀⢰⡤⢏⢃⠌⡌⢹⠠⠓⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢯⡿⣭⠷⣾⣹⠾⣽⠾⣭⢿⣹⢶⡻⣼⢏⡷⢯⣳⢟⣵⡻⢧⣷⢫⡽⣞⣭⣟⡶⢯⣛⣷⣻⠷⣏⡿⣽⢯⡷⣾⣽⣳⣟⡾⣽⢯⡿⣽⢯⣟⡷⣯⢿⣞⣷⣻
# ⣿⡿⣽⣻⣷⣯⣟⣽⢣⡝⠬⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⡱⠁⠀⠀⠀⠀⠀⠃⡇⠋⠔⡨⠒⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣳⡟⣧⣟⣻⣭⢿⣹⠾⣭⢷⣛⣧⢿⣹⢯⣳⢟⣮⣽⢻⡼⣏⣿⣹⣞⠾⣽⢯⣟⢾⣭⢿⣽⣻⣭⢿⣽⣳⣞⡷⣯⢿⡽⣯⢿⣽⣻⢾⡽⣯⣟⣾⣳⢿
# ⣿⣿⢿⣟⣷⡿⣞⣮⢳⡬⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠉⠡⠊⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣻⡵⣞⡷⡽⣾⡹⣟⡽⢾⣹⢮⣛⣮⢯⣗⣻⣞⡼⣯⣳⢟⣶⡻⣼⣻⡽⢾⣭⣟⢾⣻⣼⣳⢯⣟⣾⣳⢯⡿⣽⢯⡿⣽⣻⢾⡽⣯⣟⣷⣻⢾⣽⣻
# ⣿⣻⡿⣯⣿⣻⣽⢮⡳⣜⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⡴⠶⣝⡤⣤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣻⣝⡾⣽⢳⣻⣝⡾⣏⡷⣏⡿⣼⢳⢯⣞⠾⣽⠶⣏⡿⢶⣛⣷⣳⡻⣟⡼⣞⣯⢷⣳⢯⣟⣾⣳⢯⡿⣽⢯⡿⣽⣳⢯⡿⣽⣳⣟⡾⣽⣻⢾⣽
# ⣿⣳⣟⣯⠷⣯⣟⢯⡳⣍⠦⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣖⡆⢔⡶⣽⡞⣤⡗⠈⣲⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⣻⡼⣏⡿⣵⣞⣳⢯⣳⢯⣳⢯⢯⡷⣫⣟⢧⡿⣽⣹⢯⣛⡶⣯⡽⢯⣽⢻⡼⣏⣷⣻⢞⣧⣟⣯⢿⡽⣯⣟⡷⣯⢿⣽⣳⣟⡾⣽⢷⣻⣟⣾
# ⣿⣳⢾⣜⢻⡖⢯⢳⡙⣆⠣⠜⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⠼⣳⣡⠜⠒⠚⠷⠮⡄⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣻⣭⢷⣳⠾⣭⢷⣫⢯⣗⣯⣻⣼⢳⢯⣛⣾⢳⣏⡿⣭⢷⢯⣽⣛⡾⢯⣽⢻⣼⡳⣟⡾⣽⣞⣯⣟⡷⣯⢿⣽⣻⣞⡷⣯⢿⡽⣯⢷⣻⢾
# ⣿⡽⣏⢮⣓⡎⡇⢧⡙⢦⡛⡜⣜⣶⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠈⣰⡿⡿⠆⡀⠀⠀⢱⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣟⡾⣭⢿⣹⠾⣭⢷⣞⢮⢷⡞⣯⣻⣝⠾⣏⡾⣽⠽⣞⣯⢶⢯⣛⡿⣼⡻⣶⣻⡽⣽⢾⡽⣾⣽⣻⣽⣻⣞⡷⣯⢿⡽⣯⢿⣽⣻⣽⣻
# ⣿⡽⣞⣧⢻⡜⡹⢎⡝⢦⡹⣹⢮⣿⢧⡑⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠁⠀⠠⠋⣸⣷⣆⢹⠀⣆⡼⠃⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠙⠻⡾⣭⢷⣻⠽⣞⣞⢯⡷⣻⣵⣳⡞⣿⣹⡽⣞⢿⣹⡞⣯⣻⣭⢷⢯⡷⣏⣷⣻⡽⣾⣽⣳⢷⣻⣞⡷⣯⢿⡽⣯⢿⣽⣻⣞⡷⣯⢿
# ⣿⣽⡻⣜⠧⣙⢧⠫⡜⢣⠒⡁⠻⣽⠢⡑⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠏⠆⠀⠀⠰⣿⣿⣿⡘⢠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡅⡀⠀⡄⢶⣜⣿⢞⣭⢿⣹⢮⣟⣼⣳⢧⡷⣛⣧⢿⣱⢯⡟⣧⣟⣳⠷⣽⣞⣻⣼⢻⡶⣯⢷⣻⢾⡽⣯⢷⣯⢿⡽⣯⢿⣽⣻⣞⡷⣯⢿⣽⣻
# ⣟⠶⣉⠆⣁⠂⢂⠑⠨⢁⠂⠀⠁⠢⠑⡠⠁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠝⡸⠀⠀⠀⢅⠻⡿⢏⣁⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠤⠀⣿⠅⡞⣰⣶⡄⢻⣻⢮⢯⣳⡟⣼⢧⣟⡾⣝⣻⡼⣏⣯⢟⣾⣳⣭⡟⣯⢷⣞⣳⢯⣟⡷⣯⢿⡽⣯⢿⣽⣻⣞⣯⢿⣽⣻⣞⡷⣯⢿⣽⣻⢾⣽
# ⣿⢯⡷⣞⣵⣎⣦⡜⣤⢂⡐⡄⢂⠄⡡⠀⠄⠁⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠂⡇⠃⠀⠀⠈⠃⠝⠁⢜⣾⠥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⢿⣿⣿⡇⣸⡷⢯⣻⡵⣻⠽⣞⣾⣹⡽⢧⣿⣹⣞⣻⢶⣛⣶⣻⢽⡾⣭⠿⣽⠾⣽⢯⡿⣽⢯⣟⣾⣳⣟⡾⣯⡷⣟⣾⣻⡽⣟⣾⡽⣟⣾
# ⡿⣯⢿⡽⣾⡹⢾⡹⣏⢯⡳⣝⢮⡚⢤⠃⠌⡀⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡍⢰⢁⠀⠀⠈⠐⠠⠀⠀⠸⡥⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⡀⠐⠀⣻⡆⢙⣿⠟⢁⡿⡽⣏⡷⣽⢫⣿⣹⠶⣯⣽⣛⡶⢯⡾⣝⣯⢿⡼⣏⣷⣻⣽⣻⣽⣻⡽⣯⢿⣽⣻⣞⣷⣻⣞⣿⣳⣟⣯⣷⣻⣽⢯⡷⣟⣯⢿
# ⣿⡽⣯⣟⣶⣛⢯⡳⡝⣎⡳⣍⠶⣙⠦⡉⢆⠠⠁⡀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠠⠀⠀⢀⠊⠀⠀⣠⣶⣿⣿⣿⣦⣥⣒⠠⡀⠈⠢⡁⠘⢽⡀⡉⣰⣿⢻⡽⣝⣳⢯⣟⡶⢯⣟⣳⠾⣭⣟⢯⣷⢻⣞⣯⣽⢻⡾⣵⣳⣟⣾⣳⢿⣽⣻⣞⣷⣻⣞⣷⣻⣞⣷⣻⣞⣷⣻⢾⣻⣽⢿⣽⣻
# ⣿⣽⣳⢯⣶⡹⣎⠷⣝⢮⠳⢎⡹⢄⠣⢌⡐⢂⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢺⠀⠀⠁⠀⠀⠀⠀⠀⠀⠠⠀⠐⢀⠆⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⢂⠀⠱⠀⠀⡉⢉⣿⣭⢿⣹⡽⣫⣞⣧⡟⣿⡼⣫⣟⠷⣞⣻⣼⣻⢞⣧⣟⣯⣟⣳⣟⣾⣳⢯⣟⣾⣳⣟⣾⣳⣟⣾⣳⣟⡾⣷⣻⢾⣽⣻⣽⢾⣻⣞⣿
# ⣿⢾⣽⡳⣎⢷⣩⠛⣌⠦⣙⢦⠒⢎⠑⠂⢀⠂⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⡞⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡟⠃⠀⠆⠀⡇⠀⠀⣾⣟⢾⣫⢷⣛⡷⣽⣎⡿⣵⣻⣳⡽⣻⡽⣣⢷⢯⣟⡾⢧⣟⣾⣳⣟⡾⣽⣻⣞⣷⣻⣞⣷⣻⢾⣳⣟⣾⣻⢷⣻⣯⢷⡿⣽⣻⣽⣾⣻
# ⣿⣻⠾⣵⢫⢶⣡⠟⣬⠓⡍⢢⠉⣄⠊⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢰⠀⠀⠡⠂⠀⠀⠀⠀⠀⠀⠀⠠⣳⠄⣇⠀⠀⠀⠀⠈⠓⠚⠹⠛⠿⣿⣿⠀⠀⠀⠀⠀⡇⠀⣲⡿⣞⣯⡽⣏⣟⡾⣳⠾⣝⣧⢷⣻⣼⡳⣟⡽⣯⣻⢞⣽⣻⣞⡷⣻⢾⣽⣳⣟⣾⣳⣟⣾⣳⢯⣟⡿⣞⡷⣯⣿⣳⣯⡿⣽⣟⣷⣻⣾⣽
# ⣿⡽⣻⢜⡫⢚⠴⡉⢆⡱⡘⠦⡙⠠⢁⡀⢤⡰⢀⠈⠀⢀⣀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠐⠒⡄⠀⠁⡄⠀⠀⠀⠀⠀⠀⠓⠉⢹⠞⠑⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⣠⣿⡽⢯⣶⢻⡽⣺⡽⣽⢻⡽⣞⣻⢶⣳⠿⣭⢷⣏⣷⣻⣞⣷⣫⢿⣽⣻⣞⣷⣻⣞⣷⣻⢾⡽⣯⢿⡽⣯⣟⡷⣯⣷⣻⣽⣟⣾⢯⣷⣟⣾
# ⡟⡼⡑⢎⠴⡉⠖⡉⢆⠱⡈⠔⣤⢳⣬⢿⣍⢇⡀⣀⣴⣿⢾⣽⣖⡀⠀⠀⢀⡀⠤⠐⢉⣴⣔⣼⠏⠒⢄⠈⠙⠄⠀⠀⠀⠀⠐⢦⡀⠀⠀⡀⠀⠈⠀⠊⠉⣁⣒⠒⠀⠀⢀⣀⢀⡠⢞⡴⣟⢧⢻⡙⣎⢷⡹⢇⠿⣜⢧⡻⣜⢧⢯⣝⡻⣭⢷⣻⣼⣳⢯⡶⣯⣟⣾⣳⣟⣾⣳⣟⡾⣽⢯⡿⣽⢯⣟⡷⣯⢿⣳⣯⣟⣾⣽⡾⣟⣷⣯⢿
# ⣞⡴⣉⣎⣲⣉⢦⣱⣊⢶⣙⡾⣼⣻⣾⣿⣾⣾⡶⣟⣯⢯⢷⡺⣽⡭⠖⠊⡁⠀⣠⣶⡿⠃⠋⡾⠄⡀⠀⠑⠌⡐⠳⢤⡀⠂⠀⠀⠈⠑⠒⠠⠤⢤⠔⠊⠉⠉⡚⠁⠀⠠⠔⢀⣴⡖⠯⠞⡉⠦⠷⢚⡉⢦⡙⠮⡙⠎⠣⢓⣍⡚⡶⢎⠷⣭⢳⣏⡾⣝⡯⣟⣳⣟⣾⣳⣟⣾⣳⢯⡿⣽⢯⡿⣽⣻⣞⡿⣽⣻⣽⢾⣽⣾⣳⢿⣻⣾⡽⣿
# ⣿⣿⣿⣿⣿⣿⣯⣷⣽⣫⣿⣽⣿⣿⣿⣟⡯⢷⣻⣝⣮⣟⠾⠋⡁⣤⠖⣫⣥⣾⡿⠏⠀⠀⠀⠁⠀⠚⠄⠀⠀⠀⠀⠀⠢⠉⡑⠢⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠐⢀⣠⠴⠊⠁⠀⡈⠙⠂⠉⣀⠉⠉⠉⠀⠀⠠⠀⠐⠈⠃⢈⠱⢡⣋⠞⣴⢫⢞⡱⢏⡞⣱⢯⣞⣷⣻⣞⡷⣯⢿⡽⣯⢿⣽⣳⣯⢿⡽⣯⣟⣾⢯⣷⢯⣟⡿⣽⣾⣻⣽
# ⣿⡿⣿⢿⣿⡿⣿⢿⡿⣿⢿⣟⡿⣳⢯⡾⡽⣏⠷⢚⣩⡔⣰⡾⢋⣴⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠘⡄⠀⠀⠀⠈⠀⠐⠠⠠⠔⠂⠇⡀⢀⠀⢐⣄⣶⣯⣶⡿⣿⣟⣿⡻⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣉⡂⠁⢋⡔⢣⢎⠵⢋⡜⡱⢾⣻⣞⡷⣯⢿⡽⣯⢿⣽⣻⣞⡷⣯⡿⣽⢷⣯⣟⡿⣞⣿⣽⣻⣽⡾⣯⢿
# ⣿⡽⣯⣟⡾⣽⢯⡿⣽⢯⣟⡾⣹⢝⡧⠟⢋⣡⣶⠟⠋⠙⠉⠰⠟⣉⠠⠤⠤⠀⠀⠠⠄⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⢒⣩⣿⢿⢯⡷⢯⡽⣶⣻⣼⢻⡵⣯⢿⡶⣄⡀⠉⠢⠤⣀⡀⠀⠀⠀⠀⠀⠈⠙⠦⣌⠁⢊⠔⠂⠰⣉⣿⣟⡾⣽⢯⡿⣽⢯⣟⣾⣳⢯⣟⡷⣟⣯⡿⣾⣽⣻⣽⢷⣯⣟⡷⣿⣻⢿
# ⣿⣽⣳⢯⡿⣽⢫⡟⡵⢋⣐⠬⢉⣩⣴⣾⣿⡯⠁⠈⠀⠄⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⡿⢯⣻⣛⡾⣯⢟⡷⣽⣺⢯⣟⡽⡾⣝⣿⣻⣵⣢⢤⣀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠉⠂⠀⠀⠁⣰⣿⢯⡿⣽⢯⡿⣽⣻⣞⣷⣻⢯⡿⣽⢯⣷⣟⡷⣯⣷⣻⣟⣾⣽⣻⢷⣻⢿
# ⣟⠾⣭⠳⡝⢦⡏⠶⢓⣊⣥⣶⣿⣿⡿⠛⠉⠠⠔⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣮⣷⢶⣦⣴⣀⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣠⣴⡾⣟⣯⢟⣯⢷⢯⣻⡵⣯⣟⣳⣭⢷⣯⢻⡽⢯⣶⣛⡾⡽⣯⣟⡷⣿⢿⡿⣴⣖⣢⣤⣄⣀⠀⠀⠀⠀⣴⣿⢯⡿⣽⢯⡿⣽⣳⣟⣾⣳⢯⣿⡽⣯⢿⡾⣽⣻⢷⣯⢷⣻⣞⡷⣟⣯⢿⣻
# ⣎⠳⣌⡳⠞⣡⣴⢾⠿⡿⠿⢟⠋⡉⢁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣛⣾⣛⡾⣳⢯⢿⣹⢓⠈⢠⡙⢦⢖⡾⣷⣟⣯⢷⣻⡽⣞⣻⡞⣯⣻⢧⣟⡷⣽⣳⢯⣟⣞⣯⣽⣻⢶⢯⣛⣷⣳⢯⡾⣽⠾⣝⣟⡾⣽⢯⣟⣿⣻⢿⡿⣿⢿⡽⣯⢿⡽⣯⣟⣷⣻⣞⡷⣯⢿⡾⣽⢯⡿⣽⢷⣻⣟⡾⣿⡽⣯⣟⣯⣿⣻⣽
# ⠤⠡⢠⠁⣾⣋⠠⠉⠘⠡⠉⠊⠡⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⠿⣽⢶⣻⠶⣏⡷⣯⢯⣯⢳⡃⠌⠠⠁⠈⢎⢻⡷⣯⣞⢯⣗⣯⣽⢳⣻⣳⢯⣻⣞⣽⣳⢯⣟⡾⣽⡞⣧⣟⣯⣟⡽⣶⢯⡷⣻⣭⢿⡽⡾⣝⣷⣻⢞⣳⢯⡿⣽⢯⣻⡽⣯⢿⣽⣳⣟⣾⣳⢯⡿⣽⢯⡿⣽⣻⣽⢯⣟⡷⣯⣟⡷⣿⡽⣾⣻⢾⣽⣻
# ⠂⠓⠤⠦⢤⠤⠭⠤⣅⠠⣄⠡⠄⠄⠤⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⢀⣴⡿⣿⡽⣻⡽⡾⣝⣿⣹⡽⣞⣳⢯⡳⢌⠢⠁⠀⠀⠀⠘⣿⣳⣞⣟⡾⣞⣞⡯⢷⣫⣟⣳⣞⣧⡟⣯⢾⣽⡳⣟⡷⣯⣞⢾⡽⣞⣳⣟⣳⡽⡾⣽⡽⣛⡶⣯⢿⡽⣯⢿⣹⢯⣷⣻⣽⣻⣞⣷⣻⢾⡽⣯⢿⡽⣯⣟⣷⣻⣞⣯⢿⡽⣷⣻⣽⢷⣻⢷⣻⣯⡷⣿
# ⣤⣈⢀⠀⡀⠈⠀⠁⡀⠁⢀⠀⠂⠀⠀⠀⠀⠀⢀⡠⠐⡀⠔⣁⣴⡿⣯⣟⣳⣽⣳⠿⣽⣻⣼⣳⢯⣻⣭⠷⡍⢆⠡⠌⡀⠀⠀⠈⠼⣷⢯⣞⢷⣻⢮⣟⢯⡷⣽⣳⡞⣧⢿⡽⣯⢶⣻⣽⣳⢟⡼⣯⣻⣝⡷⣞⣳⢿⣹⣗⣻⡽⢯⡽⣾⡽⣏⡿⣽⣻⣞⢷⡯⣷⣻⢾⡽⣯⢿⡽⣯⣟⣷⣻⣞⡷⣯⣟⣯⣟⣷⣻⣞⡿⣽⣻⢷⣯⢿⣽
# ⠀⠉⠊⠓⠡⠋⠜⠒⠰⠉⠂⠘⠀⠁⣀⡠⠔⠒⡁⠔⢈⣴⣪⣷⢿⣽⣳⢯⡷⣯⣽⡻⣷⣛⡶⣯⢿⡵⣞⡻⡘⢄⠪⠔⡀⠄⠀⠀⢸⢻⣟⡾⣏⣷⡻⣞⣻⣼⡳⢷⣻⣭⣟⡾⣽⣫⢷⣳⢯⣻⣽⢳⣯⠾⣽⣝⣯⣞⣷⣫⢷⣻⢯⣟⣳⢿⣹⡟⣷⣛⡾⣯⣟⡷⣯⢿⡽⣯⢿⣽⣳⣟⣾⣳⢯⣟⣷⣻⢾⡽⣞⡷⣯⢿⡽⣯⣟⣾⢯⣿
# ⣿⣶⣵⣢⣔⡤⠠⢄⠠⢀⠐⠠⠐⠀⠀⢀⣀⣤⣴⡾⣟⣯⢷⣯⣟⡾⣭⣟⣳⣟⡾⣽⣳⢯⣟⡽⡾⣝⣣⠱⢌⢎⡑⠢⠐⠂⠀⠀⠀⢻⣟⡾⣽⡞⣽⡽⣧⢷⣻⢯⣳⢷⡾⣽⣳⢯⡟⣧⣟⣳⣞⡿⣼⣻⢧⣟⡾⣽⢶⢯⡿⣭⣟⡾⣽⢯⣷⣻⢷⣯⣟⡷⣯⢿⡽⣯⢿⣽⣻⣞⣷⣻⢾⣽⣻⣞⡷⣯⢿⡽⣯⢿⡽⣯⣟⣷⢯⣟⡿⣾
# ⣿⣿⣻⣟⡿⣿⣿⣶⣦⣦⡶⣖⡶⣮⢿⡽⣞⡷⣯⢿⡽⣞⡿⣶⢯⣟⡷⣯⢷⡯⣟⡷⣯⣟⡾⣽⢻⡜⢤⡓⣎⠒⡌⠥⢃⠠⠀⠀⠀⣻⣯⢿⣵⡻⣗⣿⣚⣯⠷⣯⣻⠾⣝⣳⣭⣟⣾⢳⣯⣳⢯⣞⡷⢯⣟⡾⣽⣻⣞⣯⣟⡷⣯⢿⣝⡿⣞⣽⣳⢾⡽⣽⢯⡿⣽⢯⣟⣾⣳⣟⡾⣽⣻⣞⡷⣯⢿⡽⣯⢿⡽⣯⣟⣷⣻⢾⣻⣽⣻⣽
# """)
        montype = "unspeakable horror"
        monhealth = 99999999999999999999999999999999999999999999999999999999999999999999999999
        monmaxhealth = monhealth
        monexp = 9999999999999999999999999999999999999999999999999999999999999
        wpn = celestialbreath
        wpnatk = wpn.wpnatk
        gend = unknown
        
    
        
    monster = Entity(montype,gend,monhealth,monmaxhealth,monexp,mongold,wpnatk,wpn,0,0)
    return monster

#sets up rooms
def roomsetup():
    rtype = randint(0,9)
    rtype = roomlist[rtype]
    if rtype == "encounter":
        montype = encountersetup()
    else:
        montype = "hey how did you do that exactly?"
    return rtype,montype

#rooms
r00 = Room(roomsetup()[0],roomsetup()[1],False)
r01 = Room(roomsetup()[0],roomsetup()[1],False)
r02 = Room(roomsetup()[0],roomsetup()[1],False)
r03 = Room(roomsetup()[0],roomsetup()[1],False)
r04 = Room(roomsetup()[0],roomsetup()[1],False)
r05 = Room(roomsetup()[0],roomsetup()[1],False)
r06 = Room(roomsetup()[0],roomsetup()[1],False)
r07 = Room(roomsetup()[0],roomsetup()[1],False)
r08 = Room(roomsetup()[0],roomsetup()[1],False)
r09 = Room(roomsetup()[0],roomsetup()[1],False)
r010 = Room(roomsetup()[0],roomsetup()[1],False)
r10 = Room(roomsetup()[0],roomsetup()[1],False)
r11 = Room(roomsetup()[0],roomsetup()[1],False)
r12 = Room(roomsetup()[0],roomsetup()[1],False)
r13 = Room(roomsetup()[0],roomsetup()[1],False)
r14 = Room(roomsetup()[0],roomsetup()[1],False)
r15 = Room(roomsetup()[0],roomsetup()[1],False)
r16 = Room(roomsetup()[0],roomsetup()[1],False)
r17 = Room(roomsetup()[0],roomsetup()[1],False)
r18 = Room(roomsetup()[0],roomsetup()[1],False)
r19 = Room(roomsetup()[0],roomsetup()[1],False)
r110 = Room(roomsetup()[0],roomsetup()[1],False)
r20 = Room(roomsetup()[0],roomsetup()[1],False)
r21 = Room(roomsetup()[0],roomsetup()[1],False)
r22 = Room(roomsetup()[0],roomsetup()[1],False)
r23 = Room(roomsetup()[0],roomsetup()[1],False)
r24 = Room(roomsetup()[0],roomsetup()[1],False)
r25 = Room(roomsetup()[0],roomsetup()[1],False)
r26 = Room(roomsetup()[0],roomsetup()[1],False)
r27 = Room(roomsetup()[0],roomsetup()[1],False)
r28 = Room(roomsetup()[0],roomsetup()[1],False)
r29 = Room(roomsetup()[0],roomsetup()[1],False)
r210 = Room(roomsetup()[0],roomsetup()[1],False)
r30 = Room(roomsetup()[0],roomsetup()[1],False)
r31 = Room(roomsetup()[0],roomsetup()[1],False)
r32 = Room(roomsetup()[0],roomsetup()[1],False)
r33 = Room(roomsetup()[0],roomsetup()[1],False)
r34 = Room(roomsetup()[0],roomsetup()[1],False)
r35 = Room(roomsetup()[0],roomsetup()[1],False)
r36 = Room(roomsetup()[0],roomsetup()[1],False)
r37 = Room(roomsetup()[0],roomsetup()[1],False)
r38 = Room(roomsetup()[0],roomsetup()[1],False)
r39 = Room(roomsetup()[0],roomsetup()[1],False)
r310 = Room(roomsetup()[0],roomsetup()[1],False)
r40 = Room(roomsetup()[0],roomsetup()[1],False)
r41 = Room(roomsetup()[0],roomsetup()[1],False)
r42 = Room(roomsetup()[0],roomsetup()[1],False)
r43 = Room(roomsetup()[0],roomsetup()[1],False)
r44 = Room(roomsetup()[0],roomsetup()[1],False)
r45 = Room(roomsetup()[0],roomsetup()[1],False)
r46 = Room(roomsetup()[0],roomsetup()[1],False)
r47 = Room(roomsetup()[0],roomsetup()[1],False)
r48 = Room(roomsetup()[0],roomsetup()[1],False)
r49 = Room(roomsetup()[0],roomsetup()[1],False)
r410 = Room(roomsetup()[0],roomsetup()[1],False)
r50 = Room(roomsetup()[0],roomsetup()[1],False)
r51 = Room(roomsetup()[0],roomsetup()[1],False)
r52 = Room(roomsetup()[0],roomsetup()[1],False)
r53 = Room(roomsetup()[0],roomsetup()[1],False)
r54 = Room(roomsetup()[0],roomsetup()[1],False)
r55 = Room(roomsetup()[0],roomsetup()[1],False)
r56 = Room(roomsetup()[0],roomsetup()[1],False)
r57 = Room(roomsetup()[0],roomsetup()[1],False)
r58 = Room(roomsetup()[0],roomsetup()[1],False)
r59 = Room(roomsetup()[0],roomsetup()[1],False)
r510 = Room(roomsetup()[0],roomsetup()[1],False)
r60 = Room(roomsetup()[0],roomsetup()[1],False)
r61 = Room(roomsetup()[0],roomsetup()[1],False)
r62 = Room(roomsetup()[0],roomsetup()[1],False)
r63 = Room(roomsetup()[0],roomsetup()[1],False)
r64 = Room(roomsetup()[0],roomsetup()[1],False)
r65 = Room(roomsetup()[0],roomsetup()[1],False)
r66 = Room(roomsetup()[0],roomsetup()[1],False)
r67 = Room(roomsetup()[0],roomsetup()[1],False)
r68 = Room(roomsetup()[0],roomsetup()[1],False)
r69 = Room(roomsetup()[0],roomsetup()[1],False)
r610 = Room(roomsetup()[0],roomsetup()[1],False)
r70 = Room(roomsetup()[0],roomsetup()[1],False)
r71 = Room(roomsetup()[0],roomsetup()[1],False)
r72 = Room(roomsetup()[0],roomsetup()[1],False)
r73 = Room(roomsetup()[0],roomsetup()[1],False)
r74 = Room(roomsetup()[0],roomsetup()[1],False)
r75 = Room(roomsetup()[0],roomsetup()[1],False)
r76 = Room(roomsetup()[0],roomsetup()[1],False)
r77 = Room(roomsetup()[0],roomsetup()[1],False)
r78 = Room(roomsetup()[0],roomsetup()[1],False)
r79 = Room(roomsetup()[0],roomsetup()[1],False)
r710 = Room(roomsetup()[0],roomsetup()[1],False)
r80 = Room(roomsetup()[0],roomsetup()[1],False)
r81 = Room(roomsetup()[0],roomsetup()[1],False)
r82 = Room(roomsetup()[0],roomsetup()[1],False)
r83 = Room(roomsetup()[0],roomsetup()[1],False)
r84 = Room(roomsetup()[0],roomsetup()[1],False)
r85 = Room(roomsetup()[0],roomsetup()[1],False)
r86 = Room(roomsetup()[0],roomsetup()[1],False)
r87 = Room(roomsetup()[0],roomsetup()[1],False)
r88 = Room(roomsetup()[0],roomsetup()[1],False)
r89 = Room(roomsetup()[0],roomsetup()[1],False)
r810 = Room(roomsetup()[0],roomsetup()[1],False)
r90 = Room(roomsetup()[0],roomsetup()[1],False)
r91 = Room(roomsetup()[0],roomsetup()[1],False)
r92 = Room(roomsetup()[0],roomsetup()[1],False)
r93 = Room(roomsetup()[0],roomsetup()[1],False)
r94 = Room(roomsetup()[0],roomsetup()[1],False)
r95 = Room(roomsetup()[0],roomsetup()[1],False)
r96 = Room(roomsetup()[0],roomsetup()[1],False)
r97 = Room(roomsetup()[0],roomsetup()[1],False)
r98 = Room(roomsetup()[0],roomsetup()[1],False)
r99 = Room(roomsetup()[0],roomsetup()[1],False)
r910 = Room(roomsetup()[0],roomsetup()[1],False)
r100 = Room(roomsetup()[0],roomsetup()[1],False)
r101 = Room(roomsetup()[0],roomsetup()[1],False)
r102 = Room(roomsetup()[0],roomsetup()[1],False)
r103 = Room(roomsetup()[0],roomsetup()[1],False)
r104 = Room(roomsetup()[0],roomsetup()[1],False)
r105 = Room(roomsetup()[0],roomsetup()[1],False)
r106 = Room(roomsetup()[0],roomsetup()[1],False)
r107 = Room(roomsetup()[0],roomsetup()[1],False)
r108 = Room(roomsetup()[0],roomsetup()[1],False)
r109 = Room(roomsetup()[0],roomsetup()[1],False)
r1010 = Room(roomsetup()[0],roomsetup()[1],False)

#the map
dungeon = [r010,r110,r210,r310,r410,r510,r610,r710,r810,r910,r1010,
            r09,r19,r29,r39,r49,r59,r69,r79,r89,r99,r109,
            r08,r18,r28,r38,r48,r58,r68,r78,r88,r98,r108,
            r07,r17,r27,r37,r47,r57,r67,r77,r87,r97,r107,
            r06,r16,r26,r36,r46,r56,r66,r76,r86,r96,r106,
            r05,r15,r25,r35,r45,r55,r65,r75,r85,r95,r105,
            r04,r14,r24,r34,r44,r54,r64,r74,r84,r94,r104,
            r03,r13,r23,r33,r43,r53,r63,r73,r83,r93,r103,
            r02,r12,r22,r32,r42,r52,r62,r72,r82,r92,r102,
            r01,r11,r21,r31,r41,r51,r61,r71,r81,r91,r101,
            r00,r10,r20,r30,r40,r50,r60,r70,r80,r90,r100,]


#is the gameplay for encoungter rooms
def fight(directions,monster,gender,wpn):
    fighting = True
    while fighting:
        player.stats()
        monster.stats()
        validating = True
        while validating:
            if monster.name[0].lower() not in("a","e","i","o","u"):
                print("A",monster.name,"stands before you")
            else:
                print("An",monster.name,"stands before you")
            print("what will you do?")
            action = input("flee or attack: ").lower()
            if action in("r","run","flee","escape","1"):
                if monster.name == "Goblin":
                    escchance = randint(1,20)
                    if escchance > 5:
                        escape(directions,monster)
                        fighting = False
                    else:
                        print("The tiny but still intimidating Goblin brandishing its",monster.wpn.name,"blocked your way")
                        monster.attack(player,gender,wpn)
                elif monster.name == "Orc":
                    escchance = randint(1,20)
                    if escchance > 10:
                        escape(directions,monster)
                        fighting = False
                    else:
                        print("The strong Ork brandishing its",monster.wpn.wpnname,"blocked your way")
                        monster.attack(player,gender,wpn)
                        validating = False
                elif monster.name == "Ghoul":
                    escchance = randint(1,20)
                    if escchance > 17:
                        escape(directions,monster)
                        fighting = False
                    else:
                        print("The fearsome Ghoul brandishing its claws blocked your way")
                        monster.attack(player,gender,wpn)
                        validating = False
                elif monster.name == "Golem":
                    escchance = randint(1,20)
                    if escchance > 12:
                        escape(directions,monster)
                        fighting = False
                    else:
                        print("The hulking Golem brandishing its clublike fists blocked your way")
                        monster.attack(player,gender,wpn)
                        validating = False
                elif monster.name == "Dragon":
                    escchance = randint(1,20)
                    if escchance > 15:
                        escape(directions,monster)
                        fighting = False
                    else:
                        print("The fearsome dragon snorting flame blocked your way")
                        monster.attack(player,gender,wpn)
                        validating = False
                        
            elif action in("fight","attack","atk","strike","2"):
                player.attack(monster,gender,wpn)
                
        if monster.health == 0:
            if monster.name in("goblin","orc"):
                loot()

#executes your hasty retreat
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

#feeds your never ending greed
def loot():
    lootchance = randint(1,20)
    if lootchance > 14:
        print("the",monster.name,"dropped",monster.gender[2],monster.wpn+"!")
        print(monster.name+"'s weapon-----------")
        print("name:",monster.wpn)
        print("damage:",monster.atk)
        print("your weapon")
        print("name:",player.wpn)
        print("damage:",player.atk)
        validating = True
        while validating:
            choice = input("would you like to take "+monster.gender[2],monster.wpn+"? y/n: ").lower()
            if choice in("y","yes","1"):
                print("you dropped your",player.wpn,"and you picked up the",monster.wpn,"from its corpse")
                player.wpn = monster.wpn
                print("and got",monster.gold,"gold")
                player.gold += monster.gold
                validating = False
            elif choice in("n","no","2","nien"):
                print("you kicked the",monster.name+"'s",monster.wpn,"away")
                print("and got",monster.gold,"gold")
                player.gold += monster.gold
            else:
                print("Say that again i didnt hear you")

#for when you die
# def gameover(monster)


    





#main-----------------------------------------
    
#the opening of the game
print("A large oaken door stands before",player.name,"the entrance to a dungeon that has claimed many a brave adventurer")
print("the choice before "+player.gender[1]+" is one many have asked themselves: do you go in? ")
# choice = input(":").lower()
# validating = True
# while validating:
#     if choice in("y","yes","ye","i do"):
#         player.xcor = 0
#         player.ycor = 0
#         encountersetup()
#         valdating = False
#     elif choice in("n","no","i dont"):
#         print("Despite all the money",player.name,"spent on",player.gender[2],"gear and cool sword",player.gender[0],"decides",player.gender[2],"life is worth more than fame riches and glory")
#         print("and so",player.gender[0],"walked off back to",player.gender[4],"town never to do anything brave ever again.")
#         sleep(3)
#         print("""
# ______ _       _____   __  _____ _   _  _____   _____   ___  ___  ___ _____  ____________ _________________ ___________ _   __   __
# | ___ \ |     / _ \ \ / / |_   _| | | ||  ___| |  __ \ / _ \ |  \/  ||  ___| | ___ \ ___ \  _  | ___ \ ___ \  ___| ___ \ |  \ \ / /
# | |_/ / |    / /_\ \ V /    | | | |_| || |__   | |  \// /_\ \| .  . || |__   | |_/ / |_/ / | | | |_/ / |_/ / |__ | |_/ / |   \ V / 
# |  __/| |    |  _  |\ /     | | |  _  ||  __|  | | __ |  _  || |\/| ||  __|  |  __/|    /| | | |  __/|  __/|  __||    /| |    \ /  
# | |   | |____| | | || |     | | | | | || |___  | |_\ \| | | || |  | || |___  | |   | |\ \\ \_/ / |   | |   | |___| |\ \| |____| |  
# \_|   \_____/\_| |_/\_/     \_/ \_| |_/\____/   \____/\_| |_/\_|  |_/\____/  \_|   \_| \_|\___/\_|   \_|   \____/\_| \_\_____/\_/  
#                                                                                                                                    
#                                                                                                                                    """)
#         validating = False
#     else:
#         print("I didnt catch that")
#         choice = input("do you go in? ")
