names_list = [] #creates an empty list called names_list
dobs_list = [] #creates an empty list called dobs_list

with open("DOB.txt",'r+') as file: #opens the DOB.txt file in read and write mode
    for line in file.readlines(): #iterates over each line the file 
        index1 = line.find(' ') #finds the first instance of white space and this is stored as index 1
        index2 = line.find(' ', index1 + 1) #finds the second instance of white space and this is stored in index 2
        names = line[:index2].strip() #for each line the string before index2 is classed as names
        dobs = line[index2:].strip() #for each line the string after index 2 is classed as dobs (date of births)
        names_list.append(names) #the names are added to the names list
        dobs_list.append(dobs) #the dobs are added to the dobs list

names_string = '\n'.join(names_list) #casts the names_list to a string with a new line seperator
dobs_string = '\n'.join(dobs_list) #casts the dobs to a string with a new line seperator

print('Names:\n', names_string) #prints the names after Names:
print('\nDates of Birth:\n', dobs_string)#prints the dobs after Dates of Birth:

#unsure how to remove indent from first line??

