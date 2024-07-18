#Merging lists together with ' + ' operator

list1 = [1,2,3,4,]
list2 = [5,6,7,8,]
list3 = list1 + list2
print(list3)

list1 = [1,2,3,4,]  
list2 = ["this thing", 'that thing', 'another thing']
list3 = list1 + list2

print(list3)


#Copying a list with .copy() method
#Changes made to a true copy do not affect the orginal list
 

fruit = ['apple', 'bananas', 'orange']
copy_fruit = fruit.copy()   #True copy
print(copy_fruit)
copy_fruit.pop()
print("copy_fruit: ", copy_fruit)
print("fruit: ", fruit)

copy_fruit = fruit #not a true copy , would not recommend because its still pointing to the same list, same pieve of data with 2 names now


#copying a list with a full slice  :  list[:]
copy_fruit = fruit[:]

#List slicing is a powerful way to create new lists from existing ones.
#list[start:stop] =  will return a sub list or chunk of the original list from start to stop (exclusive) 
#the default start and stop values are the beginning and end of the list respectively (Full Slice) adding a stop index will include up to but not including that index. non - inclusinve 

key_lime_pie = ['slice1', 'slice2', 'slice3', 'slice4']  #Index 0, 1, 2, 3
#neg indicies     -4           -3       -2           -1 

my_slice = key_lime_pie[0:1]

print(my_slice)
# Lets get a bigger one
my_slice = key_lime_pie[1:3] # UP to 3 but not 3- will get 2

print(my_slice)

last_slice = key_lime_pie[3:]  #Get the last slice- Defaulted to the end of the list
print(last_slice)

#Slicing can also be used to change elements in a list

another_slice = key_lime_pie[2:-1]
print(another_slice)

another_slice2 = key_lime_pie[2:-1]
print(another_slice2)

another_slice3 = key_lime_pie[-2:]

print(another_slice3)

#Not for today to study but this is how you reverse a list
another_slice4 = key_lime_pie[-1:-3:-1]            #Steps
print(another_slice4)                              #The -1 specifies a step of -1, effectively reversing the list

#Making a solid string by joining lists with the 'join()' method
#.join(list)

words = ['Hello', "I'm", 'getting' , 'joined', '!!!!!']
sentence = '_'.join(words)  

print(sentence)       # =    Hello_I'm_getting_joined_!!!!!        #The join method will join the items in the list with the string specified in the join method  Can put anythin in the () not just _ but can also be a string, list, tuple, set, etc.
