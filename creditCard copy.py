def calculate_credit_card_number_check_digit(creditCard):
        card = list(creditCard[::-1]) #reverse number and store into list
        print(card)
        evenNumber = card[::2] #Find all the even numbers
        evenNumbers = list(map(int, evenNumber))
        print(evenNumbers)
        oddNumber = card[1::2] 
        oddNumbers = list(map(int, oddNumber))
        print(oddNumbers)
        sumOdd = 0
        multipleEven = []
        sumEven = 0
        for num in evenNumbers:
                multipleEven.append(num*2) #multiply each iterative number by 2 and add it to the empty list.

        for i in range(len(multipleEven)): #remembering number if I want to change the same list
                if multipleEven[i] > 9:
                        multipleEven[i] = multipleEven[i] - 9   
        for num in evenNumbers:
                sumOdd += int(num)

        for num in multipleEven:
                sumEven += num

        totalSum = sumEven + sumOdd
        additions = [1,2,3,4,5,6,7,8,9]
        for num in additions:
                if (totalSum + num) % 10 == 0:
                        checkDigit = num
        return str(checkDigit)

print(calculate_credit_card_number_check_digit('542418027979176'))

def validate_credit_card_number_check_digit(creditCard):

        card = list(creditCard[::-1]) #reverse number and store into list
        oddNumber = card[::2] #Find all the odd numbers
        oddNumbers = list(map(int, oddNumber))
        evenNumber = card[1::2] 
        evenNumbers = list(map(int, evenNumber))
        sumOdd = 0
        multipleEven = []
        sumEven = 0
        for num in oddNumbers:
                multipleEven.append(num*2) #multiply each iterative number by 2 and add it to the empty list.

        for i in range(len(multipleEven)): #remembering number if I want to change the same list
                if multipleEven[i] > 9:
                        multipleEven[i] = multipleEven[i] - 9   
        for num in evenNumbers:
                sumOdd += int(num)

        for num in multipleEven:
                sumEven += num

        totalSum = sumEven + sumOdd

        if totalSum % 10 == 0:
                return('This is a valid credit card number.')
        else:
                return('This is an invalid credit card number.')
