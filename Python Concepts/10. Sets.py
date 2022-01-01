# Sets In Python
# A set is a collection of well-defined objects and non-repetitive elements that is - a set with 1,2,3,4,3,4,5,2, 2, and 3 as its elements can be written as {1,2,3,4,5}

# No repetition of elements is allowed in sets.
# In Python programming, sets are more or less the same. Let's look at the Python programming definition of sets:

# “A set is a data structure, having unordered, unique, and unindexed elements.”

# Elements in a set are also called entries, and no two entries could be the same within a set.


# Well, now that you have a basic idea about sets in mathematics. Let me tell you that a mathematical set has some basic operations which can be performed on them. For example, the union of two sets is a set made using all the elements from both sets. The intersection is an operation that creates a set containing common elements from both sets. A python set has all the properties and attributes of the mathematical set. The union, intersection, disjoint, etc., all methods are exactly the same and can be performed on sets in python language.

# Note: If you are a programming beginner who doesn't know much about sets in mathematics. You can simply understand that sets in python are data types containing unique elements.

# If you want to use sets in your python programs, you should know the following  properties of sets in Python:

# -> Sets are iterable(iterations can be performed using loops)
# -> They are mutable (can be updated by adding or removing entries)
# -> There is no duplication (two same entries do not occur)

# Structure:
# -> Elements of the sets are written in between two curly brackets and are separated with a comma, and in this simple way, we can create a set in Python.
# -> The other way of forming a set is by using a built-in set constructor function.

# Both of these approaches are defined in the video above.

# Let me now share some basic information about sets so that you can know why they are so important and why you should learn them.

# Unlike the dictionary (that we have learned in tutorials 10 and 11), sets are not just restricted to Python language, but nearly all commonly used programming languages have sets included in them as a data type. Examples of these languages include C++, Java, etc., even languages such as Swift and JavaScript support sets. One of the earliest languages that supported sets was Pascal. I hope you now have a rough idea of how important these sets actually are because whichever language you choose to code in, you must have a very basic understanding of sets!

# Restrictions:
# Everything has a limit to its functionality, and there are some limitations on working with sets too.

# -> Once a set is created, you can not change any of its items. Although you can add new items or remove previous but updating an already existing item is not possible.
# -> There is no indexing in sets, so accessing an item in order or through a key is not possible, although we can ask the program if the specific keyword we are looking for is present in the set by using the “in” keyword or by looping through the set by using a for loop(we will cover for loops in tutorial # 16 and 17)

# Despite these restrictions, sets play a crucial role in the life of a python programmer. In most cases, these restrictions are never a problem for the programmer, given he knows which data type to use when. And this skill is something you will learn with time after writing a lot of python programs


# Set Methods:
# There are already a lot of built-in methods that you can use for your ease, and they are easily accessible through the internet. You might want to peep into python's official documentation at times as well to check for some updates they might push down the line. Some of the methods you can use with sets include union(), discard(), add(), isdisjoint(), etc., and their functionality is the same as in the sets in mathematics. Also, the purpose of these functions can easily be understood by their names.


s = set()
print(type(s))
l = [1, 2, 3, 4]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(2)
s.remove(2)
s1 = {4, 6}
print(s.isdisjoint(s1))
