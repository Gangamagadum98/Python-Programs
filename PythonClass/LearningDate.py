import datetime
# current date
currDate=datetime.datetime.now()
print(currDate)

#Previous date
# prevDate = datetime.datetime(2019,5,12)

#dates
date=currDate.strftime("%A")
month=currDate.strftime("%m")
year=currDate.strftime("%Y")

#Timings
hour= currDate.strftime("%H")
min = currDate.strftime("%M")
sec = currDate.strftime("%S")

print(currDate.strftime("%m/%d/%Y  %H:%M"))

print(currDate.strftime("%b-%A-%Y"))

# %b-jan, %B-January, %a-sun, %A-sunday, %H-Hour, %m-month, %M-mins, %S-sec, %d-date

#Casting
x=1.5
print(int(x))
print(float(1))
print(int("25"))
print(type(str(45)))
print(float("89"))