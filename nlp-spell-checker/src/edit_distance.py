import numpy as np

def min_edit_dist(source, target):
    dp = np.zeros((len(source)+1, len(target)+1))
    dp[0, 1:] = np.arange(1, len(target)+1)
    dp[1:, 0] = np.arange(1, len(source)+1)

    for i in range(len(source)):
        for j in range(len(target)):
            if source[i] == target[j]:
                dp[i+1, j+1] = dp[i, j]
            else:
                dp[i+1, j+1] = min(dp[i, j+1]+1, dp[i+1, j]+1, dp[i, j]+2)
    return dp[-1][-1]