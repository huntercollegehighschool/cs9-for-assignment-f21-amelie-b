"""
******
PART 3
******

Write a program that prompts the user to enter two integers, one representing the base of a rectangle, and one representing the height. The program will then print a rectangle made of asterisks (*) with those dimensions. 

(Hint: this may involve nested for loops(ie. a for loop inside a for loop), but it does not have to. Concatenating/adding strings ('*' + '*') or replicating strings ('*' * 3) may be helpful here.)

An example of what should appear on the console when the program runs:

Enter the base: 7
Enter the height: 3

*******
*******
*******

"""

#write your code here 
base = int(input("Enter the base: "))
height = int(input("Enter the height: "))

star1 = 0
star = "*"
star2 = 1

while star1 <= base:
  star1 = star1 + 1

while star2 <= height:
  star2 = star2 + 1
  print(star1 * star)