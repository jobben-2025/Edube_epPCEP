# a = float(input("Enter value for a:"))# input a float value for variable a here
# b = float(input("Enter value for b:"))# input a float value for variable b here

# # output the result of addition here
# print("addition",  a+b)
# # output the result of subtraction here
# print("subtraction", a-b)
# # output the result of multiplication here
# print("multi", a*b)

# # output the result of division here
# print("divi", a/b)

# print("\nThat's all, folks!")

# #######################################
# x = float(input("Enter value for x: "))

# # Write your code here.
# y= 1/(x+1/(x+1/(x+1/x)))

# print("y =", y)


# x = int(input("Enter a number: ")) # The user enters 2
# print(x * "5")


# y = 25 // 5
# print(123+5.0)

# n = int(input("Please enter a num: "))
# print(False if n < 100 else True)



# # Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# # Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2

# # Print the result
# print("The larger number is:", "They are the same",larger_number if number1 == number2  else  larger_number)

# #### input strings
# input_string = str(input("Please enter your text here: "))

# if  "Spathiphyllum" in input_string:
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif "spathiphyllum" in input_string:
#     print("No, I want a big Spathiphyllum!")
# elif "pelargonium" in input_string:
#     print("Spathiphyllum! Not pelargonium!")
# else:
#     print("Spathiphyllum! Not [input]!")



# Scenario
# Once upon a time there was a land - a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course - their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
# Your task is to write a tax calculator.

# It should accept one floating-point value: the income.
# Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you - you'll find it in the skeleton code in the editor.
# Note: this happy country never returns money to its citizens. If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.

# income = float(input("Enter the annual income: "))

# if income <= 85528:
#     tax:float = (income * 0.18) - 556.02
# elif income > 85528:
#     tax:float = 14839.02 + ((income-85528)*0.32)
# else:
#     print("error")

# #
# tax = 0 if tax < 0 else tax

# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")






# Scenario
# As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.
# Look at the code in the editor - it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.

# The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.

# It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.

# year = int(input("Enter a year: "))

# leap = 366
# common = 365

# gregorian_begins = 1582
# #not divisible by 4 => common year
# #year not divisible by 100 == leap year
# #year not divisible  by  400 == common year
# #otherwise a leap year

# if year < gregorian_begins:
#     output_message = "Not within the Gregorian calendar period"
# elif not year%4 == 0:
#     output_message = "Common year"
# elif not year%100 == 0:
#     output_message = "Leap year"
# elif not year%400 == 0:
#     output_message = "Common year"
# else:
#     output_message = "Leap year"

# print(output_message)


# # Store the current largest number here.
# largest_number = -999999999

# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))

# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))

# # Print the largest number.
# print("The largest number is:", largest_number)



# secret_number = 777
# user_input=0
# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)

# while not secret_number == user_input:
#     user_input = int(input("Please guess a no.: "))
    
#     if user_input != secret_number:
#         print("Ha ha! You're stuck in my loop!")
    
# print("Well done, muggle! You are free now.")    


# import time
# for i in range(1,6):
#     print(i," Mississippi")
#     time.sleep(1)
    
# print("Ready or not, here I come!")



# secret = "chupacabra"

# while True:
#     user_input = str(input("What is the passcode? "))
    
#     if user_input == secret:
#         break

# print("You've successfully left the loop.")



# Prompt the user to enter a word
# and assign it to the user_word variable.
# vowels = ["A","E","I","O","U"]

# user_word = str(input("Please enter a word: ")).upper()

# for letter in user_word:
#     # Complete the body of the for loop.
#     if letter in vowels:
#         continue
#     else:
#         print(letter)


# vowels = ["A","E","I","O","U"]
# word_without_vowels = ""

# # Prompt the user to enter a word
# # and assign it to the user_word variable.
# user_input = str(input("Enter word: ")).upper()

# for letter in user_input:
#     # Complete the body of the loop.
#     if letter in vowels:
#         continue
#     else:
#         word_without_vowels += letter
#         print(letter)

# # Print the word assigned to word_without_vowels.
# print("Word without vowels: ", word_without_vowels)



# Scenario
# Listen to this story: a boy and his father, a computer programmer, are playing with wooden blocks. They are building a pyramid.

# Their pyramid is a bit weird, as it is actually a pyramid-shaped wall - it's flat. The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.

# Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

# Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

# Test your code using the data we've provided.

# blocks = int(input("Enter the number of blocks: "))
# #blocks = 1
# remaining_blocks = blocks#as start condition
# counter = 0
# height=0
# while remaining_blocks > 0: #more than 0 assumed
#     row = counter +1
#     remaining_blocks = remaining_blocks - row
#     height+=1
#     if remaining_blocks < (row+1):
#         break
#         print("Could not complete job, remaining blocks not sufficient: ", remaining_blocks)
#     else:
#         counter+=1
#         continue
    
# print("The height of the pyramid:", height)




