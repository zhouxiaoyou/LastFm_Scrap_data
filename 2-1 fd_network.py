import simplejson as json
import urllib.request as request
import csv
import time
#get friends of users
#open the Local file － username（40）
with open('/Users/zhouxiaoyou/Documents/2-0 username(40).csv') as ff:
    reader = csv.reader(ff)
    userlist = list(reader)

f = open(r'2-2 fd_edge_list.txt', r'wb')#output

for i in userlist:
    time.sleep(1) #sleep 1 second
    # request api "user.getfriends"
    text = request.urlopen(r'http://ws.audioscrobbler.com/2.0/?method=user.getfriends&user=' + str(i[0]) + r'&api_key=7e4cdb093829de7bd39653f3a128de52&format=json')
    text = text.read()
    decoder = json.JSONDecoder()
    fdlist = decoder.decode(text)
    # make sure users have fds,then get fdname
    if len(fdlist)!=0:
        fdlist = fdlist['friends']['user']
        for j in fdlist:
            fdname = j['name']
            output = str(i[0]) + '/t' + fdname + '\n'
            output = output.encode()
            f.write(output)
f.close()


