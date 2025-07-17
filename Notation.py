"""
In Python there are two main types of notation. 

This Notation can cover multiple lines and is helpfull if

you need to write a pargagraph without it going on and on and on and making it hard to read as you have to schroll to the right to even read it.

This is very helpful if for example you want to show an example of code, for example :
"""

"""
if x == 1 :

  print(f"x = 1")
  
"""

# This is the other kind of comment or notation
# And as you can see it is another collor and has to have the # at the start of each line
# This is good for commenting on lines, and is much easier to use for quick comments as # is easier than """ """
# I may have forgotten about the other one when writing my notation for the Explained, Sorry
# The main issue with these are that they can end up being to long and you having to zoom out or schroll to the right to even read them.
# However it is much Easier to quickly comment out code or to leave a quick explanation of code

# For Example if I wanted to test if there was an issue in the following code :

x = 1
if x == 1 :
  x = 2
  print(f"x = {x}")

# This prints "x = 2", but if you wanted to have it be one you could for example see if the
# x = 2 is the error by commenting it out
# While I know this is a bad example, this is one possible use

x = 1
if x == 1 :
  # x = 2
  print(f"x = {x}")

# In addition you can comment to others what the code is doing using this comment

x = 1 # Sets x = 1
if x == 1 : # Checks if (x = 1)
  x = 2 # Sets x = 2
  print(f"x = {x}") # Prints "x = " and the value of x the variable

# One last use of these comments is the fact that you can specifically indent these comment 
  # Individually like this 
  # To immitate a if, while, for, ect. statement
    # This can be helpfull to do many things such as 
      # Make lists like this
      # Comment out a whole bunch of code
      # Imply connectivity 
        # Such as implying these two sentences are combinged
      # And Many more

"""
You can also comment and use 
  Indents like this
    And achive a simular 
    Result
  This is most usefull for commenting out a whole bunch of code like for example 
    if you have a broken for statement :
"""

"""

y = 6
for x in range y :
  y = y + 1

"""

# But the most usefull way of using them is to empy emphasis
"""
Such as making it to the # are for commenting on code
and the """ """ are for commenting out code / temporarily removing code
"""
# This allows for the commeents to stand out and for the comment for you to easily see what is a commment and what is removed
# Code as it will be not only different collors, but also differnt types of comments.
