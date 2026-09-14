#imports----------------------------------------
from random import randint, choice
from time import sleep

#lists------------------------------------------
male = ["he","him","his","they","his","Sir"]
female = ["she","her","hers","they","her","Ma'am"]
unknown = ["it","them","its","they","their","Hero"]
roomlist = ["trap","encounter","encounter","encounter","chest","chest","mimic","empty","empty","blocked","blocked","shop"]
directions = ["north","south","east","west"]
#variable definitions---------------------------
shopflavour = 0

#classes-------------------------------------------------------------------------------------------
class Entity:
    def __init__(self, name, gender, health, maxhealth, exp, gold, atk, wpn, xcor, ycor,inventory):
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
        self.inventory = inventory
    
    def greeting(self):
        print("hello my name is",self.name)
        
    def attack(self,target,wpn):
        gender = target.gender
        print("***********************")
        sleep(1)
        print(self.name,self.wpn.wpnswing[randint(0,len(wpn.wpnswing)-1)],target.name)
        sleep(1)
        print("dealing",self.atk,"damage")
        sleep(1)
        target.health = target.health - self.atk
        if target.health < (target.maxhealth * 0.25):
            print(gender[0],"is barely standing")
            sleep(1)
        elif target.health < (target.maxhealth * 0.5):
            print(gender[0],"is looking weak")
            sleep(1)
        elif target.health < (target.maxhealth * 0.75):
            print(gender[0],"is a little tired")
            sleep(1)
        if target.health > 0:
            print(target.name+"'s health is now",target.health)
            sleep(1)
        else:
            target.health = 0
            print("the",target.name,"is defeated")
            sleep(1)
        print("***********************")
        print("")
        
    def heal(self):
        foodval = randint(5,30)
        if self.health + foodval > self.maxhealth:
            wchoice = randint(1,2)
            if wchoice == 1:
                print(self.name,"finds some food and eats it healing",self.maxhealth - self.health)
                sleep(1)
                self.health = self.health + foodval
            else:
                print(self.name,"finds a potion and drinks it healing",self.maxhealth - self.health)
                sleep(1)
            self.health = self.maxhealth
        else:
            wchoice = randint(1,2)
            if wchoice == 1:
                print(self.name,"finds some food and eats it healing",foodval,"HP")
                sleep(1)
                self.health = self.health + foodval
            else:
                print(self.name,"finds a potion and drinks it healing",foodval,"HP")
                sleep(1)
                self.health = self.health + foodval
    
    def stats(self):
        print("")
        print("-------------------")
        sleep(0.5)
        print("name:",self.name)
        sleep(0.5)
        print("health:",self.health)
        sleep(0.5)
        print("max health:",self.maxhealth)
        sleep(0.5)
        print("exp:",self.exp)
        sleep(0.5)
        print("gold:",self.gold)
        sleep(0.5)
        print("atk:",self.atk)
        sleep(0.5)
        print("-------------------")
            
class Weapon:
    def __init__(self,name,wpnatk,wpnswing):
        self.name = name
        self.wpnatk = wpnatk
        self.wpnswing = wpnswing

class Room:
    def __init__(self,roomtype,monster,discovered):
        self.roomtype = roomtype
        self.monster = monster
        self.discovered = discovered
        
class Potion:
    def __init__(self,name,value,description,cost):
        self.name = name
        self.value = value
        self.description = description
        self.cost = cost

class Food:
    def __init__(self,name,value,description,cost):
        self.name = name
        self.value = value
        self.description = description
        self.cost = cost

#objects-------------------------------------------------------------------------------------------------------------------------
#weapons:
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
mimic_teeth = Weapon("teeth",10,["chomps","bites","gnaws on"])
#potions:
healingpotion = Potion("Healing potion",40,"heals you 40HP upon consumption",50)
harmingpotion = Potion("Harming potion",20,"Throw this at your enemy to deal 20 damage",30)
#food:
oldbread = Food("old Bread",10,"heals 10HP when you eat it, looks a little stale",20)
freshbread = Food("fresh Bread",15,"heals 15HP when you eat it",30)
apple = Food("Apple",randint(-5,8),"doesnt heal very much, looks old enough it may actually harm you",5)
goldenapple = Food("Golden Apple",0,"doesnt heal you at all its made of solid gold",200)

