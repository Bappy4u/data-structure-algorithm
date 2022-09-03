def lcs_algo(S1, S2, m, n):
    
    dp = [[0]*(n+1)]*(m+1)
    

    for i in range(1,m+1):
        for j in range(1,n+1):
            if S1[i-1]==S2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
    
    print(dp[m][n])
    res = ""
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            res += S1[i-1]
            i -= 1
            j -= 1
      

        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    # Printing the sub sequences
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "" + res)


S1 = "befgsss"
S2 = "sefgjsshab"
m = len(S1)
n = len(S2)
lcs_algo(S1, S2, m, n)