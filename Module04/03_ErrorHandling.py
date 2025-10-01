# # try:
# #     value = int(input('Enter a natural number: '))
# #     print('The reciprocal of', value, 'is', 1/value)        
# # except ValueError:
# #     print('I do not know what to do.')    
# # except ZeroDivisionError:
# #     print('Division by zero is not allowed in our Universe.')    
# # except:                                                         #no definition, catches all -  always last,should be avoided!
# #     print('Something strange has happened here... Sorry!')



# # ZeroDivisionError
# # This appears when you try to force Python to perform any operation which provokes division in which the divider is zero, or is indistinguishable from zero. Note that there is more than one Python operator which may cause this exception to raise. Can you guess them all?

# # Yes, they are: /, //, and %.

# # ValueError
# # Expect this exception when you're dealing with values which may be inappropriately used in some context. In general, this exception is raised when a function (like int() or float()) receives an argument of a proper type, but its value is unacceptable.

# # TypeError
# # This exception shows up when you try to apply a data whose type cannot be accepted in the current context. Look at the example:

# # short_list = [1]
# # one_value = short_list[0.5]


# # You're not allowed to use a float value as a list index (the same rule applies to tuples, too). TypeError is an adequate name to describe the problem, and an adequate exception to raise.

# # AttributeError
# # This exception arrives – among other occasions – when you try to activate a method which doesn't exist in an item you're dealing with. For example:

# # short_list = [1]
# # short_list.append(2)
# # short_list.depend(3)


# # The third line of our example attempts to make use of a method which isn’t contained in the lists. This is the place where AttributeError is raised.

# # SyntaxError
# # This exception is raised when the control reaches a line of code which violates Python's grammar. It may sound strange, but some errors of this kind cannot be identified without first running the code. This kind of behavior is typical of interpreted languages – the interpreter always works in a hurry and has no time to scan the whole source code. It is content with checking the code which is currently being run. An example of such a category of issues will be presented very soon.

# # It's a bad idea to handle this exception in your programs. You should produce code that is free of syntax errors, instead of masking the faults you’ve caused.



# while True:
#     try:
#         number = int(input("Enter an int number: "))
#         print(5/number)
#         break
#     except ValueError:
#         print("Wrong value.")
#     except ZeroDivisionError:
#         print("Sorry. I cannot divide by zero.")
#     except:
#         print("I don't know what to do...")




# You can also specify and handle multiple built-in exceptions within a single except clause:

# while True:
#     try:
#         number = int(input("Enter an int number: "))
#         print(5/number)
#         break
#     except (ValueError, ZeroDivisionError):
#         print("Wrong value or No division by zero rule broken.")
#     except:
#         print("Sorry, something went wrong...")



# most useful Python built-in exceptions are: ZeroDivisionError, ValueError, TypeError, AttributeError


# Estimated time
# 30-120 minutes

# Level of difficulty
# Medium/Hard

# Objectives
# perfecting the student's skills in using Python for solving complex problems;
# integrating programming techniques in one program consisting of many various parts.
# Scenario
# Your task is to write a simple program which pretends to play tic-tac-toe with the user. 
# To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

# 4.7.2.1 PROJECT: Tic-Tac-Toe
########################################################################################################################################################################
# the computer (i.e., your program) should play the game using 'X's;
# the user (e.g., you) should play the game using 'O's;
# the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
# all the squares are numbered row by row starting with 1 (see the example session below for reference)
# the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
# the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
# the computer responds with its move and the check is repeated;
# don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.
# The example session with the program may look as follows:

# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 1




# def display_board(board):
#     # The function accepts one parameter containing the board's current status
#     # and prints it out to the console.


# def enter_move(board):
#     # The function accepts the board's current status, asks the user about their move, 
#     # checks the input, and updates the board according to the user's decision.


# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.



# **
# li - *,dann //
# li +, dann -


# result = (2 + ((3 * (5 ** 2)) // 4)) - 6
# print(result)




