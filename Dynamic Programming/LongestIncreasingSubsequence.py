# Time complexity: O(n^2)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

"""
Time complexity: O(nlogn)
# -----------------------------------------------------------
        回傳嚴格遞增子序列（LIS）的長度。
        維護 tails，使 tails[k] = 長度 k+1 的所有遞增序列中「最小的結尾值」。
        對每個 x：
          - i = 第一個 >= x 的位置（bisect_left）
          - 若 i == len(tails) → 追加 x（LIS 變長）
          - 否則 tails[i] = x（用更小的結尾替換，利於未來延伸）
# -----------------------------------------------------------
from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: List[int] = []
        for x in nums:
            i = bisect_left(tails, x)   # 找第一個 >= x 的位置
            if i == len(tails):
                tails.append(x)          # x 大於所有尾巴 → 開新長度
            else:
                tails[i] = x             # 用 x 取代，讓該長度的結尾更小
        return len(tails)


# -----------------------------------------------------------
# 例子（註解步驟演示，不會實際執行）：
#
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# tails 初始為 []
#
# x=10 → tails=[]，i=0（>=10 的第一個位置）→ 追加 → tails=[10]
# x=9  → tails=[10]，i=0 → 替換 tails[0]=9      → tails=[9]
# x=2  → tails=[9]，  i=0 → 替換 tails[0]=2      → tails=[2]
# x=5  → tails=[2]，  i=1 → 追加                  → tails=[2, 5]
# x=3  → tails=[2,5]，i=1 → 替換 tails[1]=3      → tails=[2, 3]
# x=7  → tails=[2,3]，i=2 → 追加                  → tails=[2, 3, 7]
# x=101→ tails=[2,3,7],i=3→ 追加                  → tails=[2, 3, 7, 101]
# x=18 → tails=[2,3,7,101],i=3→ 替換 tails[3]=18 → tails=[2, 3, 7, 18]
#
# 最終 len(tails) = 4，就是 LIS 長度。
# -----------------------------------------------------------

"""
