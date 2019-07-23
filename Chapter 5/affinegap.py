#need to refactor for readability
import math
Penaltys = {'a':[4,  0, -2, -1, -2,  0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1,  0,  0, -3, -2],
          'c':[0,  9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
          'd':[-2, -3,  6,  2, -3, -1, -1, -3, -1, -4, -3,  1, -1,  0, -2,  0, -1, -3, -4, -3],
          'e':[-1, -4,  2,  5, -3, -2,  0, -3,  1, -3, -2,  0, -1,  2,  0,  0, -1, -2, -3, -2],
          'f':[-2, -2, -3, -3,  6, -3, -1,  0, -3,  0,  0, -3, -4, -3, -3, -2, -2, -1,  1,  3],
          'g':[0, -3, -1, -2, -3,  6, -2, -4, -2, -4, -3,  0, -2, -2, -2,  0, -2, -3, -2, -3],
          'h':[-2, -3, -1,  0, -1, -2,  8, -3, -1, -3, -2,  1, -2,  0,  0, -1, -2, -3, -2, 2],
          'i':[-1, -1, -3, -3,  0, -4, -3,  4, -3,  2,  1, -3, -3, -3, -3, -2, -1,  3, -3, -1],
          'k':[-1, -3, -1,  1, -3, -2, -1, -3,  5, -2, -1,  0, -1,  1,  2,  0, -1, -2, -3, -2],
          'l':[-1, -1, -4, -3,  0, -4, -3,  2, -2,  4,  2, -3, -3,-2, -2, -2, -1,  1, -2, -1],
          'm':[-1, -1, -3, -2,  0, -3, -2,  1, -1,  2,  5, -2, -2,  0, -1, -1, -1,  1, -1, -1],
          'n':[-2, -3,  1,  0, -3,  0,  1, -3,  0, -3, -2,  6, -2,  0,  0,  1,  0, -3,-4, -2],
          'p':[-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2,  7, -1, -2, -1, -1, -2, -4, -3],
          'q':[-1, -3,  0,  2, -3, -2,  0, -3,  1, -2,  0,  0, -1,  5,  1,  0, -1, -2, -2, -1],
          'r':[-1, -3, -2,  0, -3, -2,  0, -3,  2, -2, -1,  0, -2,  1,  5, -1, -1, -3, -3, -2],
          's':[1, -1,  0,  0, -2,  0, -1, -2,  0, -2, -1,  1, -1,  0, -1,  4,  1, -2, -3, -2],
          't':[0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1,  0, -1, -1, -1,  1,  5,  0, -2, -2],
          'v':[0, -1, -3, -2, -1, -3, -3,  3, -2,  1,  1, -3, -2, -2, -3, -2,  0,  4, -3, -1],
          'w':[-3, -2, -4, -3,  1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11,  2],
          'y':[-2, -2, -3, -2,  3, -3,  2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1,  2,  7]}

Penkeys=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']  
penind=[x.lower() for x in Penkeys]


def LCSBacktrackweights(v,w,Penaltys,sigma=-11,epsilon=-1):
    lower = {}
    middle = {}
    upper = {} 
    backtrackupper={}
    backtracklower={}
    backtrackmid={}
    if len(w)>=len(v):
        row=w
        col=v
    else:
        row=v
        col=w
    middle[0,0] = 0
    upper[0,0] = -math.inf
    lower[0,0]=-math.inf
    backtracklower[0,0]=(0,(0,0),'lower','lower')
    for j in range(1,len(col)+1):
        lower[0,j]=-math.inf
        upper[0,j]=j*epsilon
        backtracklower[0,j]=(lower[0,j],(0,j),'lower','lower')
        backtrackupper[0,j]=(upper[0,j],(0,j-1),'upper','upper')
    backtrackupper[0,0]=(0,(0,0),'upper','upper')
    for i in range(1,len(row)+1):
        lower[i,0]=i*epsilon 
        upper[i,0]=-math.inf
        backtrackupper[i,0]=(upper[i,0],(i,0),'upper','upper')
        backtracklower[i,0]=(lower[i,0],(i-1,0),'lower','lower')
    for i in range(1,len(row)+1):
        middle[i,0]=0
    for j in range(len(col)+1):
        middle[0,j] = 0
    for i in range(1,len(row)+1):
        for j in range(1,len(col)+1):
            Penal = Penaltys[v[i-1].lower()][penind.index(w[j-1].lower())]
            upper[i,j] = max(sigma + middle[i,j-1],epsilon  + upper[i,j-1])
            lower[i,j] = max(sigma + middle[i-1,j], epsilon + lower[i-1,j])
            middle[i,j] = max(Penal + middle[i-1,j-1], upper[i,j], lower[i,j])
            if upper[i,j]==sigma + middle[i,j-1]:
                backtrackupper[i,j]=(upper[i,j],(i,j),(i,j-1),'upper','middle' )
            elif upper[i,j]==epsilon+upper[i,j-1] : 
                backtrackupper[i,j]=(upper[i,j],(i,j),(i,j-1),'upper','upper' )  
                
            if lower[i,j]==sigma + middle[i-1,j]:
                backtracklower[i,j]=(lower[i,j],(i,j),(i-1,j),'lower','middle' )
            elif lower[i,j]==epsilon+lower[i-1,j]: 
                backtracklower[i,j]=(lower[i,j],(i,j),(i-1,j),'lower','lower' ) 
            if middle[i,j]==upper[i,j]:
                backtrackmid[i,j]=(middle[i,j],(i,j),(i,j),'middle','upper' )
            elif middle[i,j]==lower[i,j]:
                backtrackmid[i,j]=(middle[i,j],(i,j),(i,j),'middle','lower' )
            else:
                backtrackmid[i,j]=(middle[i,j],(i,j),(i-1,j-1),'middle','middle' )          
    return (backtrackupper, backtrackmid, backtracklower)

def findpath(gu,gm,gl,v,w):
    path={}
    ind=(len(v),len(w))
    graph=gm
    path[0]=[graph[ind][2],graph[ind][3]] #starting node
    i=1
    #not(ind[0]==0 and ind[1]==0) or not(graph[ind][2]=='middle')
    while(1):
        try:
            path[i]=[graph[ind][2],graph[ind][4]]
            if graph[ind][4]=='upper':
                ind=graph[ind][2]
                graph=gu
            elif graph[ind][4]=='lower':
                ind=graph[ind][2]
                graph=gl
            elif graph[ind][4]=='middle':
                ind=graph[ind][2]
                graph=gm
            i+=1
        except KeyError:
            break
    ov=''
    ow=''
    for s in range(1,len(path)):
        if path[s][1]=='upper':
            if path[s-1][1]=='upper':
                ov='-'+ov
                ow=w[path[s][0][1]-1]+ow
        if path[s][1]=='middle':
            if path[s-1][1]=='middle':
                ov=v[path[s][0][0]]+ov
                ow=w[path[s][0][1]]+ow
            else:
                if path[s-1][1]=='lower':
                   ov=v[path[s][0][0]]+ov
                   ow='-'+ow  
                if path[s-1][1]=='upper':
                   ov='-'+ov
                   ow=w[path[s][0][1]]+ow 
        if path[s][1]=='lower':
            if path[s-1][1]=='lower':
                ov=v[path[s][0][0]]+ov
                ow='-'+ow
    return(ov,ow) 

w = "PRTEINS"
v= "PRTWPSEIN"

gu,gm,gl=LCSBacktrackweights(v,w,Penaltys,sigma=-11,epsilon=-1)
print(gm[len(v),len(w)][0],findpath(gu,gm,gl,v,w))

v='ELQWVLEICFVWTFKQQYMRRNGETKTYPQMNELHQLHFDAKEWRARDIHGFVACQYHMYELNPLAQGNRCEADPWGCQPMSTGVGDA'
w='ELQWVLEGCWEPMEFKQKTYPQMDELHQFHFDTIHGFVACQYHMYELNPLAQGNRCEADGCQPMPTGHGDA'

gu,gm,gl=LCSBacktrackweights(v,w,Penaltys,sigma=-11,epsilon=-1)
print(gm[len(v),len(w)][0],findpath(gu,gm,gl,v,w))
