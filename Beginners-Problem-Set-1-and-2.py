def convert_minutes_to_seconds():
    minutes = int(input("Enter an integer in minutes: "))
    
    seconds = minutes * 60
    
    print(f"{seconds} seconds")

convert_minutes_to_seconds()

example 2 ->

def converting_age_to_days():
   
    age_years = int(input("Enter  age in years: "))
    

    age_days = age_years * 365
    

    print(f"You are {age_days} days old.")
    

    days_to_100 = (100 - age_years) * 365
    print(f"In {days_to_100} days you will be 100 years old!")


converting_age_to_days()
