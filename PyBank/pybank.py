import csv

with open("Resources/budget_data.csv","r") as budget_data:
    csvreader = csv.reader(budget_data)
    total_months=0
    column_names = next(csvreader)   
    for row in csvreader: 
        print(row)
        total_months=total_months+1 


financial_analysis=f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
"""
print (financial_analysis)

with open("analysis/budget_analysis.txt","w") as budget_analysis:
    budget_analysis.write(financial_analysis)
