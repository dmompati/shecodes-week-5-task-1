# creditCard = "4012000033330086"

def calculate_credit_card_number_check_digit(creditcardnumber):
        
        card = list(creditCard[::-1]) #reverse number and store into list
        # print(card)
        oddNumber = card[::2] #Find all the odd numbers
        oddNumbers = list(map(int, oddNumber))
        evenNumber = card[1::2] 
        evenNumbers = list(map(int, evenNumber))
        sumOdd = 0
        multipleEven = []
        sumEven = 0

        for num in evenNumbers:
                multipleEven.append(num*2) #multiply each iterative number by 2 and add it to the empty list.

        for i in range(len(multipleEven)): #remembering number if I want to change the same list
                if multipleEven[i] > 9:
                        multipleEven[i] = multipleEven[i] - 9   

        for num in oddNumbers:
                sumOdd += int(num)    

        for num in multipleEven:
                sumEven += num

        totalSum = sumEven + sumOdd



 def validate_credit_card_number_check_digit(creditcardnumber):
        if totalSum % 10 == 0:
                print('Credit card Valid')

        else: 
                print("Your card is not valid")

        

#if the length of num is = 2 then seperate the number and add them together
# if the length is 2 then take 9 from the number
# - 15 numbers starting at 0
# - Sum of odd places (Starting from right to left)
#     - Add all the numbers that are in the odd indexes
# - Get all even places and double them
#     - if number is double digits seperate number to 2 digits and add those to produce 1 whole number
#     - Once all numbers are calculated add the doubled numbers together
# - Add sum of even and sum of odd together
# - If the number is divisible by 10 the card is valid