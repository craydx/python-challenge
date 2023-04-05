#import os and csv modules
import os
import csv

counter = 0
numbers = 0
avg = 0
increase_profit = 0
decrease_profit = 0
average_change=0
change_row=0
total_change=0
total=0
numbers = []

#open csv file to read
budget_data_csv = os.path.join('Resources','budget_data.csv')
analysis = os.path.join('analysis','analysis.txt')

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Read the header row
    header = next(reader) 

#Average change per month, add a month list to find min and max and add counter
monthly_profits=[]
month = []
with open(budget_data_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader) 
    for row in (reader):
        monthly_profits.append(int(row[1]))
        month.append(row[0])
        counter = counter +1
        
#find the monthly changes        
monthly_changes=[]
for i in range(1, 1+len(monthly_profits[1:])):
    difference = monthly_profits[i] - monthly_profits[i-1]
    monthly_changes.append(difference)
     
    
total = 0
for d in monthly_changes:
    total = total + d
    average_change = round(total/len(monthly_changes),2)
    
#find the max and min months using a list 
maxmonthindex = monthly_changes.index(max(monthly_changes))
Max_Month = month[maxmonthindex +1]
minmonthindex = monthly_changes.index(min(monthly_changes))
Min_Month = month[minmonthindex +1]
        
#Print Financial Analysis
print ("Financial Analysis")
print ("--------------------------------------")

#print totals 
print("Total Months:   ", counter)
print("Total:  $",(sum(monthly_profits)))
print("Average Change:  $", average_change )
print("Greatest Increase in Profits: ",(Max_Month),"($",max(monthly_changes),")")
print("Greatest Decrease in Profits: ",(Min_Month),"($",min(monthly_changes),")")

with open (analysis, 'w') as txt_file:
     
    txt_file.write ("Financial Analysis\n")
    txt_file.write ("--------------------------------------\n") 
    txt_file.write ("Total Months:   " + str(counter)+'\n')
    txt_file.write ("Total:  $" + str(sum(monthly_profits))+'\n')
    txt_file.write ("Average Change:  $" + str(average_change)+'\n')
    txt_file.write("Greatest Increase in Profits: " + str(Max_Month) + " ($" + str(max(monthly_changes)) + ")" + "\n")
    txt_file.write ("Greatest Decrease in Profits: " +str((Min_Month)+" ($"+str(min(monthly_changes)))+")")



