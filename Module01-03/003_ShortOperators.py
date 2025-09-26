# You may use an expression like this if you can't fall asleep and you're trying to deal with it using some good, old-fashioned methods:

# sheep = sheep + 1

# Python offers you a shortened way of writing operations like these, which can be coded as follows:

x *= 2
sheep += 1

# Let's try to present a general description for these operations.

# If op is a two-argument operator (this is a very important condition) and the operator is used in the following context:

# variable = variable op expression

# It can be simplified and shown as follows:

# variable op= expression

# Take a look at the examples below. Make sure you understand them all.

i = i + 2 * j ⇒  i += 2 * j

var = var / 2 ⇒  var /= 2

rem = rem % 10 ⇒  rem %= 10

j = j - (i + var + rem) ⇒  j -= (i + var + rem)

x = x ** 2 ⇒  x **= 2