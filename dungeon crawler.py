from random import randint

class Entity:
    def __init__(self, name, health, maxhealth, exp, atk):
        self.name = name
        self.health = health
        self.maxhealth = maxhealth
        self.exp = exp
        self.atk = atk
    
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

player1 = Entity("steven the brave",100,100,0,20)#
player1.name = input("what is the heros name: ").title()


player1.greeting()
print("-------------------")
print("name:",player1.name)
print("health:",player1.health)
print("max health:",player1.maxhealth)
print("exp:",player1.exp)
print("atk:",player1.atk)
print("-------------------")
player1.heal()
print("-------------------")
print("name:",player1.name)
print("health:",player1.health)
print("exp:",player1.exp)
print("atk:",player1.atk)
print("-------------------")