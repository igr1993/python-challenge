
#lets go PyPoll! 

import os
import csv

candidates = {}

election_csv = os.path.join('.','Resources','election_data.csv')
with open(election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else:
            candidates[row[2]] = 1

        total = candidates.values()
        total_votes = sum(total)

            
        list_candidates = candidates.keys()
            
        votes_per = [f'{(x/total_votes)*100:.3f}%' for x in candidates.values()]
            

        winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        winner
        


print("Election results")

print("--------------------------------")

print(f" Total votes: {int(total_votes)}")

print("---------------------------------")
i = 0
for candidate, vote in candidates.items():
    print(f'{candidate}, {vote} , {votes_per[i]}') 
    i+=1
print("------------------------------")

print(f" Winner: {winner}")

print("------------------------------")