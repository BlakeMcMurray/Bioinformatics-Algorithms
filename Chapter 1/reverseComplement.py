def reverseComp(st):
    revComp = ""
    for i in reversed(st):
        if i == "A":
            revComp = revComp + "T"
        elif i == "T":
            revComp = revComp + "A"
        elif i == "G":
            revComp = revComp + "C"
        elif i == "C":
            revComp = revComp + "G"
    return(revComp)

