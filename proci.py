'''Tomi: 3,4,6 Hbence: 1,2,5'''

file = open("processzorok.txt", "r")
ujproci=open("ujproci.txt", "w")
file_data=[]
márka = []
celeron = []




for jatek in file:
    if jatek[-1] == "\n":
        file_data.append(jatek[:-1].split("\t"))
    else:
         file_data.append(jatek[:-1].split("\t"))

del file_data[0]


#1

for i in range(len(file_data)):
    márka.append(file_data[i][1])

print(len(márka))


#2
print("AMD db száma: ", márka.count("AMD"))
print("Intel db száma: ", márka.count("Intel"))

#4
for i in range(len(file_data)):
    if "Celeron" in file_data[i][2]:
        celeron.append(file_data[i][2])

print("Ezek a celeron proceszorok állnak rendelkezésre: ",celeron)

#5
AMD = márka.count("AMD")
print("Százalékosan ennyi AMD található:",len(márka)/100*AMD,"%")