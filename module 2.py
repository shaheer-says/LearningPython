# To check whether a number is even or odd.
x = int(input("enter a number :"))
if x%2==0:
   print("The given number is even")
else:
    print("The given number is odd")
##Ex 2.1->
#Create a variable `number` and assign it an integer value (e.g., 10).
#2.  Write an `if` statement that checks if `number` is positive.
#3.  If it is positive, print the message "The number is positive."
#4.  Run your code. Then, change `number` to a negative value (e.g., -5) and run it again to see what happens.
num = 10
if num>=0:
    print("The  number is positive :)")
num = -10
if num>=0:
    print("The  number is positive :)") 
#Ex 2.2 ->
 #Check a string**
#1.  Create a variable `name` and assign it a string value (e.g., "Alice").
#2.  Write an `if` statement that checks if `name` is equal to "Alice".
#3.  If it is, print "Hello, Alice!".
#4.  Test with a different name.
name = "Alice"
if name == "Alice":
    print("Hello, Alice!") 
#Ex 2.3 ->
#Check pass/fail**
#1.  Create a variable `score` and assign it an integer value (e.g., 75).
#2.  Write an `if...else` statement to determine if the `score` is passing (60 or above) or failing.
#3.  Print "You passed!" if the score is 60 or above, otherwise print "You failed."
score = int(input("Enter your marks :"))
if score>=60:
    print("You passed :)")
else:
    print("You failed :(")
#Ex 2.4 ->
#Positive or not**
#1.  Take the `number` variable from Exercise 2.1.
#2.  Modify the code to use an `if...else` statement. If the number is positive, print "The number is positive." Otherwise, print "The number is not positive." (This covers zero and negative numbers).
num= int(input("Enter your number :"))
if num>=0:
    print("The number is positive:)")
else:
    print("The number is negative")
#Ex 2.5 ->
# Determine movie ticket price**
#1.  Create a variable `age` and assign it an integer value.
#2.  Use an `if...elif...else` chain to determine the movie ticket price based on age:
 #   *   0-5 years old: Free
  #  *   6-12 years old: £5
   # *   13-64 years old: £10
    #*   65+ years old: £7
#  Print the appropriate ticket price
age = int(input("enter your age :"))
price =0
if age>=0 and age<=5:
    print("Ticket is free :")
elif age>=6 and age<=12:
    print("price will be: £5")
elif age>=13 and age<=64:
    print("price will be: £10")
else:
    print("price will be: £7")
#Ex 2.6 ->
#red": Print "Stop!"
 #   *   "yellow": Print "Prepare to stop."
  #  *   "green": Print "Go!"
   # *   Any other value: Print "Invalid light color.

light_color = "white"
if light_color == "red":
    print("Stop!")
elif light_color == "yellow":
    print("Prepare to stop.")
elif light_color == "green":
    print("Go!")
else:
    print("Invalid light color.")
#Ex 2.7 ->
#Create variables: `gpa` (float, e.g., 3.8), `extracurriculars` (integer, e.g., 3),
#is_eligible_for_financial_aid` (Boolean, e.g., `True`).
#2.  Use nested `if` statements to check for scholarship eligibility:
 #   *   First, check if `gpa` is 3.5 or higher.
  #  *   **Inside** that `if` block, check if `extracurriculars` is 2 or more.
   ### *   **Inside** that `if` block, check if `is_eligible_for_financial_aid` is `True`.
    #*   If all conditions are met, print "Eligible for full scholarship!".
    #*   Provide `else` statements for each level of nesting to explain why the student is 
    #not eligible (e.g., "GPA too low", "Not enough extracurriculars", "Not eligible for financial aid").
#3.  Test with different values to see all paths.

gpa = 3.9
extracurriclars = 3
is_eligible_for_financial_aid =True
if gpa>=3.5:
    if extracurriclars >=2:
        if is_eligible_for_financial_aid:
            print("Eligible for scholarship :)")
        else:
            print("Not eligible for financial aid")
    else:
        print("extracurriculars is less than 2")
else:
    print("gpa is too low")
#Ex 2.8 ->
#Simple calculator**
#1.  Ask the user for two numbers using `input()`.
#2.  Convert these inputs to integers.
#3.  Calculate their sum, difference, product, and quotient.
#.  Print all the results in a user-friendly format.
#5.  Use `float()` for the quotient to handle potential decimal results.

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
sum = num1+num2
diff = num1-num2
product = num1*num2
quotient = float(num1)/num2

print(f"Sum = {sum}")
print(f"Difference = {diff}")
print(f"Product = {product}")
print(f"Quoteint = {quotient}")
#Ex 2.9 ->
 # Ask the user to enter a sentence using `input()`.
#2#.  Use `len()` to print the total number of characters in the sentence.
#3.  (Bonus) Use `split()` (a string method) to split the sentence into words,
#and then use `len()` on the resulting list to count the number of words.
sen_tences = input("enter a sentence :")
print(len(sen_tences))
word = sen_tences.split()
print(len(word))
#Ex 2.10 ->
#Calculate hypotenuse**
#1.  Import the `math` module.
#2.  Ask the user for the lengths of the two shorter sides of a right-angled 
#triangle.
#3.  Calculate the hypotenuse using the Pythagorean theorem
#(`c = sqrt(a^2 + b^2)`). You'll need `math.sqrt()` and the exponentiation
#operator `**`.
#4.  Print the result.
import math
a = float(input("enter one side :"))
b = float(input("enter second side :"))
hypotenuse  = math.sqrt(a**2 + b**2)
print(hypotenuse)
#Ex 2.11 ->
#ice roll simulator**
#1.  Import the `random` module.
#2.  Simulate rolling two dice. Generate two random integers between 1 and 6 
#(inclusive).
#3.  Print the result of each die roll and their sum.

import random
integer1 = random.randint(1,6)
integer2 = random.randint(1,6)
print(f"dice rolled:{integer1}")
print(f"dice rolled:{integer2}")
print(f"sum is :{integer1 + integer2}")





    
    

    

    

    


    