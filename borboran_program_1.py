# Program 1

# Write a program where the user can input the number that ranges from 0 to 100

# range       print()

# 0-3         Toddler
# 4-12        Child
# 13-17       Teen
# 18          Debutant
# Above 18    Adult

# Print error if it is out of range

# The code that I created:

# user_input = input("Enter a number:")
# for i in range(100):
#   if i <= 3:
#       print("Toddler")
#   elif i <= 12:
#       print("Child")
#   elif i <= 17:
#       print("Teen")
#   elif i == 18:
#       print("Debutant")
#   elif i > 18:
#       print("Adult")
#   else:
#       print("Error! Out of range")

#   As you can clearly see the I only got the gist of what the program would do yet
# I made mistake on some parts: 
#   - I used for loop
#   - Instead of user_input I stated i in the if else statement

# Now, here is the revise version:

user_input = int(input("Enter a number:"))

if user_input >= 0 and user_input <=3:
    print("Toddler")

elif user_input >=4 and user_input <=12:
    print("Child")

elif user_input >= 13 and user_input <=17:
    print("Teen")

elif user_input == 18:
    print("Debutant")

elif user_input > 18 and user_input <= 100:
    print("Adult")
                    
else: 
    user_input > 100
    print("Error! Out of range")