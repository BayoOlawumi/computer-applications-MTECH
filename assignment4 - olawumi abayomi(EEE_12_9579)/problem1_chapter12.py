import calendar

print("-------------1b-----------------")
cal = calendar.TextCalendar()
cal.setfirstweekday(calendar.THURSDAY)
cal.pryear(2012)

print("-------------1c-----------------")
print("This my calender month")
print(calendar.month(1995, 6))

print("-------------1d-----------------")
d = calendar.LocaleTextCalendar(6,"SPANISH")
d.pryear(2012)

print("------------------------------")
print(calendar.isleap(2012))