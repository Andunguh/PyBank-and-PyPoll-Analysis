import csv
months_list=[]
values_list=[] 
differences_list=[]

with open("Resources/budget_data.csv","r") as budget_data:
    csvreader = csv.reader(budget_data)
    
    column_names = next(csvreader)   
    for row in csvreader: 
        
        months_list.append(row[0])
        values_list.append(int(row[1]))

for index ,value in enumerate(values_list):
    if index ==0:
        differences_list.append(0)
    else:
        differences_list.append(value-values_list[index-1])

financial_analysis=f"""
Financial Analysis
----------------------------
Total Months: {len(months_list)}
Total: ${sum(values_list)}
Average  Change: ${round(sum(differences_list)/len(differences_list),3)}
Greatest Increase in Profits: {months_list[differences_list.index(max(differences_list))]} (${max(differences_list)})
Greatest Decrease in Profits: {months_list[differences_list.index(min(differences_list))]} (${min(differences_list)})
"""

print (financial_analysis)

with open("analysis/budget_analysis.txt","w") as budget_analysis:
    budget_analysis.write(financial_analysis)
