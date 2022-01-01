# “If, else and elif statement can be defined as a multiway decision taken by our program due to the certain conditions in our code.”

# Our compiler will execute the if statement to check whether it is true or false now
# if it’s true, the compiler will execute the code in the “if” section of the program and skip the bunch of code written in “elif” and “else.” But if the “if” condition is false, then the compiler will move towards the elif section and keep on running the code until it finds a true statement(there could be multiple elif statements). If this does not happen, then it will execute the code written in the “else” part of the program.

# An “if” statement is a must because without an if, we cannot apply “else” or “else-if” statements. On the other hand else or else if statement is not necessary because if we have to check between only two conditions, we use only “if and else” and even though if we require code to run only when the statement returns true and do nothing if it returns false then an else statement is not required at all.

# Now Let’s talk about some technical issues related to the working of decision statements:

# -> There is no limit to the number of conditions that we could use in our program. We can apply as many elif statements as we want, but we can only use one “else” and one “if” statement.
# -> We can use nested if statements, i.e., if statement within an if statement. It is quite helpful in many cases.
# -> Decision statements can be written using logical conditions, which are:
# -> Equal to
# -> Not equal to
# -> Less than
# -> Greater than
# -> Greater than equal to
# -> Less than equal to

# We can also use Boolean or our custom-made conditions too.


var1 = 6
var2 = 56
var3 = int(input())
if var3 > var2:
    print("Greater")
elif var3 == var2:
    print("Equal")
else:
    print("Lesser")

list1 = [5, 7, 3]
print(15 not in list1)
if 15 not in list1:
    print("No its not in the list")

# Example
print("\nExample")
print("What is your age?")
age = int(input())
if age < 18:
    print("You cannot drive")

elif age == 18:
    print("We will think about you")

else:
    print("You can drive")
