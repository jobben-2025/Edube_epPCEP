# Bitwise operators ==== INTEGERS no floats!
# However, there are four operators that allow you to manipulate single bits of data. They are called bitwise operators.

# They cover all the operations we mentioned before in the logical context, and one additional operator. This is the xor (as in exclusive or) operator, and is denoted as ^ (caret).

# Here are all of them:

# & (ampersand) - bitwise conjunction;
# | (bar) - bitwise disjunction;
# ~ (tilde) - bitwise negation;
# ^ (caret) - bitwise exclusive or (xor).

# Bitwise operations (&, |, and ^)
# Argument A	Argument B	A & B	 A | B	    A ^ B
# 0	            0	        0	        0	    0
# 0	            1	        0	        1	    1
# 1	            0	        0	        1	    1
# 1	            1	        1	        1	    0

# Bitwise operations (~)
# Argument	~ Argument
# 0	            1
# 1	            0

# Let's make it easier:

# & requires exactly two 1s to provide 1 as the result;
# | requires at least one 1 to provide 1 as the result;
# # ^ requires exactly one 1 to provide 1 as the result.

# abbreviated form. These are the examples of their equivalent notations:

# x = x & y	x &= y
# x = x | y	x |= y
# x = x ^ y	x ^= y

# NOTICE:

# log = i and j  ========= True
# bit = i & j ========= addition

# logneg = not i ========= False
# bitneg = ~i ========= negative_value #if i is 16, this would be -16


# Single bit manipulation

# How do we deal with single bits?
# We'll now show you what you can use bitwise operators for. Imagine that you're a developer obliged to write an important piece of an operating system. You've been told that you're allowed to use a variable assigned in the following way:

# flag_register = 0x1234


# The variable stores the information about various aspects of system operation. Each bit of the variable stores one yes/no value. You've also been told that only one of these bits is yours - the third (remember that bits are numbered from zero, and bit number zero is the lowest one, while the highest is number 31). The remaining bits are not allowed to change, because they're intended to store other data. Here's your bit marked with the letter x:

# flag_register = 0000000000000000000000000000x000


# You may be faced with the following tasks:

# 1. Check the state of your bit - you want to find out the value of your bit; comparing the whole variable to zero will not do anything, because the remaining bits can have completely unpredictable values, but you can use the following conjunction property:

# x & 1 = x
# x & 0 = 0


# If you apply the & operation to the flag_register variable along with the following bit image:

# 00000000000000000000000000001000

# (note the 1 at your bit's position) as the result, you obtain one of the following bit strings:

# 00000000000000000000000000001000 if your bit was set to 1
# 0000000000000000000000000000000 if your bit was reset to 0
# Such a sequence of zeros and ones, whose task is to grab the value or to change the selected bits, is called a bit mask.

# Let's build a bit mask to detect the state of your bit. It should point to the third bit. That bit has the weight of 23 = 8. A suitable mask could be created by the following declaration:

# the_mask = 8



# You can also make a sequence of instructions depending on the state of your bit i here it is:

# if flag_register & the_mask:
#     # My bit is set.
# else:
#     # My bit is reset.


# 2. Reset your bit - you assign a zero to the bit while all the other bits must remain unchanged; let's use the same property of the conjunction as before, but let's use a slightly different mask - exactly as below:

# 11111111111111111111111111110111


# Note that the mask was created as a result of the negation of all the bits of the_mask variable. Resetting the bit is simple, and looks like this (choose the one you like more):

# flag_register = flag_register & ~the_mask
# flag_register &= ~the_mask



# 3. Set your bit - you assign a 1 to your bit, while all the remaining bits must remain unchanged; use the following disjunction property:

# x | 1 = 1
# x | 0 = x


# You're now ready to set your bit with one of the following instructions:

# flag_register = flag_register | the_mask
# flag_register |= the_mask


# 4. Negate your bit - you replace a 1 with a 0 and a 0 with a 1. You can use an interesting property of the xor operator:

# x ^ 1 = ~x
# x ^ 0 = x


# and negate your bit with the following instructions:

# flag_register = flag_register ^ the_mask
# flag_register ^= the_mask


# #Binary left shift and binary right shift
# Python offers yet another operation relating to single bits: shifting. This is applied only to integer values, and you mustn't use floats as arguments for it.

# You already apply this operation very often and quite unconsciously. How do you multiply any number by ten? Take a look:

# 12345 × 10 = 123450


# As you can see, multiplying by ten is in fact a shift of all the digits to the left and filling the resulting gap with zero.

# Division by ten? Take a look:

# 12340 ÷ 10 = 1234

# Dividing by ten is nothing but shifting the digits to the right.

# The same kind of operation is performed by the computer, but with one difference: as two is the base for binary numbers (not 10), shifting a value one bit to the left thus corresponds to multiplying it by two; respectively, shifting one bit to the right is like dividing by two (notice that the rightmost bit is lost).

# The shift operators in Python are a pair of digraphs: << and >>, clearly suggesting in which direction the shift will act.

# value << bits
# value >> bits

# The left argument of these operators is an integer value whose bits are shifted. The right argument determines the size of the shift.

# It shows that this operation is certainly not commutative.

# The priority of these operators is very high. You'll see them in the updated table of priorities, which we'll show you at the end of this section.

# Take a look at the shifts in the editor window.

# The final print() invocation produces the following output:

# 17 68 8

# Note:

# 17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 (shifting to the right by one bit is the same as integer division by two)
# 17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 (shifting to the left by two bits is the same as integer multiplication by four)

# And here is the updated priority table, containing all the operators introduced so far:

# Priority	Operator	
# 1	 ~, +, -	unary
# 2	 **	
# 3	 *, /, //, %	
# 4	 +, -	binary
# 5	 <<, >>	
# 6	 <, <=, >, >=	
# 7	 ==, !=	
# 8	 &	
# 9	 |	
# 10 =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=




# x = 4
# y = 1

# a = x & y   #0
# b = x | y   #5 , or (4,1,both)
# c = ~x  # tricky!   -5
# d = x ^ 5   #1 , x(4) deducted from 5
# e = x >> 2  #1
# f = x << 2  #16

# print(a, b, c, d, e, f)

# output: 0 5 -5 1 1 16







