import csv
#record pure_edge(I and my friends have same tag) or motley_edge(I and my friends do not have same tag)
#open a flie that is contain all edges
with open('/Users/zhouxiaoyou/Desktop/6-0 fd_edge_list.csv') as ff:
    reader = csv.reader(ff)
    userlist = list(reader)
#open a flie that is contain users' tag
with open('/Users/zhouxiaoyou/Desktop/6-1 user_tag_dic.csv') as f:
    reader = csv.reader(f)
    alltag = dict(reader)

file = open(r'6-3-11 egde_tag_world.txt', r'wb')#output

for i in userlist:
# get 2 nodes(user and fd) in the edge list
    user=i[0]
    fd=i[1]
#try to get tag from the tag dictionary "alltag"
    try:
        user_tag =alltag[user]
        fd_tag = alltag[fd]
#print exception cases
    except:
        print(user)
        print(fd)
        continue

    if user_tag =="World_Music": #selet one of a tag,if need all tags, this step is not necessary
        # judge tags of user and fd ,if they had same tag, code as 1,0
        if user_tag == fd_tag:
            output = b'1' + b'|' + b'0' + b'\n'

            file.write(output)
        # else, they did not have same tag, code as 0,1
        else:
            output = b'0' + b'|' + b'1' + b'\n'

            file.write(output)


f.close()



