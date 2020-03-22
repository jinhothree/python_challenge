import os
import csv
from operator import itemgetter 
total_vote_count = 0
candidate_list = []
row_count = 0
candidate ={}
percent = {}
csvpath = os.path.join("election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    for row in csvreader:
        total_vote_count += 1
        candidate_list.append(row[2])
        if row[2] not in candidate:
            candidate[row[2]] = 1
        else:
            candidate[row[2]] = candidate[row[2]] + 1
    candidate = {name: float(vote) for name, vote in candidate.items()}
    total_vote_count = float(total_vote_count)
    for vote in candidate:
        cand_per = round((candidate[vote]/total_vote_count)*100,2)
        percent[vote] =  cand_per
    winner = max(candidate, key=candidate.get)
    unique_cand_name = set(candidate_list)
    sort_candidates = sorted(unique_cand_name)
    print("Total Vote: ", total_vote_count)
    for name in sort_candidates:
        print(name, percent[name],'%', candidate[name])
    print('Winner is ', winner)
    output_path = os.path.join("analysis.txt")
with open(output_path, "w+") as textfile:
    textfile.writelines("Election Results" + "\n")
    textfile.writelines("________________________" + "\n")
    for name in sort_candidates:
        textfile.writelines(name +' '+ str(percent[name])+'%'+" "+ str(candidate[name])+'\n')
    textfile.writelines("________________________" + "\n")
    textfile.writelines("Winner: "+ str(winner) + "\n")