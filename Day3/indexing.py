#indexing accessing elements of a sequence using []
               # [start:end:step]

credit_number = "123-456-789"
#print(credit_number[2])
#print(credit_number[0:3])
#print(credit_number[4:11]) #or we can use:
#print(credit_number[4:]) #- python interprete's as you want everything from 4th digit
                        #upto the last digit. = 456-789



#last_four = credit_number[6:]


#to reverse the credit card number we use:
credit_number = credit_number[::-1]
print(credit_number)