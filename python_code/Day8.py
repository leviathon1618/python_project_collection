# def Listsum(numbers): 

#     total = 0 
#     numbers.sort()
    
#     for x in numbers: 
#         if (x+1) == x:
#             del x
#         #total = x * (x+1) 

#     return numbers 

# print(Listsum([8, 2, 3, 1, 1, 7]))


# initial_list = [1, 2, 3]

# def duplicate_last(a_list):
#     last_element = a_list[-1]
#     a_list.append(last_element)
#     return a_list

# new_list = duplicate_last(a_list = initial_list)
# print(new_list)



# def circularly_identical(list1, list2):
#     list3 = list1 * 2 
#     for x in range(0, len(list1)):
#         z = 0
#         for y in range(x, x + len(list1)):
#             if list2[z]== list3[y]:
#                 z+= 1 
#             else:
#                 break 
#         if z == len(list1):
#             return True
#     return False 

# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 1, 2, 3, 4]
# list3 = [4, 5, 1, 2, 3]

# # check for list 1 and list 2
# if(circularly_identical(list1, list2)):
#     print("Yes, List 1 & List 2 are circularly_identical")
# else:
#     print("No, List 1 & List 2 are not circularly_identical") 

# # check for list 2 and list 3
# if(circularly_identical(list2, list3)):
#     print("Yes, List 2 & List 3 are circularly_identical") 
# else:
#     print("No, List 2 & List 3 are not circularly_identical")




# def second_smallest(numbers):
#   if (len(numbers)<2):
#     return
#   if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
#     return
#   xyz = set()
#   ymca = []
#   for x in numbers:
#     if x not in xyz:
#       ymca.append(x)
#       xyz.add(x)
#   ymca.sort()
#   return  ymca[1]

# print(second_smallest([10, 22, -88, 112, 0, -2]))
# print(second_smallest([1100, 1000, 1900, 190, 200, 10, -12]))
# print(second_smallest([19, 11, 12, 10, 110, 130, 12, -22, -2]))
# print(second_smallest([2,2]))
# print(second_smallest([2]))