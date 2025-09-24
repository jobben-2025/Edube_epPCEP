# Estimated time
# 15-20 minutes         ====== finished in 6:50 

# Level of difficulty
# Easy

# Objectives
# improving the ability to use numbers, operators, and arithmetic operations in Python;
# using the print() function's formatting capabilities;
# learning to express everyday-life phenomena in terms of programming language.
# Scenario
# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

# Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.

# Test your code carefully. Hint: using the % operator may be the key to success.

# Test Data
# Sample input:
# 12
# 17
# 59

# Expected output: 13:16


# Sample input:
# 23
# 58
# 642

# Expected output: 10:40


# Sample input:
# 0
# 1
# 2939

# Expected output: 1:0




hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# hour=2
# mins=30
# dura=120


# Write your code here.

beginning_time = hour*60 +mins

ending_time= beginning_time+dura

day = 24*60

if ending_time > day:
    ending_time = ending_time - day

output_ending_mins= ending_time%60

output_ending_hours= int(ending_time/60)
if output_ending_hours > 24:
    output_ending_hours = output_ending_hours - 24


print(f"{output_ending_hours}:{output_ending_mins}")







