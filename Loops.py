"""

The first kind of loop I will cover will be for loops.

There are a few kind of loops:
  For loops
  Ranges
  Nested Loops
  While loops

While everything, but while loops, is techncally considered under 'for' loops, they each function differently
in fact the for loop functions diferently from most likely all the code you have encountered in the past
as the range function is required to loop (while in other programs that is natural.)

'For' loops, in Python, are used for seperating parts of an array or string into individual parts. 
This can be used to make something like a decoder or to allow you to check an array for its values individually,
among other things. It can be used on sets of statements such as a list, tuple, set, string, etc. One way to use the 
string 'for' loop is due to how motors send their position through a list of numbers and letters in a string with
use of commas to seperate sections. You can use the loop to add to an list by making a new section every comma
and adding the letters after that comma to the new section / adding the letter to the newest section.

"""

print("BASIC FOR LOOPS : \n \n") # Heading for running the code

#Now onto the first kind of for loops, the rope, no string kind

BadPassword = "password123"

print("\nEnter the password : ")
  
for letter in BadPassword:
  
  print(letter)

# The other use besides sepperating strings is lists or arrays

Quotes = ["Why am I here just to suffer", "I am tired", "Icescream", "Quote - Someone, somewhere, sometime"]

for Q in Quotes:

  print(f"\n Here is a highly inspirational quote : {Q}")

# In addition to stings you can also use the 'for' loop for intergers and bools and more

MonteyPython = [1, 2, 5]

print("""\nYou must count to three, no greater and no less.
You must not count to four or to two but to three.
Three is the number you must count to.""")

for HandGranade in MonteyPython :

  print(HandGranade)

print("\nNo three ... Kaboooom (Vicious Rabit goes 'Bleh')")

# Or this

TotalyRealLieDetector = [True, False, False, True, True]

for IsTrue in TotalyRealLieDetector :

  print(f"\nQ : *Guberish Quesjin* \nA : *Jibberich Antswear* \nLie Detection : The Answer is {IsTrue}")

"""

Range functions are how you can accive the tratiditonal 'for' loop that you see in other coding langueges.
They are use to repeate what ever is contained in said loop X number of times starting for ( 0 ) and
Ending at ( X - 1 ) for example if you were to have it repeate 4 times, it would start with a value of 0 and end 
with a value of 3. Therefore repeating 4 times. This starting at 0 is common and used not just among many code 
langueges but also in computer base code such as the camera where the 1st camera is actually camera 0.

This can be used to do many things such as counting, or repeating a task to achive things such as adding extra 
time to do something or making it so that you do not have to make 30 line of code to make a proccess repeate multiple
times. There are many other uses, just none I can think of off the top of my head.

"""

print("\n \n RANGE FOR LOOPS : \n \n") # Name of Code Section

# Basic Range function

print("\n 0 to 9 :") #Addinng Spaces

for x in range(10):
 
  print(x)

# You can also make the range start at another value other than zero, but it will still not reach the max number

print("\n 1 to 10 :") 


for x2 in range(1, 11):

  print(x2)

# In addition you can like in other codiding langeges make it incread by specific incraments other than 1

print("\n 3 to 30 :") #Addinng Spaces

for x3 in range(3, 32, 3):

  print(x3)

# One very basic use / example of it is to declutter the code below

print("\n 1 to 4 :") #Addinng Spaces

print(1)
print(2)
print(3)
print(4)

# --------------------

print("\n 1 to 4 :") #Addinng Spaces

for numbee in range(1, 5):
  
  print(numbee)

"""

Nested Loops are when you have loops in loops, this can be use to multiple digits together,
Seperate arrays futher down, have combinations, have you check if things match, and many other things.

"""

print("\n \nNESTED LOOPS : \n \n")

#
