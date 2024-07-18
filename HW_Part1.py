#Problem Statement: You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

#Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

#Sort the grades in descending order and display the sorted list.

list.sort(grades)
print(grades)

grades.reverse()
print(grades)


#Task 2: Calculate the average grade from the list above and display it (reminder: The average is calculated by dividing the sum of all grades by the length of the grades list).

average_grade = sum(grades) / len(grades)
print(average_grade)

#Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]



second_week = temperatures[7:14]
print(second_week)

#Task 2: Extract all the temperatures above 100 (reminder: when slicing to the end of a list you don't need a stop index).

above_100 = temperatures[-7:]
print(above_100)

#Task 3  extract temperatures from the 5th to the 10th.

fifth_to_ten = temperatures[4:10]
print(fifth_to_ten)





