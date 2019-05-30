import copy
import math

def elimDup(list):
    noDup = []
    for k in range (len(list)):
        if list[k] not in noDup:
            noDup.append(list[k])
    return(noDup)  
    
def distance(P,Q):
    ''' looks for min dist for 2break
    to get from P to Q '''
    count=0
    visited=[]
    graphi={}
    EPr=Edges(P)
    EQc=Edges(Q)
    Edgescomb=[x for x in EPr]
    for s in EQc:
        if s not in EPr:
            Edgescomb.append(s) 
    edgess=copy.deepcopy(Edgescomb)
    graphe=makedict(edgess)
    for s in graphe:
        if graphe[s][0]==graphe[s][1]:
            count+=0.5
            visited.append(s)
        else:
            graphi[s]=graphe[s]
    while(len(graphi)>0):
        search=0
        visited=[]
        nextt=list(graphi.keys())[0]
        start=copy.deepcopy(nextt)
        visited.append(nextt)
        while(search==0):
            next1,visited,count,search=moves(graphi,nextt,visited,start,count,search)
            nextt=next1
        for s in visited[1:]:
            del graphi[s]
    return(len(P)-int(count))
    
def moves(graph,index,visited,start,cycle,search):
    if (graph[index][0]==start or graph[index][1]==start) and (graph[index][1] in visited and graph[index][0] in visited):
#        print('cycle found',visited)
        cycle+=1
        visited.append(start)
        search=1
        return(start,visited,cycle,search)
    nextt=graph[index][0]
    if nextt in visited:
        nextt=graph[index][1]
    visited.append(nextt)
    return(nextt,visited,cycle,search)
    
def makedict2(edges):
    ''' 1 represents Red or P edges, 0 is for Blue or Q
    edges '''
    graph={}
    for s in range(len(edges)):
        graph[s]=edges[s]
    return(graph)
    
def pairequal(x,y):
    ''' returns true if (x1,x1)~(y1,y2)
    in an unorder sense ''' 
    if (x[0]==y[0] or x[0]==y[1]) and (x[1]==y[0] or x[0]==y[1]):
        return(True)
        
def findcycolor(Redg,Blueg):
    ''' finds cycle in gengraph by toggling
    between Red and blue edges '''
    found=0
    cycle=[]
    visitedred=[]
    visitedblue=[]
    Redgraph=copy.deepcopy(Redg)
    Bluegraph=copy.deepcopy(Blueg)
    Rdg={}
    Bdg={}
    for s in Redgraph:   # remove simple cycles
        for t in Bluegraph:
            if not(pairequal(Redgraph[s],Bluegraph[t])):
                Rdg[s]=Redgraph[s]
                Bdg[t]=Bluegraph[t] 
    if len(Rdg)==0 or len(Bdg)==0:
        return(cycle,visitedred,visitedblue)
    start=Rdg[0]   # start with a red edge
    nexx=copy.deepcopy(start[1])
    visitedred.append(start)
    cycle.append(start[0])
    while(found==0):
        for s in Bdg:
            val=Bdg[s]
            if nexx in val:
                visitedblue.append(val)
                cycle.append(nexx)# look for next color
                nexx=val[(val.index(nexx)+1)%2]
            if  nexx == start[0]:
                found=1
                break
        for s in Rdg:
            val=Rdg[s]
            if nexx in val:
                visitedred.append(val)
                cycle.append(nexx)# look for next color
                nexx=val[(val.index(nexx)+1)%2]
            if  nexx == start[0]:
                found=1
                break
#        print(cycle,visitedred,visitedblue)
    return(cycle,visitedred,visitedblue)
            

def makedict(edges):
    graph={}
    for s in edges:
        if not(s[0] in graph):
            graph[s[0]]=[s[1]]
        else:
            graph[s[0]].append(s[1])
        if not(s[1] in graph):
            graph[s[1]]=[s[0]]
        else:
            graph[s[1]].append(s[0])
    return(graph)


