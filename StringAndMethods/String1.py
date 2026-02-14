str="pranav"
lo="My name is pranav"
n="019292"
dob= "17march1997"
str1="       "

print("Length of the string:",len(str)) #6
print("Upper Case:",str.upper())    #PRANAV It used to turn the string into upper case
#It will not change permentaly, it will temp change. we need to reinitialize
str=str.upper() #Reinitialize
print(str)
print("Lower Case:",str.lower()) #It used to turn the string into lower case
str=str.lower()  #Reinitialize
print(str)
print("Char occurrence in the string:",str.count('a')) #2
print("Turn first letter in capitalized: ", str.capitalize()) #Pranav
print("Turn every first letter in capitalized: ", lo.title())
print("To check the total alphabets in the string: ",str.isalpha())
print("To check the total digit in the string: ",n.isdigit())
print("To check the combination in the string:",dob.isalnum())
print("To check only spaces in the string: ",str1.isspace())
