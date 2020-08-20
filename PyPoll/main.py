import os
import csv

election_path = "Resources/election_data.csv"
votes = {}   
with open(election_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print (header)
    totalVotes = 0    
 
    for row in csvreader:
        if len(row) < 3:
            break
        candidate = row[2]
        if candidate in votes:
            votes[candidate]=votes[candidate]+1
        else:
            votes[candidate]=1

        totalVotes = totalVotes + 1


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")
maxVotes = 0
winner = "n/a"
for k in votes:
    percent = round((votes[k] / totalVotes)*100,0)
    if(votes[k] > maxVotes):
        maxVotes = votes[k]
        winner = k
    print(k + ": " + str(percent) + "00% (" + str(votes[k])+")" )
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")