file=open("processzorok.txt", "r")
file_data=[]

2
1
5

jatekosok = open("jatekos2.txt","r",encoding="UTF-8")
Ljatekosok = []
poszt = []

for jatek in jatekosok:
    if jatek[-1] == "\n":
        Ljatekosok.append(jatek[:-1].split("\t"))
    else:
         Ljatekosok.append(jatek[:-1].split("\t"))

del Ljatekosok[0]
