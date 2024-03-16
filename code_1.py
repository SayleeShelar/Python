'''PYTHON CASE SENSITIVE HAI
Datatypes in python:
1)	Int
2)	Float
3)	String
4)	Boolean
5)	Complex

VARIABLES IN PYTHON:
	WE DONT DEFINE DATATYPE OF VARIABLE HERE UNLIKE OTHER LANGUAGES
	a = 2 
 Note: String is stored in double quotes
'''
name = "Saylee"
is_intelligent = True
print(name)
print(is_intelligent)

'''Output:
Saylee
True'''

#  Concatenation 
# We use ‘ + ‘ for concatenation
name = "Saylee"
surname = "Shelar"
print(name + "  "+ surname)

# Output:
#Saylee  Shelar

# Input and concatenation:

#	Example 1
name = input("Enter your name:")
print("hello" + name)

'''Output:
Enter your name: Saylee
hello Saylee
Note: yahe pe bas “hello” double quotes mein hai. Variable name is not in double quotes while printing
'''
#	Example 2
a = input("Enter first number:")
b = input("Enter second number:")
sum = a+b
print(sum)


'''input – we use input to take input from the user
lets say user enter 2 as the 1st value and 3 as the 2nd number
	here the output will be 23 because it has taken the input in string form and then concatenated a and b.
   
so to get the right output we need to typecast a and b
Output
Enter first number:2
Enter second number:3
23  //    Reason vo a and b ko string consider kar raha hai.'''

# Type conversion and concatenation:

# Example 1:
a = input("Enter first number")
a = int(a)
b = input("Enter second number")
b = int(b)
sum = a+b
print(sum)

'''Output
Enter first number2
Enter second number3
5'''

#	Example 2:

first_number = input("Enter 1st number : ")
second_number = input("Enter 2nd number : ")
sum = float(first_number) + float(second_number)
print("the sum is : " + str(sum))

'''Output
Enter 1st number : 2
Enter 2nd number : 3
the sum is : 5.0
Note - concatenation is done of the same data type so we converted sum to string(str) datatype.
'''
# String:

# 1) .upper() – to convert data into upper case
name = "Saylee Shelar"
print(name.upper())

'''Output:
SAYLEE SHELAR'''

# 2)	.lower() – to convert data to lower case
name = "Saylee Shelar"
print(name.lower())

'''Output:
saylee shelar'''

# 3)	.find() – to find a char or string 

# Example 1:

name = "Iron man"
print(name.find('m'))
print('m' in name)

'''Output
5
True
 Note: find is a function used to get the index of a any particular string or char you to have to find.
Here the index will be returned.
Indexing starts from 0.'''

# Example 2:
name = "Iron man"
print(name.find('man'))

''' Output: 5
Note: jaise likha hai vaise hi find karo. Now if you write print(name.find('Man')) then it will give error because in input you have 'm'  of man is in small letters.
'''
# 4)	in: in is not a function. It is used to check if that string or char exists. The output is in the form of true or false

name = "Iron man"
print(name.find('man'))
print('m' in name)

'''Output:
5
True'''

