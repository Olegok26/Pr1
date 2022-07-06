import math
a = '358'
b= int(a)
x = True
x2 = 2e3+0.6
print(a, x, x2)
print(type(a), type(x), type(x2))
print()
print(b//x2)
print(b%x2)
print(pow(b,2))
print(round(x2))
print(math.floor(x2))

string1 = 'String\'s'
string2 = "String"
print(string1, string2)
string = "First line of text. \n" \
        "Second line of text."
print(string)
Multiline_string = """ Lesson2. Variables and Data Types
Some data types explained in this lesson:
int
- bool
- float
- complex
- str
"""
print(Multiline_string)

string = input("Enter a string: ")
print('You have entered "{}"'.format(string))
print('Press Enter to continue')
input()
n = int(input('First number: '))
m = int(input("Second number: "))
print('{} + {} = {}'.format(n, m, n + m))