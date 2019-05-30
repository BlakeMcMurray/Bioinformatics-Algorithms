fileo='/Users/blakemcmurray/text.txt'   
  
def printoutfor(onp):
    outstr='('
    for s in range(len(onp)):
       if onp[s]>=0:
           outstr=outstr+'+'+str(onp[s])+' '
       else:
           outstr=outstr+str(onp[s])+' '
    outstr=outstr[:len(outstr)-1]+')'
    return(outstr)

mouseGenome = [+115, -59, -20, -30, +139, +23, -5, -17, +130, +105, -52, +112, -73, -138, -66, -106, +142, -10, -26, +132, -107, +3, -103, -48, +75, -96, -89, -72, +12, +14, +44, -57, +55, +39, -134, -97, -126, +29, +129, -36, -31, +82, -136, +83, -54, -121, +127, -38, +22, -76, -78, +67, -61, +51, -6, -2, -86, +108, -8, +60, +19, -7, -85, -81, +69, -124, +46, +131, +56, +128, -11, +123, +133, +18, -37, +90, -63, -35, +41, -91, +114, -33, -111, +77, +102, -84, +135, +93, +13, -34, +92, -45, -80, -79, -98, +50, -58, +141, +113, +140, -117, +47, +16, +95, -71, -68, +1, -87, +32, +109, -74, -65, +70, -4, -116, -49, -100, -110, -120, -27, -94, +118, -125, -42, -62, +104, -24, +64, -88, +28, +40, -43, -53, +122, +21, -99, +9, +137, -119, -101, -25, -15]
breakList = ""
with open(r'/Users/blakemcmurray/text.txt') as f:
    breakList = f.read().replace('(','').replace(')','').replace(' ',', ')

def greedySorting(mouseGenome):
    with open(fileo,'w') as f:
        here = {}
        k = 0
        for i in range(len(mouseGenome)):
            if(mouseGenome[i] != i+1):
                for k in range(i,len(mouseGenome)): 
                    if(i+1 == abs(mouseGenome[k])):
                        break
                mouseGenome[i:k+1] = reversed(mouseGenome[i:k+1])
                for n in range(i,k+1):
                    mouseGenome[n] =  -1*mouseGenome[n]
                if mouseGenome[i] < 0:
                    printoutfor(mouseGenome)
                    f.write(printoutfor(mouseGenome)+'\n' )
                    mouseGenome[i] = -(mouseGenome[i])
                printoutfor(mouseGenome)
                f.write(printoutfor(mouseGenome)+'\n' )
    f.close()          
        

greedySorting(mouseGenome)