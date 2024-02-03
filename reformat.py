from teamFile import hasRecentMatch
from datetime import datetime

def reformatSpacing(teamFile, newTeamFile):
    contents = teamFile.readlines()
    for line in range(0, len(contents)):
        currentLine = contents[line]
        index1 = currentLine.find(' ') # Finds end index of the Team Number ID
        index2 = currentLine.rfind(' ') # Finds end index of the Team Name
        newLine = currentLine[0:index1] + " /!/ "
        newLine = newLine + currentLine[index1 + 1: index2] + " /!/ "
        newLine = newLine + currentLine[index2 + 1: len(currentLine)]
        newTeamFile.write(newLine)
    
def reformatRecent(teamFile, newTeamFile, maxYear):
    currentDate = datetime.now()
    contents = teamFile.readlines()
    for line in range(0, len(contents)):
        currentLine = contents[line]
        index1 = currentLine.rfind(' ') # Finds end index of the Last Match Played
        newLine = currentLine[0: index1] # Cuts the R or N out
        index2 = newLine.rfind(' ') # Finds start index of the Last Match Played
        matchDate = newLine[index2 + 1: len(newLine)] # Takes only the Match Date
        if(hasRecentMatch(matchDate, currentDate, maxYear)):
            newLine = newLine + " R"
            newTeamFile.write(newLine + "\n")
        else:
            newLine = newLine + " N"
            newTeamFile.write(newLine + "\n")
