def checkChars(cad):
    exist = {}
    result = ""
    for i in cad:
        if not i in exist:
            exist[i] = i
            result = result + i
        else:
            break
    print(result)
    
checkChars("mesllarga")      
