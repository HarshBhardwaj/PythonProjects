#Harsh Bhardwaj
print("This is Magic Date Appliation")

_month = int(input('Enter a month: '))
_day = int(input('Enter a day: '))
_year = int(input('Enter two digit year: '))

#Check for Valid Date 
if _month > 0 and _month <= 12:
  print(_month, "Month is valid")
else:
  print(_month, "not a valid month")
if _year >= 00 and _year <= 99:
  print(_year, "Year is valid")
else:
  print(_year, "not a valid year")

_month_31 = [1,3,5,7,8,10,12]
_month_30 = [4,6,9,11]
_month_28 = [2]

if _day >= 1 and _month in _month_31 and _day <= 31:
  print(_day, "Day is valid")
elif _day >=1 and _month in _month_30 and _day <=30:
    print(_day, "Day is valid")
elif _day >=1 and _month in _month_28 and _day <=28:
    print(_day, "Day is valid")
else:
  print(_day, "Day is invalid")

_magic_year = _day * _month
if _magic_year == _year:
    print(str(_month) + '/' + str(_day) + '/' + str(_year), "Date is magic")
else:
    print(str(_month) + '/' + str(_day) + '/' + str(_year), "Date is not magic")
exit = input("")
