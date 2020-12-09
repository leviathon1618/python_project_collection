# '''number = input("enter a number")
# if number > 0:
#     print("number is positive")'''


# '''number = int(input("test number is?"))
# if number %2 == 0:
#     print("number is even")
# else:
#     print("number is uneven")'''


# '''num1 = int(input("number 1 value?"))
# num2 = int(input("number 2 value?"))

# if num1 > num2:
#     print("success")
# else:
#     print("num1 1 is less than num 2")'''


# '''name = input("what is ya name?")
# sales = int(input("how much did you sell?"))
# if sales > 500000:
#     print(name + " you will recive your bonus of 1000$")
# else:
#     print("you are a failiure")'''

# '''number = int(input("test number is?"))
# if number %2 == 0:
#     print("number is even")
# else:
#     print("number is uneven")'''

# '''a = int(input("num1"))
# b = int(input("num2"))
# c = int(input("num3"))

# if a > b and a > c:
#     print(a)
# if b > a and b > c:
#     print(b)
# if c > a and c > b:
#     print(c)'''


# '''weight = int(input("what is the weight"))

# if weight > 20:
#     print("25$ surcharge")
# if weight == 20:
#     print("just right")
# if weight < 20:
#     print("have a good flight")'''

# '''age = int(input("what is the age"))
# if age<=18:
#     if age <= 3:
#         print("infant")
#     else:       
#         if age <= 7:
#            print("baby")
#         else:            
#              if age <= 13:
#                 print("child")
#              else:
#                 print("teenager")
# else:
#     print("adult")'''


# '''grades = int(input("what is the grade"))


# if grades < 0 :
#     print("error message")
# if grades > 0 and grades < 40:
#     print("E")
# if grades >= 40 and grades < 45:
#     print("D")
# if grades >= 45 and grades < 60:
#     print("C")
# if grades >= 60 and grades < 75:
#     print("B")
# if grades >= 75 and grades < 100:
#     print("A")
# if grades > 100:
#     print("error message")'''


# '''a= 0
# while a < 100:
#     a+=1
#     print(a)'''


# number = 1
# newNumber = 0 
# while number > 0 :
#     number = int(input("what is the number? "))
#     if number > 0:
#         newNumber += number    
# print(newNumber)


# import random

# for i in range(0,100):
#     print(random.randrange(0,500))


# for i in range(1,11):
#     for j in range(1,11):
#         print(i * j)


# temperature = int(input("please put in a temperature in farenhiet "))
# if temperature > 90:
#     print("wear a swim suit")
# elif temperature > 70:
#     print("wear shorts")
# elif temperature > 50:
#     print("wear long pants")
# elif temperature <=50:
#     print("wear thermal underwear and long pants")


# print("student 1 ***")
# studentAvg1 = 0
# for i in range(1,5):
#     student1 = float(input("please enter you mark for course " + str(i) + "in rane 0 - 4 "))
#     studentAvg1 = studentAvg1 + student1


# print("student 2 ***")
# studentAvg2 = 0
# for i in range(1,5):
#     student2 = float(input("please enter you mark for course " + str(i) + "in rane 0 - 4 "))
#     studentAvg2 = studentAvg2 + student2


# print("student 3 ***")
# studentAvg3 = 0
# for i in range(1,5):
#     student3 = float(input("please enter you mark for course " + str(i) + "in rane 0 - 4 "))
#     studentAvg3 = studentAvg3 + student3


# grade1 = studentAvg1/4
# grade2 = studentAvg2/4
# grade3 = studentAvg3/4


# print("the student1 GPA is " + str(studentAvg1/4))
# print("the student2 GPA is " + str(studentAvg2/4))
# print("the student3 GPA is " + str(studentAvg3/4))


# if 4.00 >= grade1 > 3.67 :
#     print("the student1 alphabetic grade is A")
# if 3.67 >= grade1 > 3.00 :
#     print("the student1 alphabetic grade is B")
# if 3.00 >= grade1 > 2.00 :
#     print("the student1 alphabetic grade is C")
# if 2.00 > grade1 :
#     print("the student1 alphabetic grade is F")

# if 4.00 >= grade2 > 3.67 :
#     print("the student2 alphabetic grade is A")
# if 3.67 >= grade2 > 3.00 :
#     print("the student2 alphabetic grade is B")
# if 3.00 >= grade2 > 2.00 :
#     print("the student2 alphabetic grade is C")
# if 2.00 > grade2 :
#     print("the student2 alphabetic grade is F")

# if 4.00 >= grade3 > 3.67 :
#     print("the student3 alphabetic grade is A")
# if 3.67 >= grade3 > 3.00 :
#     print("the student3 alphabetic grade is B")
# if 3.00 >= grade3 > 2.00 :
#     print("the student3 alphabetic grade is C")
# if 2.00 > grade3 :
#     print("the student3 alphabetic grade is F")


# name = input("please enter your full name ")
# hours = int(input("please enter your hours "))
# print("*** payslip ***")
# print("employee name = " , name)
# print("total working hours = " , hours)
# regularPay = 20
# overtimePay = 25
# overTimeHours = 0
# regularhours = hours
# totalPay = 0
# print("regular pay rate" , regularPay)
# if hours >= 40:
#     overTimeHours = hours - 40
#     totalPay += overTimeHours * overtimePay
#     totalPay += 40 * regularPay
# else:
#     overTimeHours = 0
#     totalPay = hours * regularPay
# print("overtime" , overTimeHours)
# print(overtimePay)
# print("total pay is",totalPay)

# if totalPay > 700:
#     tax = totalPay / 100 * 30
#     #print(tax)

# elif totalPay > 500 and totalPay < 700:
#     tax = totalPay / 100 * 25
#     #print(tax)

# elif totalPay > 350 and totalPay <= 500:
#     tax = totalPay / 100 * 15
#     #print(tax)   
# elif totalPay <= 350:
#     tax = totalPay / 100 * 5
# print("your tax is " , tax)    
# netPay = totalPay - tax
# print("your net payment is " , netPay , "NZD") 
# print("* your payment will be put directly into your account")


# number = 1
# count = 0
# while number != 0:
#     number = int(input("please enter a number and press 0 to exit "))
#     count += 1
# print("youve enterd " , count -1 , "numbers")


# for i in range (0,4):
#     for j in range (0,4):
#         if i == j:
#             continue
#         print(i,j)

# n1, n2 = 0, 1
# while n1 < 1000:
#     print(n1)
#     nth = n1 + n2    
#     n1 = n2
#     n2 = nth
    


# nterms = int(input("How many terms? "))
# # first two terms
# n1, n2 = 0, 1
# count = 0
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
       
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1
# print(n1)