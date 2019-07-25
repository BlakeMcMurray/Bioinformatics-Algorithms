def reverse_comp(st):
    rev_comp = ""
    for i in reversed(st):
        if i == "A":
            rev_comp = rev_comp + "T"
        elif i == "T":
            rev_comp = rev_comp + "A"
        elif i == "G":
            rev_comp = rev_comp + "C"
        elif i == "C":
            rev_comp = rev_comp + "G"
    return(rev_comp)

