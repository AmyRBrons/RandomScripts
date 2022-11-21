# This program imports and analyizes a set of data from a csv
# and returns the data as requested by the user. In this particular
# module there are five functions. The functions deliver a selection of
# data from the dataset.

# Amy Brons 20252295
# CISC ###


import databaseReader # import the data
    

"""
The displayInfo(electNum) function takes the electoral district number as a
parameter and returns the number of polling stations, valid ballots, ballots cast,
and voter turnout for that district.
"""
def displayInfo(electNum):
    # define the data set
    dataset = databaseReader.databaseDefine()
    # if the parameter exists, then for that location in the dataset, loop
    if electNum in dataset:
        for i in dataset:
            # if the selected dictionaries 3rd place is the same as the input,
            # return selected info
            if dataset[2:i] == electNum:
                print(" The number of polling stations in electoral district" , electNum, "is", dataset[5:i], " \n  \
                       The number of valid ballots in electorial district " , electNum, "is", dataset[6:i], "\n \
                       The number of total ballots cast in electoral district" , electNum, "is", dataset[10:i], "\n \
                       The percentage of voter turnout in electoral district  " , electNum, "is", dataset[11:i])

    #error catching
    else:
        print("Sorry this is not a valid electoral number")



"""
This function takes in a parameter of a province name and then returns a
list of districts within that province. 
"""
def uniqueDistricts(province):
    # define the data set
    dataset = databaseReader.databaseDefine()
    # empty list is intialized
    districts = []
    # if province is in the dataset, loop
    if province in dataset:
        for i in dataset:
            # if the province is the key, append all
            # district names to the empty list
            if dataset[0:i] == province:
                districts.append(dataset[1:i])
        return districts # return list
    #error catching
    else:
        print("Sorry this is not a valid province.")



"""
The findMax function returns the maximum value associated with a key. This
function takes an inputted key as the parameter.
"""        
def findMax(key):
    # define the data set
    dataset = databaseReader.databaseDefine()
    # if the key is in the data set, loop
    if key in dataset:
        # for all values on a key
        for i in dataset[key:i]:
            # return the max value
            result = max(i)
        return result

    # error catching
    else:
        print("Sorry, there is no max value for this key.")



"""
This function takes a key as the parameter, and returns the minimum
value associated on that key.
"""
def findMin(key):
    # define data set
    dataset = databaseReader.databaseDefine()
    # if the key is in the data set, loop
    if key in dataset:
        # for all values on a key
        for i in dataset[key:i]:
            # return the min value
            result = min(i)
        return result

    # error catching
    else:
        print("Sorry, there is no min value for this key.")
        


