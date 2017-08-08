import simplejson as json
import urllib.request as request
import csv
import time
#get users' favorite artist
#open the Local file － all_users(nodes)
with open('/Users/zhouxiaoyou/Desktop/3-0 all_users(nodes).csv') as ff:
   reader = csv.reader(ff)
   userlist = list(reader)

f = open(r'3-2 users’ TopArtists.txt', r'wb')#output

for i in userlist:
    time.sleep(1)
    #request api "user.gettopartists"
    # make sure i can request this url
    try:
        text = request.urlopen(r'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=' + str(i[0]) + r'&api_key=7e4cdb093829de7bd39653f3a128de52&format=json')
    except:
        print(i) #print Exception case
        continue

    text = text.read()
    decoder = json.JSONDecoder()
    artlist = decoder.decode(text)
    #get top artists' name
    if len(artlist['topartists']['artist'])!=0:
            artlist = artlist['topartists']['artist']
            art=artlist[0]['name']
            output = i[0]+ '|' + art + '\n'
            output = output.encode()
            f.write(output)
f.close()


