# Matrix of days in normal year (28 days in februar):
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

# Matrix of days in leap year (29 days in februar):
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

jahr_b = int(input("What year is today? "))
tag_b = int(input("What day is it? "))
monat_b = int(input("Which month is it? "))

# Full moon was on this date:
jahr = 2019
monat = 11
tag = 12

while True:
    # If there is no full moon day (day-1 and day+1) to your year+1000, then exit infinite loop with error:
    if jahr - jahr_b > 1000: break
    # Check, if it is a leap year:
    if (jahr % 4 == 0) and (jahr % 100 != 0) or (jahr % 400 == 0):  
        matrix = matrix_s
    else:
        matrix = matrix_n
    
    # Define full moon days
    for i in range(monat - 1, len(matrix)):
        mondtag = matrix[i][tag - 1] 
        # If we found these days, then exit loop
        if (mondtag == tag_b - 1) and (monat == monat_b) or (mondtag == tag_b) and (monat == monat_b) 
            or (mondtag == tag_b + 1) and (monat == monat_b): break
        # This line will show all full moon days begins with 'jahr_b' year:
        #print(mondtag, '.', monat, '.', jahr)
        monat += 1
        tag -= 1
        # Fixing bug in the leap year
        if (tag == 29) and (monat == 2): tag -= 1
        # Preventing to have negative indexes
        if tag == 0: tag = matrix[i + 1][-1]
    
    if jahr >= jahr_b:
        if (mondtag == tag_b - 1) and (monat == monat_b) or (mondtag == tag_b) and (monat == monat_b)
            or (mondtag == tag_b + 1) and (monat == monat_b): break
        
    jahr += 1
    monat = 1
    
if jahr - jahr_b > 1000: 
    print("Looks like there are no triplet of full moon days in this day. Try another day bigger or smaller than previous")
else:
    print("Your next date of full moon is with approx. 2% error in middle of triplet of your day:")
    print(mondtag, '.', monat, '.', jahr) 
            
            
            
            
# New moon was on this date:
jahr = 2019
monat = 10
tag = 28

while True:
    # If there is no new moon day (day-1 and day+1) to your year+1000, then exit infinite loop with error:
    if jahr - jahr_b > 1000: break
    # Check, if it is a leap year:
    if (jahr % 4 == 0) and (jahr % 100 != 0) or (jahr % 400 == 0):  
        matrix = matrix_s
    else:
        matrix = matrix_n

    # Define new moon days
    for i in range(monat - 1, len(matrix)):
        mondtag = matrix[i][tag - 1]  
        # If we found these days, then exit loop
        if (mondtag == tag_b - 1) and (monat == monat_b) or (mondtag == tag_b) and (monat == monat_b)
            or (mondtag == tag_b + 1) and (monat == monat_b): break
        # This line will show all new moon days begins with 'jahr_b' year
        #print(mondtag, '.', monat, '.', jahr)
        monat += 1
        tag -= 1
        # Fixing bug in the leap year
        if (tag == 29) and (monat == 2): tag -= 1
        # Preventing to have negative indexes
        if tag == 0: tag = matrix[i + 1][-1]
            
    if jahr >= jahr_b:       
        if (mondtag == tag_b - 1) and (monat == monat_b) or (mondtag == tag_b) and (monat == monat_b)
            or (mondtag == tag_b + 1) and (monat == monat_b): break
        
    jahr += 1
    monat = 1

if jahr - jahr_b > 1000: 
    print("Looks like there are no triplet of new moon days in this day. Try another day bigger or smaller than previous")
else:
    print("Your next date of new moon is with approx. 2% error in middle of triplet of your day:")
    print(mondtag, '.', monat, '.', jahr)   
