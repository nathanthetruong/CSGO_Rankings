from multiprocessing.sharedctypes import Value
from typing import Type
import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime

baseURL = "https://www.hltv.org/team/"
random.seed()

currentDate = datetime.now()

# Handles Team ID
def findTeamID(teamURL):
    index1 = teamURL.rfind('/') # Finds the end index of Team ID
    teamURL = teamURL[0: index1] # Removes /a from URL String
    index2 = teamURL.rfind('/') # Finds the start index of Team ID
    teamID = teamURL[index2 + 1: index1]
    return teamID

# Handles Team Name
def findTeamName(soup):
    h1TeamName = soup.find("h1", {"class": "profile-team-name text-ellipsis"}) # Finds header of Team Name
    if(h1TeamName): # Makes sure the Team Name exists
        teamName = h1TeamName.get_text()
        return teamName
    return "N/A" # Default sets Team Name to N/A

# Handles Team Rank
def findTeamRank(soup):
    divTeamRank = soup.find("div", {"class": "profile-team-stat"}) # Finds div of Team Rank
    if(divTeamRank): # Makes sure the Team Rank exists
        spanTeamRank = divTeamRank.find("span", {"class": "right"})
        teamRank = spanTeamRank.get_text()
        teamRank = teamRank.replace("#", "")
        return teamRank
    return "N/A" # Default sets Team Rank to N/A

# Handles Last Match Played
def findTeamMatch(soup):
    trMatchPlayed = soup.find("tr", {"class": "team-row"})
    if(trMatchPlayed):
        tdMatchPlayed = trMatchPlayed.find("td", {"class": "date-cell"})
        spanMatchPlayed = tdMatchPlayed.find("span")
        lastMatchPlayed = spanMatchPlayed.get_text()
        if(lastMatchPlayed.find(':') >= 0): # Sets any matches with a time of today as today's date
            dayString = str(currentDate.day)
            monthString = str(currentDate.month)
            yearString = str(currentDate.year)
            if(len(dayString) < 2):
                dayString = "0" + dayString
            if(len(monthString) < 2):
                monthString = "0" + dayString
            lastMatchPlayed = dayString + "/" + monthString + "/" + yearString
        return lastMatchPlayed 
    return "N/A" # Default sets Last Match Played to N/A

# Boolean that finds if the team has played a match in a time frame
def hasRecentMatch(matchDate, currentDate, maxYear):
    if(matchDate != "N/A"):
        index1 = matchDate.find('/')
        index2 = matchDate.rfind('/')
        matchDay = int(matchDate[0: index1])
        matchMonth = int(matchDate[index1 + 1: index2])
        matchYear = int(matchDate[index2 + 1: len(matchDate)])
        if(matchYear + maxYear - 1 >= currentDate.year): # Match is within the Max Year for sure
            return True
        if(matchYear + maxYear == currentDate.year): # Match is the same year as the Max Year
            if(matchMonth > currentDate.month): # Match Month later than Current Date's Month
                return True
            if(matchMonth == currentDate.month): # Match Month is same as Current Date's Month
                if(matchDay >= currentDate.day): # Match Day is the same or later than Current Date's Day
                    return True
        return False # The Match isn't within the Max Year
    return False # The Team has no Match History

# Handles all the output
def findOutput(teamURL, soup, currentDate, maxYear):
    output = findTeamID(teamURL) + " "
    output = output + findTeamName(soup) + " "
    output = output + findTeamRank(soup) + " "
    output = output + findTeamMatch(soup) + " "
    if(hasRecentMatch(findTeamMatch(soup), currentDate, maxYear)):
        output = output + "R"
    else:
        output = output + "N"
    return output

# Handles Team URL from Input ID
def findTeamURLs(start, end):
    teamURLs = []
    # Loops through range of [start, end]
    for teamNum in range(start, end + 1):
        # Gets the Team Page URL
        teamURL = baseURL + str(teamNum) + "/a"
        teamURLs.append(teamURL)
    return teamURLs

# Handles all the Webscraping
def updateTeamFile(teamURLs, teamFile, maxYear):
    startTime = time.time()
    
    # Loops through all of the Team URLs and outputs onto a given .txt file
    for teamCount in range(0, len(teamURLs)):
        # Adds a delay to avoid overloading and detection
        timeRange = (random.random() * 5) + 5
        time.sleep(timeRange)
        print(teamCount + 1, timeRange)

        # Gets the Team Page Data
        page = requests.get(teamURLs[teamCount])
        soup = BeautifulSoup(page.content, "html.parser")

        output = findOutput(teamURLs[teamCount], soup, currentDate, maxYear)

        # Outputs information onto teamFile.txt
        print(output)
        teamFile.write(output + "\n")
    
    endTime = time.time()
    totalTime = endTime - startTime
    print(totalTime)

# Handles Updating teamFile.txt
def updateMainFile(start, end, teamFile, maxYear):
    teamURLs = findTeamURLs(start, end)
    updateTeamFile(teamURLs, teamFile, maxYear)
