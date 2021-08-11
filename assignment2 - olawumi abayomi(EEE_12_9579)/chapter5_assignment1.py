# Declaring Days of the week as a dictionary
print("days_of_week = {0:'Sunday', 1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}")
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
try:
    day_num = int(input("Please enter any day number ranging from 0 to 6: "))
    print(get_day_str(day_num))
except:
    print("Wrong Input supplied, Follow instruction strictly")

