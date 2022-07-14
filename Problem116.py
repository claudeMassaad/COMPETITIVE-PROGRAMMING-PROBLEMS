class tiles(object):
    nums = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200

    def combtiles(tiles, i):        
        dp = [0 for j in range (tiles)]
        dp[tiles - i] = 1
        for a in range (tiles - i - 1 , -1 , -1):
            dp[a] = 1 + sum(dp[a+i:])

        return sum(dp)
    print(combtiles(50, 3) + combtiles(50, 4) + combtiles(50, 2))

    def combtiles(tiles):        
        dp = [[0 for j in range (tiles)] for i in range (3)]

        dp[0][tiles - 2] = 1
        for a in range (tiles - 1 - 2 , -1 , -1):
            dp[0][a] = 1 + sum(dp[0][a+2:])

        dp[1][tiles - 3] = 1
        for a in range (tiles - 1 - 3 , -1 , -1):
            dp[1][a] = 1 + sum(dp[1][a+3:]) + sum (dp[0][tiles-a+3:]) + sum(dp[0][tiles - a :])
        
        dp[2][tiles - 4] = 1
        for a in range (tiles - 1 - 4 , -1 , -1):
            dp[2][a] = 1 + sum(dp[2][a+4:]) + sum (dp[1][tiles-a+4:]) + sum(dp[1][tiles - a :])
            
        return sum(dp[2])
    print(combtiles(50) + 1)