import csv

with open("Resources/election_data.csv","r") as election_data:
    csvreader = csv.reader(election_data)
    total_votes=0
    column_names = next(csvreader)   
    for row in csvreader: 
        total_votes=total_votes+1 


election_analysis=f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
"""
print (election_analysis)

with open("analysis/election_results.txt","w") as election_results:
    election_results.write(election_analysis)
