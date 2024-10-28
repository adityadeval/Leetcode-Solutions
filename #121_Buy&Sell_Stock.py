# Leetcode problem : 121. Best Time to Buy And Sell Stock
# Problem description : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -1
        left, right = 0, 0
        for right in range(len(prices)):
            # If below statement is true, then surely it would result in a loss and not a profit.
            # Also, we need to buy at the lowest price to earn a good profit.
            # So we can ignore the price at left pointer as its of no use since we found a lower
            # price (pointed to by the right pointer).
            if prices[right] < prices[left]:
                left = right
            else:
                # In this case, we definately won't make a loss. Profit would be 0 or higher.
                # So calculate the profit and compare it with the current highest profit.
                # Update max_profit if a higher profit is found.
                curr_profit = prices[right] - prices[left]
                max_profit = max(max_profit, curr_profit)
        return max_profit

# Note that in the case where we're making a loss (right < left) we're making the left pointer jump directly to position of right pointer (skipping all numbers in between). The reason is that at any given time, all numbers before right pointer would certainly be greater than the left. So we can skip these. 
# Eg: 3, 7, 8, 11, 5, 2, 4
# Here assume left points to 3 and right goes pointing to 3 --> 7 --> 8 --> 11 --> 5
# Now, when right points to 2, we can make left jump directly to 2 as all numbers before it are certainly greater than 3, so we can skip them.
