import requests
import json
from urllib.request import urlopen
#sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes?limit=5

url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2023/teams/18/athletes?limit=5"
response = urlopen(url)
data_json = json.loads(response.read())
#print(len(data_json))
urllist = []
for i in range(len(data_json['items'])):
    #print(data_json['items'][i]['$ref'])
    urllist.append(data_json['items'][i]['$ref'])

#print(urllist)
playerlist = {}
for i in urllist:
    url2 = i
    response = urlopen(url2)
    data_json = json.loads(response.read())
    # print(data_json['displayName'])
    #print(data_json['age'])

    # age1 = int(data_json['age'])
    try:
        playerlist.update({data_json['displayName']: data_json['age']})
    except KeyError:
        print(data_json['displayName'] + ' age is unknown')
#print(playerlist)

for i in playerlist:
    #print(i)
    playerlist.update({i: 99})
    break
print(playerlist)

try:
    playerlist.pop("Kevin Austin Jr.")
except KeyError:
    print("not found")

#print(playerlist)



#players = {}
#players.update({"hi":1, "h2":2, "h3":3})




#==========Save file
f = open("demofile4.txt", "a")
for i in playerlist:
    f.write(i + " " +  str(playerlist[i]) + "\n")
f.close()


# #open and read the file after the appending:
f = open("demofile4.txt", "r")
print(f.read())