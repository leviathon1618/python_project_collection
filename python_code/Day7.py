# num = int(input("Enter a first number: "))
# numlist = [num]
# while True:
#     next_num = int(input("Enter a number, or 0 if there are no new numbers: "))
#     numlist.append(next_num)
#     if next_num == 0:
#         numlist.reverse()
#         print(numlist)
#         exit()


# message = []
# for i in range(5):    
#     words = input("what is message " + str(i+1) + "? ")
#     message.append(words)    
# output = int(input("what message would you like to see? "))

# if output > 5:
#     print("sorry there isnt a value with that index")
# elif output <1:
#     print("sorry there isnt a value with that index")
# else:
#     print(message[output -1])


# num = int(input("Enter a first number: ")) 
# numlist = [] 
# product = 1 
# while True: 
#     numlist.append(num) 
#     product *= num 
#     num = int(input("Enter a number, or 0 if there are no new numbers: "))      
#     if num == 0: 
#         break        

# output = str(numlist[0]) 

# for i in range(len(numlist) - 1):  

#     output = output + " X " + str(numlist[i + 1])    
# output += " = " + str(product)  

# print(output)


# num = input("Enter a first Name: ")
# numlist = []
# while True:
#     numlist.append(num)
#     num = input("Enter another Name, or press Enter: ")
    
#     if num == "":
#         numlist.sort() 
#         for name in numlist:
#             print(name)
#         break


a = [10,20,30,40,50,0]
b= [1,20,2,40,0]



list = [10,20,30,40,50,0]
tinylist = [1,20,2,40,0]
 
 
#comparing value of two list
for item in list:
	for item1 in tinylist:
		if item == item1:
			print(item)
		
