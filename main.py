from teamFile import updateMainFile, findTeamID
from filter import filterRecent, filterRanked
from reformat import reformatRecent
from sorting import sortTeams
from update import updateRankedFile, isFilled

settings = open("settings.txt")

settingContents = settings.readlines()
maxYear = int(settingContents[0])
print("Max Year: " + str(maxYear))

settings.close()

def menu():
    print("Hello! Welcome to my HLTV Team Database Manager! What would you like to do today?\n")
    print("a) Update Teams File")
    print("b) Filter Recent Teams")
    print("c) Filter Ranked Teams")
    print("d) Change the Max Year for Recent Matches")
    print("e) Sort the Ranked Teams")
    print("f) Update Ranks")
    print("z) Testing Commands")
    print("q) Quit")
    print("--Input Choice Below--")

# Menu Handling
try:
    menu()
    commandChoice = input()

    if(len(commandChoice) != 1): # Checks for if multiple characters are pressed
        raise ValueError("Must be only one letter input")
    
    if(not commandChoice.isalpha()): # Checks for if input isn't alphanumeric
        raise ValueError("Must be only apart of alphabet")


    while(commandChoice != 'q'):
        # Case a (Updates Teams File)
        if(commandChoice.lower() == 'a'):
            teamFile = open("teamFile.txt", 'a')

            # Takes input for data range
            print("Input Starting Team ID:")
            start = int(input())
            if(start < 1): # Throws exception if start is less than or equal to 0
                raise ValueError("Can't be a value 0 or less")

            print("Input Ending Team ID:")
            end = int(input())
            if(end < 1): # Throws exception if end is less than or equal to 0
                raise ValueError("Can't be a value 0 or less")

            if(start > end): # Throws exception if the start is greater than the end
                raise ValueError("Can't have start larger than end")

            updateMainFile(start, end, teamFile, maxYear)

            teamFile.close()

        # Case b (Filter Recent Teams)
        elif(commandChoice.lower() == 'b'):
            teamFile = open("teamFile.txt")
            teamFiltered = open("teamRecentFiltered.txt", 'w')
            teamOutsideFilter = open("teamOutsideRecent.txt", 'w')

            filterRecent(teamFile, teamFiltered, teamOutsideFilter)

            teamFile.close()
            teamFiltered.close()
            teamOutsideFilter.close()

        # Case c (Filter Ranked Teams)
        elif(commandChoice.lower() == 'c'):
            teamFile = open("teamFile.txt")
            teamFiltered = open("teamRankedFiltered.txt", 'w')
            teamOutsideFilter = open("teamOusideRanked.txt", 'w')

            filterRanked(teamFile, teamFiltered, teamOutsideFilter)

            teamFile.close()
            teamFiltered.close()
            teamOutsideFilter.close()

        # Case d (Change Max Year)
        elif(commandChoice.lower() == 'd'):
            teamFile = open("teamFile.txt")
            newTeamFile = open("newTeamFile.txt", 'w')
            settings = open("settings.txt", "w")

            print("--Enter an Integer for the Maximum Year for Recent Matches Below--")
            maxYear = input()
            settings.write(maxYear)
            maxYear = int(maxYear)
            reformatRecent(teamFile, newTeamFile, maxYear)

            teamFile.close()
            newTeamFile.close()
            settings.close()

            teamFile = open("teamFile.txt", 'w')
            newTeamFile = open("newTeamFile.txt")

            teamContents = newTeamFile.readlines()
            for line in range(0, len(teamContents)):
                teamFile.write(teamContents[line])

            teamFile.close()
            newTeamFile.close()

        # Case e (Sort the Ranked Teams)
        elif(commandChoice.lower() == 'e'):
            teamFiltered = open("teamRankedFiltered.txt")
            teamSorted = open("teamRankedSorted.txt", 'w')
            
            sortTeams(teamFiltered, teamSorted)

            teamFiltered.close()
            teamSorted.close()

        # Case f (Update Team Ranks)
        elif(commandChoice.lower() == "f"):
            teamFiltered = open("teamRankedSorted.txt")
            teamUpdated = open("teamUpdatedRanks.txt", 'w')
            teamUpdatedSorted = open("teamUpdatedRanksSorted.txt", 'w')

            updateRankedFile(teamFiltered, teamUpdated, teamUpdatedSorted, maxYear)

            teamFiltered.close()
            teamUpdated.close()
            teamUpdatedSorted.close()

        # Case q (Quits the program)
        elif(commandChoice.lower() == 'q'):
            break

        # Case z (Testing Commands)
        elif(commandChoice.lower() == 'z'):
            teamSorted = open("teamRankedSorted.txt", 'r')

            isFilled(teamSorted)

            teamSorted.close()

        menu()
        commandChoice = input()

        if(len(commandChoice) != 1): # Checks for if multiple characters are pressed
            raise ValueError("Must be only one letter input")
        
        if(not commandChoice.isalpha()): # Checks for if input isn't alphanumeric
            raise ValueError("Must be only apart of alphabet")

except Exception as e:
    print(repr(e))