emptyslot = Food("empty",999999999999,"this is an empty slot",0)

   
# count = 0
# for x in d:
#     print(count)
#     for i in x:
#         print(i.roomtype)
#     count += 1


#player setup--------------------------------------------------------------------------------------
player = Entity("steven the brave",male,100,100,0,500,shortsword.wpnatk,shortsword,0,0,["nuclear bomb"])
# validating = True
# while validating:
#     nchoice = input("what is the heros name: ").title()
#     sleep(1)
#     print("")
#     answer = str(input("you have chosen \""+nchoice+"\" is this correct? y/n: ")).lower()
#     sleep(1)
#     print("")
#     if answer in("y","ye","yes"):
#         print("name set to",nchoice)
#         sleep(1)
#         player.name = nchoice
#         validating = False
#     elif answer in("n","no","nien"):
#         print("trying again")
#         sleep(1)
#     else:
#         print("invalid input try again")
#         sleep(1)
# 
# validating = True
# while validating:
#     gender = input("what is the heros gender(m/f/n): ").lower()
#     sleep(1)
#     print("")
#     if gender in("m","male","man"):
#         print(player.name+"'s gender is now male")
#         sleep(1)
#         player.gender = male
#         validating = False
#     elif gender in("f","female","girl"):
#         print(player.name+"'s gender is now female")
#         sleep(1)
#         player.gender = female
#         validating = False
#     elif gender in("n","non","nonbinary","non-binary","non binary","none","no","other"):
#         print(player.name+"'s gender is now beyond the people of the time")
#         sleep(1)
#         player.gender = unknown
#         validating = False
#     else:
#         print("invalid input try again")
#         sleep(1)

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
        mongold = 999999999999999999999999999999
        wpn = celestialbreath
        wpnatk = wpn.wpnatk
        gend = unknown
        
    
        
    monster = Entity(montype,gend,monhealth,monmaxhealth,monexp,mongold,wpnatk,wpn,0,0,[])
    return monster

#sets up rooms
def roomsetup():
    rtype = randint(0,10)
    rtype = roomlist[rtype]
    if rtype == "encounter":
        montype = encountersetup()
    else:
        montype = "hello so there actually isnt any monster here and i dont think you should be able to see this"
    return rtype,montype

#rooms
rtype,rmon = "empty","hello so there actually isnt any monster here and i dont think you should be able to see this"
r00 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r01 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r02 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r03 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r04 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r05 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r06 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r07 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r08 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r09 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r010 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r10 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r11 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r12 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r13 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r14 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r15 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r16 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r17 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r18 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r19 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r110 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r20 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r21 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r22 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r23 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r24 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r25 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r26 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r27 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r28 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r29 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r210 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r30 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r31 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r32 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r33 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r34 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r35 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r36 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r37 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r38 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r39 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r310 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r40 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r41 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r42 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r43 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r44 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r45 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r46 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r47 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r48 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r49 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r410 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r50 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r51 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r52 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r53 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r54 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r55 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r56 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r57 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r58 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r59 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r510 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r60 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r61 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r62 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r63 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r64 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r65 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r66 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r67 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r68 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r69 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r610 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r70 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r71 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r72 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r73 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r74 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r75 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r76 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r77 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r78 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r79 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r710 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r80 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r81 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r82 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r83 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r84 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r85 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r86 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r87 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r88 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r89 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r810 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r90 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r91 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r92 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r93 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r94 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r95 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r96 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r97 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r98 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r99 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r910 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r100 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r101 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r102 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r103 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r104 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r105 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r106 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r107 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r108 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r109 = Room(rtype,rmon,False)
rtype,rmon = roomsetup()
r1010 = Room(rtype,rmon,False)

