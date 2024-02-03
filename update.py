from teamFile import updateTeamFile
from sorting import sortTeams

baseURL = "https://www.hltv.org/team/"

# Finds the URLs of each Ranked Team's ID
def findRankedURLs(teamFiltered):
    teamURLs = []
    contents = teamFiltered.readlines()
    for line in range(0, len(contents)):
        currentLine = contents[line]
        index1 = currentLine.find(' ') # Finds the index of the end of the Team ID
        teamNum = currentLine[0: index1]
        teamURL = baseURL + teamNum + "/a"
        teamURLs.append(teamURL)
    return teamURLs

# Tests to see if every team spot is filled in the sorted list (Returns bool)
def isFilled(teamSorted):
    contents = teamSorted.readlines()
    currentNum = 1
    for line in range(0, len(contents)):
        currentLine = contents[line]
        index1 = currentLine.rfind(' ') # Finds the index for the start of Team Rank
        teamRank = currentLine[index1 + 1: len(currentLine)]
        if(teamRank != currentNum): # Checks for if the expected next rank isn't met and returns false
            return False
        currentNum = currentNum + 1
    return True # Returns true if every team rank is in its expected spot

# Final Function to automatically update all ranking information
def updateRankedFile(teamFiltered, teamNewFiltered, teamSorted, maxYear):
    teamURLs = findRankedURLs(teamFiltered)
    updateTeamFile(teamURLs, teamNewFiltered, maxYear)
    sortTeams(teamFiltered, teamSorted)
