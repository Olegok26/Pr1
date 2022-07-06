pass
number = int(input("Enter a number: "))
if number > 5:

   print("This number is greater than five.")

pass

if number is not None:
   pass # TODO: add some logic here later

x = float(input("x = "))
if x>0:
  y=x** 0.5
else:
  y=x** 12
print(y)

name = input("Enter your name: ")

if name == "Oleg":
   print("You have entered", name)
   print("This is my name, too.")
else:
   print("Your name differs from mine.")

x = float(input("x = "))
if 0<x<7:
  print("Value is in range, let's continue")
  y=2*x-5
  if y <0:
    print("y is negative")
  elif y > 0:
    print("y is positive")
  else:
    print("y = 0")

print("""Menu
1. File
2. View
3. Exit
""")

choice = int(input("Enter your choice: "))
if choice == 1:
   print("You have selected 'File' menu")
elif choice == 2:
   print("You have selected 'View' menu")
elif choice == 3:
   print("Stopping.")
else:
   print("Incorrect choice")

is_ready = False

# if is_ready:
#  state_msg = "Ready"
# else:
#  state_msg = "Not ready yet"
state_msg = is_ready and "Ready" or "Not ready yet"
print (state_msg)

number = int(input("Enter an integer: "))
if number:
  print('The number is not zero')
else:
  print('The number is zero')