#the map
dungeon = [[r00,r10,r20,r30,r40,r50,r60,r70,r80,r90,r100],
           [r01,r11,r21,r31,r41,r51,r61,r71,r81,r91,r101],
           [r02,r12,r22,r32,r42,r52,r62,r72,r82,r92,r102],
           [r03,r13,r23,r33,r43,r53,r63,r73,r83,r93,r103],
           [r04,r14,r24,r34,r44,r54,r64,r74,r84,r94,r104],
           [r05,r15,r25,r35,r45,r55,r65,r75,r85,r95,r105],
           [r06,r16,r26,r36,r46,r56,r66,r76,r86,r96,r106],
           [r07,r17,r27,r37,r47,r57,r67,r77,r87,r97,r107],
           [r08,r18,r28,r38,r48,r58,r68,r78,r88,r98,r108],
           [r09,r19,r29,r39,r49,r59,r69,r79,r89,r99,r109],
           [r010,r110,r210,r310,r410,r510,r610,r710,r810,r910,r1010]]


#is the gameplay for encoungter rooms
def fight():
    monster = dungeon[player.ycor][player.xcor].monster
    wpn = dungeon[player.ycor][player.xcor].monster.wpn
    fighting = True
    while fighting:
        player.stats()
        monster.stats()
        validating = True
        while validating:
            if monster.name[0].lower() not in("a","e","i","o","u"):
                print("A",monster.name,"stands before you")
                sleep(1)
            else:
                print("An",monster.name,"stands before you")
                sleep(1)
            print("what will you do?")
            sleep(1)
            action = input("flee or attack: ").lower()
            sleep(1)
            print("")
            if action in("r","run","flee","escape","1"):
                if monster.name == "Goblin":
                    escchance = randint(1,20)
                    if escchance > 5:
                        escape(monster)
                        fighting = False
                    else:
                        print("The tiny but still intimidating Goblin brandishing its",monster.wpn.name,"blocked your way")
                        sleep(1)
                        monster.attack(player,gender,wpn)
                elif monster.name == "Orc":
                    escchance = randint(1,20)
                    if escchance > 10:
                        escape(monster)
                        fighting = False
                    else:
                        print("The strong Ork brandishing its",monster.wpn.name,"blocked your way")
                        sleep(1)
                        monster.attack(player,gender,wpn)
                        validating = False
                elif monster.name == "Ghoul":
                    escchance = randint(1,20)
                    if escchance > 17:
                        escape(monster)
                        fighting = False
                    else:
                        print("The fearsome Ghoul brandishing its claws blocked your way")
                        sleep(1)
                        monster.attack(player,gender,wpn)
                        validating = False
                elif monster.name == "Golem":
                    escchance = randint(1,20)
                    if escchance > 12:
                        escape(monster)
                        fighting = False
                    else:
                        print("The hulking Golem brandishing its clublike fists blocked your way")
                        sleep(1)
                        monster.attack(player,gender,wpn)
                        validating = False
                elif monster.name == "Dragon":
                    escchance = randint(1,20)
                    if escchance > 15:
                        escape(monster)
                        fighting = False
                else:
                    print("The fearsome dragon snorting flame blocked your way")
                    sleep(1)
                    monster.attack(player,gender,wpn)
                    validating = False
                        
            elif action in("fight","attack","atk","strike","2"):
                player.attack(monster,monster.wpn)
                monster.attack(player,player.wpn)
                
            if monster.health == 0:
                loot(monster)

