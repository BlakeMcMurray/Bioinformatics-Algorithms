import copy
def readin(filen):
    with open(filen) as f:
        read_data = f.read() 
    return(read_data)

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
            chromo.append(int(cycle[2*s+1]/2))
        else:
            chromo.append(-int(cycle[2*s]/2))
    return(chromo)
    
def moves(graph,index,visited,start,cycle,search):
    if (graph[index][0]==start or graph[index][1]==start) and (graph[index][1] in visited and graph[index][0] in visited):
        print('cycle found')
        cycle+=1
        visited.append(start)
        search=1
        return(start,visited,cycle,search)
    nextt=graph[index][0]
    if nextt in visited:
        nextt=graph[index][1]
    visited.append(nextt)
    return(nextt,visited,cycle,search)
    
def makeP(fileo):
    P=[]
    Qmy=readin(fileo)
    R1=Qmy.replace(' ',',')
    numb=''
    for s in range(R1.find('(')+1,len(R1)):
        if R1[s] == ',':
            P.append(numb)
            numb=''
        elif R1[s] == ')':
            P.append(numb)
            numb=''
            break
        else:
            numb+=R1[s]
    R2=R1[R1.index(P[-1]):]
    del R1
    del Qmy
    return(P,R2)

def makeQ(R2):
    Q=[]
    numb=''
    for s in range(R2.find('(')+1,len(R2)):
        if R2[s] == ',':
            Q.append(numb)
            numb=''
        elif R2[s] == ')':
            Q.append(numb)
            numb=''
            break
        else:
            numb+=R2[s]
    R3=R2[R2.index(Q[-1]):]
    return(Q,R3)   

def Edges(chromo):
    BE=[]
    CE=[]
    cycle=chromosometoCycle(chromo)
    for s in range(0,len(cycle),2):
        BE.append([cycle[s],cycle[s+1]])
    for s in range(len(BE)-1):
        CE.append([BE[s][1],cycle[cycle.index(BE[s][1])+1]])
    CE.append([cycle[-1],cycle[0]])
    return(CE)

def distance(chromoP,chromoQ):
    count=0
    visited=[]
    graphi={}
    EdgesPc=Edges(chromoP)
    EQc=Edges(chromoQ)
    Edgescomb=[x for x in EdgesPc]
    for s in EQc:
        if s not in EdgesPc:
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
#            print(visited,'\t',nextt,next1,search)
            nextt=next1
        for s in visited[1:]:
            del graphi[s]
    return(len(chromoP)-int(count))
      
fileo='/Users/blakemcmurray/text.txt'

def buildup(fileo):
    P=[]
    lnn=[]
    PT=[]
    PP,R2=makeP(fileo)   
    P1=[int(x) for x in PP]
    P.append(P1)
    summ=len(P1)
    lnn.append(len(P1))
    while(len(R2)>9):
        QQ,R2=makeQ(R2)
        P2=[int(x) for x in QQ]
        P.append(P2)
        summ+=len(P2)
        lnn.append(len(P2))
    tot=0
    s=0
    while(tot<=summ/2):
       PT.append(P[s]) 
       tot+=len(P[s])
       s+=1
    PT=P[:s-1]
    QT=P[s-1:]
    return(PT,QT)

P,Q=buildup(fileo)
chromoP=[]
chromoQ=[]
for s in P:
    chromoP+=s
for t in Q:
    chromoQ+=t
    
print(distance(chromoP,chromoQ))