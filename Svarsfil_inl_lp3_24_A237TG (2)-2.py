# Skriv en inledande kommentar som talar om vad programmet gör. 


# Placera dina modulimpoter här:
import csv
import matplotlib.pyplot as plt

# Deluppgift 1: Funktioner från deluppgift 1 i ordning.
# Skriv din kod här:


#lägger in filnamnet'
pisadata = 'pisadata' 
def read_file(pisadata):
                         #läser in filen till en lista
    data = []
    with open (pisadata, 'r', encoding = 'UTF-8') as file: #funktionen öppnar filen och läser genom den och säkerställer att inläsningen fungerar
        reader = csv.reader(file, delimiter = ';')
        for rad in list(reader):
            data.append(rad)
    return data
#funktionen returnerar listan 

# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
# Skriv din kod här:


#vi ska ha parameter 1 -'in:listan som ska sorteras
#parameter 2- in:kolumnen som bestämmer
def coloumns(lista, index):   
    data = []

#skiva ut 10 bästa & 10 sämsta, döpa funktionen till ett valfritt namn
    for row in lista[2:]:
        data.append([row[0],row[index]])
    semst = sorted(data, key=lambda x: x[1]) [0:10]
    best = sorted(data, key=lambda x: x[1], reverse=True)[0:10]
       #  ut: sorterad lista 
        
    print(semst) 
    print(best)
#funktionen ska sortera listan utifrån vald kolumn

# skapa två tabeller och skriva ut dem
    print(f'{'De tio länder som hade bäst resultat år 2018':<70}' )
    print(70*'-')
    print(f'{'Land':<35}{'Resultat':>35}')
    print(70*'-')
#funktionen ovan utgör en tabell för de länder med bäst resultat under år 2018
    for row in best:
        print(f'{row[0]:<35} {row[1]:>35}')
    #denna for sats loopar genom listan och lägger ut de 10 bästa länderna 

#här görs en ny tabell för de länder med sämst resultat under 2018
    print(f'{'De tio länder som hade sämst resultat år 2018':<70}' )
    print(70*'-')
    print(f'{'Land':<35}{'Resultat':>35}')
    print(70*'-')
#for satsen anger lägger ut då dem länderna samt deras sämsta resultat
    for row in semst:
        print(f'{row[0]:<35} {row[1]:>35}')

    return best,semst


# Deluppgift 3: Funktioner från deluppgift 3 i ordning.
# Skriv din kod här:


def kolumnmedel(pisadata, index):
    lista = []
    for rad in pisadata[2:]:
        vald_kolumn = int(rad[index]) #lägger in värden från kolumnen och omvandlar till siffror
        lista.append(vald_kolumn) #sparar värden i lista
    sum = 0
    for e in lista:
        sum += e 
    medelvärde = sum / float(len(lista)) #räknar ut medelvärde
    return medelvärde

#skapar lista med medelvärde från 2003 till 2018
def armedel(lista):
    lista_armedel = [] #tom lista
    lista2 = [] #tom lista
    for rad in lista[0:]:
        lista_armedel.append(rad) #sparar värden i den tomma listan

    for i in range(13, 19): 
        lista2.append(kolumnmedel(lista_armedel, i)) 
    return lista2


def nordtabell(pisadata, armedel_lista):
    #skriver ut rubriker för tabellen
    print('\nKunskapsutveckling i matematik enligt PISA-undersökningen 2003 - 2018.')
    print('-'*70)
    
    nord_länder = ['Sweden', 'Norway', 'Denmark', 'Finland', 'Iceland' ]
    nordtabell = []
    medelvärden = []

    #loopar igenom länderna och matchar det med respektive värden
    for land in nord_länder:
        for i in pisadata:
            if land == i[0]:
                nordtabell.append(i)
                medelvärden.append(i[13:19])

    #skriver ut rubriker för tabellen
    Länder = 'Länder:'
    print(f'{Länder:^65}')
    print("\nÅr", end="  ")

    for x in range(5):
        print(f'{nordtabell[x][0]}', end="  " )
        alla_länder = "alla länder"
    print(f"Medelvärde\n {alla_länder:^140}") 
    print('-'*75)

    ar = pisadata[0]
    nordtabell.append(f'{ar[13:19:2]}')
    lista_år = ar[13:19]

    #skriver ut svaren som vi letar efter
    for x in range(0, len(lista_år)):
        print(f'{lista_år[x]}{medelvärden[0][x]:>2}{medelvärden[1][x]:>6} {medelvärden[2][x]:>11} {medelvärden[3][x]:>10} {medelvärden[4][x]:>12} {armedel_lista[x]:>10.0f} ')
   

def nordGraf(pisadata, armedel_lista):
#De nordiska länderna som vi ska få ut resultaten från 
    nord_länder = ['Sweden', 'Norway', 'Denmark', 'Finland', 'Iceland' ]
    nordtabell = []
    medelvärden = []

    #loopar igenom länderna och matchar det med respektive värden
    for land in nord_länder:
        for i in pisadata:
            if land == i[0]:
                #sparar värden 
                nordtabell.append(i) 
                medelvärden.append(i[13:19]) 

    ar = pisadata[0] #tar med första raden med år
    lista_år = ar[13:19] #tar endast med åren med medelvärde för grafen sen
    nordtabell.append(f'{ar[13:19]}')
    
    #beräknar y-värden osedan sparar dem frö att sedan kunna använda dem till plottningen
    y_värden = [list(map(float, reversed(medelvärden[i]))) for i in range(5)] 
    y_värden.append(armedel_lista) 
  
    x = sorted(lista_år) # x-axeln 
    medel = [float(armedel_lista[i]) for i in range(len(lista_år) -1,-1,-1)] #koden loopar genom medlevärden

    #plottar ut resultaten för varje land samt bestämmer olika färg och stilar för ländernas linjer i grafen
    plt.plot(x, y_värden[0], color='g', label='Sweden', linestyle='-')
    plt.plot(x, y_värden[1], color='m', label='Norway', linestyle='-')
    plt.plot(x, y_värden[2], color='b', label='Denmark', linestyle='-')
    plt.plot(x, y_värden[3], color='c', label='Finland', linestyle='-')
    plt.plot(x, y_värden[4], color='y', label='Iceland', linestyle='-')
    
    
    plt.plot(x, medel, color='r', label='Medel', linestyle='-') #medelvärde

