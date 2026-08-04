class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                width = max(i,j) - min(i,j)
                height = min(heights[i],heights[j])
                a = width*height
                if a>max_a:
                    max_a=a
        return max_a