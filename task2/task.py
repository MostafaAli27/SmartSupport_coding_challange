class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        day=0
        count=0
        for i in range(1,len(prices)):
            m=min(m,prices[i])
            if prices[i]<prices[i-1]:
                count+=1 
            else:
                diff=prices[i]-m
                day=max(day,diff)
                
        if count==len(prices):
            return 0
        else:
            return day
                
              
             
