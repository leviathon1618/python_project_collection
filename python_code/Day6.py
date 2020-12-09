import random
import getpass
player1 = str(input("what is the first players name? "))
player2 = str(input("what is the second players name? "))

starter = random.randrange(1,3)

if starter == 1:
    print(player1,"is starting ")
if starter == 2:
    print(player2, "is starting ")

rounds = int(input("how many rounds do you want to play?"))
p1score = 0
p2score = 0 

for i in range(rounds):
    p1Choice = 0
    p2Choice = 0
    while p1Choice == p2Choice:
            
        if starter == 1:
            print(player1)
            p1Choice = int(getpass.getpass(prompt = "choose your weapon \n 1:rock \n 2:paper \n 3:scissors "))        
            print(player2)
            p2Choice = int(input("choose your weapon \n 1:rock \n 2:paper \n 3:scissors "))    

        if starter == 2:
            print(player2)
            p2Choice = int(getpass.getpass(prompt = "choose your weapon \n 1:rock \n 2:paper \n 3:scissors "))
            print(player1)
            p1Choice = int(input("choose your weapon \n 1:rock \n 2:paper \n 3:scissors "))
        
        if p1Choice == p2Choice:
            print("tie, you've both chosen the same weapon!")
            

        else:
            if p1Choice == 1 and p2Choice == 2:
                print(player2, " wins! they chose paper" )
                p2score = p2score + 1
            if p1Choice == 2 and p2Choice == 1:
                print(player1, " wins! they chose paper" )
                p1score = p1score + 1

            if p1Choice == 1 and p2Choice == 3:
                print(player1, " wins! they chose rock")
                p1score = p1score + 1
            if p1Choice == 3 and p2Choice == 1:
                print(player2, " wins! they chose rock")
                p2score = p2score + 1

            if p1Choice == 3 and p2Choice == 2:
                print(player1, " wins! they chose scissors")
                p1score = p1score + 1
            if p1Choice == 2 and p2Choice == 3:
                print(player2, " wins! they chose scissors")
                p2score = p2score + 1
        


print("the total scores from the rounds are!")
print(p1score , " - " , p2score)
if p1score == p2score:
    print("its a tie!")
if p1score > p2score:
    print(player1, " wins!")
else:
    print(player2, " wins!")
