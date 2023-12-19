month=int(input())
if month==2:
    year=int(input("Enter the Year:"))
    if(year%4==0 and (year%100!=m m  0 or year%400==0)):
        print("29days")
    else:
        print("28days")
else:
    month_30=(4,6,9,11)
    month_31=(1,3,5,7,8,10,12)
    if month in month_30:
        print("30 days")
    elif month in month_31:
        print("31days")
    else:
        print("Invalid month")
        
