"""#EX 1.2
city_name
active_user
is_administrator
product_price
#EX 1.3
for = 5
print(for)
# after creating a variable named for, output is showing invalid syntax because ,for is a reserved keyword in python used in loops.
1.  `result = 15 * 3`= Expression
2.  `"Python is fun"`= Expression
3.  `print("Coding...")`= Statements
4.  `if temperature > 25:`= Statements
5.  `fahrenheit = celsius * 9/5 + 32`= Expression
#EX1.6
##Expression => name = ali, mult = 2* 10;
#EX1.7 Create three variables: `city_name`, `population`, and `is_capital`. Assign appropriate values (e.g., "London", 9000000, True) to them. Then print the values of these variables.
city_name = "London";
population = 9000000;
is_capital = True;
print(city_name);
print(population);
print(is_capital);
#EX1.7Start with a variable `count = 5`. On the next line, reassign `count` to `10`. Then create a new variable `double_count` and assign it `count * 2`. Print all three variables at the end.
count = 5
count = 10
double_count = count*2
print(count)
#EX1.10
#Write a single Python expression that uses at least three different arithmetic operators, one comparison operator, and one logical operator. Assign the result to a variable and print it. For example, `(5 + 3 * 2) > 10 or False`.
x=(10*5/2-20)<80 or True
print(x)
#EX1.11
# Your favourite movie title.
fav_movie = "Gymkhana"
print(fav_movie);
print(f"Fav :{fav_movie}, Type{type(fav_movie)}")
#  The current year.
year = 2025;
print(year);
print(f"curryear: {year}, Type:{type(year)}")
#  The average rating of a book (e.g., 4.5).
rat_ing = 3.9;
print(rat_ing);
print(f"RATing: {rat_ing}, Type{type(rat_ing)}")
#  Whether a light switch is on.
is_lightOn = True;
print(is_lightOn)
print(f" Bool:{is_lightOn}, Type = {type(is_lightOn)}")
#  A list of three of your favourite colours.
fav_color = ["Black" , "Violet" , "Orange"]
print(fav_color);
print(f"List: {fav_color}, Type: {type(fav_color)}")
#A dictionary storing a student's name and their age.
stu_info = { "Name": "Shaheer" , "Age": "20"}
print(stu_info)
print(f"DICT: {stu_info}, Type: {type(stu_info)}")
#EX1.12
first_word = "Python"
second_word = " Programming"
full_phrase = first_word + second_word;
print(full_phrase)
print(full_phrase*3)
print("Python\tProgramming")
#EX1.14
x = 20;
if(x >= 18):
    
        print("CAN VOTE ");
        print("CAN DRIVE ");
#EX1.17
name=input("enter your name :")
fav_colour = input("enter your fav color :")
luc_num = int(input("enter your lucky num:"))
print(f"MY NAME IS: {name}! My favourite color is {fav_colour}, and My lucky number is {luc_num}.")
#EX1.18
a = int(input("enter first number :"))
b = int(input("enter second number :"))
sum = 0;
sum = a+b;
diff = a-b;
product = a*b;
div = a/b;
print(sum);
print(diff);
print(product);
print(div);
#EX1.19You have 3 Books in your cart. Each Book costs £12.50.
item = "Book";
quantity = 3;
price = ("£12.50");
print(f"You have {quantity} {item} in your cart. Each costs {price}.")
#EX 1.20
print("1", "2", "3", "4", "5", sep=",")
print("\nEnd of sequence.")
#EX1.21
birth_year = int(input("enter you birth year :"))
current_year = 2025;
My_age = current_year - birth_year;

print(f"My age is {My_age}  in {current_year} :)" );
#EX1.22
item_count = 10;
unit_price = 5.99;
item_count = str(item_count)
unit_price = str(unit_price)
print(f"You ordered {str(item_count)} items at {unit_price} each")
#EX 1.23
#Create variables `favourite_number = 7`, `gpa = 3.8`, `is_member = False`, and `name_list = ["Anna", "Ben"]`. Use the `type()` function to print the type of each variable.

favourite_num = 7;
gpa = 3.8;
is_member = False;
name_list =["Anna", "Ben"];
print(type(favourite_num))
print(type(gpa))
print(type(is_member))
print(type(name_list))
#EX1.24
#Create two integer variables `num_a = 5` and `num_b = 5`. Create two string variables `str_a = "hello"` and `str_b = "hello"`.
##Finally, create `list_c = list_a`.
num_a = 5
num_b = 5
str_a = "hello"
str_b = "hello"
list_a = [1, 2, 3, 4, 5]
list_b = [1, 2, 3, 4, 5]
list_c = list_a;
#EX1.25
Create a variable `my_data`.
1.  Assign an integer value to `my_data` and print its value and type.
2.  Reassign `my_data` to a string value and print its value and type.
3.  Reassign `my_data` to a boolean value and print its value and type
my_data = 10;
print(my_data)
print(type(my_data))
my_data = "Hello Everyone"
print(my_data)
print(type(my_data))
my_data = False
print(my_data)
print(type(my_data))""
#EX1.26
my_variable = 10;
list_no = [1,2,3,4,5]
result= my_variable + list_no
print(result)
# We cant add two different datatypes without conversion.
#updated script after conversion
my_variable = 10;
my_variable = [my_variable]
list_no =[1,2,3,4,5]
result = my_variable + list_no;
print(result)
#MODULE EXERCISES
#Q1->
your_name = input("enter your name: ")
fav_hobby = input("enter your fav hobby: ")
"Hello [Name]! I heard you love [Hobby]! That sounds like fun."
print(f"Hello {your_name}! I heard you love {fav_hobby}! That sounds like fun.")
#Q2->
orginal_price = float(input("Enter original price :"))
dis_percent = float(input("Enter discount percentage :"))
dis_amount = (dis_percent / 100)*orginal_price;
final_price = orginal_price - dis_amount
print(final_price)
#Q3->
len_gth = float(input("Enter length in meters:"))
conv_centi = len_gth*100;
conv_km = len_gth/ 1000;
print(conv_centi,"cm")
print(conv_km,"km")
#Q4->  *   "Child" (0-12)
  #  *   "Teenager" (13-19)
   ### (Hint: Use an `if-elif-else` structure, which relies on indentation and boolean expressions).
your_age = int(input("Enter your Age :"))
if(your_age < 0):
        {
        print("Invalid age")
        }
elif(your_age <= 12):
        {
        print("Child :)")
        }
elif(13<= your_age <=19):
        {
        print("Teenager :)")
        }
else: {
        print("Adult :)")
}
#Q5->
is_sunny = True
is_weekend = False
has_plans = True
has_sunglasses_str = input("Do you have sunglasses? (yes/no) ")"""

your_age = int(input("enter your age"))