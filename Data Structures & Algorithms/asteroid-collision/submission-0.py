class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            destroyed=False
            if asteroids[i]>0:
                stack.append(asteroids[i])
                continue
            while asteroids[i]<0 and stack and stack[-1]>0:
                
                if abs(asteroids[i])<stack[-1]:
                    destroyed=True
                    break
                elif abs(asteroids[i])>stack[-1]:
                    stack.pop()
                else:
                    destroyed=True
                    stack.pop()
                    break
            if not destroyed:
                stack.append(asteroids[i])
        return stack