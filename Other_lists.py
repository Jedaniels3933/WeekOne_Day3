#Other cool stuff to do with list methods

food = ['tacos', 'pizza', 'tiramisu']

#list.append(item)

print("Adding ice cream")
food.append("ice cream")
print(food)

print("Inserting a potato into our list of food")
food.insert(2, "potato")

print(food)

#adding to a list at an index that doesn't exist will add it to the end of the list 

food.insert(6, 'cheese')
print(food)

#Lets remove pizza from our list

food.remove('pizza')

print(food)

#  list.pop() will remove the last item in the list and return it back to you- does not mean we have to store it or use it again

print("Putting our cheese in the fridge")

fridge = food.pop()
print("What's in the fridge:", fridge)

#Cheese is now back in the fridge variable 

#Another way to use .pop 
# Can remove an item from a specific index

print("Putting potato back in the oven")

oven = food.pop(1)
print("Oven: ", oven)
print(food)


print('='*50)

print(f"I really like {food[0]},I hate {food[1]}, and I love {food[2]}") 


food.append('key lime pie')
food.append('cheese burger')
food.append('fish')
food.append('sushi')
food.append('beer')
food.append('salad')

print("We went to the grocery store")
print(food)
#list.index (item) will return the index of the first occurrence of the item in the list
print('Finding the index of beer using .index()')
beer_idx = food.index('beer')
print("the indexical position of beer in our food list as: ", beer_idx)  #beer is index #7 in the list

#Mutability of lists

#Lists are mutable, meaning they can be changed after they are created. You can add, remove, or change items in a list.
#Modify data at a specific index/position. MUTABILITY : list[index] = new_value or item

food[7] = 'juice'
print(food)            #Changed beer to juice

#add another cheese burger using .count methood

food.append('cheese burger')
#list.count (item) will return the number of occurrences of an item on the list and return an integer

burger_count = food.count('cheese burger')
print("Burger count: ", burger_count)

#list.reverse method will reverse the order of items in the list
food.reverse()
print('Orignial food list:', food)
print("Our food list reversed: ", food)

#Can only sort a list with same data type
#list.sort() will sort the items in the list in ascending order

food.sort()
print("Sorted food list: ", food)   #sorted in alphabetical order- also now showing cheese burger twice 

#list.sort(reverse=True) will sort the items in the list in descending order    
#Mult dat types do not work together
#---------------

#####test = [1, 'string', 3.14, true]
#test.sort()
#print(test)  Wont work because strings are not sortable with integers

food.sort(reverse=True)
print(food)

#list functions 
# -- len(item) will return the number of items in the list
print(" the length of our food list is : ", len(food))


# -- max(item) will return the largest item in the list















