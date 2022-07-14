from ast import Num


class Solution(object):
    arr = [[int(i) for i in line.split()] for line in open('/Users/claudemassaad/Desktop/p18.txt')]
    dp = [[0 for i in line.split()] for line in open('/Users/claudemassaad/Desktop/p18.txt')]
    dp[0][0] = arr[0][0]
    for i in range (1 , len(arr)):
        for j in range (len(arr[i])):
            if j == 0:
                dp[i][j] = arr[i][j] + dp[i-1][j] 
            elif j == len(arr[i]) - 1:
                dp[i][j] = arr[i][j] + dp[i-1][j-1] 
            else:
                dp[i][j] = arr[i][j] + max ( dp[i-1][j-1] , dp[i-1][j] )

    print(max(dp[len(arr) - 1]))
        

