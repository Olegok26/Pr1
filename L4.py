response = exit
while response != "exit":
 response = input("Type 'exit' to exit: ")

 number = 0
 while number <= 0:
  number = int(input("Enter a positive integer: "))
 print("You have entered", number)

 n = 1
 while n <= 3:
  print("n =", n)
  n += 1

 while True:
  print("Enter 'exit' to exit loop")
  response = input("> ")
  if response == "exit":
   break

number = 0
while number < 10:
 number += 1
 if number == 5:
  continue
 print("Current number is", number)

attempts_left = 3
while attempts_left > 0:
   attempts_left -= 1
   password = input("Enter your password "
       "(you have {} attempts left): ".format(attempts_left + 1))
   if password == "98eaxc":
     print("Access granted")
     break
else:
 print("Access denied")

for row in range(5):
  for column in range(30):
   print("*", end="")
   print()