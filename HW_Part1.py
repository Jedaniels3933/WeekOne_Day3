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