def findcolor(RedP,BlueQ):
    ''' finds cycle in gengraph by toggling
    between Red and blue edges '''
    singlered=[]
    found=0
    cycle=[]
    visitedred=[]
    visitedblue=[]
    Reds=copy.deepcopy(RedP)
    for s in Reds:
        if s in BlueQ or (s[1],s[0]) in BlueQ:
            singlered.append(s)
            Reds.remove(s)
    if len(Reds)==0:
        return(cycle,visitedred,visitedblue)
    start=Reds[0]   # start with a red edge
    nexx=copy.deepcopy(start[1])
    visitedred.append(start)
    cycle.append(start[0])
    while(found==0):
        for s in BlueQ:
            if nexx in s:
                visitedblue.append(s)
                cycle.append(nexx)# look for next color
                nexx=s[(s.index(nexx)+1)%2]
            if  nexx == start[0]:
                found=1
                break
        for s in Reds:
            if nexx in s:
                visitedred.append(s)
                cycle.append(nexx)# look for next color
                nexx=s[(s.index(nexx)+1)%2]
            if  nexx == start[0]:
                found=1
                break
#        print(cycle,visitedred,visitedblue)
    return(cycle,visitedred,visitedblue)
#P=[1,-2,-3,4]
#Q=[1,2,-4,-3]
P = [-9, -13, -10, -6, -12, +5, +2, -7, -1, +8, +4, -3, -11]
Q = [+12, -3, -6, +5, -2, -11, -4, +10, -7, +1, -13, +9, +8]
'''
Output
(+9 -8 +12 +7 +1 -14 +13 +3 -5 -11 +6 -2 +10 -4)
(+9 -8 +12 -3 -13 +14 -1 -7 -5 -11 +6 -2 +10 -4)
(+9 -8 +12)(+7 +1 -14 +13 +3 +4 -10 +2 -6 +11 +5)
(+9 -8 +12)(+1 -14 +13 +3 +4 -10 +2 -6 +11)(+5 +7)
(+9 -8 +12)(+13 +3 +4 -10 +2 -6 +11 +1 +14)(+5 +7)
(+9 -8 +12)(+13 +3 +4 -10 +2 -6 +11 +1 +14 -7 -5)
(-8 +12 +9 +5 +7 -14 -1 -11 +6 -2 +10 -4 -3 -13)
(-8 +12 +9 +5 +7 -14 -1 -11 +6 -2 +10)(+13 +3 +4)
(+13 +3 +4)(-11 +6 +12 +9 +5 +7 -14 -1)(-2 +10 -8)
(-2 +10 -8)(+5 +7 -14 -1 -11 +3 +4 +13 +6 +12 +9)
(+5 +7 -14 -1 -11 +10 -8 -2 +3 +4 +13 +6 +12 +9)
(+5 +7 -14 -1 -11 +8 -10 -2 +3 +4 +13 +6 +12 +9)
'''
def Edges(chromo):
    ''' from chromosome string generate color and
    black edges '''
    BE=[]
    CE=[]
    cycle=chromosometoCycle(chromo)
    for s in range(0,len(cycle),2):
        BE.append((cycle[s],cycle[s+1]))
    for s in range(len(BE)-1):
        CE.append((BE[s][1],cycle[cycle.index(BE[s][1])+1]))
    CE.append((cycle[-1],cycle[0]))
    return(CE)
    
def chromosometoCycle(chromosome):
    s = []
    for i in range(len(chromosome)):
        j = chromosome[i]
        if(j < 0):
            s.append(2*(-j))
            s.append(2*(-j)-1)
        if(j > 0):
            s.append(2*(j)-1)
            s.append(2*(j))
    return(s)
def CyctoChromo(cycle):
    chromo=[]
    for s in range(int(len(cycle)/2)):
        if cycle[2*s]<cycle[2*s+1]:
            chromo.append(math.floor(cycle[2*s+1]/2))
        else:
            chromo.append(-math.ceil(cycle[2*s]/2))
    return(chromo)
     
        
def fcycle(Reds):
    cycle=[]
    start=Reds[0][0]
    cycle.append(start)
    cycle.append(Reds[0][1])
    nextt=Reds[0][1]
    Reds.remove(Reds[0])
    found=0
    while(found==0):
        for s in Reds:
            if nextt%2 ==0 and nextt-1 in s:
                indx=s.index(nextt-1)
                cycle.append(nextt-1)
                cycle.append(s[(indx+1)%2])
                if s[(indx+1)%2] == start:
                    found=1
                if s[(indx+1)%2]%2==0 and s[(indx+1)%2]-1==start:
                    found=1
                if s[(indx+1)%2]%2 !=0 and s[(indx+1)%2]+1==start:
                    found=1
                nextt=s[(indx+1)%2]
                Reds.remove(s)
                break
            elif nextt%2 !=0 and nextt+1 in s:
                indx=s.index(nextt+1)
                cycle.append(nextt+1)
                cycle.append(s[(indx+1)%2])
                if s[(indx+1)%2] == start:
                    found=1
                if s[(indx+1)%2]%2==0 and s[(indx+1)%2]-1==start:
                    found=1
                if s[(indx+1)%2]%2 !=0 and s[(indx+1)%2]+1==start:
                    found=1
                nextt=s[(indx+1)%2]
                Reds.remove(s)
                break
    cycle.insert(0,cycle[-1])
    cycle.pop()
    return(Reds,cycle)
                  
