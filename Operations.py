#List Operations

# Membership Checks within the 'in' keyword to check if an item is in a list, bool data type value is returned 

guest_list = ['Adam', 'Bob', 'Charlie', 'James', 'Dylan' , 'Ethan']

print('Albert' in guest_list)  # Returns True or False     False cause not on the list

#Dylan? Check

print('Dylan' in guest_list)  # Returns True or False     True cause on the list

#guest_list.append(name)  Add a name to the list

name = input("What's your name? ")

if name in guest_list:
    print("Welcome to the party!: ", name + '!!!')
    
elif name not in guest_list:               #using else in this case will return same results 

    print("Sorry, you're not on the guest list.")


#Secondary example of above scenario condition with a second condition to check for 

if (name in guest_list):
    print("Welcome to the party!: ", name + '!!!')
elif name not in guest_list:
    print("Sorry, you're not on the guest list.")
    print("Would you like to add you to the list?")
    if input("Yes or No? ").lower() == 'yes':
        guest_list.append(name)
        print("Welcome to the party!: ", name + '!!!')





