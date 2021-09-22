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

#End of the Module