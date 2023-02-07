

'''Tomi: 3,4,6 Hbence: 1,2,5'''


file=open("processzorok.txt", "r")
file_data=[]

for jatek in file:
    if jatek[-1] == "\n":
        file_data.append(jatek[:-1].split("\t"))
    else:
         file_data.append(jatek[:-1].split("\t"))

del file_data[0]

#3
