file = open("playernames.txt","r")
filecont = file.readlines()
file.close()
item = input("enter the first character of the item youre looking for: ").lower()

for i in range(0,len(item)):
    pos = len(filecont) // 2
    search = True
    while search:
        try:
            if ord(filecont[pos][i].lower()) > ord(item[i]):
                filecont = filecont[:len(filecont) // 2]
                pos = len(filecont) // 2
            elif ord(filecont[pos][i].lower()) < ord(item[i]):
                filecont = filecont[len(filecont) // 2:]
                pos = len(filecont) // 2
            elif ord(filecont[pos][i].lower()) == ord(item[i]):
                search = False
                search2 = True
                pos2 = pos
                while pos2 > 0 and search2 == True:
                    try:
                        pos2 -= 1
                        if ord(filecont[pos2][i].lower()) < ord(item[i]):
                            filecont = filecont[pos2 + 1:]
                            search2 = False
                    except:
                        filecont.remove(filecont[pos2])
                search2 = True
                pos2 = 0
                while pos2 < len(filecont)-1 and search2 == True:
                    try:
                        pos2 += 1
                        if ord(filecont[pos2][i].lower()) > ord(item[i]):
                            filecont = filecont[:pos2]
                            search2 = False
                    except:
                        filecont.remove(filecont[pos2])
            else:
                search = False
                print("item not found")
        except:
            filecont.remove(filecont[pos])

for i in range(0,len(filecont)):
                    print(filecont[i].strip())