#executes your hasty retreat
def escape(monster):
    directions = ["north","south","east","west"]
    if player.xcor == 0 or dungeon[player.ycor][player.xcor-1].roomtype == "blocked":
        directions.remove("west")
    elif player.xcor == 10 or dungeon[player.ycor][player.xcor+1].roomtype == "blocked":
        directions.remove("east")
    if player.ycor == 10 or dungeon[player.ycor+1][player.xcor].roomtype == "blocked":
        directions.remove("south")
    elif player.ycor == 0 or dungeon[player.ycor-1][player.xcor].roomtype == "blocked":
        directions.remove("north")
    validating2 = True
    while validating2:
        print("which way?")
        sleep(1)
        esc = input((', '.join(directions))+": ").lower()
        sleep(1)
        print("")
        if esc in("n","north","up","1") and "north" in directions:
            print("you dodge past the",monster.name,"and escape to the north chamber")
            sleep(1)
            print("the",monster.name,"gives no chase, as it stays in its chamber")
            sleep(1)
            player.ycor = player.ycor - 1
            validating2 = False
            enterroom()
        elif esc in("e","east","right","2") and "east" in directions:
            print("you dodge past the",monster.name,"and escape to the east chamber")
            sleep(1)
            print("the",monster.name,"gives no chase, as it stays in its chamber")
            sleep(1)
            player.xcor = player.xcor + 1
            validating2 = False
            enterroom()
        elif esc in("s","south","down","3") and "south" in directions:
            print("you dodge past the",monster.name,"and escape to the south chamber")
            sleep(1)
            print("the",monster.name,"gives no chase, as it stays in its chamber")
            sleep(1)
            player.ycor = player.ycor + 1
            validating2 = False
            enterroom()
        elif esc in("w","west","left","4") and "west" in directions:
            print("you dodge past the",monster.name,"and escape to the west chamber")
            sleep(1)
            print("the",monster.name,"gives no chase, as it stays in its chamber")
            sleep(1)
            player.xcor = player.xcor - 1
            validating2 = False
            enterroom()
        else:
            print("can't do that")
            sleep(1)
            validating2 = True

#feeds your never ending greed
def loot(monster):
    if monster.name in("goblin","orc"): 
        lootchance = randint(1,20)
        if lootchance > 14:
            print("the",monster.name,"dropped",monster.gender[2],monster.wpn+"!")
            sleep(1)
            print(monster.name+"'s weapon-----------")
            sleep(1)
            print("name:",monster.wpn)
            sleep(1)
            print("damage:",monster.atk)
            sleep(1)
            print("your weapon")
            sleep(1)
            print("name:",player.wpn)
            sleep(1)
            print("damage:",player.atk)
            sleep(1)
            validating = True
            while validating:
                choice = input("would you like to take "+monster.gender[2],monster.wpn+"? y/n: ").lower()
                sleep(1)
                print("")
                if choice in("y","yes","1"):
                    print("you dropped your",player.wpn,"and you picked up the",monster.wpn,"from its corpse")
                    sleep(1)
                    player.wpn = monster.wpn
                    print("and got",monster.gold,"gold")
                    sleep(1)
                    player.gold += monster.gold
                    validating = False
                elif choice in("n","no","2","nien"):
                    print("you kicked the",monster.name+"'s",monster.wpn,"away")
                    sleep(1)
                    print("and got",monster.gold,"gold")
                    sleep(1)
                    player.gold += monster.gold
                else:
                    print("Say that again i didnt hear you")
                    sleep(1)
    else:
        print("The",monster.name,"dropped",monster.gold,"gold")#
        sleep(1)
        player.stats()

#for when you die
def gameover(monster):
    if monster.name.lower() not in("a","e","i","o","u"):
        print("you died to a",monster.name)
        sleep(1)
    else:
        print("you died to an",monster.name)
        sleep(1)
    player.stats()
    monster.stats()
    print("""
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄    
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌   
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌   
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌   
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓    
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒    
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒    
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░    
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░       
 ░ ░                           ░                  ░         """)

#lets u do stuff
def actions():
    validating = True
    while validating:
        action = input("what do yo want to do? move/move: ").lower()
        sleep(1)
        print("")
        if action in("move","go"):
            move()
            validating = False
        else:
            print("come again?")
            sleep(1)

