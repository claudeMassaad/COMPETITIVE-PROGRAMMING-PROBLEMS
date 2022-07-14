class coins(object):
    nums = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200

    def combinationSum4(nums, target):        
        dp = [[0 for j in range (target + 1)] for i in range (len(nums) + 1)]
        dp[0][0] = 1
        for i in range (1 , len(nums) + 1):
            for j in range (0 , target + 1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-nums[i-1]] + dp[i-1][j]

        print("Ways to make change = ", dp[len(nums)][target]) 

    combinationSum4(nums, target)