import calendar

def printMonthCalendar () :
    i = 1
    while i< 13 :
        cal = calendar.month(2019,i)
        print cal
        i = i+1


def my_own_function (str) :
    print 'Im in the function'
    cal = calendar.month(2019,2)
    print 'printing february \n' + cal