import pytest

NAMES = [ ' arnold schwarzenegger ' , 'alec baldwin' , 
'julian sequeira', 'sandra bullock' , 'bob belderbos' , 
'keanu reeves ', 'julbob pybites', 'bob belderbos', 
'julian sequeira', 'al pacino', 'brad pitt', 'matt damon', 'brad pitt'] 

def unique_list_of_names(namelist): 
    return namelist

def test_answer():
    assert unique_list_of_names(NAMES) == [ ' arnold schwarzenegger ' , 'alec baldwin' , 
'julian sequeira', 'sandra bullock' , 'bob belderbos' , 
'keanu reeves ', 'julbob pybites', 'bob belderbos', 
'julian sequeira', 'al pacino', 'brad pitt', 'matt damon', 'brad pitt'] 

def check_duplicates():
    
    flag = 0
    flag = len(set(NAMES)) == len(NAMES) 
    # printing result 
    if(flag) : 
        print(flag)
        print ("List contains all unique elements") 
    else :  
        print ("List contains does not contains all unique elements") 
    assert check_duplicates() == True
    
