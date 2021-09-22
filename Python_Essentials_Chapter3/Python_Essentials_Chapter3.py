#SSgt Binod Gurung, MODULE 3.1 LAB CODES  Date: 21 Sep 2021
#MODULE 3.1.1.4 Comparision Operators

n = int(input("Enter a numerical value:")) # Input the numerical value to compare.
print(n >= 100)                            #n is compared to value of n greater OR equals to 100.

#MODULE 3.1.1.10 Comparing operators and conditional execution.

flower = input("Enter the best plant Spathiphyllum properly: ")  #Input the flower name.
if flower == "Spathiphyllum":                                    #Comparing the user's input with Spathiphyllum using If-Else.
    print('"Yes - Spathiphyllum is the best plant ever!"')
    if flower == "spathiphyllum": 
        print('"No, I want a big Spathiphyllum!"')
else:
    print("Spathiphyllum! Not", flower )

#MODULE3.1.1.11 LAB: Essential of the if-else statement. Calculating the tax

income = float(input("Enter the annual income: ")) #User input for the annual income.
if income <= 85528:                                #if-else condition for annual income more,equal or less than 85,528. 
    tax = ((18/100)*income)-556.02                 #18% of income - 556.02.
else:
    tax = 14839.02 + ((32/100)*(income-85528))     #14839.02 plue 32% of surplus amount from 85528.
if tax < 0:                                        #if condition for tax less than 0, tax displayed as 0.
    tax = 0
tax = round(tax, 0)                                #tax is rounded using round() function.
print("The tax is:", tax, "thalers")

#MODULE 3.1.1.12 LAB: Essentials of if-elif-else statement. Determining Leap and Common year.

year = int(input("Enter a year: "))        #Input year.
if year > 1581:                            #If-else condition to check if the year is in Gregorian calendar.
    if (year % 4) != 0:                    #Condition to check the year isn't divisible by 4.
        print(year,"is a Common year.")    
    elif (year % 100) != 0:                #Condition to check the year isn't divisible by 100.
        print(year," is a Leap year.")
    elif (year % 400) != 0:                #Condition to check the year isn't divisible by 400.
        print(year,"is a Common year.")
    else:
        print(year,"is a Leap year.")      #Any other condition, it's a Leap year.     
else:
    print(year,"is not within the Gregorian Calendar period.") #This confirms year before 1581 is not in Gregorian calendar.

#MODULE 3.2.1.3 LAB: Essentials of the while loop - Guess the secret number

secret_number = 777                                 #Assigned secret number 777.
print(                                              #Displays as shown. Looks fancy.
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
user_number = input("Enter an integer number: ")    #Input user's guess number. Input give the output as string.
while int(user_number) != secret_number:            #int(user_number) is used to change the string value to be integer. Comparing the secret value with the secret number.
    print("Ha ha! You are stuck in my loop!")       #Displays this output if the entered number doesn't match to the sercret number 777

print(secret_number, "is the secret number.", "Well done, muggle! You\'re free now.") #prints this when the user enters the correct number.

#MODULE 3.2.1.6 LAB: For Loop - Counting Mississippi

import time
count = 1                           #counter set to 1
for count in range(1,6):            #For loop, that counts to 5. range starts at 1 and ends at 6; which gives 1 to 5.
    print(count, "Mississippi")     #prints the number and Mississippi
    time.sleep(1)   
print("Ready or not, here I come!")#Prints the final message.

#MODULE 3.2.1.9 LAB: The break statement - Stuck in a loop

while True:                                         #Set while condition if True
    word = input("Enter the sercret word: ")        #Request's user's input of secret word
    if word == "chupacabra":                        #if the word is chupacabra, the next line will print as displayed.
        print("You\'ve successfully left the loop.")
        break                                       #If the word isn't chupacabra, it breaks and goes back to the user's input line.

#MODULE 3.2.10 LAB: The continue statement - the Ugly Vowel Eater

user_word = input("Enter a word: ") #It allows user to input a word and assign to user_word variable.
user_word = user_word.upper()       #changes the word to Uppercase.
for letter in user_word:            #For loop to check A,E,I,O,U in uppercased word.
    if letter == "A":               #Checks letter 'A' in user_word. It if is there.
        continue                    #If A is found in user_word, it will continue to next statement.
    elif letter == "E":             #Checks letter 'E' in user_word. 
        continue                    #If E is found in user_word, it will continue to next statement.
    elif letter == "I":             #Chceks letter 'I' in user_word
        continue                    #If I is found, it will continue to next statement.
    elif letter == "O":             #Checks letter 'O' in user_word
        continue                    #If O is found, it will continue to next statement.
    elif letter == "U":             #Checks letter 'U' in user_word.
        continue                    #If U is found, it will continue to next statement.
    else:                           
        print(letter)               #If A, E, I, O, U is not found, it will print the rest of the words on each iteration.  

#MODULE 3.2.1.11 LAB: The continue statement - The Pretty Vowel Eater

word_without_vowels = ""
user_word = input("Enter a word: ") #It allows user to input a word and assign to user_word variable.
user_word = user_word.upper()       #changes the word to Uppercase.
for letter in user_word:                #For loop to check A,E,I,O,U in uppercased word.
    if letter == "A":                   #Checks letter 'A' in user_word. It if is there.
        continue                        #If A is found in user_word, it will continue to next statement.
    elif letter == "E":                 #Checks letter 'E' in user_word. 
        continue                        #If E is found in user_word, it will continue to next statement.
    elif letter == "I":                 #Chceks letter 'I' in user_word
        continue                        #If I is found, it will continue to next statement.
    elif letter == "O":                 #Checks letter 'O' in user_word
        continue                        #If O is found, it will continue to next statement.
    elif letter == "U":                 #Checks letter 'U' in user_word.
        continue                        #If U is found, it will continue to next statement.#
    else:
        word_without_vowels += letter   #Every character is added on each iteration and assigned to word_without_vowels variable.
print(word_without_vowels)              #It prints the word without vowels in single line.  



#End of the Module