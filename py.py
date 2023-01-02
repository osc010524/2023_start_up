f= open("C:/Users/osc01/OneDrive/바탕 화면/problem2/strem2.txt",'r')

F=f.read()

# print(F)

def mid(l,n1,n2):
    l_list=list(l)
    temp = l_list[n1:n1+n2]
    s = ''.join(temp)
    return "0x"+s

def rigmarole(es):
    furphy = str()
    c = int()
    s = int()
    cc= int()
    furphy=""
    for i in range(0,len(es),4):
        c = int(mid(es,i,2),16)
        s = int(mid(es,i+2,2),16)
        cc=c-s
        furphy =furphy+chr(cc)
    return furphy

def folderol():
    wabbit = bytes()
    fn = int()
    onzo = list(str())
    mf = str()
    # xertz
    onzo = F.split(".")
    # for i in onzo:
    #     print(rigmarole(i))
    # fudgel = rigmarole(onzo[7])
    # fudgel2 = rigmarole(onzo[8])
    # fudgel3 = rigmarole(onzo[9])
    #
    # print(fudgel)
    # print(fudgel2)
    # print(fudgel3)

    for i in range(0,len(onzo)):
        print(i,":",rigmarole(onzo[i]))

folderol()



