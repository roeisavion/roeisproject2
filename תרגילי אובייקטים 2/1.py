class animal():
    def __init__(self,name):
        self.name=name
        self.hunger_level=5
        self.energy_level=5

    def __str__(self):
        return (f'my name is {self.name}, my energy level is {self.energy_level}, my hunger level is {self.hunger_level}')

    def eat(self,food_grams):
        if food_grams//50<=cat.hunger_level and food_grams//100<=cat.energy_level :
            cat.hunger_level-=food_grams//50
            cat.energy_level-=food_grams//100
            print('done eating')
            return
        if food_grams//50>cat.hunger_level :
            cat.energy_level -= (cat.hunger_level) // 2
            cat.hunger_level=0
            print('did not finish eating not hungry')
            return
        if food_grams//100>cat.energy_level:
            cat.hunger_level-=food_grams//50
            cat.energy_level=0
            print('finish eating but tired')
            return

    def play(self,play_minutes):
        if cat.energy_level>=play_minutes//5:
            cat.energy_level-=play_minutes//5
            cat.hunger_level+=play_minutes//5
            if cat.hunger_level >10:
                cat.hunger_level =10
            print('done playing')
        else:
            cat.hunger_level+=cat.energy_level
            cat.energy_level=0
            print('didn\'t finish the game because too tired')


    def rest(self,rest_minutes):
         if (10-cat.energy_level)>=rest_minutes//20 and (10-cat.hunger_level)>=rest_minutes//30 :
            cat.hunger_level+=rest_minutes//30
            cat.energy_level+=rest_minutes//20
            print('rested')
            return
         if (10-cat.energy_level)<rest_minutes//20 :
            print('done resting want to play')
            cat.hunger_level += (10 - cat.energy_level) * 20 // 30
            cat.energy_level=10
            return
         if (10 - cat.hunger_level) < rest_minutes // 30:
             print('too hungry want to eat')
             cat.energy_level += (10 - cat.hunger_level) * 30 // 20
             cat.hunger_level=10
             return












cat=animal(input('enter cat name'))
print(cat)
action=int(input("1-eat 2-play 3-rest 0-exit"))
how_much=int(input('how much'))
while action!=0 :
    if action==1:
        cat.eat(how_much)
    if action==2:
        cat.play(how_much)
    if action==3:
        cat.rest(how_much)
    print(cat)
    action = int(input("1-eat 2-play 3-rest 0-exit"))
    how_much = int(input('how much'))

















# def eat(self,food_grams):
# if self.hunger_level>0:
#     count = 0
#     for i in range(food_grams//50):
#         self.hunger_level-=1
#         if count==1:
#             self.energy_level-=1
#             count=0
#         else: count=1
#         if self.hunger_level==0 and self.energy_level==0 and i!=food_grams//50:
#             print("not hungry, tired and didnt finish eating")
#             break
#         if self.hunger_level==0 and i!=food_grams//50:
#             print("not hungry and didnt finish eating")
#             break
#         if self.energy_level==0:
#             print("tired")
#             break
#     else: print("finished eating")