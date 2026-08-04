class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        max_a=0
        while i<j:
            height = min(heights[i],heights[j])
            a=(j-i)*height
            max_a = max(max_a,a)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_a

