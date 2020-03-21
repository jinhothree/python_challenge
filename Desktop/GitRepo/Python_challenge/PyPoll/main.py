import os
import csv
from operator import itemgetter 
vote_list = []
candidate_list = []
row_count = 0
khan_vote = []
correy_vote = []
li_vote = []
tool_vote = []
#Set up the csv reader
csvpath = os.path.join("election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    for row in csvreader:
#Count the total number of votes
        vote_list.append(row[1])
#Store all the values in the "Candidate" into a list
        candidate_list.append(row[2])
#Store vote count for each candidates
        if row[2] == "Correy":
            correy_vote.append(row[2])
        elif row[2] == "Khan":
            khan_vote.append(row[2])
        elif row[2] == "Li":
            li_vote.append(row[2])
        elif row[2] == "O'Tooley":
            tool_vote.append(row[2])
#Find the names of the candidates
candidates = set(candidate_list)
sort_candidates = sorted(candidates)
#Find the total number of votes
total_vote = len(vote_list)
#Find the vote count for each candidate
khan_total = len(khan_vote)
correy_total = len(correy_vote)
li_total = len(li_vote)
tool_total = len(tool_vote)
#Find the percentage of votes gained for each candidates
khan_per = round((khan_total/total_vote)*100,2)
correy_per = round((correy_total/total_vote)*100, 2)
li_per = round((li_total/total_vote)*100,2)
tool_per = round((tool_total/total_vote)*100,2)
#Find the winner
tally = [{"Name":"Correy" , "Vote":correy_total},{"Name":"Khan" , "Vote": khan_total},
{"Name":"Li" , "Vote":li_total},{"Name":"O'Tooley" , "Vote":tool_total}]
sort_tally = sorted(tally, key=itemgetter('Vote'),reverse = True) 
winner = sort_tally[0]
#Printing the total vote
print("Total Votes: ", total_vote)
#Printing the summary table. 
# a) Can I sort it the table by the most popular vote?
# b) Is this hard coding????
print(sort_candidates[0],':', correy_per,'%', '(',correy_total, ')')
print(sort_candidates[1],':', khan_per,'%','(', khan_total, ')')
print(sort_candidates[2], ':',li_per,'%', '(',li_total, ')')
print(sort_candidates[3], ':',tool_per ,'%','(',tool_total, ')')
print("Winner: ", winner)
#Write the result on a text file
output_path = os.path.join("analysis.txt")
with open(output_path, "w+") as textfile:
    textfile.writelines("Election Results" + "\n")
    textfile.writelines("________________________" + "\n")
    textfile.writelines(sort_candidates[0]+':'+ str(correy_per)+'%'+ '('+str(correy_total)+')'+ "\n")
    textfile.writelines(sort_candidates[1]+':'+ str(khan_per)+'%'+'('+ str(khan_total)+ ')'+ "\n")
    textfile.writelines(sort_candidates[2]+ ':'+str(li_per)+'%'+ '('+str(li_total)+ ')'+ "\n")
    textfile.writelines(sort_candidates[3]+ ':'+str(tool_per) +'%'+'('+str(tool_total)+')'+ "\n")
    textfile.writelines("________________________" + "\n")
    textfile.writelines("Winner: "+ str(winner) + "\n")