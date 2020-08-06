"""
Python assignment 1 
--->divisible by 7 but not a multiple of 5,
between 2000 and 3200 (inclusive)
--->the number obtained should be printed in 
comma -seperated sequence on a single line.
"""

num=[]
for x in range(2000, 3201):
    if x % 7==0 and x%5!=0:
        num.append(x)
print ('There are %s numbers between 2000 and 3200 which are divisible by 7 but are not a multiple of 5' % (len(num)))
print ('The numbers are ', *num, sep=",") # * is to print the numbers without the brackets   