def manhattan_tourist(n,m,down,right):
    s = {}
    s[0,0] = 0    
    for i in range(1,n+1):
        s[i,0] = s[i-1,0] + down[0][i-1]

    for j in range(1,m+1):
        s[0,j] = s[0,j-1] + right[0][j-1]
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            s[i,j] = max(s[i,j-1] + right[i][j-1],s[i-1,j]+down[j][i-1])
    return s[n,m]

