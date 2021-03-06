import time
def lev_distance(first,second):
    l1 = len(first)+1
    l2 = len(second)+1
    matrix = [[0] * l2 for x in range(l1)]
    for x in range(l1):
        matrix[x][0] = x
    for y in range(l2):
        matrix[0][y] = 0
    for x in range(1,l1):
        for y in range(1,l2):
            delete = matrix[x-1][y] + 2
            insert = matrix[x][y-1] + 2
            substitution = matrix[x-1][y-1]
            if first[x-1] != second[y-1]:
                substitution += 1
            matrix[x][y] = min(delete,insert,substitution)
    return matrix
    
def dna(patrons,fitxer):
    result = []
    t1 = time.clock()
    for element in patrons:
        f = open(fitxer, "r")
        minDistance = -1
        count = 1
        minCount = 0
        for line in f.readlines():
            len1 = len(element)+1
            len2 = len(line)+1
            matrix = lev_distance(element,line)
            distance = min([matrix[len1-1][y] for y in range(len2)])
            
            
            if minDistance >= 0 and minDistance > distance:     
                minDistance = distance
                minCount = count
            elif minDistance < 0:
                minDistance = distance
                minCount = count
                           
            count += 1
        f.close()               
        result.append([element, minCount, minDistance])
    t2 = time.clock()
    return result, t2-t1
