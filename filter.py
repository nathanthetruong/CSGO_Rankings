def filterRecent(teamFile, teamFiltered, teamOutsideFilter):
    contents = teamFile.readlines()
    for line in range(0, len(contents)):
        currentLine = contents[line]
        if(currentLine[-2] == 'R'):
            teamFiltered.write(currentLine)
        else: # Places teams that haven't played recently in a separate file
            teamOutsideFilter.write(currentLine)

def filterRanked(teamFile, teamFiltered, teamOutsideFilter):
    contents = teamFile.readlines()
    for line in range(0, len(contents)):
        currentLine = contents[line]
        # Finds and removes first space
        spaceIndex = currentLine.rfind(' ')
        currentLine = currentLine[0: spaceIndex]
        # Finds and second space removes all the parts of the string
        spaceIndex = currentLine.rfind(' ')
        currentLine = currentLine[0: spaceIndex]
        # Finds ranking
        if(currentLine[-1].isnumeric()):
            currentLine = contents[line]
            teamFiltered.write(currentLine)
        else: # Places unranked teams in a separate file
            currentLine = contents[line]
            teamOutsideFilter.write(currentLine)
