year = int(input("Enter the year (1901 to 2099): "))
month = int(input("Choose a month: "))
day = int(input("Choose a day from the given month: "))
dict_month = {1:[31,"January"],2:[28,"February"],3:[31,"March"],4:[30,"April"],5:[31,"May"],6:[30,"June"],7:[31,"July"],8:[31,"August"],9:[30,"September"],10:[31,"October"],11:[30,"November"],12:[31,"December"]}
week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

temp = 0
for i in range(1,month):
    temp += dict_month[i][0]
total_days = (year - 1900)*365 + (year - 1900)//4  + temp
if ((year - 1900)%4 == 0):
    dict_month[2][0] = 29
    if month in (1,2):
        total_days -= 1
number_of_days_of_pre_month = total_days % 7

print("{:^28}".format(dict_month[month][1] + " " + str(year)))
for i in week:
    print("{:>4}".format(i),end="")
print()
count = 0
for i in range(-number_of_days_of_pre_month,dict_month[month][0]):
    if i+1 <= 0:
        print("{:>4}".format(" "),end="")
        count += 1
        continue
    print("{:>4}".format("*" + str(i+1) if i+1 == int(day) else str(i+1)),end="")
    count += 1
    if count == 7:
        count = 0
        print()











