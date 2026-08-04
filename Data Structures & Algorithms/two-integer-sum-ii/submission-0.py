class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        res = []*len(numbers)
        while left < right :
            if numbers[left] + numbers[right]==target :
                res.append(numbers[left])
                res.append(numbers[right])
                return res
            elif numbers[left] + numbers[right]<target :
                left+=1
            elif numbers[left]+numbers[right]>target:
                 right-=1