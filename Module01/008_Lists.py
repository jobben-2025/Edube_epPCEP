# # # my_list = [10, 1, 8, 3, 5]
# # # length = len(my_list)

# # # for i in range(length // 2):
# # #     print(my_list[i], my_list[length - i - 1])
# # #     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

# # # print(my_list)


# # # step 1
# # beatles = []
# # print("Step 1:", beatles)

# # # step 2
# # beatles.append("John Lennon")
# # beatles.append("Paul McCartney")
# # beatles.append("George Harrison")
# # print("Step 2:", beatles)

# # # step 3
# # #for i in range(1,3):
# #     #user_input = str(input("Please enter name: "))
# #     #beatles.append(user_input)
# # beatles.append("Stu Sutcliffe")
# # beatles.append("Pete Best")
# # print("Step 3:", beatles)

# # # step 4
# # del beatles[-2]
# # del beatles[-1]
# # print("Step 4:", beatles)

# # # step 5
# # beatles.insert(0,"Ringo Starr")
# # print("Step 5:", beatles)


# # # testing list legth
# # print("The Fab", len(beatles))

# Lists can be indexed and updated, e.g.:

# my_list = [1, None, True, 'I am a string', 256, 0]
# print(my_list[3])  # outputs: I am a string
# print(my_list[-1])  # outputs: 0

# my_list[1] = '?'
# print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

# my_list.insert(0, "first")
# my_list.append("last")
# print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']


