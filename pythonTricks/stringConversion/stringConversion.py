
import datetime

today = datetime.date.today()
print(str(today))
print(repr(today))
print(datetime.date(2021, 1, 5))

# __str__ => Easy to read, for the user mainly
# __repr__ => unambiguous
