def check_year(year):
    if(year % 4 == 0):
        if( year % 100 == 0):
            if(year % 400 == 0 ):
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a  leap year")
        else:
            print(f"{year} is  a  leap year")
    else:
        print(f"{year} is not a  leap year")

year=int(input("Enter the Year:"))
check_year(year)
"""
def check_year(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year = int(input("Enter the Year:"))
check_year(year)"""