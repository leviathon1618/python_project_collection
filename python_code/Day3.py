# print("the first 10 natural numbers are")
# sum = 0
# count = int(input("what is the nth number? "))
# for i in range(1,count + 1):
#     print("the cube of ", i ," is ",i * i * i)
#     sum += i
# print(sum)


# number = int(input("what is the number to be calculated "))
# cubed = 0
# for i in range(1,number):
#     tables = number * i
#     print(tables)


# count = int(input("how many numbers do you want to generate? "))
# for i in range(1,count +1):
#     print(i*2 +1)


#for i in range(1, 2, 3, 4, 5, 6, 7, 8, 9):



# for i in range(0,50):
#     if i % 3 == 0:
#         print("fizz")
#     if i % 5 == 0:
#         print("buzz")
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizz buzz")



# for i in range(0,6):
#     if i == 1:
#         print("....1")
#     if i == 2:
#         print("...22")
#     if i == 3:
#         print("..333")
#     if i == 4:
#         print(".4444")
#     if i == 5:
#         print("55555") 


# balance = int(input("what is the bank balance"))
# interest = float(input("what is the interest rate?")) +1
# target = int(input("how big is your target"))

# while balance < target:
#     balance = balance * interest
    
#     print(round(balance,2))
# print("done")



# para = input("please enter a paragraph ")
# A = 0
# E = 0
# I = 0
# O = 0
# U = 0

# for i in range(len(para)):
#     output = para[i]
#     if output == "a":        
#         A = A + 1
#     elif output == "e":       
#         E = E + 1
#     elif output == "i":        
#         I = I + 1
#     elif output == "o":       
#         O = O + 1
#     elif output == "u":       
#         U = U + 1

# print("a = ",A)
# print("e = ",E)
# print("i = ",I)
# print("o = ",O)
# print("u = ",U)
# vowels = A + E + I + O + U
# print("total vowels are " ,vowels)


# import random

# randomNumber = random.randrange(0,11)
# for i in range(0,5):
#     guess = int(input("guess a number from 1 - 10 "))
#     if guess == randomNumber:
#         print("you got it!")
#         quit()
#     if guess > randomNumber:
#         print("too high")
#     if guess < randomNumber:
#         print("too low")
# print("you've used all of your guesses")


