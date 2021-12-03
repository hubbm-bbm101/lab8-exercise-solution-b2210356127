import sys
with open(sys.argv[1],"r") as f:
    d=dict()
    l=list()
    for line in f.readlines():
        l.append(line.strip("\n").split(":"))
    for i in l:
            d[i[0]]=i[1]
for i in sys.argv[2].split(","):
    try:
            print("Name: {}, University {}".format(i,d[i]),end=" ")
    except KeyError:
        print("No record of '{}' was found!".format(i))