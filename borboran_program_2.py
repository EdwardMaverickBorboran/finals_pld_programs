# Program 1

# Write a program where the user can their name and then it will count how many vowels are there, Big and small.
# Ex. Danilo -> 3

# The code that I created:

# name_input = input("Enter your name:")
# vowels = ["a", "e", "i", "o", "u"]
# count_vowels = vowels.count()
# print("count_vowels")

# The code that I created:

name_input = input("Enter your name:")
vowels = ("a, e, i, o ,u")
count_vowels = 0

for letters in name_input:
    if letters.lower() in vowels:
        count_vowels += 1
print(f"{count_vowels}")

#   So my take on this is that since the letters should be big and small, we can use the lower method as to it will 
# replace the string to a lower case and then it will run through and check if it has the same characters of vowels
# that are indicated. Then we can use a for loop to 