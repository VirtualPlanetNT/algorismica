def getK(dicc1, search):
    for x,y in dicc1.items(): 
        if y == search:
            return x
def cesar(n,word):
    abc = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,
                  "h":8,"i":9,"j":10,"k":11,"m":12,"n":13,
                  "o":14,"p":15,"q":16,"r":17,"s":18,"t":19,
                  "u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    chars = ""
    for element in word:
        if not element in abc:
            chars = chars + " "
        else:
            result = abc[element] + n
            if result > 25:
                result -= 25
            chars = chars + getK(abc,result)  
    return chars
cesar(2,"alberto el gay")
