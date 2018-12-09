def era1(n):  
    llista1 = [x for x in range(2,n+1)]
    primers = []
    while llista1[0] < n**1/2:
        primers.append(llista1[0])
        llista1 = [i for i in llista1 if i%llista1[0] != 0]        
    primers = primers + llista1    
    print(primers)
    
//ERA 2 
    
import timeit 
import time
def era2(n):
    primers = []
    auxiliar = [True]*n
    i = 0
    for x in range (2, (n**1//2) +1):
        for check in range(x**2, n+1, x):
            auxiliar[check-1] = False
    primers = [x for x in range (2,n+1) if auxiliar[x-1]]
print(primers)