#dessa koder bildar nu våran graf utseede mässigt, då den bestämmer bakgrundsfärg, rubriker och liknande
    plt.gca().set_facecolor('Lightblue') 
    plt.grid() 
    plt.xlabel('År') 
    plt.ylabel('Poäng') 
    plt.title('PISA: Kunskapsutvecklingen i matematik 2003 - 2018') 
    plt.legend() 
    plt.show() 

                       
# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
# Skriv din kod här:

#funktionen har två argument en lista och en boolvariabel
#den skriver ut dem länder som har förbättrats om boolvariabeln är sant och de länder som har  försämrats om boolvariabeln är falsk    
def Battresamre(pisadata, battre):
     #definierar samt skriver ut rubrikerna
    datum = ['2018', '2015', '2012', '2009', '2006', '2003']
    print('-'*83)
    rubrik = ('År och resultat:')
    print(f'{rubrik:^80}') #placerar rubriken i mitten
    print()
    print(f"{'Land':<20}", end='')
    for år in datum:
        print(f"{år:>10}", end='')
    print()  
    print('-'*83)

    #loopar igenom varje land 
    for datan in pisadata[2:]:
        land = datan[0]  
        värden = [int(siffror) for siffror in datan[13:19]]  
        
        # Kontrollerar om landet har kontinuerligt förbättrat eller försämrat sina resultat
        kontinuerligt = all(värden[i] >= värden[i+1] for i in range(len(värden)-1)) if battre else all(värden[i] <= värden[i+1] for i in range(len(värden)-1))
      
        
        #kontrollerar om landet uppfyller kraven och skriver ut landet och dess resultat
        if kontinuerligt:
            print(f"{land:<20}", end='')  #skriver ut landets namn
            for resultat in värden:
                print(f"{resultat:>10}", end='')  #skriver ut resultaten för varje år
            print()  #ny rad för nästa land

    
# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
# Skriv din kod här:

def kvinna_man(pisadata):
    #tabellen
    print('År och länder när kvinnorna presterar bättre än männen under åren 2003–2018.') 
    print('År\t      Land\t    \tKvinnor\t\tMän')
    print('-'*75)
    data = []
    for kolumn in range(1,13,2):
        for rad in range(2,len(pisadata)): #loopar genom alla rader från index 2 och så vidare
           if pisadata[rad][kolumn] < pisadata[rad][kolumn+1]: #satsen kollar om kvinnornas resultat genom åren för varje land är lägre än männens
               data.append([int(pisadata[0][kolumn]), pisadata[rad][0], pisadata[rad][kolumn+1], pisadata[rad][kolumn]]) #informationen om männen och kvinnornas poäng sparas i en tom lista 'data
    
    
    samma_år = None
    for rad in data:
        if rad[0] != samma_år:
            samma_år = rad[0]
            print()
            print(f'{rad[0]:<12}{rad[1]:<5}\t\t{rad[2]:>3}\t\t{rad[3]:<5}') 
        else: 
            print(f'{rad[1]:<5}\t\t{rad[2]:>3}\t\t{rad[3]:<5}')
        #Den samlade datan skrivs ut för varje gång kvinnorna presterar bättre
            


# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:

# meny 1 - b fråga efter filnamn, endaast enter ger default. 
#c) anropa funktionen, och listan ska sparas  i filnamnet pisadata
# skriva ut fem första rader

while True:

    print('meny')
    print('1. läs in csv-filen')
    print('2. bästa resp. sämsta resultat år 2018')
    print('3. Matematikkunskaper i norden år 2003 - 2018')
    print('4. kontinuerligt förbättrat resp. försämrat år 2003 - 2018')
    print('5. kvinnor presterar bättre än män under åren 2003 - 2018')
    print('6. avsluta programmet')
  
    Choice = int(input('välj ett mney alternativ (1 - 6): '))
    
    
    if Choice == 1:     
        pisadata = input('ange filnamn eller tryck bara enter för data.csv') or 'data.csv'
        print('angivet filnamn:',pisadata)
        pisadata= read_file('pisadata (3).csv')
        print(pisadata[:5])
    elif Choice == 2:
        pisadata= read_file('pisadata (3).csv')
        coloumns(pisadata, 13)
    elif Choice == 3:
        pisadata= read_file('pisadata (3).csv')
        armedel_lista = armedel(pisadata) 
        lander = ['svergie','Norge','Danmark','Finland','Island']
        nordtabell_1 = nordtabell(pisadata, armedel_lista)
        nordGraf(pisadata,armedel_lista)
    elif Choice == 4:
        pisadata= read_file('pisadata (3).csv')
        Battresamre(pisadata,True)
        Battresamre(pisadata,False)
    elif Choice == 5:
        kvinna_man(pisadata)
    elif Choice == 6:
        print('programmet avslutas')
        break

