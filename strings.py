"""
 #####EX1 **Favourite Language:** Create a string variable named `favorite_language` 
  and assign it the name of your favorite programming language using **single quotes**.
    On the next line, reassign the variable to another programming language
      using **double quotes**. Print the value of `favorite_language` after each assignment."""

favorite_language= 'Python'
print(favorite_language)
favorite_language="Javascript"
print(favorite_language)

"""#####**Combine Words:** Create three string variables: `word1 = "Python"`,
word2 = "is"`, `word3 = "fun"`. Concatenate them with spaces in between to form the sentence
"Python is fun" and store it in `sentence`. Print `sentence`."""

word1="Python"
word2="is"
word3="fun"
sentence=word1+" "+word2+" "+word3
print(sentence)
"""#####**Border Line:** Ask the user to enter a character (e.g., `*`, `-`, `=`). 
Then, use the repetition operator to print a line of 20 of those characters, acting as a border."""
x =input("enter your character:")
y = x*20
print(y)

"""#####First and Last:** Create a string variable `my_name = "John Doe"`. 
Print the first character of your name using a positive index,
and then print the last character using a negative index """
my_name="John Doe"
print(my_name[0])
print(my_name[-1])
"""######Character Access Error:** Create a string `short_word = "bug"`.
 Try to print the character at index `3` (which is out of bounds).
 Observe the error message Python provides """
short_word="bug"
print(short_word[3])
#####Extract Domain:** Given an email address string 
"""`email = "student@example.com"`, use slicing to extract
and print just the domain part ("example.com")."""
email="student@example.com"
print(email[7:19])
"""##### Create a list of directory names: `dirs = ["home", "user", "documents", "project"]`. 
Use the `join()` method to create a single string representing a file path,
separated by `/` (e.g., "home/user/documents/project"). Print the resulting path."""
dirs=["home","user","documents","project"]
x ="/".join(dirs)
print(x)
"""#####Create a variable `user_input = "   PyThOn PrOgRaMmInG   "`. 
Convert this string to a "normalized" version where it's all lowercase
and leading/trailing whitespace is removed.
Print the normalized string."""
user_input="   PyThOn PrOgRaMmInG  "
print(user_input.lstrip())
print(user_input.rstrip())
print(user_input.lower())
"""#####**Tag Processor:** Given a string of tags `tags_str = "python, programming, tutorial, beginners"`,
use the `split()` method to turn it into a list of individual tags. Then, print the list."""
tags_str="python, programming, tutorial, beginners"
x = tags_str.split()
print(x)
"""#### **Product Summary (f-string):** Create variables `product_name = "Smartphone"` and `quantity = 2`.
Use an **f-string** to print a message like: "You have ordered 2 units of Smartphone"""
product_name="Smartphone"
quantity=2
print(f"You have ordered {quantity} units of {product_name}.")
"""#####**Event Details (`.format()`):** Create variables `event_title = "Python Workshop"` 
and `event_date = "2024-10-26"`. Use the **`.format()` method** to
 print: "The event 'Python Workshop' is scheduled for 2024-10-26."""
event_title="Python Workshop"
event_date="2024-10-26"
print(f"The event '{event_title}' is scheduled for {event_date}.")

"""####.  **Personalized Greeting & Status:**
    *   Ask the user for their **name** and **age** using `input()`.
    *   Use an **f-string** to print a personalized greeting, e.g., "Hello, [Name]!"
    *   Based on their age, use an **if-elif-else** statement to print a
      message stating if they are "a minor," "a young adult," or "an adult."
    *   **Example Output:**
        ```
        Enter your name: Jane
        Enter your age: 16
        Hello, Jane! You are a minor."""

name= input("enter your name :")
age=int(input("enter your age :"))
print(f"Hello,{name}!")
if age <=18:
    print("You are minor")
elif 18<age<=30:
    print("You are young adult")
else:
    print("you are an adult:)")
    
    """#####**Sentence Analyzer:**
    *   Ask the user to enter any **sentence**.
    *   Print the sentence in **ALL CAPS** using a string method.
    *   Print the **length** of the sentence.
    *   Extract and print the **first word** of the sentence.
    *   Extract and print the **last word** of the sentence. (Hint: use `split()` and indexing).
    *   **Example Output:**
        ```
        Enter a sentence: Python is a powerful language.
        PYTHON IS A POWERFUL LANGUAGE.
        Length: 29
        First word: Python
        Last word: language."""
   
sentence=input("enter a sentence:")
print(sentence.upper())
print(len(sentence))
print(sentence[0:4])
print(sentence[-4:-1])
"""####*Basic Mad Libs Game:**
    *   Create variables for a story template: `noun`, `verb`, `adjective`.
    *   Prompt the user to enter a `noun`, a `verb`, and an `adjective` using `input()`.
    *   Construct a short story using these words and print it using **f-strings**.
    *   **Example Story Template:** "The {adjective} {noun} decided to {verb} across the park."""

noun=input('enter noun:')
verb=input("enter verb :")
adjective=input("enter adjective :")
print(f"The {adjective} {noun} decided to {verb} across the park")
"""####4 ->>  **Simple Password Strength Checker:**
    *   Ask the user to enter a **password**.
    *   Check the password's strength using **if-elif-else**:
        *   If the password is less than 8 characters, print "Weak: Password too short."
        *   If it's between 8 and 12 characters (inclusive), print "Moderate: Password length is okay."
        *   If it's more than 12 characters, print "Strong: Good password length!"
    *   Additionally, if the password contains the word "password" (case-insensitive), 
    print a warning: "Warning: Do not use 'password' in your password!" (Hint: use `lower()`
      and the `in` operator)."""

p_ass = input("enter password:")
if len(p_ass)<8:
    print("Weak: Password too short.")
elif 8< len(p_ass)<=12:
    print("Moderate: Password length is okay.")
else:
    print("Strong: Good password length!")
        
if "password" in p_ass.lower():
    print("Warning: Do not use 'password' in your password!")

"""##### 5 ->> **Shopping List Formatter:**
    *   Create a **list of at least 5 grocery items** (strings).
    *   Use a **`for` loop** to iterate through the list.
    *   For each item, print it with a **numbered prefix** (starting from 1) using an **f-string** and
     a tab for indentation.
    *   **Example Output:**
        ```
        Your Shopping List:
            1. Milk
            2. Eggs
            3. Bread"""
    
gro_cery = ['bisuits','onions','apples','oil']
print(" Your Shopping List:")
for names, item in enumerate (gro_cery,start=1): 
    print(f"\t{names}.{item}")
 