class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        from collections import deque

        MOD = 10**9 + 7
        n = len(nums)

        # dp[i] = number of ways to partition nums[0..i-1]
        dp = [0] * (n + 1)
        dp[0] = 1  # base case

        # prefix sums of dp for fast range queries
        prefix = [0] * (n + 1)
        prefix[0] = 1

        minQ = deque()  # stores indexes, increasing values
        maxQ = deque()  # stores indexes, decreasing values

        left = 0

        for right in range(n):
            # Maintain minQ (increasing)
            while minQ and nums[minQ[-1]] >= nums[right]:
                minQ.pop()
            minQ.append(right)

            # Maintain maxQ (decreasing)
            while maxQ and nums[maxQ[-1]] <= nums[right]:
                maxQ.pop()
            maxQ.append(right)

            # Shrink window until valid
            while nums[maxQ[0]] - nums[minQ[0]] > k:
                left += 1
                if minQ[0] < left:
                    minQ.popleft()
                if maxQ[0] < left:
                    maxQ.popleft()

            # Compute dp[r+1] = sum(dp[left]..dp[r])
            dp[right + 1] = (prefix[right] - (prefix[left - 1] if left > 0 else 0)) % MOD

            # Update prefix sum
            prefix[right + 1] = (prefix[right] + dp[right + 1]) % MOD

        return dp[n] % MOD
