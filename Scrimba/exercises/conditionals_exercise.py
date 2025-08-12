
def num_days(month):
  thirty_one_days = ('jan','mar','may','jul','aug','oct','dec')
  thirty_days = ('apr', 'jun','sep','nov')
  twenty_eight = ('feb',)

  if month in thirty_one_days:
      print(f"{month[0:]} Has 31 Days")
  elif month in thirty_days:
      print(f"{month[0:]} Has 30 Days")
  elif month in twenty_eight:
      print(f"{month[0:]} Has 28 Days")
  else:
      print(f"{month} Isn't a valid month")







    # if month == 'jan':
    #     print('number of days in',month,'is',31)
    # elif month == 'feb':
    #     print('number of days in',month,'is',28)
    # elif month == 'mar':
    #     print('number of days in',month,'is',31)
    # elif month == 'apr':
    #     print('number of days in',month,'is',30)
    # elif month == 'may':
    #     print('number of days in',month,'is',31)
    # elif month == 'jun':
    #     print('number of days in',month,'is',30)
    # elif month == 'jul':
    #     print('number of days in',month,'is',31)
    # elif month == 'aug':
    #     print('number of days in',month,'is',31)
    # elif month == 'sep':
    #     print('number of days in',month,'is',30)
    # elif month == 'oct':
    #     print('number of days in',month,'is',31)
    # elif month == 'nov':
    #     print('number of days in',month,'is',30)
    # elif month == 'dec':
    #     print('number of days in',month,'is',31)

num_days('jan')
# optimize/shorten the code in the function
# try to reduce the number of conditionals
