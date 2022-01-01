# Dictionary & Its Functions Explained

# basic definition of a Python Dictionary:

# “Python dictionary is an unordered collection of items. Each item of the dictionary has a key and value pair / key-value pair.”

# Every programming language has its distinct features, commonly known as its key features. With that said, Python’s one out-of-the-box feature is “dictionaries”. Dictionaries may look very similar to a “List”. Still, dictionaries have some distinct features that do not hold true for other data types like lists, and those features make it(python dictionary) special.

# Here are a few important features of a python dictionary:

# -> It is unordered(no sequence is required - data or entries have no order)
# -> It is mutable(values can be changed even after its formation, or new data/information can be added to the already existing dictionary, we can also pop/remove an entry completely)
# -> It is indexed(Dictionary contains key-value pairs, and indexing is done with keys. Also, after the Python 3.7th update, the compiler stores the entries in the order they are created)
# -> No duplication of data(each key is unique
#                        no two keys can have the same name, so there is no chance for a data being overridden)


# If we talk a little about how it works, its syntax comprises of key and values separated by colons in curly brackets, where the key is used as a keyword, as we see in real life dictionaries, and the values are like the explanation of the key or what the key holds(the value). And for the successful retrieval of the data, we must know the key so that we can access its value, just like in a regular oxford dictionary where if we don't know the word or its spelling, we cannot obtain its definition. Let's look into the syntax of a Python dictionary:

# a = {'key', 'value', 'me': 'you'}
# print(a['me'])

# # will print "you" on the screen
# With the help of dictionaries, we do not have to do most of our work manually through code like in C or C++. I mean that Python provides us with a long list of already defined methods for dictionaries that can help us do our work in a shorter span of time with a minimal amount of code. Some of these methods are, clear(), copy(), popitem(), etc. The best part about them is that no extra effort is required to be put in order to learn the functionality as their names explain their functions (in most of the cases), such as clear() will clear all the data from the dictionary, making it empty, copy() will make a copy of the dictionary, etc.


# Some distinct features that a dictionary provides are:

# We can store heterogeneous data into our dictionary, i.e., numbers, strings, tuples, and the other objects can be stored in the same dictionary.
# Different data types can be used in a single list, making the value of some keys in the dictionary.


# Dictionary is nothing but key value pairs

d1 = {}
# print(type(d1))
d2 = {"Yatharth": "1",
      "khushbu": "2",
      "Raj": "3",
      "Deep": {"A": "4", "B": "5", "C": "6"}}

d2["Dev"] = "7"
d2[8] = "me"
print(d2)

del d2[8]
print(d2["Deep"])

d3 = d2.copy()
del d3["Yatharth"]
d2.update({"You": "9"})
print(d2.keys())
print(d2.items())
