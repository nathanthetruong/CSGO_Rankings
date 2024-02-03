import Team

Teams = []

def loadTeams(teamFiltered):
    contents = teamFiltered.readlines()
    for line in range(0, len(contents)):
        currentLine = contents[line]
        index1 = currentLine.find(' ') # Finds index for end of teamID
        teamNum = currentLine[0: index1]
        currentLine = currentLine[index1 + 1: len(currentLine)] # Cuts out the teamID
        index2 = currentLine.rfind(' ') # Finds index for the start of Recency Check
        recencyCheck = currentLine[index2 + 1: len(currentLine)]
        currentLine = currentLine[0: index2] # Cuts out the Recency Check
        index3 = currentLine.rfind(' ') # Finds index for the start of Last Match Played
        teamMatch = currentLine[index3 + 1: len(currentLine)]
        currentLine = currentLine[0: index3] # Cuts out the Last Match Played
        index4 = currentLine.rfind(' ') # Finds index for the start of the Team Rank
        teamRank = currentLine[index4 + 1: len(currentLine)]
        currentLine = currentLine[0: index4] # Cuts out the Team Rank
        teamName = currentLine

        newTeam = Team.Team(teamNum, teamName, teamRank, teamMatch, recencyCheck)
        print("Class: " + teamNum + " " + teamName + " " + teamRank + " " + teamMatch + " " + recencyCheck)
        Teams.append(newTeam)
    return Teams

def sortTeams(teamFiltered, teamSorted):
    Teams = loadTeams(teamFiltered)
    Teams.sort(key = Team.getTeamRank)
    for teamIndex in range(0, len(Teams)):
        newLine = Teams[teamIndex].teamNum + " "
        newLine = newLine + Teams[teamIndex].teamName + " "
        newLine = newLine + str(Teams[teamIndex].teamRank) + "\n"
        #newLine = newLine + Teams[teamIndex].lastMatchPlayed + " "
        #newLine = newLine + Teams[teamIndex].recencyCheck

        teamSorted.write(newLine)
