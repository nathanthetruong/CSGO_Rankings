class Team:
    teamNum = ""
    teamName = ""
    teamRank = 0
    lastMatchPlayed = ""
    recencyCheck = ""

    def __init__(self, newTeamNum, newTeamName, newTeamRank, newTeamMatch, newRecencyCheck):
        self.teamNum = newTeamNum
        print(self.teamNum + "A")
        self.teamName = newTeamName
        print(self.teamName + "A")
        self.teamRank = int(newTeamRank)
        print(str(self.teamRank) + "A")
        self.lastMatchPlayed = newTeamMatch
        print(self.lastMatchPlayed + "A")
        self.recencyCheck = newRecencyCheck
        print(self.recencyCheck + "A")

# Allows the sort() function to access Team's class data
def getTeamRank(team):
    return team.teamRank
