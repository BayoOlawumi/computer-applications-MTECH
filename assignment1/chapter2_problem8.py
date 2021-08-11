print("________________Question 8___________________")
t_now = input("Enter the time now in hours in 24-hour clock, e.g 2pm as 14, 8am as 8: ")
# cast the received value to integer
t_now = int(t_now)
# Ensure the 24-hour constraint is maintained
if(t_now>24):
    print("The time now entered is invalid")
else:
    t_wait = input("Enter the number of hours to wait: ")
    t_wait = int(t_wait)
    t_sum = t_wait + t_now
    # When the number of hours exceed 24 hours
    if t_sum > 24:
        t_sum_left = t_wait - (24 - t_now)
        t_days = t_sum_left // 24
        t_remainder = t_sum_left % 24
        if t_remainder > 12:
            t_remainder = str(24 - t_remainder) + "pm"
        else:
            t_remainder = str(t_remainder) + "am"
        print ("The alarm will go off in {0} days's time by {1}".format(t_days+1,t_remainder))
    # When the number of hours is within the same day
    elif t_sum <= 24:
        t_remainder = t_sum
        if t_remainder > 12:
            t_remainder = str(24 - t_remainder) + "pm"
        else:
            t_remainder = str(t_remainder) + "am"
        print ("The alarm will go off {0} today".format(t_remainder))