#where you spend your wealth
def shop():
    wares = [healingpotion,healingpotion,harmingpotion,harmingpotion,oldbread,oldbread,oldbread,freshbread,freshbread,apple,apple,apple,goldenapple]
    sinventory = ["you arent supposed to see this"]
    print("as you walk into the chamber you see a shop")
    sleep(1)
    for i in range(1,10):
        item = randint(0,12)
        sinventory.append(wares[item])
    if dungeon[player.ycor][player.xcor].discovered == False:
        dungeon[player.ycor][player.xcor].discovered = True
        global shopflavour
        shopflavour += 1
        if shopflavour == 1:
            print("you wonder how anyone could run a shop in a place like this")
        elif shopflavour == 2:
            print("this shop looks exactly like the other one, strange")
        elif shopflavour == 3:
            print("its the same shop, it has to be")
        else:
            print("its the same shop, same as always")
        choice = input("The shopkeeper smiles at you, do you go over? ").lower()
        if choice in("y","yes","yeah","i do","of course","always","ja"):
            print("you walk over to the shop")
            validating = True
            while validating:
                player.stats()
                print("------------------")
                sleep(0.5)
                print("Wares:")
                sleep(0.5)
                for i in range(1,10):
                    print(str(i)+":",sinventory[i].name,"G"+str(sinventory[i].cost))
                    sleep(0.5)
                print("Gold:",player.gold)
                choice = input("what would you like adventurer? buy/sell/inspect/bye: ").lower()
                if choice in("buy","gimme","b"):
                    validating2 = True
                    while validating2:
                        choice = input("what number? ").lower()
                        if choice[0] in("1","2","3","4","5","6","7","8","9"):
                            choice = int(choice)
                            validating2 = False
                        else:
                            print("pick a number 1-9")
                    if player.gold > (sinventory[choice].cost)-1:
                        print("of course",player.name)
                        if sinventory[choice].name[0] not in("a","e","i","o","u"):
                            print(sinventory[choice].name,"was added to your inventory")
                            player.inventory.append(sinventory[choice])
                            sinventory[choice] = emptyslot
                        else:
                            print("you dont have enough gold for that",player.name)
                elif choice in("s","sell","get rid of","dump"):
                    if len(player.inventory) == 1:
                        print("you have nothing to sell me")
                    else:
                        print("what have you to sell me adventurer? ")
                        for i in range(1,len(player.inventory)-1):
                            print(player.inventory[i])

#lets you move
def move():
    directions = ["north","south","east","west"]
    if player.xcor == 0 or dungeon[player.ycor][player.xcor-1].roomtype == "blocked":
        directions.remove("west")
    elif player.xcor == 10 or dungeon[player.ycor][player.xcor+1].roomtype == "blocked":
        directions.remove("east")
    if player.ycor == 10 or dungeon[player.ycor+1][player.xcor].roomtype == "blocked":
        directions.remove("south")
    elif player.ycor == 0 or dungeon[player.ycor-1][player.xcor].roomtype == "blocked":
        directions.remove("north")
    if player.health > player.health*0.75:
        action = "stride"
    elif player.health > player.health*0.5:
        action = "walk"
    elif player.health > player.health*0.25:
        actiyeson = "limp"
    elif player.health > 0:
        action = "hobble"
    else:
        print("you are dead how tf are you doing that?")
    validating2 = True
    while validating2:
        print("which way now?")
        sleep(1)
        esc = input((', '.join(directions))+": ").lower()
        sleep(1)
        print("")
        if esc in("n","north","up","1") and "north" in directions:
            print("you",action," over to the north chamber")
            sleep(1)
            player.ycor = player.ycor - 1
            validating2 = False
            enterroom()
        elif esc in("e","east","right","2") and "east" in directions:
            print("you",action,"over to the east chamber")
            sleep(1)
            player.xcor = player.xcor + 1
            validating2 = False
            enterroom()
        elif esc in("s","south","down","3") and "south" in directions:
            print("you",action,"over to the south chamber")
            sleep(1)
            player.ycor = player.ycor + 1
            validating2 = False
            enterroom()
        elif esc in("w","west","left","4") and "west" in directions:
            print("you",action,"over to the west chamber")
            sleep(1)
            player.xcor = player.xcor - 1
            validating2 = False
            enterroom()
        else:
            print("can't do that",player.gender[5])
            validating2 = True

