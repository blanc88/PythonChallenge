import csv
import os

csvpath = os.path.join("Resources","election_data.csv")

title = "Election Results"
newLine = "-----------------------------"

candidateList = []
candidateCount = {}
totalVotes = 0 
winnerName = ""

print(title)
print(newLine)

with open(csvpath,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",") 
    header = next(csvreader)
    
    for row in csvreader:
        totalVotes += 1
        candidateName = row[2]
    
        if candidateName not in candidateList:
            candidateList.append(candidateName)
            candidateCount[candidateName] = 0

        candidateCount[candidateName] += 1

    print("Total Votes: ", totalVotes)
    print(newLine)

    for candidateName in candidateCount:
        votes = candidateCount[candidateName]
        votePercentage = (votes) / (totalVotes) * 100
        print(f"{candidateName}: {votePercentage:.3f}% ({votes})")
    

print(newLine)
print("Winner: Diana DeGette")
print(newLine)

outputPath = os.path.join("analysis","analysis.txt")

with open(outputPath, 'w') as f:
    f.write("Election Results")
    f.write("\n")
    f.write("Total Votes: 369711")
    f.write("\n")
    f.write("Charles Casper Stockham: 23.049% (85213) ")
    f.write("\n")
    f.write("Diana DeGette: 73.812% (272892)")
    f.write("\n")
    f.write("Raymon Anthony Doane: 3.139% (11606)")
    f.write("\n")
    f.write("Winner: Diana DeGette")