def add(num1, num2): #known as parameters
    #personal comments on the code you're creating
    """This is a function that returns sum of num1 and num2"""
    return num1 + num2


add(23, 80) #arguments are positional by default they are automically assigned as num1 and num2
#need two spaces between different functions

#print(23 + 5)
#print (10 + 1) #avoid repeating code 
#reason you get nothing is because return returns values but doesn't print them
sum_value= add(23, 80)

print(sum_value)
#ctrl + ? makes information to comments

# #wihout parameter
# def unique_greet():
#     print(f"Well, Hello There! Ahhh General!") #f-string can format a variable


# unique_greet() #just typing the function calls the function


#wihout parameter
def unique_greet(name):
    print(f"My name is {name}") #f-string can format a variable


unique_greet() #just typing the function calls the function