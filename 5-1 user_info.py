import simplejson as json
import urllib.request as request
import csv
import time
#get users' information - playcount&country
#open the Local file － all_users(nodes)
with open('/Users/zhouxiaoyou/Desktop/3-0 all_users(nodes).csv') as ff:
    reader = csv.reader(ff)
    userlist = list(reader)

f = open(r'5-2 user_info.txt', r'wb')

for i in userlist:
    time.sleep(1)  # sleep 1 second
    # request api "user.getinfo"
    text = request.urlopen(r'http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=' + str(i[0]) + r'&api_key=7e4cdb093829de7bd39653f3a128de52&format=json')
    text = text.read()
    decoder = json.JSONDecoder()
    user_play_country_list = decoder.decode(text)
    #make sure this user had information
    #get infor
    if len(user_play_country_list)!=0:

            usercity = user_play_country_list['user']['country']
            userplay = user_play_country_list['user']['playcount']

            output = str(i[0]) + "|" + usercity + '|' + userplay + '\n'
            output = output.encode()
            f.write(output)
f.close()



