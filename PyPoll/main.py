import os
import csv

total_votes = 0
candidate_list = []
dict = {}

election_csv = os.path.join("Resources", "election_data.csv")
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)


    for row in csvreader:
        name = row[2]
        if name not in candidate_list:
            candidate_list.append(row[2])
            dict[name] = 1
        else:
            dict[name]+=1

#Total votes
total_votes = sum(dict.values()) 
# print(total_votes)
#Percent of votes by each candidate
percent_Correy = round((dict["Correy"] / total_votes) * 100, 3)
total_Correy = dict["Correy"]
# print(percent_Correy)
# print(total_Correy)
percent_Khan = round((dict["Khan"] / total_votes) * 100, 3)
total_Khan = dict["Khan"]
# print(percent_Khan)
# print(total_Khan)
percent_Li = round((dict["Li"] / total_votes) * 100, 3)
total_Li = dict["Li"]
# print(percent_Li)
# print(total_Li)
percent_OTooley = round((dict["O'Tooley"] / total_votes) * 100, 3)
total_OTooley = dict["O'Tooley"]
# print(percent_OTooley)
# print(total_OTooley)
#Winner
max_key = max(dict, key=lambda k: dict[k])
# print(max_key)
print("Election Results")
print(f"Total Votes: {total_votes}")
print(f"Khan: {percent_Khan}% ({total_Khan})")
print(f"Correy: {percent_Correy}% ({total_Correy})")
print(f"Li: {percent_Li}% ({total_Li})")
print(f"O'Tooley: {percent_OTooley}% ({total_OTooley})")
print(f"Winner: {max_key}")