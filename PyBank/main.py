import os
import csv

budget_path = "Resources/budget_data.csv"

with open(budget_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print (header)
    totalMonths = 0    
    count = 1
    totalProfitLoss = 0
    totalChange = 0
    max = 0
    min = 0
    maxMonth = ""
    lastProfitLoss = 0
    for row in csvreader:
        if len(row) < 2:
            break
        thismonth = row[0]
        profitLoss = int(row[1])

        changeProfitLoss = profitLoss - lastProfitLoss
        if changeProfitLoss > max:
            max = changeProfitLoss 
            maxMonth = thismonth
        if changeProfitLoss < min:
            min = changeProfitLoss
            minMonth = thismonth
        totalChange = totalChange + changeProfitLoss
        totalProfitLoss = totalProfitLoss + profitLoss
        #print("Line{}: {}".format(count, line.strip())) 
        count += 1
        lastProfitLoss = profitLoss
  
totalMonths=count-1
averageChange = (max - min) / (totalMonths-1) 
print("Financial Analysis")
print("----------------------------")
print("Total Months: " +str(totalMonths))
print("Total: $" + str(totalProfitLoss))
print("Average Change: $" + str(averageChange))
print("Greatest Increase in Profits: "+maxMonth+" ($" + str(max) + ")")
print("Greatest Decrease in Profits: "+minMonth+" ($" + str(min) + ")")

