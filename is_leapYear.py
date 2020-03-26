#determines if a year is a leap year or not

def is_leap(year):
    leap = False
    
    if(year%4==0):

        if(year%100 != 0):

            return True
        elif(year%400==0):
            
            return True
        else:
            return leap

    return leap


year = int(raw_input())
print is_leap(year)
