def alternative_character(input_string): # Defining alternative character function
    result = [] # Empty list
    for i, char in enumerate(input_string): # Loops through the individual characters in input string
        if i % 2 == 0: # If it is even then it makes the character upper
            modified_char = char.upper()
        else:
            modified_char = char.lower() # Else statement becomes a lower case character
        result.append(modified_char) #Appends the modified characters to the results empty list
    return ''.join(result) #joins the characters together

def alternative_words(user_input): #same method but with words instead
    words = user_input.split() #splits based on empty space
    transformation = []

    for i, word in enumerate(words):
        if i % 2 == 0:
            transformation.append(word.upper())
        else:
            transformation.append(word.lower())
    
    new_string = ' '.join(transformation)
    return new_string

input_string = input("Write a sentence where you would like each alternative character to be a different case: ")
output_chars = alternative_character(input_string) # Calls the alternative character function
print("The edited sentence (alternate characters) is:", output_chars)

user_input = input("Write a sentence where you would like each word to be alternately cased: ")
output_words = alternative_words(user_input) # Calls the alternative words function
print("Edited sentence (alternate words) is:", output_words)