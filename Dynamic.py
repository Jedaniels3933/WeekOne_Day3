#Dynamic list can change , grow and shrink as needed

bec_class = ['David' , 'James', 'Adam', 'Tyler']

print(bec_class)


#Adding to lists changes from type, like intergers to strings or booleens to intergers

#Append List Method adds to the END of the list (item)

bec_class.append('Vincent')

print(bec_class)

#bec_class.append('Jeremiah')

bec_class.append(str(2))

print(bec_class)


#print(bec_class)
 #The append method will not add to the list if the item is not compatible with the list's data type
 #So, we commented out the append line to show an error message.
 #If you uncomment it, it will throw an error.
 #TypeError: 'str' object cannot be interpreted as an integer

#print(My kid is " + str(age) + "years old") 
#This will throw an error as we are trying to concatenate a string with an integer
#TypeError: can only concatenate str (not "int") to str

some_stuff = [12, True, 'blue', 1345.6789]

print(some_stuff)

#How to Remove items from a list
# list.remove(item) method removes the first occurance of the item in the list

bec_class.remove('2')

print(bec_class)
bec_class.remove('James')

print(bec_class)

#Can only remove one thing at a time



       

        



