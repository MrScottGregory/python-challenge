# import os and csv modules
import os
import csv
import operator

# connect to data
election_data = os.path.join('..', 'Resources', 'election_data.csv')
#election_data = '../Resources/election_data.csv'


with open(election_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # >> test point >> print(f"CSV Header: {csv_header}")

    # set variable to hold row count and start at 0
    total_votes = 0
    # set variables to hold vote counts for each candidate
    Khan_total = 0
    Correy_total = 0
    Li_total = 0
    OTooley_total = 0
    # establish set to hold candidate names
    unduplicated_candidates = set()
    
    # -----------------------------------------------------------------------------------------------
    # TASK #1 calculate total number of votes cast
    # -----------------------------------------------------------------------------------------------

    # loop through each row
    for row in csvreader:
        # add 1 for each row in loop (total # of row = total votes)
        total_votes = total_votes + 1
    # >> test point >> print(total_votes)

    # -----------------------------------------------------------------------------------------------
    # TASK #2 generate list unique list of candidates
    # -----------------------------------------------------------------------------------------------

        # while looping through rows, begin to add candidate names to set 
        # (as a set, it will only add unique names)  
        unduplicated_candidates.add(row[2]) 
     # >> test point >> print(unduplicated_candidates)

    # -----------------------------------------------------------------------------------------------
    # TASK #3 number of votes each candidate won
    # -----------------------------------------------------------------------------------------------

        # create a conditional that looks for an index with each candidate name 
        if row[2] == "Khan":
            # and then increment their vote count
            Khan_total = Khan_total +1
        
        elif row[2] == "Correy":
            Correy_total = Correy_total +1

        elif row[2] == "Li":
            Li_total = Li_total +1

        elif row[2] == "O'Tooley":
            OTooley_total = OTooley_total +1

    # >> test point >> print(Khan_total)
        
    # -----------------------------------------------------------------------------------------------
    # TASK #4 percentage of votes each candidate won
    # -----------------------------------------------------------------------------------------------

        # divide each candidates total by total_votes
        Khan_precent = (Khan_total / total_votes) * 100
        Correy_percent = (Correy_total / total_votes) * 100
        Li_percent = (Li_total / total_votes) * 100
        OTooley_percent = (OTooley_total / total_votes) * 100
    
     # >> test point >> print(f'{Khan_precent:.3f}')

    # -----------------------------------------------------------------------------------------------
    # TASK #5 identify the winner of the election
    # -----------------------------------------------------------------------------------------------

        # create a dictionary with candidate vote percentages and totals
        election_dict = {
                        "Khan": [Khan_precent, Khan_total],
                        "Correy": [Correy_percent, Correy_total],
                        "Li": [Li_percent, Li_total],
                        "O'Tooley": [OTooley_percent, OTooley_total]
                        }
    # >> test point >> print(election_dict)
    
        # run max function to identify key in dict corresponding to max value 
        winner = max(election_dict.items(), key=operator.itemgetter(1))[0]
    # >> test point >> print(winner)

    # -----------------------------------------------------------------------------------------------
    # TASK  # 6 print election results to terminal  
    # -----------------------------------------------------------------------------------------------

    print("Election Results\n")
    print("---------------------------------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print("---------------------------------------------------\n")
    print(f'Khan: {Khan_precent:.3f}% {Khan_total}\n')
    print(f'Correy: {Correy_percent:.3f}% {Correy_total}\n')
    print(f'Li: {Li_percent:.3f}% {Li_total}\n')
    print(f"O'Tooley: {OTooley_percent:.3f}% {OTooley_total}\n")
    print("---------------------------------------------------\n")
    print(f'Winner: {winner}\n')

    # -----------------------------------------------------------------------------------------------
    # TASK  # 7 print election results to new txt file  
    # -----------------------------------------------------------------------------------------------

    file = open("PyPollResults.txt", "w+")

    file.write("Election Results\n")
    file.write("---------------------------------------------------\n")
    file.write(f'Total Votes: {total_votes}\n')
    file.write("---------------------------------------------------\n")
    file.write(f'Khan: {Khan_precent:.3f}% ({Khan_total})\n')
    file.write(f'Correy: {Correy_percent:.3f}% ({Correy_total})\n')
    file.write(f'Li: {Li_percent:.3f}% ({Li_total})\n')
    file.write(f"O'Tooley: {OTooley_percent:.3f}% ({OTooley_total})\n")
    file.write("---------------------------------------------------\n")
    file.write(f'Winner: {winner}\n')