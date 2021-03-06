import simplejson as json
import urllib.request as request
import csv
import time
# get artists' top tags
# open the Local file － artists_list
# encoding latin-1 because many artists' name are unicode
with open('/Users/zhouxiaoyou/Desktop/4-0 artists_list.csv', encoding='latin-1') as ff:
   reader = csv.reader(ff)
   artistslist = list(reader)

f = open(r'4-2 artists_top_tag.txt', r'wb')#output

for i in artistslist:
    time.sleep(1)
    # request api "artist.gettoptags"
    # make sure i can request this url
    try:
        text = request.urlopen(r'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&user=' + str(i[0]) + r'&api_key=7e4cdb093829de7bd39653f3a128de52&format=json')
    except:
        print(i)
        continue
    text = text.read()
    decoder = json.JSONDecoder()
    artlist = decoder.decode(text)
    #get artists' top tag name
    if len(artlist['topartists']['artist'])!=0:
            artlist = artlist['topartists']['artist']
            art=artlist[0]['name']
            output = i[0]+ "|" + art + '\n'
            output = output.encode()
            f.write(output)
f.close()


