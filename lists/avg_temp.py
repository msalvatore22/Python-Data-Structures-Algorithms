numDays = int(input("How many day's temperature? "))
total = 0
temps = []
for i in range(numDays):
    nextDay =  int(input("Day " + str(i) + "'s high temp:"))
    temps.append(nextDay)
    total += temps[i]

avg = round(total/numDays, 2)
print("\nAverage = " + str(avg))
above = 0

for i in temps:
    if i > avg:
        above += 1
print(str(above) + " day(s) above avergage.")
