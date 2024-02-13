#otvorenie suboru
subor = open("sutaz_vbehu.txt","r")

#zadeklarovanie premennej
dokopy = 0

#vytvorenie prazdneho slovnika
vykony = {}

def zistenie_info(): #funkcia na zistenie info
    #zadeklarovanie globalnej premennej
    global dokopy
    
    for riadok in subor: #cyklus na prechadzanie riadkov v subore
        #rozdelenie riadku na hodnoty
        riadocek = riadok.split()

        #priradenie info do slovnika
        vykony[riadocek[0]] = riadocek[1]

        #zmena premennej
        dokopy += 1

#zavolanie funkcie
zistenie_info()

#zistenie najlepsieho bezca
naj_bezec = min(vykony, key=vykony.get)
naj_cas = int(vykony.get(naj_bezec))

#vypocet premeny zo sekund na minuty
naj_cas_final = naj_cas // 60
naj_cas %= 60

#vypisanie pozadovanych hodnot
print("Počet zúčastnených športcov:",dokopy)

for i in range(dokopy):
    print("Súťažiaci",list(vykony.keys())[i],"dobehol do cieľa za",list(vykony.values())[i],"sekúnd.")

print("Najlepší súťažiaci bol",naj_bezec,"s časom",naj_cas_final,"min.",naj_cas,"sek.")

#zatvorenie suboru
subor.close()