# Arithmatic Operators
print(5+2)
print(5-2)
print(5*3) 
print(5%2)  #remainder
print(5**2) # power
print(5/2)
print(int(5/2))
print(5//2)

'''Output:
7
3
15
1
25
2.5
2
2
Note
when when you want only int as the output u have to use 
“ // ”
so the output of print(5//2) is 2
 or u can even type cast i.e print(int(5/2)) u will get 2 as the output
'''

i = 2
i+=2
print(i)

# output: 4



#2)

i = 2
i*=2
print(i)

 #output: 4

# 3) 
i = 2
i-=2
print(i)

#output: 0

# Operator precedence


 

print(2+3*5)
print((2+3)*5)

'''Output:

17
25'''

# Comment
'''Comment can be done in two ways
1)	Using # for single line comment
2)	Using ‘’’  ‘’’(triple quotes)  for multi line comment'''
'''print(2+3*5)
print((2+3)*5)
There is no output for these as we have turned it into comment'''
# python notes


# Comparsion Operator(Output is in the form of true or false)
print(2>3)
print(2<3)
print(5>=5)
print(5<=6)
print(5==5)
print(5!=5)

'''Output:
False
True
True
True
True
False'''

# Logical Operators(or, and, not)
print(2>3 or 5<10)
print(2>3 and 5<10)
print(not 2>3 )

'''Output:
True
False
True'''

# if else
age = 19
age
if age >= 18:
    print("you are an adult")
    print("you are eligible to vote")


print("Thankyou")

'''Output:
you are an adult
you are eligible to vote
Thankyou'''

# if age is less than 18

age = 16
if age >= 18:
    print("you are an adult")
    print("you are eligible to vote")


print("Thankyou")

'''Output:
Thankyou

Note: 
We dont use curly braces here we use “ : ”
We make use of indentation(space which u can see after : )'''



#  for multiple conditions

age = 16
if age >= 18:
    print("you are an adult")
    print("you are eligible to vote")
elif age<18 and age>3:
    print("you are in school")
else:
    print("you are kid")

'''Output:
You are in school

note:
	: is very important. Do not forget to put “ : “ after if or elif or else'''



# building calculator using if else


first = input("Enter first number")
first = int(first)
operator = input("Enter operator from the following (+,-,*,/,%): ")
second= input("Enter second number")
second = int(second)
if operator=='+':
    print(first + second)
elif operator=='-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator=='/':
    print(first / second)
elif operator == '%':
    print(first % second)
else: print("Invalid Operator")

'''Output:
Enter first number 10
Enter operator from the following (+,-,*,/,%):  +
Enter second number 8
18'''


# Range
number=(range(5))
print(number)

'''Output:
range(0, 5)'''

#	While loop
i = 1
while i<=5:
    print(i)
    i+=1

'''Output:
1
2
3
4
5
Note : “ : “ is very important in while as well'''


# printing patterns using while loop

i = 1
while i<=5:
    print(i * '*')
    i+=1

'''Output:
*
**
***
****
*****
'''
 

# printing the same pattern in other way

i = 5
while i>=1:
    print(i * '*')
    i-=1

'''Output:

*****
****
***
**
*'''

#	For loop

for item in range(5):
        print(item)

# note
        
'''this will print all numbers from 0 to 4.
 Indentation should be proper, wrong indentation can cause error
	: is very important
	Python ka for loop java aur c ke for loop jaisa nahi hota, yahe pe for(iteration, condtion, updation) NAHI hota.
	Pythons for loop looks like this:

    for <var> in <iterable>:
    <statement(s)>

Output:
0
1
2
3
4
'''

#	More examples on for loop

#	Example 1: (for loop in list)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
'''Output
apple
banana
cherry'''

# Example 2: for and break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

'''Output
apple
'''
# For and continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

'''Output
apple
cherry'''

# List
'''Enclosed in [ ]  bracket
	Can store different type of data
	Mutable
	Does not support the concept of object reusability
	Slicing operation can be performed
	Can perform append, insert'''


L1= [95, 98, 97]
print(L1)

'''Output
[95, 98, 97]'''

l2 = [95, 98, 97, "marks"]
print(l2)

'''Output
[95, 98, 97, ’marks’]'''

# To print marks of a given index
marks = [95, 98, 97]
print(marks[2])

'''Output
97'''

#	Python mein indexing piche se bhi kar sakte
#Example:

marks = [95, 98, 97]
print(marks[-1])

'''Output
97'''

marks = [95, 98, 97]
print(marks[-4])

'''Output
IndexError: list index out of range'''

# Slicing 
marks = [95, 98, 97]
print(marks[0:2])

'''Output
[95, 98]'''

#	Append in list

marks = [95, 98, 97]
marks.append(99)
print(marks)

'''Output
[95, 98, 97, 99]'''

#	Insertion in list:
'''( agar hume koi new element enter karna hai at a particular index to insert ka use karenge)'''
marks = [95, 98, 97]
marks.insert(1,96)
print(marks)
'''Output
[95, 96, 98, 97]'''

# To find if an element exists in our list we will use “in”
print(97 in marks)
'''Output
True'''


#	To print length i.e. size of list or number of elements in list:
print(len(marks))
'''Output:
4'''


# To print all the elements of list using while loop:
marks = [95, 98, 97]
marks.insert(1,96)
i=0
while i < len(marks):
     print(marks[i])
     i+=1

'''Output:
95
96
98
97'''

#	Marks.clear() will clear the list


#Tuples
'''Enclosed in Round bracket() or even if u don’t enclose it then also there will be no issue.
	Non mutable, i.e. once u have created a tuple u cannot make any changes in it
	Only Tuple follows the concept of object reusability
	List, set, dictionary does not follows the concept of object reusability.
	Since it is immutable we can perform any operation such append, insert 
	We can perform 2 operations in tuple
1)	Count( to count how many times a number is repeated)
2)	Index( to find index of a given element)'''

tup = (95, 96,99,97,97,98)
print(tup.count(97))
print(tup.index(97))
'''Output:
2
3'''

#  Set
''' Enclosed in curly braces
	Only unique values are allowed
	Unordered
	Operations such as union, intersection can be performed.'''
marks= {95, 96,99,97,98}
for x in marks:
    print(x)

# Output
'''96
97
98
99
95'''

# Dictionary
# There are two parts of dictionary key and value

marks = { "physics":88,"chemistry":89,"biology":90}
print(marks)

# Output: {'physics': 88, 'chemistry': 89, 'biology': 90}
# to print marks of chemistry

print(marks["chemistry"])


# Functions
'''Function is a piece of code that performs some task. (In a tv remote, each button performs a functions, so a function is like that button in code)
 There are 3 types of functions in Java :'''
# a.	In-built functions 
# int() str() float() min() range() max()
# b.	Module functions 
# Module is a file that contains some functions & variables which can be imported for use in other files. Each module should contain some related tasks Example: math, random, string 
'''import math print(dir(math)) 
import random print(dir(random)) 
import string print(dir(string))
 from math import sqrt print(sqrt(4))'''

 #c. User-defined functions def sum(a, b=4): print(a + b) sum(1, 2) sum(1)








