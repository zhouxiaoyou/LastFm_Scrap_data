import simplejson as json
import urllib.request as request

f = open(r'1-2 alltags.txt', r'wb')#output
# request api "tag.gettoptags"
text = request.urlopen(r'http://ws.audioscrobbler.com/2.0/?method=tag.getTopTags&api_key=7e4cdb093829de7bd39653f3a128de52&format=json')
text = text.read()
# simplejson deals with the api content
decoder = json.JSONDecoder()
toptags = decoder.decode(text)
# get a list of toptags
toptags = toptags['toptags']['tag']
# get the top50 tags
tags = toptags[0:49]
# get tags' name
for i in tags:
    tag = i['name']
    output = tag + '\n'
    output = output.encode()
    f.write(output)
f.close()
