import sys
def get_day_num(str_day):
    if str_day=='Sunday':
        return 0
    elif str_day=='Monday':
        return 1
    elif str_day=='Tuesday':
        return 2
    elif str_day=='Wednesday':
        return 3
    elif str_day=='Thursday':
        return 4
    elif str_day=='Friday':
        return 5
    elif str_day=='Saturday':
        return 6

def get_day_str(day_no):
    if day_no==0:
        return 'Sunday'
    elif day_no==1:
        return 'Monday'
    elif day_no==2:
        return 'Tuesday'
    elif day_no==3:
        return 'Wednesday'
    elif day_no==4:
        return 'Thursday'
    elif day_no==5:
        return 'Friday'
    elif day_no==6:
        return 'Saturday'
    else:
        return 'Day Number out of range'


def day_add(day_name, leave_day):
    if leave_day > 6:
        leave_day = leave_day % 7
    else:
        leave_day = leave_day
    return get_day_str(get_day_num(day_name) + leave_day)


def test_day(day_add):
    lineno = sys._getframe(1).f_lineno
    if day_add == True:
        msg = 'Test at line {0} was OK '.format(lineno)
    else:
        msg = 'Test at line {0} Failed '.format(lineno)
    print(msg)


def test_suite():
    test_day(day_add('Monday', 4) == "Friday")
    test_day(day_add('Tuesday', 0) == "Tuesday")
    test_day(day_add('Tuesday', 14) == "Tuesday")
    test_day(day_add('Sunday', 100) == "Tuesday")

test_suite()
# Collect day name and Capitilize the first character so as to match up with the algorithm
day_name = str(input("Please enter day in string, Today is what :")).title()
leave_day = int(input("When are you leaving, integer only, e.g. 4 ----"))
day_add(day_name, leave_day)
