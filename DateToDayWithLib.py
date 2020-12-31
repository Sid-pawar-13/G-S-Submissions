# Python program to find the first day of given year.
# Input : 2010
# Output :Friday
# Input :2019
# Output :Tuesday
# (Hint: Read about the datetime library and use it to code your solution)

import datetime
year = int(input("Enter a year : "))
x = datetime.datetime(2019,1,1)
print(f"Day on the 1/1/{year} : {x.strftime('%A')}")
