# string = input("please input text: ")
# for i in string:
#     print(i)


# def getvowels(string):
#     vowels = ["a","e","i","o","u"]
#     for i in range(len(string)):
#         if string[i].lower() in vowels:
#             print(string[i] + " is in index " + str(i) + ".")

# getvowels(input("Enter a text: "))


# string = input("enter a string")
# string2 = "this is a test"

# for i in range(len(string)):
#     if string[i] == string2[i]:
#         print("both have " , string[i] ,"at ", i)
#     else:
#         print("no match")


# string = input("please enter a sentence ")

# string = list(string)
# string.reverse()
# print("".join(string))


# string = input("please enter text ")
# string2 = ""
# i = -1
# while i < len(string)-1:
#     string2 = string.replace(string[i], "")
#     i = i + 2
# print(string2)


# string = input("enter a text: ")
# number = int(input("plaese enter a number"))

# string2 = string.replace(string[number], "")
# print(string2)



# string = input("enter a text: ")
# a=0
# e=0
# i=0
# o=0
# u=0
# for i in range(len(string)-1):
#     if string[i] == "a":
#         a = a + 1
#     if string[i] == "e":
#         e = e + 1
#     if string[i] == "i":
#         i = i + 1
#     if string[i] == "o":
#         o = o + 1
#     if string[i] == "u":
#         u = u + 1
# print("there are " , a , "a's")
# print("there are " , i , "e's")
# print("there are " , e , "i's")
# print("there are " , o , "o's")
# print("there are " , u , "u's")


import string 
words = """How much wood would a woodchuck chuck If a woodchuck 
could chuck wood? He would chuck, he would, as much as he could, 
And chuck as much as a woodchuck would If a woodchuck could chuck wood.""".translate(str.maketrans('', '', string.punctuation)).split() 
print(words.count("wood"))