# Lists are created with [ ] seperated with comma ( , ) 

# Empty List

empty_list = []

#Populated List

#populated_list = ['Apple', 'Banana', 'Cherry']

person = "Jill"

people = [person, 'Bob',"Barry", "Bill"]

#Python lists can contain many diff data types

stuff = [1, 'apple', 3.14, True, ['tacos']]

#each item in a list can be accessed using its index    
#Indicies are in numeric order starting from 0 we can use them to access items in a list

alist = ['item1', 'item2', 'item3', 'item4']      #item 1 = Idex 0 

#Indicies can be used to access or modidy, remove items from the list or too them =====   Item one is ZERO

#print(alist)
#print(person)
#print(people)

#grab item 3 with idex 2

print("Third item: ", alist[2])

print("Item1, first item:", alist [0])

print("The last item: ", alist[-1])     

#Can use the Index  (-1) to get the last item in a list 
# (-2) will get the second last item and so on...

#grab the 3rd item in a series of 4 using -2

print("Second to last item: ", alist[-3])

#Potential Pitfalls with lists
#Index error
#Index out of range , trying to access an item that does not exist in the list

print("alist"[4])

    






