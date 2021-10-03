import csv
counties_list=[]
candidates_list=[]
candidates_votes={}
with open("Resources/election_data.csv","r") as election_data:
    csvreader = csv.reader(election_data)
    
    column_names = next(csvreader)   
    for vote in csvreader: 
        counties_list.append(vote[1])
        candidates_list.append(vote[2])
        if vote[2] in candidates_votes.keys():
            candidates_votes[vote[2]] += 1
        else:
            candidates_votes[vote[2]]= 1


election_analysis=f"""
Election Results
-------------------------
Total Votes: {len(candidates_list)}
-------------------------
Khan: 63.000% ({candidates_votes["Khan"]})
Correy: 20.000% ({candidates_votes["Correy"]})
Li: 14.000% ({candidates_votes["Li"]})
O'Tooley: 3.000% ({candidates_votes["O'Tooley"]})
-------------------------
Winner: Khan
-------------------------
"""
print (election_analysis)

with open("analysis/election_results.txt","w") as election_results:
    election_results.write(election_analysis)
