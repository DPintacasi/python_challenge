#import modules
import os
import csv

#make file path
filepath_input = os.path.join("resources","election_data.csv")

#extract data
with open(filepath_input, 'r') as election_data_file:

    data = csv.reader(election_data_file, delimiter = ",")
    data_header = next(data)

    #extract votes
    votes = []

    for row in data:
        votes.append(row[2])

    #build candidate list and count votes
    candidate_list = []
    candidate_vote_count = []
    
    for vote in votes:
        if vote not in candidate_list:
             candidate_list.append(vote)
             candidate_vote_count.append(int(1))
        else:
            candidate_vote_count[candidate_list.index(vote)] = candidate_vote_count[candidate_list.index(vote)] + 1
    
    #zip cadidate and vote count together
    results = zip(candidate_list,candidate_vote_count)

    #search for winner
    winning_count = max(candidate_vote_count)
    winner = candidate_list[candidate_vote_count.index(winning_count)]

#print results
print("------------------------")
print("Election Results")
print("------------------------")
print(f"Total Votes: {len(votes)}")
print("------------------------")
for row in results:
    print(f"{row[0]}: {round(row[1]*100/len(votes),2)}% ({row[1]})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

#write results to file
filepath_output = os.path.join("analysis","election_analysis.txt")

with open(filepath_output, "w") as analysis:
    analysis.write("------------------------\n")
    analysis.write("Election Results\n")
    analysis.write("------------------------\n")
    analysis.write(f"Total Votes: {len(votes)}\n")
    analysis.write("------------------------\n")
    for c in range(len(candidate_list)):
        analysis.write(f"{candidate_list[c]}: {round(candidate_vote_count[c]*100/len(votes),2)}% ({candidate_vote_count[c]})\n")
    analysis.write("------------------------\n")
    analysis.write(f"Winner: {winner}\n")
    analysis.write("------------------------\n")

#for csv file 
# with open(filepath_output, "w", newline = "") as election_analysis:

#     analysis = csv.writer(election_analysis, delimiter=',')

#     analysis.writerow(["Election Results"])
#     analysis.writerow(["Total Votes",len(votes)])
#     analysis.writerow(["candidate","percentage of votes", "no. of votes"])
#     for c in range(len(candidate_list)):
#         analysis.writerow([candidate_list[c],f"{round(candidate_vote_count[c]*100/len(votes),2)}%",candidate_vote_count[c]])
#     analysis.writerow(["Winner", winner])
    









    

    

    
    

    
     