#punishes you for your greed
def trap():
    if dungeon[player.ycor][player.xcor].discovered == False:
        dungeon[player.ycor][player.xcor].discovered = True
        chance = randint(0,100)
        if chance < 70:
            damage = randint(5,20)
            player.health = player.health - damage
            print("As you enter the room a trap is sprung but sadly you are too slow to react")
            sleep(1)
            print("you take",damage,"damage")
            sleep(1)
            player.stats()
            print("you consider your options")
            sleep(1)
            actions()
        else:
            print("As you enter the room a trap is sprung but you manage to dodge out of the way")
            sleep(1)
            print("you move around the newly sprung trap and consider your options")
            sleep(1)
            actions()
    else:
        print("You enter the room, you have been here before")
        sleep(1)
        print("you look at the trap before considering where to go next")
        sleep(1)
        actions()

#fuels your greed
def chest():
    print("As you walk into the room you see a chest")
    sleep(1)
    validating = True
    while validating:
        choice = input("Do you go over and open it? ").lower()
        sleep(1)
        print("")
        if choice in("yes","yeah","i do"):
            gold = randint(10,100)
            sleep(1)
            print("")
            print("you walk over to the chest and open it, inside you find",gold,"gold")
            sleep(1)
            player.gold += gold
            player.stats()
            validating = False
            print("")
            actions()
        elif choice in("no","no i dont","nah"):
            print("")
            print("you decide against opening the chest")
            dungeon[player.ycor][player.xcor].discovered = False
            sleep(1)
            validating = False
            print("")
            actions()
        else:
            print("i cant hear you")
            sleep(1)

#punishes you for your greed even more
def mimic():
    print("As you walk into the room you see a chest")
    sleep(1)
    validating = True
    while validating:
        choice = input("Do you go over and open it? ").lower()
        sleep(1)
        print("")
        if choice in("yes","yeah","i do"):
            dungeon[player.ycor][player.xcor].discovered = True
            print("you walk over to the chest and open it, inside you find hundreds of teeth")
            sleep(1)
            damage = randint(5,20)
            player.health -= damage
            print("you get bitten by the mimic")
            sleep(1)
            if player.health < 1:
                print("and feel its teeth sink deep into you")
                sleep(1)
                montype = "Mimic"
                monhealth = 20
                monmaxhealth = monhealth
                monexp = 30
                mongold = 50
                wpn = mimic_teeth
                wpnatk = wpn.wpnatk
                gend = unknown
                monster = Entity(montype,gend,monhealth,monmaxhealth,monexp,mongold,wpnatk,wpn,0,0,[])
                gameover(monster)
            else:
                print("dealing",damage,"damage")
                sleep(1)
                player.stats()
                validating = False
                print("")
                actions()
        elif choice in("no","no i dont","nah"):
            print("you decide against opening the chest")
            dungeon[player.ycor][player.xcor].discovered = False
            sleep(1)
            validating = False
            actions()
        else:
            print("i cant hear you")
            sleep(1)

