'''Implement a Money class, for a currency with dollars and cents.

>>> m1 = Money(10, 0)
>>> m1.dollars
10
>>> m1.cents
0

>>> m2 = Money(25, 50)
>>> m2.dollars
25
>>> m2.cents
50

Also give your class __str__ and __repr__ methods. These both return
strings. The __str__ method lets you specify what happens when you
pass the object to print(); it's also what is returned by the built-in
str() function. It's meant to be user-friendly representation of the
object.

>>> print(m2)
$25.50
>>> str(m1)
'$10.00'

The __repr__ method specifies the interpreter's output when you enter
just the object at the interactive prompt; it's also what is returned
by the built-in repr() function. This is meant to be a
machine-friendly representation, for logging, debugging, etc.

>>> m2
Money(25, 50)
>>> repr(m1)
'Money(10, 0)'

Notice the repr() output is what you'd want to type in to recreate the
exact object! This is a helpful convention to follow with __repr__,
whenever practical.

Now give your Money class the ability to be used with some different
operators:

>>> m1 + m2
Money(35, 50)
>>> m2 - m1
Money(15, 50)

>>> Money(0, 75) + Money(0, 75)
Money(1, 50)
>>> Money(3, 50) - Money(0, 75)
Money(2, 75)
>>> m1 * 3
Money(30, 0)
>>> m2 * 2
Money(51, 0)

>>> Money(5, 0) + Money(3, 50) == Money(8, 50)
True
>>> Money(3, 50) == Money(3, 51)
False

>>> m1 >= m2
False
>>> m1 < m2
True

'''

# Write your code here:
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        centStr = str(self.cents)
        if len(centStr) < 2:
            return "$" + str(self.dollars) + ".0" + str(self.cents)
        else:
            return "$" + str(self.dollars) + "." + str(self.cents)

    def __repr__(self):
        return "Money(" + str(self.dollars) + ", " + str(self.cents) + ")"

    def __add__(self, other):
        cents = self.cents + other.cents
        dollars = self.dollars + other.dollars
        if cents > 100:
            cents = cents - 100
            dollars = dollars + 1
        return Money(dollars, cents)


    def __sub__(self, other):
        cents = self.cents - other.cents
        dollars = self.dollars - other.dollars
        if cents < 0:
            cents = cents + 100
            dollars = dollars - 1
        return Money(dollars, cents)



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
