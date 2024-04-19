import os
import csv

election = os.path.join("election_data.csv")
#creating empty lists we can use later on to get the count of each column
votes_total = []
vote_getters = []
votes_per = []
per = []
#reading file
with open(election) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter= ',')
    header = next(csv_reader)
# i had help from the learning assistant on how to make the rows of the csv file a number to iteriate by
# but I changed it a little to make a list of the reader itself and then got the lenght of the list and made it into a number
    election_data = list(csv_reader)
    rows = len(election_data)
    count = []
# here i am just counting up how many people voted
    for row in csv_reader:
        votes_total.append(row[0])
        rows = len(votes_total)
#here we are loopoing for each row in rows and having names be all the names of the csv file
#then we are adding all the name of the names in vote_getters into names_count
#then we loop through names and taking only the names that show up once and then only adding those names so no dupllicates
    for row in range(0,rows):     
        names = election_data[row][2]
        count.append(vote_getters)
        if names not in  vote_getters:
            vote_getters.append(names)
    num_candi = len(vote_getters)


print("ELection Results")
print("-----------------------")
print(f"Total Votes: {rows}")
print("-----------------------")
print(f'{vote_getters[0]}')
print(f'{vote_getters[1]}')
print(f'{vote_getters[2]}')


print(("ELection Results"), file =open("PyBank.txt","a"))
print(("-----------------------"),file =open("PyBank.txt","a"))
print((f"Total Votes: {rows}"),file =open("PyBank.txt","a"))
print(("-----------------------"),file =open("PyBank.txt","a"))
print((f'{vote_getters[0]}'),file =open("PyBank.txt","a"))
print((f'{vote_getters[1]}'),file =open("PyBank.txt","a"))
print((f'{vote_getters[2]}'),file =open("PyBank.txt","a"))