#hello
def enterroom():
    if dungeon[player.ycor][player.xcor].roomtype == "trap":
        trap()
    elif dungeon[player.ycor][player.xcor].roomtype == "encounter":
        if dungeon[player.ycor][player.xcor].discovered == False:
            dungeon[player.ycor][player.xcor].discovered = True
            print("")
            print("You enter the chamber and")
            sleep(1)
            fight()
        else:
            if dungeon[player.ycor][player.xcor].monster.health > 0:
                sleep(1)
                print("")
                print("you enter the room, and the fight continues")
                sleep(1)
                fight()
            else:
                sleep(1)
                print("")
                print("you enter the room and see the battle that was")
                sleep(1)
                print("the",dungeon[player.ycor][player.xcor].monster.name,"laying still on the stone floor")
                sleep(1)
                actions()
    elif dungeon[player.ycor][player.xcor].roomtype == "chest":
        if dungeon[player.ycor][player.xcor].discovered == False:
            dungeon[player.ycor][player.xcor].discovered = True
            chest()
        else:
            sleep(1)
            print("")
            print("you enter the room to see the chest you previously looted sitting empty against the wall")
            sleep(1)
            actions()
    elif dungeon[player.ycor][player.xcor].roomtype == "mimic":
        if dungeon[player.ycor][player.xcor].discovered == False:
            dungeon[player.ycor][player.xcor].discovered = True
            mimic()
        else:
            sleep(1)
            print("")
            print("you enter the room and steer clear of the mimic this time")
            sleep(1)
            actions()
    elif dungeon[player.ycor][player.xcor].roomtype == "empty":
        if dungeon[player.ycor][player.xcor].discovered == False:
            dungeon[player.ycor][player.xcor].discovered = True
            sleep(1)
            print("")
            print("as you enter the chamber your eyes dart side to side looking for any signs of danger")
            sleep(1)
            print("but you find none as the room is bare")
            sleep(1)
        else:
            print("you enter the room warily but its as bare as it was before")
        actions()
    elif dungeon[player.ycor][player.xcor].roomtype == "shop":
        shop()
    elif dungeon[player.ycor][player.xcor].roomtype == "blocked":
        sleep(1)
        print("")
        print("you are inside solid stone and die immediately")
        sleep(1)
        print("""
▓██   ██▓ ▒█████   █    ██    ▓█████▄  ██▓▓█████ ▓█████▄    ▄▄▄█████▓ ▒█████      ▄▄▄          █     █░ ▄▄▄       ██▓     ██▓    
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▒██▀ ██▌▓██▒▓█   ▀ ▒██▀ ██▌   ▓  ██▒ ▓▒▒██▒  ██▒   ▒████▄       ▓█░ █ ░█░▒████▄    ▓██▒    ▓██▒    
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ░██   █▌▒██▒▒███   ░██   █▌   ▒ ▓██░ ▒░▒██░  ██▒   ▒██  ▀█▄     ▒█░ █ ░█ ▒██  ▀█▄  ▒██░    ▒██░    
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ░▓█▄   ▌░██░▒▓█  ▄ ░▓█▄   ▌   ░ ▓██▓ ░ ▒██   ██░   ░██▄▄▄▄██    ░█░ █ ░█ ░██▄▄▄▄██ ▒██░    ▒██░    
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▓ ░██░░▒████▒░▒████▓      ▒██▒ ░ ░ ████▓▒░    ▓█   ▓██▒   ░░██▒██▓  ▓█   ▓██▒░██████▒░██████▒
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒     ▒▒▓  ▒ ░▓  ░░ ▒░ ░ ▒▒▓  ▒      ▒ ░░   ░ ▒░▒░▒░     ▒▒   ▓▒█░   ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ▒  ▒  ▒ ░ ░ ░  ░ ░ ▒  ▒        ░      ░ ▒ ▒░      ▒   ▒▒ ░     ▒ ░ ░    ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░     ░ ░  ░  ▒ ░   ░    ░ ░  ░      ░      ░ ░ ░ ▒       ░   ▒        ░   ░    ░   ▒     ░ ░     ░ ░   
 ░ ░         ░ ░     ░           ░     ░     ░  ░   ░                    ░ ░           ░  ░       ░          ░  ░    ░  ░    ░  ░
 ░ ░                           ░                  ░                                                                              """)
    else:
        print("")
        print("have you been messing with the code?")



#main-----------------------------------------
    
#the opening of the game
shop()
print("A large oaken door stands before",player.name,"the entrance to a dungeon that has claimed many a brave adventurer")
sleep(1)
choice = input("the choice before "+player.gender[1]+" is one many have asked themselves: do you go in? ").lower()
sleep(1)
validating = True
while validating:
    if choice in("y","yes","ye","i do"):
        player.xcor = 0
        player.ycor = 0
        validating = False
        #enterroom()
    elif choice in("n","no","i dont"):
        sleep(1)
        print("")
        print("Despite all the money",player.name,"spent on",player.gender[2],"gear and cool sword",player.gender[0],"decides",player.gender[2],"life is worth more than fame riches and glory")
        sleep(1)
        print("and so",player.gender[0],"walked off back to",player.gender[4],"town never to do anything brave ever again.")
        sleep(5)
        print("""
______ _       _____   __  _____ _   _  _____   _____   ___  ___  ___ _____  ____________ _________________ ___________ _   __   __
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
        sleep(1)
        print("")
