#Terrence Cummings
#03-Python Honework
#PyPoll exercise

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")

# Read each row of data after the header
#Initialize counter and tracker variables to null
    num_votes = 0
  
# candidate dictionary in form {name: [votes, pct]}
    candidate_dict = {}

#for each vote
    for row in csvreader:
        vote_for = row[2]
        if vote_for not in candidate_dict:
            candidate_dict[vote_for] = [1, 0]
        else:
            candidate_dict[vote_for] = [candidate_dict[vote_for][0]+1, 0]
            
        num_votes = num_votes+1
    
    for candidate in candidate_dict:
        pct_vote = candidate_dict[candidate][0]/num_votes
        candidate_dict[candidate][1]=pct_vote

#print table to terminal and file
    f= open("PyPoll.txt", "w+")
    print("Election Results")
    f.write("Election Results\r\n")
    print("---------------------------------")
    f.write("---------------------------------\r\n")
    print("Total Votes: "+str(num_votes))
    f.write("Total Votes: "+str(num_votes)+"\r\n")
    print("---------------------------------")
    f.write("---------------------------------\r\n")
#set tracker variable to find winner    
    winner_count = 0
    for candidate in candidate_dict:
        #extract total vote and pct vote from dict list for the candidate
        cand_pct_vote = candidate_dict[candidate][1]
        cand_tot_vote = candidate_dict[candidate][0]
        #find winner
        if cand_tot_vote > winner_count:
            winner = candidate
            winner_count = cand_tot_vote
        print(candidate+": "+'{:.3%}'.format(cand_pct_vote)+" ("+str(cand_tot_vote)+")")
        f.write(candidate+": "+'{:.3%}'.format(cand_pct_vote)+" ("+str(cand_tot_vote)+")\r\n")
    print("---------------------------------")
    f.write("---------------------------------\r\n")
    print("Winner: "+winner)
    f.write("Winner: "+winner+"\r\n")
    print("---------------------------------")
    f.write("---------------------------------\r\n")
    f.close()

