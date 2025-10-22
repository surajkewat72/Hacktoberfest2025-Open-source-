class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        damageSum = {}
        for p in power:
            damageSum[p] = damageSum.get(p, 0) + p

        unique = sorted(damageSum.keys())
        n = len(unique)
        dp = [0] * n

        for i in range(n):
            val = damageSum[unique[i]]

            j = bisect_right(unique, unique[i] - 3) - 1
            include = val + (dp[j] if j >= 0 else 0)
            exclude = dp[i - 1] if i > 0 else 0

            dp[i] = max(include, exclude)

        return dp[-1]
        
