print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Fairy Land!!!!")
print("Your mission is to finish the game.. get any one wish from BUBU.")
print("WARNING! PLAY AT ON YOUR RISK\nIf you lose,you will die in but in real BUBU will mad at you :[")

print("\nTips : There will be five questions you have to answer each and every question correct If you don't.. you will die\nlet's begin <3 BEST OF LUCK :) ")


eye_color=input("\nThere is river in front of you full of hungry crocodile, if you answer your 1st question then you will get the boat to cross the river\n1. What is the BUBU's eye colour? type 'B' for Black or 'D' for dark brown").lower()
if eye_color == 'd':
  print("correct answer ummaaaaah! moving forward..")



  flavour=input("\nNow, The floor ahead is made of LAVA, you have to get bamboocopter to cross the floor\n2. What is her favorite ice-cream or pastery flavour? type 'C' for chocolate or 'S' for butterscotch" ).lower()
  if flavour == 's':
    print("hurray! correct answer next question..")



    anniversary= input("\noh no! the floor is shrinking hurry up and answer the next question or you will supressed\n3. When we had our first lip kiss? type date and month (without space)")
    if anniversary =="20february":
      print("congrats! you won again.. moving ahead")


      game=input("\nThe floor is made of glass,it will break and you will fall down if your answer is incorrect\n4. Which game she haven't played yet.. type 'C' for call of duty or 'M' for coin master").lower()
      if game=='c':
        print("yayyy! one question left Moving ahead..")


        afraid=input("\nyou can see The Big door,Fairy land is behind the door one step ahead...\n5. What is she most afraid of...\n type a * loosing dignity\n type b for * loosing someone she loves\ntype c for * loosing her favorate stuff").lower()
        if afraid== 'b':
          print("congratulation, you have won the game, now you can grant one wish from BUBU by saying IloveU<3\n THANK YOU FOR PLAYING..")
        else:
            print("you lost! bubu see behind A devil is coming to eat u run!! hehahahahah")

      else:
           print("you loose, you will fall..")
    else:
         print("you loose, you will be collapsed in few minutes")
  else:
       print("you loose, be ready to jump in the lava..")
else:
    print("you loose! now, you will be the crocodiles delicious dinner hehahaha")




