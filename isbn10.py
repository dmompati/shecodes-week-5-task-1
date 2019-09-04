isbn = '188879997'

#Multiply all isbn number from one end to another with numbers starting from 10
#convert and split string into list of integers
isbnList = list(map(int, isbn[::-1]))
print(isbnList)
#multiple each number by a number starting from 10

counter = 1
# while counter < range(len(isbnList)):
#     isbnList.append(isbnList[counter]*counter)
#     counter += 1

for num in range(len(isbnList)):
    num * counter
    counter += 1

print(isbnList)


#Add the sum of the products
#get the remainder of the sum divided by 11
#The check digit is 11 minus the remainder

