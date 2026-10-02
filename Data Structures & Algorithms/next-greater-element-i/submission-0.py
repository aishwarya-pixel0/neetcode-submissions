class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater={}
        stack=[]
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                next_greater[stack[-1]]=nums2[i]
                stack.pop()
            stack.append(nums2[i])
        while stack:
            next_greater[stack.pop()]=-1
        answer=[]
        for num in nums1:
            answer.append(next_greater[num])
        return answer