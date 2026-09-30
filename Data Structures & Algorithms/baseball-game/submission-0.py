class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        result=0
        for i in range(len(operations)):
            if operations[i]=='+':
                stack.append(stack[-1]+stack[-2])
            elif operations[i]=='D':
                stack.append(2*stack[-1])
            elif operations[i]=='C':
                stack.pop()
            else:
                stack.append(int(operations[i]))
        for i in range(len(stack)):
            result+=int(stack[i])
        return result