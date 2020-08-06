"""
Python assignment 1
Accept user's first and last name 
print them in reverse order with a space between them
"""
first_name = input(" Enter your first name : ")
last_name = input(" Enter your last name : ")
name = [first_name, last_name]
name.reverse()
print(*name)