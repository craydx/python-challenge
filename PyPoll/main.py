#import os and csv modules
import os
import csv

winning_count=0
winning_cand=0
loosing_count=0
second_place=0
second_cand=0
secon_vote=0

#open csv file to read
election_data_csv = os.path.join('Resources','election_data.csv')
analysis = os.path.join('analysis','analysis.txt')
 


total_votes=0
candidate = []
candidate_votes_dict={}

#open csv file to read
with open(election_data_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    
#read first row (header)
    for row in (reader):
        candidate_name = row[2]
        total_votes+=1
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate:

            # Add it to the list of candidates in the running
            candidate.append(candidate_name)
            candidate_votes_dict[candidate_name]=0
    
        candidate_votes_dict[candidate_name] = candidate_votes_dict[candidate_name] + 1

        
#print (candidate_votes_list)
         
    for candidate in candidate_votes_dict:
        votes = candidate_votes_dict.get(candidate)   
     
        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_cand = candidate
        #Determin loosing candidate    
        elif (votes < winning_count):
             loosing_count = votes
             loosing_cand=candidate
        #Finish statement with true
        else: 1
     #find second place   
    for candidate in candidate_votes_dict:
        second_vote = candidate_votes_dict.get(candidate)
        
        if (second_vote < winning_count) and (second_vote > loosing_count):
            second_place = second_vote
            second_cand = candidate
                        

#from the above  use values to calc % of votes
total_percentage_charles = second_place/total_votes*100
total_percentage_diana = winning_count/total_votes*100
total_percentage_raymon = loosing_count/total_votes*100

total_percentage_charles = round(total_percentage_charles,3)
total_percentage_diana = round(total_percentage_diana,3)
total_percentage_raymon = round(total_percentage_raymon,3)
winner= max(total_percentage_charles,total_percentage_diana,total_percentage_raymon)
     
#print results in recommended format
print("Election Results")
print("--------------------------------")
print("total votes", total_votes)
print("--------------------------------")
print ("Charles Casper Stockham:",total_percentage_charles,"%","(",second_place,")")
print ("Diana DeGette:",total_percentage_diana,"%","(",winning_count,")")    
print ("Raymon Anthony Doane:",total_percentage_raymon,"%","(",loosing_count,")")
print("--------------------------------")
print("Winner:  ", winning_cand)

#save to file as analysis_Py_election
with open (analysis, 'w') as txt_file:
     
    txt_file.write ("Election Results\n")
    txt_file.write ("--------------------------------------\n") 
    txt_file.write ("total votes " + str(total_votes) +"\n")  
    txt_file.write ("--------------------------------------\n") 
    txt_file.write ("Charles Casper Stockham:" + str(total_percentage_charles)+"%"+" ("+ str(second_place)+")"+"\n")
    txt_file.write ("Diana DeGette:"+str(total_percentage_diana)+"%"+" ("+ str(winning_count)+")"+"\n")    
    txt_file.write ("Raymon Anthony Doane:"+str(total_percentage_raymon)+"%"+" ("+str(loosing_count)+")"+"\n")
    txt_file.write ("--------------------------------\n")
    txt_file.write ("Winner:  " + str(winning_cand)) 
