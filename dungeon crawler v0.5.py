from random import randint, choice

monlist = ["goblin","orc","ghoul","golem","dragon"]
male = ["he","him","his"]
female = ["she","her","hers"]
unknown = ["it","it","its"]
class Entity:
    def __init__(self, name, gender, health, maxhealth, exp, atk, wpn):
        self.name = name
        self.gender = gender
        self.health = health
        self.maxhealth = maxhealth
        self.exp = exp
        self.atk = atk
        self.wpn = wpn
    
    def greeting(self):
        print("hello my name is",self.name)
        
    def attack(self,target):
        print("***********************")
        print(self.name,"swung on",target.name)
        print("dealing",self.atk,"damage")
        target.health = target.health - self.atk
        print(target.name+"'s health is now",target.health)
        print("***********************")
        
    def heal(self):
        foodval = randint(5,30)
        if self.health + foodval > self.maxhealth:
            print(self.name,"finds some food and eats it healing",self.maxhealth - self.health)
            self.health = self.maxhealth
        else:
            print(self.name,"finds some food and eats it healing",foodval,"HP")
            self.health = self.health + foodval
            
class Weapon:
    def __init__(self,wpnname,wpnatk,wpnswing):
        self.wpnname = wpnname
        self.wpnatk = wpnatk
        self.wpnswing = wpnswing

shortsword = Weapon("shortsword",10,["slices at","slashes","cleaves into","strikes","jabs","pokes"])
longsword = Weapon("longsword",20,["slices at","slashes","cleaves into","strikes","jabs","pokes"])
sword = Weapon("sword",15,["slices at","slashes","cleaves into","strikes","jabs","pokes"])
stick = Weapon("stick",5,["thwacks","bonks","whacks","whips","jabs","","",""])
metalbar
mace
flail
fists = Weapon("fists",3,["punches","jabs at","swings at","hooks","thumps","whacks"])
golemfists = Weapon(golemfists,20,["punches","swipes at","crushes","flings"])
claws = Weapon("claws",20,["slashes","slices","claws at","bites"])
knuckleduster


player1 = Entity("steven the brave",["he,him,his"],100,100,0,shortsword.wpnatk,shortsword)
player1.name = input("what is the heros name: ").title()

def encounter(monlist):
    montype = randint(1,100)
    if montype < 26:
        monype = "Goblin"
        monhealth = randint(15,30)
        monmaxhealth = monhealth
        monexp = 10
        wpn = choice[shortsword]
        wpnatk = wpn.wpnatk
    elif montype < 51:
        montype = "Orc"
        monhealth = randint(30,50)
        monmaxhealth = monhealth
        exp = 30
        wpn = choice[shortsword]
        wpnatk = wpn.wpnatk
    elif montype < 81:
        montype = "Ghoul"
        monhealth = randint(40,60)
        monmaxhealth = monhealth
        exp = 80
        wpn = choice[claws]
        wpnatk = wpn.wpnatk
    elif montype < 96:
        montype = "Golem"
        monhealth = randint(60,80)
        monmaxhealth = monhealth
        exp = 100
        wpn = choice[golemfists]
        wpnatk = wpn.wpnatk
    elif montype < 101:
        montype = "Dragon"
    else:
        print("??????????????????????????")
    
        
    monster = Entity(montype,)
























# print("-------------------")
# print("name:",player1.name)
# print("health:",player1.health)
# print("max health:",player1.maxhealth)
# print("exp:",player1.exp)
# print("atk:",player1.atk)
# print("-------------------")