"""    
The totalVotes function returns the total votes for each province
wiithin the data set. The data set is put in as a parameter,
and 13 dictionaries are returned.
"""
def totalVotes(data):

    # if the data set is good, loop
    if data == True:

        # all vote counts are initialized
        abVotenum = 0
        qcVotenum = 0
        nflVotenum = 0
        nsVotenum = 0
        nbVotenum = 0
        peiVotenum = 0
        onVotenum = 0
        manVotenum = 0
        skVotenum = 0
        bcVotenum = 0
        ykVotenum = 0
        nwtVotenum = 0
        nvtVotenum = 0


        # initialize the dictionaries
        abVotesDict = {"Name":[], "Total Ballots Cast":[]}
        qcVotesDict = {"Name":[], "Total Ballots Cast":[]}
        nflVotesDict = {"Name":[], "Total Ballots Cast":[]}
        nsVotesDict = {"Name":[], "Total Ballots Cast":[]}
        nbVotesDict  = {"Name":[], "Total Ballots Cast":[]}
        peiVotesDict = {"Name":[], "Total Ballots Cast":[]}
        onVotesDict = {"Name":[], "Total Ballots Cast":[]}
        manVotesDict = {"Name":[], "Total Ballots Cast":[]}
        skVotesDict = {"Name":[], "Total Ballots Cast":[]}
        bcVotesDict = {"Name":[], "Total Ballots Cast":[]}
        ykVotesDict = {"Name":[], "Total Ballots Cast":[]}
        nwtVotesDict = {"Name":[], "Total Ballots Cast":[]}
        nunVotesDict = {"Name":[], "Total Ballots Cast":[]}
        
        # for each dictionary province name, loop
        for i in data[10:i]:

            # if the province is Alberta
            if i == "Alberta":
                # add votes to vote count
                abVotenum + data[10:i]
            
            # if the province is Quebec   
            if i == "Quebec":
                # add votes to vote count
                qcVotenum + data[10:i]

            # if the province Newfoundland and Labrador
            if i == "NewfoundlandLabrador":
                # add votes to vote count
                nflVotenum + data[10:i]
            
            # if the province Nova Scotia
            if i == "NovaScotia":
                # add votes to vote count
                nsVotenum + data[10:i]
                
            # if the province is New Brunswick
            if i == "NewBrunswick":
                # add votes to vote count
                nbVotenum + data[10:i]
                
            # if the province is PEI
            if i == "PrinceEdwardIsland":
                # add votes to vote count
                peiVotenum + data[10:i]
                
            # if the province is Ontario
            if i == "Ontario":
                # add votes to vote count
                onVotenum + data[10:i]
            
            # if the province is Manitoba    
            if i == "Manitoba":
                # add votes to vote count
                manVotenum + data[10:i]

            # if the province is Sakatchewan                
            if i == "Saskatchewan":
                # add votes to vote count
                skVotenum + data[10:i]
                
            # if the province is BC
            if i == "BritishColumbia":
                # add votes to vote count
                bcVotenum + data[10:i]
                
            # if the province is Yukon    
            if i == "Yukon":
                # add votes to vote count
                ykVotenum + data[10:i]

            # if the province is NWT                
            if i == "NorthwestTerritories":
                # add votes to vote count
                nwtVotenum + data[10:i]
                
            # if the province is Nunavut    
            if i == "Nunavut":
                # add to vote count
                nvtVotenum + data[10:i]


        # append to dict
        abVotesDict["Name"].append("Alberta")
        abVotesDict["Total Ballots Cast"].append(abVotenum)

        qcVotesDict["Name"].append("Quebec")
        qcVotesDict["Total Ballots Cast"].append(qcVotenum)

        nflVotesDict["Name"].append("Newfoundland and Labrador")
        nflVotesDict["Total Ballots Cast"].append(nflVotenum)

        nsVotesDict["Name"].append("Nova Scotia")
        nsVotesDict["Total Ballots Cast"].append(nsVotenum)

        nbVotesDict["Name"].append("New Brunswick")
        nbVotesDict["Total Ballots Cast"].append(nbVotenum)

        peiVotesDict["Name"].append("Prince Edward Island")
        peiVotesDict["Total Ballots Cast"].append(peiVotenum)

        onVotesDict["Name"].append("Ontario")
        onVotesDict["Total Ballots Cast"].append(onVotenum)

        manVotesDict["Name"].append("Manitoba")
        manVotesDict["Total Ballots Cast"].append(manVotenum)
        
        skVotesDict["Name"].append("Saskatchewan")
        skVotesDict["Total Ballots Cast"].append(skVotenum)

        bcVotesDict["Name"].append("British Columbia")
        bcVotesDict["Total Ballots Cast"].append(bcVotenum)
        
        ykVotesDict["Name"].append("Yukon")
        ykVotesDict["Total Ballots Cast"].append(ykVotenum)

        nwtVotesDict["Name"].append("Northwest Territories")
        nwtVotesDict["Total Ballots Cast"].append(nwtVotenum)
        
        nunVotesDict["Name"].append("Nunavut")
        nunVotesDict["Total Ballots Cast"].append(nvtVotenum)

        # print the updated 13 dictionaries
        print(abVotesDict, "\n", qcVotesDict, "\n", nflVotesDict,"\n", nsVotesDict, "\ ",
              nbVotesDict, "\n", peiVotesDict,"\n", onVotesDict, "\n", manVotesDict, "\ ", 
              skVotesDict, "\n", bcVotesDict, "\n", ykVotesDict, "\n", nwtVotesDict, "\n", nunVotesDict)

    # error catching
    else:
        print("Not a valid set of data.")
    
