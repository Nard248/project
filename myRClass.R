#### HELPER CODE #######
setClass("Person", slots=c(name = "character", age = "numeric"))
### END HELPER CODE ###

# Part 1. 
# Your program is based on S4 objects.
# Consider that an employee is a person who has a salary and gets a raise from time to time.

# 1. Write an inherited class from the Person class, called Employee, who's attributes are boss (which is a Person object) and the salary (which is a numeric object).
# 2. Write a Generic function called raise with the following arguments: An object and a percentage numeric variable.   
# 3. Write the Employee's specific method for the generic function raise which will take the object and percentage as an argument.
# For example if raise was called on an Employee object it should be used as follows:
# raise(john, percent=10) where john is an instance of the Employee object and percent is the raise percentage that will be applied on John's salary.

# Part 2.
# 4. Create a generic function called secret with th following arguments: The object and a message variable which will be a string. 
# 5. Create a Person object's method for secret with the object and message arguments and let this method, encrypt a message using your Python encrypter. This function returns a string.
# 6. Create an Employee's object's method for secret with the object and message arguments and let this method, decrypt a message using your Python encrypter ONLY for Employees whos name is "John"! 
# If the employee's name is not "John", apply more encryption on top of the encrypted message. This function returns a string.