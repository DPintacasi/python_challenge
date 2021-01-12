import os
import csv

filepath = os.path.join("resources","election_data.csv")

with open(filepath, 'r') as election_data_file:

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
    
    winning_count = max(candidate_vote_count)
    winner = candidate_list[candidate_vote_count.index(winning_count)]
    
    #print results
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {len(votes)}")
    print("------------------------")
    for c in range(len(candidate_list)):
        print(f"{candidate_list[c]}: {round(candidate_vote_count[c]*100/len(votes),2)}% ({candidate_vote_count[c]})")
    print("------------------------")
    print(f"Winner: {winner}")
    print("------------------------")



    

    

    
    

    
     