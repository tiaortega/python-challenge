import os
import csv

totalMonths = 0

with open("c:/Users/Tiaan/Homework/03-Python/python-challenge/PyBank/Resources/budget_data.csv") as file1:
    count = 0
    totalProfitLoss = 0
    totalChange = 0
    file1.readline()
    max = 0
    min = 0
    maxMonth = ""
    lastProfitLoss = 0
    while True: 
        line = file1.readline()
        col = line.split(",")
        if len(col) < 2:
            break
        thismonth = col[0]
        profitLoss = int(col[1])
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

