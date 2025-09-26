#Python Essentials 1:

#Module 1
#Introduction to Python and computer programming

#In this module, you will learn about:

#the fundamentals of computer programming, i.e., how the computer works, how the program is executed, how the programming language is defined and constructed;
#the difference between compilation and interpretation;
#what Python is, how it is positioned among other programming languages, and what distinguishes the different versions of Python.

print("My name is", "Python.", end=" ")
print("Monty Python.")
#will output:
# My name is Python. Monty Python.


print("My", "name", "is", "Monty", "Python.", sep="-")
#The keyword argument that can do this is named sep (like separator).

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

print("Programming","Essentials","in",sep="***", end=" ")
print("Python")


#manipulation with 'print'
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


#arrow in one line:
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

#twice as large:
print("    *\n")
print("   * *\n")
print("  *   *\n")
print(" *     *\n")
print("***   ***\n")
print("  *   *\n")
print("  *   *\n")
print("  *****\n")


#double arrow:
print("     *     "*2)
print("    * *    "*2)
print("   *   *   "*2)
print("  *     *  "*2)
print(" ***   *** "*2)
print("   *   *   "*2)
print("   *   *   "*2)
print("   *****   "*2)

#If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.

print(0o123) #is an octal number with a (decimal) value equal to 83.

#hexadecimal numbers. Such numbers should be preceded by the prefix 0x or 0X (zero-x).

print(0x123) #is a hexadecimal number with a (decimal) value equal to 291.




#Scientific notation:
# Written directly it would look like this: 300000000.

#To avoid writing out so many zeros, physics textbooks use an abbreviated form, which you have probably already seen: 3 x 108.

#It reads: three times ten to the power of eight.

#In Python, the same effect is achieved in a slightly different way - take a look:

print(3E8)

#The letter E (you can also use the lower-case letter e - it comes from the word exponent) is a concise record of the phrase times ten to the power of.

#Note:
#the exponent (the value after the E) has to be an integer;
#the base (the value in front of the E) may be an integer.


#A physical constant called Planck's constant (and denoted as h), according to the textbooks, has the value of: 6.62607 x 10-34.

#If you would like to use it in a program, you should write it this way:

print(6.62607E-34)

#When you run this literal through Python:

print(0.0000000000000000000001)

#this is the result:
#1e-22

#output
#Python always chooses the more economical form of the number's presentation


#The backslash can escape quotes too. A quote preceded by a backslash changes its meaning - it's not a delimiter, but just a quote. This will work as intended
print("I like \"Monty Python\"")
print('I like "Monty Python"')

print('"I\'m"'+'\n'+'""learning""'+'\n'+'"""Python"""')
#will output:
#"I'm"
#""learning""
#"""Python"""

#modulus, give remainder:
print(14 % 4)   #14:4 = 3; 3*4=12; 14-12=2 remaining

print(12 % 4.5) #12:4,5=2; 2*4,5=9; 12-9=3 remaining

#* before -/+; left to right:
print(9 % 6 % 2)

#BUT exponentiation is right to left:
print(2 ** 2 ** 3)      # 2**3 first=8, then 2**8 = 256
