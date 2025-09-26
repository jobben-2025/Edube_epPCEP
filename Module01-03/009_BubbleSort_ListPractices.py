


# # # # # my_list = [8, 10, 6, 2, 4]  # list to sort
# # # # # swapped = True  # It's a little fake, we need it to enter the while loop.

# # # # # while swapped:
# # # # #     swapped = False  # no swaps so far
# # # # #     for i in range(len(my_list) - 1):
# # # # #         if my_list[i] > my_list[i + 1]:
# # # # #             swapped = True  # a swap occurred!
# # # # #             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# # # # # print(my_list)




# # # # # a = 3
# # # # # b = 1
# # # # # c = 2

# # # # # lst = [a, c, b]
# # # # # lst.sort()

# # # # # print(lst)

# # # # # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # # # to_find = 5
# # # # # found = False

# # # # # for i in range(len(my_list)):
# # # # #     found = my_list[i] == to_find
# # # # #     if found:
# # # # #         break

# # # # # if found:
# # # # #     print("Element found at index", i)
# # # # # else:
# # # # #     print("absent")



# # # # # my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# # # # # temp_list = []
# # # # # # Write your code here.
# # # # # for i in my_list:
# # # # #     if i not in temp_list:
# # # # #         temp_list.append(i)

# # # # # my_list = temp_list[:]

# # # # # print("The list with unique elements only:")
# # # # # print(my_list)



# # # # # row = []
# # # # # for i in range(8):
# # # # #     row.append("WHITE_PAWN")
# # # # # print(row)

# # # # ############ list comprehension
# # # # # row = ["WHITE_PAWN" for i in range(8)]
# # # # # print(row)


# # # # # squares = [x ** 2 for x in range(10)]

# # # # # twos = [2 ** i for i in range(8)]

# # # # # odds = [x for x in squares if x % 2 != 0 ]

# # # # #The board variable is now a two-dimensional array. It's also called, by analogy to algebraic terms, a matrix.
# # # # # board = []
# # # # # for i in range(8):
# # # # #     row = ["EMPTY" for j in range(8)]
# # # # #     board.append(row)
# # # # # print(board)

# # # # #board = [["EMPTY" for i in range(8)] for j in range(8)]




# # # # #Chessgame:
# # # # EMPTY = "_"
# # # # ROOK = "ROOK"
# # # # board = []

# # # # for i in range(8):
# # # #     row = [EMPTY for j in range(8)]
# # # #     board.append(row)

# # # # board[0][0] = ROOK
# # # # board[0][7] = ROOK
# # # # board[7][0] = ROOK
# # # # board[7][7] = ROOK

# # # # print(board)





# # # # Multidimensional nature of lists: advanced applications
# # # # Let's go deeper into the multidimensional nature of lists. To find any element of a two-dimensional list, you have to use two coordinates:

# # # # a vertical one (row number)
# # # # and a horizontal one (column number).
# # # # Imagine that you develop a piece of software for an automatic weather station. The device records the air temperature on an hourly basis and does it throughout the month. This gives you a total of 24 × 31 = 744 values. Let's try to design a list capable of storing all these results.

# # # # First, you have to decide which data type would be adequate for this application. In this case, a float would be best, since this thermometer is able to measure the temperature with an accuracy of 0.1 ℃.

# # # # Then you take an arbitrary decision that the rows will record the readings every hour on the hour (so the row will have 24 elements) and each of the rows will be assigned to one day of the month (let's assume that each month has 31 days, so you need 31 rows). Here's the appropriate pair of comprehensions (h is for hour, d for day):

# # # # temps = [[0.0 for h in range(24)] for d in range(31)]


# # # # The whole matrix is filled with zeros now. You can assume that it's updated automatically using special hardware agents. The thing you have to do is to wait for the matrix to be filled with measurements.

# # # # Now it's time to determine the monthly average noon temperature. Add up all 31 readings recorded at noon and divide the sum by 31. You can assume that the midnight temperature is stored first. Here's the relevant code:

# # # # temps = [[0.0 for h in range(24)] for d in range(31)]
# # # # #
# # # # # The matrix is magically updated here.
# # # # #

