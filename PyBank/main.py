import os
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    #previous_row = 1
    delta = []
    months = []
    pl = []
    for row in csvreader:
        months.append(row[0])
        pl.append(int(row[1]))
    #print(months)
    #print(pl)
    for row2 in range(len(pl)-1):
        delta.append(pl[row2+1]-pl[row2])
    maxPL = str(max(delta))
    minPL = str(min(delta))
    for row3 in range(len(delta)):
        month = str(months[row3+1])
        target = str(delta[row3])
        if target == maxPL:
            max_conc = (str(month) + " ($ " + target + ")")
        elif target == minPL:
            min_conc = (str(month) + " ($ " + target + ")")
    #print(max_conc)
    #print(min_conc)
    #print(delta)
    #Calculation for net profit/loss
    totalPL = sum(delta)
    #print(totalPL)
    #Average change in profit/loss over entire period
    avgPL = totalPL / len(delta)
    #print(avgPL)
    #Greatest increase in profit - date and amount - over the entire period
    #print(maxPL)
    #print(minPL)
    #Greastet decrease in losses - date and amount - over the entire period
    #Print out summary
    print(f"Total months: {len(months)}")
    print(f"Total: {totalPL}")
    print(f"Average change in profit/loss: {avgPL}")
    print(f"Greatest Increase in Profits: {max_conc}")
    print(f"Greatest Decrease in Profits: {min_conc}")