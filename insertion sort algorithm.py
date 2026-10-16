file = open("playernames.txt","r")
filecont = file.readlines()
file.close()

pos = 0
i = 0
sortlist = []
sortlist.append(filecont[0])
item = 0
search = True
while item < (len(filecont)-1) and search:
    pos = 0
    empty = filecont[item]
    if ord(empty[i]) >= ord(sortlist[item][i]):
        pos += 1
    elif ord(empty[i]) < ord(sortlist[item][i]):
        