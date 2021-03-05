class Solution:
    def findSmallerOne(self,a,b) -> int:
        if(a>=b):
            return b
        else:
            return a

    def maxArea(self, height: List[int]) -> int:
        maximumArea = 0
        area = 0
        for i in range(0,len(height)):
            for j in range (i + 1 , len(height)):
                area = (j - i) * (self.findSmallerOne(height[j],height[i]))
                if(maximumArea < area):
                    maximumArea = area
        
        return maximumArea