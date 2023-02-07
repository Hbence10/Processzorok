file=open("processzorok.txt", "r")
file_data=[]

2
1
5
for i in file:
    if i[-1] == "\n":
        file_data.append(i[:-1].split("\t"))
    else:
         file_data.append(i[:-1].split("\t"))

del file_data[0]


