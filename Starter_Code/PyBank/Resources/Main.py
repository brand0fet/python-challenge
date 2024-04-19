import os
import csv

budget_csv = os.path.join("budget_data.csv")
# make the values we want into lists so we can just add the data into them
# when we go through the csv file
months = []
prof = []
month_prof = []
avg_change = 0
max_month = 0
min_month = 0
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ",")
    # skipping the header to move onto the next rows with data
    header = next(csv_reader)
    for row in csv_reader:
#want to go through row 0 to get the months and row 1 for the numbers for the profit 
        months.append(row[0])
        prof.append(int(row[1]))


# here is what i got help from the learning assistant 
# i changed it around and used the found funciton to match the data needed
# also created an empty list where I can store the number i found for the avg
    for row in range(len(prof)-1):
        month_prof.append(prof[row+1]-prof[row])


#here i used max and min to find the max profit in months and the min
# since we did -1 in the formual to find the month_prof in order to find the coressponding month
# we would need to go to the months list and index it by +1
max_prof = max(month_prof)
min_prof = min(month_prof)
max_ = (month_prof.index(max(month_prof)) +1)
min_ = (month_prof.index(min(month_prof)) +1)
avg_change = round((sum(month_prof)/(len(month_prof))),2)

# i saw that it was returning numbers when i would call max_ and min_ so i did the index of months with the coressponding number and it returned the right date
max_month = months[max_]
min_month = months[min_]

print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {len(months)}")
print(f'Total: ${sum(prof)}')
print(f"Average Change: ${avg_change}")
print(f'Greatest Increase in Profits: {max_month} (${max_prof})')
print(f'Greatest Decrease in Profits: {min_month} (${min_prof})')

print("Financial Analysis", file =open("PyBank.txt","a"))
print(("-----------------------"), file =open("PyBank.txt","a"))
print((f"Total Months: {len(months)}"), file =open("PyBank.txt","a"))
print((f'Total: ${sum(prof)}'), file =open("PyBank.txt","a"))
print((f"Average Change: ${avg_change}"), file =open("PyBank.txt","a"))
print((f'Greatest Increase in Profits: {max_month} (${max_prof})'), file =open("PyBank.txt","a"))
print((f'Greatest Decrease in Profits: {min_month} (${min_prof})'),file =open("PyBank.txt","a"))