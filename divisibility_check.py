# Collaborators: 
#In the same repo as before, switch to 'divisibility_check.py' and write a short Python divisibility checker program.
# Your program will take the numbers from 2 through 50 (inclusive).  It will check to see if the number is divisible by 3
# (hint: % operator).  If the number is divisible by three, print a message that says, "x is divisible by three" where x
# is the number being tested.  If it is not divisible by 3 print a message to that effect as well.
#Submit your work (both programs) by committing and pushing to GitHub. (There is no test code to run for this assignment.)



for (x) in range(2,51,1):
    ((x) % 3)
    remainder = ((x) % 3)
    if (remainder) == 0:
        print(str(x)+' is divisible by 3')
    else:
        print (str(x)+' is not divisible by 3')



