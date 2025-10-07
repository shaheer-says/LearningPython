"""Exercise 2.23: List printer**
1.  Create a list of your favorite fruits.
2.  Use a `for` loop to print each fruit name in the list.
3.  Inside the loop, print a message like "I love [fruit_name]!".
4.  After the loop, print a final message like "I really enjoy fruits!"."""

fruits = ['banana','mango','apple','orange']
for i in fruits:
    print(f"i love {i}")

print("I really enjoy fruits")

"""#Multiples of 3**
1.  Use the `range()` function to generate numbers from 1 to 10.
2.  Use a `for` loop to iterate through these numbers.
3.  Inside the loop, use an `if` statement to check if the current number is a multiple of 3 (i.e., `number % 3 == 0`).
4.  If it is a multiple of 3, print the number."""
for number in range(1,11):
 if number % 3 == 0:
    print(number)
    """Exercise 2.25: Validate positive input**
1.  Use a `while True` loop to continuously ask the user to "Enter a positive number:".
2.  If the user enters a non-positive number (zero or negative), print "Invalid input. Please try again." and use `continue` to ask again.
3.  If the user enters a positive number, print "You entered: [number]." and use `break` to exit the loop."""

while True:
    num = int(input("enter your number :"))
    if num <=0:
        print("invalid number please try again ;")
        continue
    elif num>=0:
        print(f"you entered : {num}")
        break   
"""Skip specific names**
1.  Create a list of names: `students = ["Anna", "Ben", "Chris", "Dana", "Ethan", "Frank"]`.
2.  Use a `for` loop to iterate through the `students` list.
3.  If a student's name is "Chris" or "Ethan", use `continue` to skip printing their name and instead print "Skipping [name] for now.".
4.  For all other students, print "Processing student: [name]".
5.  After the loop, print "Finished processing all students."."""
students =["Anna","Ben","Chris","Dana","Ethan","Frank"]
for names in students:
   print(names)
   if names == "Chris" or names =="Ethan":
      print(f"Skipping {names} for now")
      continue
   print(f"Processing students:{names}.")

print("Finished processing all students.")

"""Password Strength Checker**
Write a function that checks the strength of a password.
1.  Define a function `check_password_strength(password)` that takes a `password` string as input.
2.  Inside the function, implement the following checks using `if...elif...else` statements and `len()`:
    *   If `len(password) < 8`: Return "Weak: Password is too short."
    *   If `password.lower() == password` (all lowercase): Return "Weak: Password needs uppercase letters."
    *   If `password.upper() == password` (all uppercase): Return "Weak: Psword needs numbers or sassword needs lowercase letters."
    *   If `password.isalpha()` (contains only letters): Return "Weak: Paspecial characters."
    *   Otherwise: Return "Strong: Password meets requirements."
3.  Prompt the user to "Enter a new password:" using a `while True` loop.
4.  Call `check_password_strength()` with the user's input.
5.  Print the result. If the password is "Strong", `break` the loop; otherwise, `continue` to ask again."""

def check_password_strength(password):
    if len(password) < 8:
        return "weak: password is too short."
    if password.lower() == password:
        return "weak: Password needs uppercase letters "
    if password.upper() == password:
       return "weak: Password needs numbers or sassword needs lowercae  letters"
    if password.isalpha():
   
     return "strong: password  meets requirement:"

while True: 
     user_password = input("enter your password :")


     result = check_password_strength(user_password)
     print(result)

     