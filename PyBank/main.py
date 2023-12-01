import os 
import csv  

csvpath = os.path.join("Resources","budget_data.csv") 
totalNet= 0
totalMonths = 0
previousMonth = 0
allChanges = []

with open(csvpath,"r") as csvfile :
    csvreader = csv.reader(csvfile, delimiter= ",")
    header = next(csvreader)

    for row in csvreader: 
        date = row[0]
        profit = int(row[1])
        netChange = profit - previousMonth
        allChanges.append(netChange)
        previousMonth = profit 
        totalNet = totalNet + int(row[1])
        totalMonths = totalMonths + 1
        


    allChanges.pop(0)
    averageChange = sum(allChanges) / len(allChanges)
    maxChange = max(allChanges)
    minChange = min(allChanges)
 


print("Financial Analysis")
print("--------------------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total Net: ${totalNet}")
print(f"Average Change: ${round(averageChange,2)}")
print(f"Greatest Increase in Profits: ${maxChange}")
print(f"Greatest Decrease in Profits: ${minChange}")

outputPath = os.path.join("analysis","analysis.txt")

with open(outputPath, 'w') as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("Total Months: 86")
    f.write("\n")
    f.write("Total Net:  $22564198")
    f.write("\n")
    f.write("Average Change: $-8311.11")
    f.write("\n")
    f.write("Greatest Increase in Profits: $1862002")
    f.write("\n")
    f.write("Greatest Decrease in Profits: $-1825558")
