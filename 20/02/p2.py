data = open("data.txt", "r")            # Open data.txt
dataArray = data.read().splitlines()    # Put each line into an array

validpwds = 0                           # Start with no valid passwords

for x in dataArray:                     # For loop for every value in the array
    x = x.replace(":","",1)             # Remove the colon from input text
    x = x.replace("-"," ",1)            # Replace the hyphen with a space for easy split in next step
    x = x.rsplit(' ',3)                 # Split the input string into an array with 4 variables
    
    pos1 = int(x[0])                    # First and second variables are integers
    pos2 = int(x[1])
    char = x[2]                         # Throw each value into easy to use variables
    pwd = x[3]

    validity = 0                        # Set up validity check 

    if pwd[pos1-1] == char:             # Check validity of first identified character
        validity += 1
    if pwd[pos2-1] == char:             # Check validity of second identified character
        validity +=1

    if validity%2 == 1:                 # If only one character was valid,
        validpwds += 1                      # add 1 to the number of valid passwords

print('The number of valid passwords is {}.'.format(validpwds))
