matrix_n = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]]

matrix_s = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
            [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]]

jahr_b = int(input("Welches ist heute Jahr? "))
tag_b = int(input("Welcher Tag? "))
monat_b = int(input("Welcher Monat? "))

# Vollmond war an diesem Tag:
jahr = 2019
monat = 11
tag = 12

while True:
    if jahr - jahr_b > 1000: break
    # Prüfen, ob heute ein Schaljahr ist:
    if (jahr % 4 == 0) and (jahr % 100 != 0) or (jahr % 400 == 0):  
        matrix = matrix_s
    else:
        matrix = matrix_n

    for i in range(monat - 1, len(matrix)):
        mondtag = matrix[i][tag - 1]  
        if (mondtag == tag_b - 1) and (monat == monat_b) or (mondtag == tag_b) and (monat == monat_b) or (mondtag == tag_b + 1) and (monat == monat_b): 

            break
        #print(mondtag, '.', monat, '.', jahr)
        monat += 1
        tag -= 1
        if (tag == 29) and (monat == 2): tag -= 1
        if tag == 0: tag = matrix[i + 1][-1]
    
    if jahr >= jahr_b:
        if (mondtag == tag_b - 1) and (monat == monat_b) or (mondtag == tag_b) and (monat == monat_b) or (mondtag == tag_b + 1) and (monat == monat_b): break
        
    jahr += 1
    monat = 1
    
if jahr - jahr_b > 1000: 
    print("Es scheint sich, dass dieser Tag zwischen 2 Tagen des Vollmondes nicht existiert. Probieren sie anderer Tag")
else:
    print("Ihr nächstes Datum des Vollmondes ist mit ungefähr 2% Fehler zwischen 2 Tagen am:")
    print(mondtag, '.', monat, '.', jahr) 




# Neumond war an diesem Tag:
jahr = 2019
monat = 10
tag = 28

while True:
    if jahr - jahr_b > 1000: break
    # Prüfen, ob heute ein Schaljahr ist:
    if (jahr % 4 == 0) and (jahr % 100 != 0) or (jahr % 400 == 0):  
        matrix = matrix_s
    else:
        matrix = matrix_n

    for i in range(monat - 1, len(matrix)):
        mondtag = matrix[i][tag - 1]  
        if (mondtag == tag_b - 1) and (monat == monat_b) or (mondtag == tag_b) and (monat == monat_b) or (mondtag == tag_b + 1) and (monat == monat_b): 

            break
        #print(mondtag, '.', monat, '.', jahr)
        monat += 1
        tag -= 1
        if (tag == 29) and (monat == 2): tag -= 1
        if tag == 0: tag = matrix[i + 1][-1]
            
    if jahr >= jahr_b:       
        if (mondtag == tag_b - 1) and (monat == monat_b) or (mondtag == tag_b) and (monat == monat_b) or (mondtag == tag_b + 1) and (monat == monat_b): break
        
    jahr += 1
    monat = 1

if jahr - jahr_b > 1000: 
    print("Es scheint sich, dass dieser Tag zwischen 2 Tagen des Neumondes nicht existiert. Probieren sie anderer Tag")
else:
    print("Ihr nächstes Datum des Neumondes ist mit ungefähr 2% Fehler zwischen 2 Tagen am:")
    print(mondtag, '.', monat, '.', jahr)   
