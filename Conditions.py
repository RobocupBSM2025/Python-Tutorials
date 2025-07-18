"""

If, elif, and else are the three main holder conditions, as in the other additions are only possible
inside these three. You always have to have an if statement and then can use elif or else staements afterwards
to refer to the previous most recent and accesable if statement. (I am not certain if you can continue the
elif or else statements inside a looping function, but I know it cannot access if statements in a 
function on a higher indent level.) After you use an if statement any else of elif statements cannot go through
if the if statement goes through, as it has the highest priority. If an elif condition goes after the if statement 
then that elif statement has priority for every folllowing elif or else statements. This formula goes on until the end of
set of conditions either due to not more conditions or a forcefull ending such as an else condtion which covers for 
everyhting that is not incuded as a condition for the previous if and if there are any elif conditions.

Sorry for the mass amount of text.

Here is the uses, making conditions, checking if something matches a predetermined or live setting, making different
values export different things, and many more.

To make the explanations of the conditions I will explain it through running the program. / in the terminal

"""

print("CONDITIONS FOR IF STATEMENTS (Confusion addition) : \n \n")

Equals = "Equals" # Or in English Equals Equals Equals, I am tired and wanted to have fun sorry if it is confuzzing

if Equals == "Equals" :

  print(f"""{Equals} Equals Equals Equals. \n ' == ' means same as so if they are the same the 
  condition is true and the stuff inside the condtion is ran""")

if Equals != "Not Equals" :

  print(f"""\n \n{Equals} Does Not Equal Not Equals. \n ' != ' means ' not the same as ' so if they are the not same the 
  condition is true and the stuff inside the condtion is ran. This is due to the factthat having a '!'  before a 
  condition flips the bool result""")

# Now I will explain the number side of things and I will try to make it at least semi serious

a = 1
b = 1
c = 2
d = 0

print("""\n \nI have set a and b equal to 1 and c equal to 2. I have also set d equal to 3.
For now I will only be using true staements, but I will change that when I reach elif and else statements""")

if a == b :

  print(f"\na == b ({a} equals {b})")

if a != c :

  print(f"\na != c ({a} does not equal {c})")

if a < c :

  print(f"\na < c ({a} is less than {c})")

if a <= c :

  print(f"\na <= c ({a} is less than or equal to {c})")

if a <= b :

  print(f"\na <= b ({a} is less than or equal to {b})")

if a > d :

  print(f"\na > d ({a} is greater than {d})")

if a >= d :

  print(f"\na >= d ({a} is greater than or equal to {d})")

if a >= b :

  print(f"\na >= b ({a} is greater than or equal to {b})")

if a !> c : # While I am not cetain if this is the correct and works without issue as I do not curretly have internet, I have done this in other coding langeges and while it is not practical, I thought I should bring attention to the fact that I think it is possible

  print(f"\na !> c ({a} is not greater than {c})")

"""

Next up I will show off elif and else statements as well as having anif stamenet have it condition to be false.
Using elif statements are very helpful as it enables a hierachy in the chain of what is most important. In addition
using else statements are very helpful to avoid errors that may come as a result of having nothing that is returned
if all previous conditions are failed and a result is reuired for the code to work. While this issue can be avaoided 
else statements make it obvious to any people looking at you code in the future what you were aiming for.

"""

print("\n \nFAILED CONDITION :\n \n")

print("if True == False: then I will do something ... Testing \n ... Testing \n ... Testing \n ... \n ...")

if True == False :

  print("something")

print("\n ... \n ... \n ... I dont think it did something so the thing was skipped as the condition failed")

# Now onto Else statements

print("\n \nELSE STATEMENT : \n \n")

print("
