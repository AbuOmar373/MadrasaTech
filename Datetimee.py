from datetime import *

today = datetime.today()
print(today)

month = today.month  #today^
print(month)

year = today.year
print(year)

month2 = today.strftime('%B') # day ('%A') year ('%Y')
print(month2)
