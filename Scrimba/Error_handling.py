#try:
    #code you want to run
#except:
    #executed if error occurs
#else:
    #executed if no error
#finally:
    #always executed



try:
    num = int(input('Enter a number between 1 and 30: '))
    num_1 = 30/ num

    if num > 30:
        raise ValueError(num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Bad value!")

except:
    print("Invalid input")
else:
    print("30 divided by", num, "is: ", 30 / num)
finally:

print("** THANK YOU FOR PLAYING **")
