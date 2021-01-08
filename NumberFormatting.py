#Andrey Ilkiv Assignment 5 Problem 3 Section 01 10/19/2020

#this was fun...


#Asks user for starting number and ending number
Startnum = int(input("Start number: "))
Endnum = int(input("End number: "))

#count for amount of numbers printed
cnt = 0
#max length of the final number we will print for formating others
maxdigits = len(str(Endnum))

#looping from start number to end number
for i in range(Startnum , Endnum):
    #count for amount of divisible numbers happened
    count = 0
    #looping from 1 to the number i, +1 because we never include end
    for j in range(1, i+1) :
        #if the number i is divisible perfectly with no remained count ++
        if i % j == 0:
            count += 1
    #if the count only hit 2 times during the full loop that means that this number i is only divisible by 1 and itself
    #this is one of the prime number properties
    if count == 2:
        #adds 1 to the number of times a number was printed
        cnt += 1
        #gets length of the digit printing
        digits = len(str(i))
        #spaces needed before each digit that is about to be printed
        spaces = maxdigits - digits
        #for print spaces the amount of times need which is max digit length - current digit length
        for k in range(spaces):
                print("  ", end="")
        else:
            #after spaces are printed checks if 10 numbers have been printed
            #if no then print and dont go to next line
            #if yes then print and go to next line and set printed count to 0
            if cnt < 10 :
                print(i, end=" " )
            else:
                cnt = 0
                print(i , sep='\n')
print()