def GraphToGenome(Rds):
    Reds=copy.deepcopy(Rds)
    P=[]
    for s in Reds:
        if (s[0]-s[1]==1 and (s[1]+1)%2==0):
            P.append([-int(s[0]/2)])
            Reds.remove(s)
        if (s[1]-s[0]==1 and (s[0]+1)%2==0):
            P.append([int(s[1]/2)])
            Reds.remove(s)
    while(len(Reds)>0):
        Reds,cycles=fcycle(Reds)
        P.append(CyctoChromo(cycles))
    return(P)
    
def twobreakongenomegraph(BlueQ,RedP,i,ip,j,jp):
    ''' performs an i,ip and j,jp  break and 
    reconnects to i,j and ip,jp ,assumes ec is a dict'''
    ec=[x for x in RedP]
    if (i,ip) in ec or (ip,i) in ec:
        try:
            indi=ec.index((i,ip))
            ec.remove((i,ip))
            if (ip,jp) in BlueQ:
                inn=ip
                jn=jp
            else:
                inn=jp
                jn=ip
            ec.insert(indi,(inn,jn))
        except ValueError:
            indi=ec.index((ip,i))
            ec.remove((ip,i))
            if (ip,jp) in BlueQ:
                inn=ip
                jn=jp
            else:
                inn=jp
                jn=ip
            ec.insert(indi,(inn,jn))
    if (j,jp) in ec or (jp,j) in ec:
        try:
            indj=ec.index((j,jp))
            ec.remove((j,jp))
            if (i,j) in BlueQ:
                inn=i
                jn=j
            else:
                inn=j
                jn=i
            ec.insert(indj,(inn,jn))
        except ValueError:
            indj=ec.index((jp,j))
            ec.remove((jp,j))  
            if (i,j) in BlueQ:
                inn=i
                jn=j
            else:
                inn=j
                jn=i
            ec.insert(indj,(inn,jn))
    return(ec)
    
def twobreakongenome(P,i,ip,j,jp):
    EC=Edges(P)
    ec=copy.deepcopy(EC)
    ec=twobreakongenomegraph(ec,i,ip,j,jp)
    P1=GraphToGenome(ec)
    return(P1)

def findijipjp(bluv,RedP):
    ''' finds indices from RedP,bluv list
    of edges '''
    ip_jp=bluv[0]
    jp=ip_jp[1]
    ip=ip_jp[0]
    for s in RedP:
        if ip in s:
            ip_i=s
            if ip==ip_i[0]:
               i=ip_i[1]
            else:
               i=ip_i[0]
        if jp in s:
           jp_j=s
           if jp==jp_j[0]:
               j=jp_j[1]
           else:
               j=jp_j[0]
    return(i,ip,j,jp)

def printoutform(lists): 
    outtp=''
    for s in lists:
        outp='('
        for t in s:
            if t>0:
                outp+='+'+str(t)+' '
            else:
                outp+=str(t)+' '
        outp+')'
        outtp+=outp +')'
    return(outtp)

def mintransformPtoQ(P,Q):
    RedP=Edges(P)
    BlueQ=Edges(Q)
    d=0
    print(printoutform(GraphToGenome(RedP)))
    while(d<15):
       d+=1
       RedPP=[]
       for s in RedP:
           if s not in BlueQ:
               RedPP.append(s)
       cyc,redv,bluv=findcolor(RedPP,BlueQ)# go in with dictionary out with lists
       i,ip,j,jp=findijipjp(bluv,RedP)
       RedP=twobreakongenomegraph(BlueQ,RedP,i,ip,j,jp)
       print(printoutform(GraphToGenome(RedP)))
    return(distance(P,Q))

breakList = ""
with open(r'/Users/blakemcmurray/Downloads/rosalind_ba6d.txt') as f:
    breakList = f.read().replace('(','').replace(')','').replace(' ',', ')
    
print(mintransformPtoQ(P,Q))