# # # # total = 0.0

# # # # for day in temps:
# # # #     total += day[11]

# # # # average = total / 31

# # # # print("Average temperature at noon:", average)


# # # # Note: the day variable used by the for loop is not a scalar - each pass through the temps matrix assigns it with the subsequent rows of the matrix; hence, it's a list. It has to be indexed with 11 to access the temperature value measured at noon.

# # # # Now find the highest temperature during the whole month - see the code:

# # # # temps = [[0.0 for h in range(24)] for d in range(31)]
# # # # #
# # # # # The matrix is magically updated here.
# # # # #

# # # # highest = -100.0

# # # # for day in temps:
# # # #     for temp in day:
# # # #         if temp > highest:
# # # #             highest = temp

# # # # print("The highest temperature was:", highest)


# # # # Note:

# # # # the day variable iterates through all the rows in the temps matrix;
# # # # the temp variable iterates through all the measurements taken in one day.
# # # # Now count the days when the temperature at noon was at least 20 ℃:

# # # # temps = [[0.0 for h in range(24)] for d in range(31)]
# # # # #
# # # # # The matrix is magically updated here.
# # # # #

# # # # hot_days = 0

# # # # for day in temps:
# # # #     if day[11] > 20.0:
# # # #         hot_days += 1

# # # # print(hot_days, "days were hot.")





# # # Three-dimensional arrays
# # # Python does not limit the depth of list-in-list inclusion. Here you can see an example of a three-dimensional array:

# # # Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor. For this, you need an array which can collect and process information on the occupied/free rooms.

# # # First step - the type of the array's elements. In this case, a Boolean value (True/False) would fit.

# # # Step two - calm analysis of the situation. Summarize the available information: three buildings, 15 floors, 20 rooms.

# # # Now you can create the array:

# # # rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]


# # # The first index (0 through 2) selects one of the buildings; the second (0 through 14) selects the floor, the third (0 through 19) selects the room number. All rooms are initially free.

# # # Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:

# # # rooms[1][9][13] = True


# # # and release the second room on the fifth floor located in the first building:

# # # rooms[0][4][1] = False


# # # Check if there are any vacancies on the 15th floor of the third building:

# # # vacancy = 0

# # # for room_number in range(20):
# # #     if not rooms[2][14][room_number]:
# # #         vacancy += 1


# # # The vacancy variable contains 0 if all the rooms are occupied, or the number of available rooms otherwise.


# # # Congratulations! You've made it to the end of the module. Keep up the good work!


# # #!!!!!!!!!!      [expression for element in list if conditional]

# # #equates to code:
# # #for element in list:
# #     if conditional:
# #         expression

# # cubed = [num ** 3 for num in range(5)]
# # print(cubed)  # outputs: [0, 1, 8, 27, 64]


# #2. You can use nested lists in Python to create matrices (i.e., two-dimensional lists). For example:
# # A four-column/four-row table ‒ a two dimensional array (4x4)

# table = [[":(--", ":)", ":(", ":)000"],
#          [":)", ":(", ":)", ":)"],
#          [":(", ":)", ":)", ":("],
#          [":)", ":)", ":)", ":("]]

# print(table)
# print(table[0][0])  # outputs: ':('
# print(table[0][3])  # outputs: ':)'



# 3. You can nest as many lists in lists as you want, thereby creating n-dimensional lists, e.g., three-, four- or even sixty-four-dimensional arrays. For example (3d cube with x,y,z):

# # Cube - a three-dimensional array (3x3x3)

# cube = [[[':(', 'x', 'x'],      #line = x-axis
#          [':)', 'x', 'x'],      #row = y-axis
#          [':(', 'x', 'x']],

#         [[':)', 'x', 'x'],      #next slice in cube, z-axis
#          [':(', 'x', 'x'],
#          [':)', 'x', 'x']],

#         [[':(', 'x', 'x'],
#          [':)', 'x', 'x'],
#          [':)', 'x', 'x']]]

# print(cube)
# print(cube[0][0][0])  # outputs: ':('       #z-axis, slice / y-axis, row / x-axis, element
# print(cube[2][2][0])  # outputs: ':)'